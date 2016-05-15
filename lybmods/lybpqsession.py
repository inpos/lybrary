# -*- coding: utf-8 -*-
import cherrypy
import logging
import threading
import psycopg2
import lybmods.lybcfg as lybcfg
import pickle as pickle
import lybmods.lybtools as lybtools
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

logger = logging.getLogger('Session')

class PgsqlSession(cherrypy.lib.sessions.Session):
    sess_table_name = lybcfg.sess_table_name
    sess_data_table_name = lybcfg.sess_data_table_name
    connect_arguments = "dbname={0} user={1} password={2} host={3}".format(lybcfg.dbname, lybcfg.dbuser, lybcfg.dbpass, lybcfg.dbhost)
    
    missing = False
    "True if the session requested by the client did not exist."

    _database = None
    
    def __init__(self, sid=None, **kwargs):
        logger.debug('Initializing PgsqlSession with %r' % kwargs)
        for k, v in list(kwargs.items()):
            setattr(PgsqlSession, k, v)
        self.db = self.get_db()
        self.cursor = self.db.cursor()
        super(PgsqlSession, self).__init__(sid, **kwargs)

    @classmethod
    def get_db(cls):
        ##
        ## Use thread-local connections
        local = threading.local()
        if hasattr(local, 'db'):
            return local.db
        else:
            logger.debug("Connecting to %r" % cls.connect_arguments)
            db = psycopg2.connect(cls.connect_arguments)
            local.db = db
            
            return db
    
    def load(self):
        """Copy stored session data into this session instance."""
        exptime = self._load()
        # data is either None or a tuple (session_data, expiration_time)
        if exptime is None or exptime < self.now().utcnow():
            if self.debug:
                cherrypy.log('Expired session, flushing data', 'TOOLS.SESSIONS')
            self.regenerate()
        self.loaded = True
        
        # Stick the clean_thread in the class, not the instance.
        # The instances are created and destroyed per-request.
        cls = self.__class__
        if self.clean_freq and not cls.clean_thread:
            # clean_up is in instancemethod and not a classmethod,
            # so that tool config can be accessed inside the method.
            t = cherrypy.process.plugins.Monitor(
                cherrypy.engine, self.clean_up, self.clean_freq * 60,
                name='Session cleanup')
            t.subscribe()
            cls.clean_thread = t
            t.start()
    
    def _load(self):
        logger.debug('_load %r' % self)
        # Select session data from table
        self.cursor.execute('select expiration_time from %s '
                            'where id = %%s' % PgsqlSession.sess_table_name, (self.id,))
        row = self.cursor.fetchone()
        if row:
            expiration_time = row[0].utcfromtimestamp(row[0].timestamp())
            return expiration_time
        else:
            return None

    def _save(self, expiration_time):
        logger.debug('_save %r' % self)
        self.cursor.execute('select count(*) from %s where id = %%s and expiration_time > now()' % PgsqlSession.sess_table_name, (self.id,))
        (count,) = self.cursor.fetchone()
        if count:
            self.cursor.execute('update %s set expiration_time = %%s where id = %%s' % PgsqlSession.sess_table_name,
                                (expiration_time, self.id))
        else:
            self.cursor.execute('insert into %s (expiration_time, id) values (%%s, %%s)' % PgsqlSession.sess_table_name,
                                (expiration_time, self.id))
        self.db.commit()

    def acquire_lock(self):
        logger.debug('acquire_lock %r' % self)
        self.locked = True
        self.cursor.execute('select id from %s where id = %%s for update' % PgsqlSession.sess_table_name,
                            (self.id,))
        self.db.commit()

    def release_lock(self):
        logger.debug('release_lock %r' % self)
        self.locked = False
        self.db.commit()
        
    def clean_up(self):
        logger.debug('clean_up %r' % self)
        
        self.cursor.execute('DELETE FROM %s WHERE expiration_time < now()' % PgsqlSession.sess_table_name)
        self.db.commit()
        
    def _delete(self):
        logger.debug('_delete %r' % self)
        self.cursor.execute('DELETE FROM %s WHERE id=%%s' % PgsqlSession.sess_table_name, (self.id,))
        self.db.commit()
    
        
    def _exists(self):
        # Select session data from table
        self.cursor.execute('select count(*) from %s '
                            'where id = %%s and expiration_time > now()' % PgsqlSession.sess_table_name, (self.id,))
        (count,) = self.cursor.fetchone()
        logger.debug('_exists %r (%r)' % (self, bool(count)))
        return bool(count)

    def __getitem__(self, key):
        if not self.loaded: self.load()
        self.cursor.execute('SELECT value FROM %s WHERE key=%%s AND sid=%%s;' % PgsqlSession.sess_data_table_name, (key, self.id))
        try:
            res = self.cursor.fetchall()[0][0]
            val = pickle.loads(res)
            return val
        except:
            raise KeyError(key)
    
    def __setitem__(self, key, value):
        if not self.loaded: self.load()
        self.cursor.execute('SELECT count(*) FROM %s WHERE key = %%s AND sid = %%s;' % PgsqlSession.sess_data_table_name, (key, self.id))
        count = self.cursor.fetchone()[0]
        if count:
            self.cursor.execute('UPDATE %s SET value = %%s WHERE key = %%s AND sid = %%s;' % PgsqlSession.sess_data_table_name,
                                (pickle.dumps(value), key, self.id))
        else:
            self.cursor.execute('INSERT INTO %s (value, key, sid) VALUES (%%s, %%s, %%s);' % PgsqlSession.sess_data_table_name,
                                (pickle.dumps(value), key, self.id))
        self.db.commit()
    def __delitem__(self, key):
        if not self.loaded: self.load()
        self.cursor.execute('DELETE FROM %s WHERE key = %%s AND sid = %%s;' % PgsqlSession.sess_data_table_name, (key, self.id))
        self.db.commit()
    def pop(self, key, default=None):
        """Remove the specified key and return the corresponding value.
        If key is not found, default is returned if given,
        otherwise KeyError is raised.
        """
        if not self.loaded: self.load()
        try:
            val = self[key]
        except:
            if default is None:
                raise KeyError(key)
            else:
                val = default
                return val
        del self[key]
        return val
    
    def __contains__(self, key):
        if not self.loaded: self.load()
        self.cursor.execute('SELECT count(*) FROM %s WHERE key = %%s AND sid = %%s;' % PgsqlSession.sess_data_table_name, (key, self.id))
        return bool(self.cursor.fetchone()[0])
    
    if hasattr({}, 'has_key'):
        def has_key(self, key):
            """D.has_key(k) -> True if D has a key k, else False."""
            if not self.loaded: self.load()
            return self.__contains__(key)
        
    def get(self, key, default=None):
        """D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None."""
        if not self.loaded: self.load()
        try:
            val = self[key]
            return val
        except:
            return default
    
    def update(self, d):
        """D.update(E) -> None.  Update D from E: for k in E: D[k] = E[k]."""
        if not self.loaded: self.load()
        for k in d:
            self[k] = d[k]
    
    def setdefault(self, key, default=None):
        """D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D."""
        if not self.loaded: self.load()
        try:
            val = self[key]
        except:
            self[key] = val = default
        return val
    
    def clear(self):
        """D.clear() -> None.  Remove all items from D."""
        if not self.loaded: self.load()
        self.cursor.execute('DELETE FROM %s WHERE sid=%%s AND key != %%s;' % PgsqlSession.sess_data_table_name, (self.id, lybtools.SESSION_KEY))
        self.db.commit()
    
    def keys(self):
        """D.keys() -> list of D's keys."""
        if not self.loaded: self.load()
        k = []
        self.cursor.execute('SELECT key FROM %s WHERE sid = %%s;' % PgsqlSession.sess_data_table_name, (self.id,))
        res = self.cursor.fetchall()
        if res != []:
            for i in res:
                k.append(i[0])
        return k
    
    def items(self):
        """D.items() -> list of D's (key, value) pairs, as 2-tuples."""
        if not self.loaded: self.load()
        i = []
        self.cursor.execute('SELECT key, value FROM %s WHERE sid = %%s;' % PgsqlSession.sess_data_table_name, (self.id,))
        res = self.cursor.fetchall()
        if res != []:
            for k, v in res:
                i.append({k, pickle.loads(v)})
        return i
    
    def values(self):
        """D.values() -> list of D's values."""
        if not self.loaded: self.load()
        v = []
        self.cursor.execute('SELECT value FROM %s WHERE sid = %%s;' % PgsqlSession.sess_data_table_name, (self.id,))
        res = self.cursor.fetchall()
        if res != []:
            for i in res:
                v.append(pickle.loads(i[0]))
        return v

    def __del__(self):
        logger.debug('__del__ %r' % self)
        self.db.commit()
        self.db.close()
        self.db = None
    
    def __repr__(self):
        return '<PgsqlSession %r>' % (self.id,)

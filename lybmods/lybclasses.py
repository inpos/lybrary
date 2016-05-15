# -*- coding: utf-8 -*-
import cherrypy
import lybmods.lybcfg as lybcfg
import lybmods.lybtools as lybtools
from hashlib import sha1
class Doc:
    def __init__(self, did):
        self.sess = cherrypy.session
        self.db = self.sess.db
        self.cursor = self.db.cursor()
        self.id = did
    @property
    def text(self):
        self.cursor.execute('SELECT body FROM %s WHERE id = %%s;' % lybcfg.doc_table_name, (self.id,))
        return self.cursor.fetchone()[0]
    @property
    def bins(self):
        """D.keys() -> list of D's keys."""
        k = []
        self.cursor.execute('''SELECT b.hash FROM {bin} AS b, (SELECT binid FROM {docbin} 
                                WHERE docid = %s) AS d WHERE b.id = d.binid;'''.format(bin = lybcfg.bin_table_name,
                                                                                       docbin = lybcfg.docbin_table_name), 
                            (self.id,))
        res = self.cursor.fetchall()
        for i in res:
            k.append(i[0])
        return k
    @property
    def mtime(self):
        self.cursor.execute('SELECT mtime FROM %s WHERE id = %%s;' % lybcfg.doc_table_name, (self.id,))
        return self.cursor.fetchone()[0]
    @property
    def muser(self):
        self.cursor.execute('SELECT muser FROM %s WHERE id = %%s;' % lybcfg.doc_table_name, (self.id,))
        return Usr(self.cursor.fetchone()[0])
    @property
    def name(self):
        self.cursor.execute('SELECT name FROM %s WHERE id = %%s;' % lybcfg.doc_table_name, (self.id,))
        return self.cursor.fetchone()[0]
    def setname(self, name):
        muser = cherrypy.session.get(lybtools.SESSION_KEY, None)
        self.cursor.execute('''UPDATE {doc} SET name = %s, muser = %s WHERE id = %s;'''.format(doc = lybcfg.doc_table_name), (name, muser, self.id))
        self.db.commit()
        return True
    def setcatid(self, catid):
        muser = cherrypy.session.get(lybtools.SESSION_KEY, None)
        self.cursor.execute('''UPDATE {doc} SET catid = %s, muser = %s WHERE id = %s;'''.format(doc = lybcfg.doc_table_name), (catid, muser, self.id))
        self.db.commit()
        return True
    @property
    def cat(self):
        self.cursor.execute('SELECT catid FROM %s WHERE id = %%s;' % lybcfg.doc_table_name, (self.id,))
        catid = self.cursor.fetchone()
        if catid: return Cat(catid[0])
        else: return None
    @property
    def path(self):
        def np(p, cid):
            p.append(cid)
            if cid > 0:
                p = np(p, Cat(cid).parent.id)
            return p
        p = []
        p = np(p, self.cat.id)
        p.reverse()
        return p
    @property
    def users(self):
        """D.keys() -> list of D's keys."""
        n = []
        self.cursor.execute('''SELECT b.username FROM {pwd} AS b, (SELECT pid FROM {pwddoc_access} 
                                WHERE docid = %s) AS d WHERE b.id = d.pid;'''.format(pwd = lybcfg.pwd_table_name,
                                                                                       pwddoc_access = lybcfg.pwddoc_access_table), 
                            (self.id,))
        res = self.cursor.fetchall()
        for i in res:
            n.append(i[0])
        return n
    @property
    def groups(self):
        """D.keys() -> list of D's keys."""
        n = []
        self.cursor.execute('''SELECT b.name FROM {grp} AS b, (SELECT gid FROM {grpdoc_access} 
                                WHERE docid = %s) AS d WHERE b.id = d.gid;'''.format(grp = lybcfg.grp_table_name,
                                                                                       grpdoc_access = lybcfg.grpdoc_access_table), 
                            (self.id,))
        res = self.cursor.fetchall()
        for i in res:
            n.append(i[0])
        return n
    def __getitem__(self, key):
        self.cursor.execute("""\
            SELECT b.type, b.body FROM {bin} AS b, (SELECT binid FROM {docbin} WHERE docid = %s) AS d
                WHERE b.id = d.binid AND hash = %s;""".format(bin = lybcfg.bin_table_name, 
                                            docbin = lybcfg.docbin_table_name), (self.id, key))
        try:
            res = self.cursor.fetchone()
            (ctype, body) = res
            return {'type': ctype, 'body': body.tobytes()}
        except:
            raise KeyError(key)
    
    def __setitem__(self, key, value):
        self.cursor.execute('SELECT id FROM %s WHERE hash = %%s;' % lybcfg.bin_table_name, (key, ))
        binid = self.cursor.fetchone()
        if binid:
            binid = binid[0]
            self.cursor.execute('SELECT COUNT(*) FROM %s WHERE binid = %%s AND docid = %%s;' % lybcfg.docbin_table_name, (binid, self.id))
            count = self.cursor.fetchone()[0]
            if count:
                return
        else:
            self.cursor.execute('INSERT INTO %s (hash, type, body) VALUES (%%s, %%s, %%s) RETURNING id;' % lybcfg.bin_table_name,
                                    (key, value['type'], value['body']))
            binid = self.cursor.fetchone()[0]
        self.cursor.execute('INSERT INTO %s (binid, docid) VALUES (%%s, %%s);' % lybcfg.docbin_table_name, (binid, self.id))
        self.db.commit()
    def __delitem__(self, key):
        self.cursor.execute('DELETE FROM {docbin} WHERE binid = (SELECT id FROM {bin} WHERE hash = %s) AND docid = %s;'.format(docbin = lybcfg.docbin_table_name,
                                                                                                                               bin = lybcfg.bin_table_name), (key, self.id))
        self.db.commit()
    def pop(self, key, default = None):
        """Remove the specified key and return the corresponding value.
        If key is not found, default is returned if given,
        otherwise KeyError is raised.
        """
        try:
            val = self[key]
        except:
            if not default:
                raise KeyError(key)
            else:
                val = default
                return val
        del self[key]
        return val
    
    def __contains__(self, key):
        self.cursor.execute('SELECT count(*) FROM {docbin} WHERE binid = (SELECT id FROM {bin} WHERE hash = %s) AND docid = %s;'.format(bin = lybcfg.bin_table_name,
                                                                                                                      docbin = lybcfg.docbin_table_name),
                            (key, self.id))
        return bool(self.cursor.fetchone()[0])
    
    if hasattr({}, 'has_key'):
        def has_key(self, key):
            """D.has_key(k) -> True if D has a key k, else False."""
            return self.__contains__(key)
        
    def get(self, key, default=None):
        """D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None."""
        try:
            val = self[key]
            return val
        except:
            return default
    
    def update(self, d):
        """D.update(E) -> None.  Update D from E: for k in E: D[k] = E[k]."""
        for k in d:
            self[k] = d[k]
    
    def setdefault(self, key, default=None):
        """D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D."""
        try:
            val = self[key]
        except:
            self[key] = val = default
        return val
    
    def clear(self):
        """D.clear() -> None.  Remove all items from D."""
        self.cursor.execute('DELETE FROM {docbin} WHERE docid = %s;'.format(docbin = lybcfg.docbin_table_name), (self.id,))
        self.db.commit()
    
    def keys(self):
        """D.keys() -> list of D's keys."""
        k = []
        self.cursor.execute('SELECT hash FROM {bin} WHERE id = (SELECT binid FROM {docbin} WHERE docid = %s);'.format(bin = lybcfg.bin_table_name,
                                                                                                                      docbin = lybcfg.docbin_table_name), 
                            (self.id,))
        res = self.cursor.fetchall()
        for i in res:
            k.append(i[0])
        return k
    
    def items(self):
        """D.items() -> list of D's (key, value) pairs, as 2-tuples."""
        i = []
        self.cursor.execute('SELECT hash, type, body FROM {bin} WHERE id = (SELECT binid FROM {docbin} WHERE docid = %s);'.format(bin = lybcfg.bin_table_name,
                                                                                                                      docbin = lybcfg.docbin_table_name), 
                            (self.id,))
        res = self.cursor.fetchall()
        for k, t, v in res:
            i.append((k, {'type': t, 'body': str(v)}))
        return i
    
    def values(self):
        """D.values() -> list of D's values."""
        v = []
        self.cursor.execute('SELECT body FROM {bin} WHERE id = (SELECT binid FROM {docbin} WHERE docid = %s);'.format(bin = lybcfg.bin_table_name,
                                                                                                                      docbin = lybcfg.docbin_table_name), 
                            (self.id,))
        res = self.cursor.fetchall()
        for i in res:
            v.append(str(i[0]))
        return v

    def __del__(self):
        self.db.commit()
        self.cursor.close()
        self.cursor = None
        self.db = None
    def __repr__(self):
        return '<DocObject %r>' % (self.id,)

class Cat:
    def __init__(self, cid = 0):
        self.sess = cherrypy.session
        self.db = self.sess.db
        self.cursor = self.db.cursor()
        self.id = cid
    
    def search(self, query):
        if self.id == 0:
            self.cursor.execute("""SELECT tab.id FROM (SELECT ts_rank_cd(fts_index, q) as rank, id
                                        FROM %s, plainto_tsquery(%%s) q
                                        WHERE q @@ fts_index ORDER BY rank DESC) AS tab;""" % lybcfg.doc_table_name, (query, ))
        else:
            self.cursor.execute("""SELECT tab.id FROM (SELECT ts_rank_cd(fts_index, q) AS rank, id
                                        FROM %s, plainto_tsquery(%%s) q
                                        WHERE q @@ fts_index AND catid = %%s ORDER BY rank DESC) AS tab;""" % lybcfg.doc_table_name, (query, self.id))
        return [x[0] for x in self.cursor.fetchall()]
    @property
    def name(self):
        if self.id == 0:
            return 'Корневой'
        self.cursor.execute('SELECT name FROM %s WHERE id = %%s;' % lybcfg.cat_table_name, (self.id,))
        return self.cursor.fetchone()[0]
    def setname(self, name):
        if self.id == 0:
            return False
        self.cursor.execute('UPDATE %s SET name = %%s WHERE id = %%s;' % lybcfg.cat_table_name, (name, self.id))
        self.db.commit()
        return True
    @property
    def parent(self):
        if self.id == 0: return Cat(0)
        self.cursor.execute('SELECT parent FROM %s WHERE id = %%s;' % lybcfg.cat_table_name, (self.id,))
        parid = self.cursor.fetchone()[0]
        return Cat(parid)
    @property
    def path(self):
        def np(p, cid):
            p.append(cid)
            if cid > 0:
                p = np(p, Cat(cid).parent.id)
            return p
        p = []
        if self.id == 0: return []
        p = np(p, self.parent.id)
        p.reverse()
        return p
    def setparentid(self, parid):
        if self.id == 0:
            return False
        self.cursor.execute('UPDATE %s SET parent = %%s WHERE id = %%s;' % lybcfg.cat_table_name, (parid, self.id))
        self.db.commit()
        return True
    @property
    def categories(self):
        v = []
        self.cursor.execute('SELECT id FROM {cat} WHERE parent = %s ORDER BY name ASC;'.format(cat = lybcfg.cat_table_name), (self.id,))
        res = self.cursor.fetchall()
        for i in res:
            v.append(Cat(i[0]))
        return v
    def delete(self):
        self.cursor.execute('DELETE FROM {cat} WHERE id = %s;'.format(cat = lybcfg.cat_table_name), (self.id,))
        self.db.commit()
    @property
    def documents(self):
        v = []
        self.cursor.execute('SELECT id FROM %s WHERE catid = %%s ORDER BY name;' % lybcfg.doc_table_name, (self.id,))
        res = self.cursor.fetchall()
        for i in res:
            v.append(Doc(i[0]))
        return v
    @property
    def catcount(self):
        self.cursor.execute('SELECT count(*) FROM %s WHERE parent = %%s;' % lybcfg.cat_table_name, (self.id,))
        return self.cursor.fetchone()[0]
    @property
    def doccount(self):
        self.cursor.execute('SELECT count(*) FROM %s WHERE catid = %%s;' % lybcfg.doc_table_name, (self.id,))
        return self.cursor.fetchone()[0]
    def docidbyname(self, name):
        self.cursor.execute('SELECT id FROM %s WHERE catid = %%s AND name = %%s' % lybcfg.doc_table_name, (self.id, name))
        res = self.cursor.fetchone()
        if res:
            return res[0]
        else:
            return None
    def __getitem__(self, did):
        self.cursor.execute('SELECT id FROM %s WHERE catid = %%s AND id = %%s;' % lybcfg.doc_table_name, (self.id, did))
        docid = self.cursor.fetchone()
        if docid:
            return Doc(docid[0])
        else:
            raise KeyError(did)
    def __setitem__(self, did, value):
        muser = cherrypy.session.get(lybtools.SESSION_KEY, None)
        self.cursor.execute('SELECT id FROM %s WHERE id = %%s AND catid = %%s;' % lybcfg.doc_table_name, (did, self.id))
        docid = self.cursor.fetchone()
        if docid:
            self.cursor.execute('UPDATE %s SET name = %%s, body = %%s, muser = %%s, mtime = now() WHERE id = %%s;' % lybcfg.doc_table_name, (value['name'],
                                                                                                                              value['body'],
                                                                                                                              muser,
                                                                                                                              docid[0]))
        else:
            raise KeyError(did)
        self.db.commit()
    def insert(self, value):
        muser = cherrypy.session.get(lybtools.SESSION_KEY, None)
        self.cursor.execute('INSERT INTO %s (name, catid, muser, body) VALUES (%%s, %%s, %%s, %%s) RETURNING id;' % lybcfg.doc_table_name,
                            (value['name'], self.id, muser, value['body']))
        did = self.cursor.fetchone()[0]
        self.db.commit()
        return did
    def __delitem__(self, did):
        muser = cherrypy.session.get(lybtools.SESSION_KEY, None)
        self.cursor.execute('DELETE FROM %s WHERE catid = %%s AND id = %%s;' % lybcfg.doc_table_name, (self.id, did))
        self.db.commit()
    def pop(self, key, default = None):
        """Remove the specified key and return the corresponding value.
        If key is not found, default is returned if given,
        otherwise KeyError is raised.
        """
        try:
            val = self[key]
        except:
            if not default:
                raise KeyError(key)
            else:
                val = default
                return val
        del self[key]
        return val
    
    def __contains__(self, did):
        self.cursor.execute('SELECT count(*) FROM %s WHERE catid = %%s AND id = %%s;' % lybcfg.doc_table_name, (self.id, did))
        return bool(self.cursor.fetchone()[0])
    
    if hasattr({}, 'has_key'):
        def has_key(self, key):
            """D.has_key(k) -> True if D has a key k, else False."""
            return self.__contains__(key)
        
    def get(self, key, default=None):
        """D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None."""
        try:
            val = self[key]
            return val
        except:
            return default
    
    def update(self, d):
        """D.update(E) -> None.  Update D from E: for k in E: D[k] = E[k]."""
        for k in d:
            self[k] = d[k]
    
    def setdefault(self, key, default=None):
        """D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D."""
        try:
            val = self[key]
        except:
            self[key] = val = default
        return val
    
    def clear(self):
        """D.clear() -> None.  Remove all items from D."""
        self.cursor.execute('DELETE FROM %s WHERE catid = %%s;' % lybcfg.doc_table_name, (self.id,))
        self.db.commit()
    
    def keys(self):
        """D.keys() -> list of D's keys."""
        k = []
        self.cursor.execute('SELECT id FROM %s WHERE catid = %%s;' % lybcfg.doc_table_name, (self.id,))
        res = self.cursor.fetchall()
        for i in res:
            k.append(i[0])
        return k
    
    def items(self):
        """D.items() -> list of D's (key, value) pairs, as 2-tuples."""
        i = []
        self.cursor.execute('SELECT id FROM %s WHERE catid = %%s;' % lybcfg.doc_table_name, (self.id,))
        res = self.cursor.fetchall()
        for did in res:
            i.append((did, Doc(did)))
        return tuple(i)
    
    def values(self):
        """D.values() -> list of D's values."""
        v = []
        self.cursor.execute('SELECT id FROM %s WHERE catid = %%s;' % lybcfg.doc_table_name, (self.id,))
        res = self.cursor.fetchall()
        for i in res:
            v.append(Doc(i))
        return v
    def newcat(self, name):
        self.cursor.execute('SELECT count(*) FROM %s WHERE name = %%s AND parent = %%s;' % lybcfg.cat_table_name, (name, self.id))
        exist = self.cursor.fetchone()[0]
        if exist:
                return False
        else:
            self.cursor.execute('INSERT INTO %s (name, parent) VALUES (%%s, %%s);' % lybcfg.cat_table_name, (name, self.id))
            self.db.commit()
            return True

    def __del__(self):
        self.db.commit()
        self.cursor.close()
        self.cursor = None
        self.db = None
    
    def __repr__(self):
        return '<CatObject %r>' % (self.id,)

class Usr:
    def __init__(self, name):
        self.sess = cherrypy.session
        self.db = self.sess.db
        self.cursor = self.db.cursor()
        self.name = name
    def new(self, password, dname = None):
        dname = True and dname or self.name
        p = sha1(self.name.encode("utf-8"))
        p.update(password.encode("utf-8"))
        try:
            self.cursor.execute('INSERT INTO %s (username, dname, password) VALUES (%%s, %%s, %%s);' % lybcfg.pwd_table_name,
                                    (self.name, dname, p.hexdigest()))
        except:
            self.db.commit()
            return False
        self.db.commit()
        return True
    def delete(self):
        self.cursor.execute('DELETE FROM %s WHERE username = %%s;' % lybcfg.pwd_table_name, (self.name,))
        self.db.commit()
    @property
    def uid(self):
        self.cursor.execute('SELECT id FROM %s WHERE username = %%s' % lybcfg.pwd_table_name, (self.name,))
        uid = self.cursor.fetchone()
        if uid:
            return uid[0]
        else:
            raise KeyError(self.name)
    @property
    def groups(self):
        v = []
        self.cursor.execute("""SELECT name FROM {grp}
                                    WHERE id = (SELECT gid FROM {mbrsh} WHERE uid = %s)
                                    ORDER BY dname ASC;""".format(grp = lybcfg.grp_table_name, mbrsh = lybcfg.mbrsh_table_name), (self.uid,))
        res = self.cursor.fetchall()
        for i in res:
            v.append(Grp(i[0]))
        return v
    @property
    def fgroups(self):
        v = []
        self.cursor.execute("""SELECT name FROM {grp}
                                    WHERE id NOT IN (SELECT gid FROM {mbrsh} WHERE uid = %s)
                                    ORDER BY dname ASC;""".format(grp = lybcfg.grp_table_name, mbrsh = lybcfg.mbrsh_table_name), (self.uid,))
        res = self.cursor.fetchall()
        for i in res:
            v.append(Grp(i[0]))
        return v
    def setpwd(self, pwd):
        p = sha1(self.name.encode("utf-8"))
        p.update(pwd.encode("utf-8"))
        self.cursor.execute('UPDATE %s SET password = %%s WHERE id = %%s;' % lybcfg.pwd_table_name, (p.hexdigest(), self.uid))
        self.db.commit()
    def setname(self, name):
        try:
            self.cursor.execute('UPDATE %s SET username = %%s WHERE username = %%s;' % lybcfg.pwd_table_name,
                                    (name, self.name))
        except:
            self.db.commit()
            return False
        self.db.commit()
        self.name = name
        return True
    def setdname(self, dname):
        self.cursor.execute('UPDATE %s SET dname = %%s WHERE username = %%s;' % lybcfg.pwd_table_name,
                                    (dname, self.name))
        self.db.commit()
        return True
    @property
    def dname(self):
        self.cursor.execute('SELECT dname FROM %s WHERE username = %%s' % lybcfg.pwd_table_name, (self.name,))
        dn = self.cursor.fetchone()
        if dn:
            return dn[0]
        else:
            raise KeyError(self.name)

class Grp:
    def __init__(self, name):
        self.sess = cherrypy.session
        self.db = self.sess.db
        self.cursor = self.db.cursor()
        self.name = name
    def new(self, dname = None):
        dname = True and dname or self.name
        try:
            self.cursor.execute('INSERT INTO %s (name, dname) VALUES (%%s, %%s);' % lybcfg.grp_table_name,
                                    (self.name, dname))
            
        except:
            self.db.commit()
            return False
        self.db.commit()
        return True
    def delete(self):
        self.cursor.execute('DELETE FROM %s WHERE name = %%s;' % lybcfg.grp_table_name, (self.name,))
        self.db.commit()
    def setname(self, name):
        try:
            self.cursor.execute('UPDATE %s SET name = %%s WHERE name = %%s;' % lybcfg.grp_table_name,
                                    (name, self.name))
        except:
            self.db.commit()
            return False
        self.db.commit()
        self.name = name
        return True
    def setdname(self, dname):
        self.cursor.execute('UPDATE %s SET dname = %%s WHERE name = %%s;' % lybcfg.grp_table_name,
                                    (dname, self.name))
        self.db.commit()
        return True
    @property
    def gid(self):
        self.cursor.execute('SELECT id FROM %s WHERE name = %%s' % lybcfg.grp_table_name, (self.name,))
        gid = self.cursor.fetchone()
        if gid:
            return gid[0]
        else:
            raise KeyError(self.name)
    @property
    def members(self):
        v = []
        self.cursor.execute("""SELECT username FROM {pwd}
                                    WHERE id IN (SELECT uid FROM {mbrsh} WHERE gid = %s)
                                    ORDER BY dname ASC;""".format(pwd = lybcfg.pwd_table_name, mbrsh = lybcfg.mbrsh_table_name), (self.gid,))
        res = self.cursor.fetchall()
        for i in res:
            v.append(Usr(i[0]))
        return v
    @property
    def notmembers(self):
        v = []
        self.cursor.execute("""SELECT username FROM {pwd}
                                    WHERE id NOT IN (SELECT uid FROM {mbrsh} WHERE gid = %s)
                                    ORDER BY dname ASC;""".format(pwd = lybcfg.pwd_table_name, mbrsh = lybcfg.mbrsh_table_name), (self.gid,))
        res = self.cursor.fetchall()
        for i in res:
            v.append(Usr(i[0]))
        return v
    @property
    def dname(self):
        self.cursor.execute('SELECT dname FROM %s WHERE name = %%s' % lybcfg.grp_table_name, (self.name,))
        dn = self.cursor.fetchone()
        if dn:
            return dn[0]
        else:
            raise KeyError(self.name)
    def delmember(self, name):
        self.cursor.execute("""DELETE FROM {mbrsh}
                                    WHERE uid = (SELECT id FROM {pwd} WHERE username = %s)
                                    AND gid = %s;""".format(pwd = lybcfg.pwd_table_name, mbrsh = lybcfg.mbrsh_table_name), (name, self.gid))
        self.db.commit()
    def addmember(self, name):
        self.cursor.execute("""SELECT count(*) FROM {mbrsh}
                                    WHERE uid = (SELECT id FROM {pwd} WHERE username = %s)
                                    AND gid = %s;""".format(pwd = lybcfg.pwd_table_name, mbrsh = lybcfg.mbrsh_table_name), (name, self.gid))
        count = self.cursor.fetchone()[0]
        if count:
            return False
        else:
            self.cursor.execute("""INSERT INTO {mbrsh}
                                        (uid, gid) 
                                        VALUES ((SELECT id FROM {pwd} WHERE username = %s), %s);""".format(mbrsh = lybcfg.mbrsh_table_name, pwd = lybcfg.pwd_table_name),
                                    (name, self.gid))
            self.db.commit()
        return True

class Users:
    def __init__(self):
        self.sess = cherrypy.session
        self.db = self.sess.db
        self.cursor = self.db.cursor()
    @property
    def list(self):
        v = []
        self.cursor.execute('SELECT username FROM %s ORDER BY dname;' % lybcfg.pwd_table_name)
        res = self.cursor.fetchall()
        for i in res:
            v.append(Usr(i[0]))
        return v

class Groups:
    def __init__(self):
        self.sess = cherrypy.session
        self.db = self.sess.db
        self.cursor = self.db.cursor()
    @property
    def list(self):
        v = []
        self.cursor.execute('SELECT name FROM %s ORDER BY dname;' % lybcfg.grp_table_name)
        res = self.cursor.fetchall()
        for i in res:
            v.append(Grp(i[0]))
        return v

import cherrypy
import hashlib
import urllib.parse
import lybmods.lybtools as lybtools
import lybmods.lybpqconn as lybpqconn
from lybmods.lybclasses import Grp

def check_credentials(username, password):
    """Проверяет имя пользователи и пароль.
    Возвращает None при успехе иначе строку с описанием ошибки"""
    cur = lybpqconn.conn.cursor()
    newhash = hashlib.sha1()
    newhash.update(username.encode("utf-8"))
    newhash.update(password.encode("utf-8"))
    cur.execute(lybtools.qChkUserAndPwd, (username, newhash.hexdigest()))
    res = cur.fetchone()[0]
    if res > 0:
        return None
    else:
        return "Incorrect username or password."

def check_auth(*args, **kwargs):
    """A tool that looks in config for 'auth.require'. If found and it
    is not None, a login is required and the entry is evaluated as alist of
    conditions that the user must fulfill"""
    conditions = cherrypy.request.config.get('auth.require', None)
    # format GET params
    get_parmas = urllib.parse.quote(cherrypy.request.request_line.split()[1])
    if conditions is not None:
        username = cherrypy.session.get(lybtools.SESSION_KEY)
        if username:
            cherrypy.request.login = username
            for condition in conditions:
                # A condition is just a callable that returns true orfalse
                if not condition():
                    # Send old page as from_page parameter
                    raise cherrypy.HTTPRedirect("/denied")
        else:
            # Send old page as from_page parameter
            raise cherrypy.HTTPRedirect("/loginpage?from_page=%s" % get_parmas) 
    
#cherrypy.lybtools.auth = cherrypy.Tool('before_handler', check_auth)

def require(*conditions):
    """A decorator that appends conditions to the auth.require config
    variable."""
    def decorate(f):
        if not hasattr(f, '_cp_config'):
            f._cp_config = dict()
        if 'auth.require' not in f._cp_config:
            f._cp_config['auth.require'] = []
        f._cp_config['auth.require'].extend(conditions)
        return f
    return decorate


# Conditions are callables that return True
# if the user fulfills the conditions they define, False otherwise
#
# They can access the current username as cherrypy.request.login
#
# Define those at will however suits the application.

def member_of(groupname):
    def check():
        username = cherrypy.session.get(lybtools.SESSION_KEY, None)
        try:
            if username and username in [x.name for x in Grp(groupname).members]:
                return True
            else:
                return False 
        except KeyError:
            return False
    return check

def name_is(reqd_username):
    return lambda: reqd_username == cherrypy.session.get(lybtools.SESSION_KEY, None)

# These might be handy

def any_of(*conditions):
    """Returns True if any of the conditions match"""
    def check():
        for c in conditions:
            if c():
                return True
        return False
    return check

# By default all conditions are required, but this might still be
# needed if you want to use it inside of an any_of(...) condition
def all_of(*conditions):
    """Returns True if all of the conditions match"""
    def check():
        for c in conditions:
            if not c():
                return False
        return True
    return check


# Controller to provide login and logout actions

class AuthController(object):
    
    def on_login(self, username):
        """Called on successful login"""
    
    def on_logout(self, username):
        """Called on logout"""

    @cherrypy.expose
    def login(self, username=None, password=None, from_page="/"):
        if username is None or password is None:
            raise cherrypy.HTTPRedirect("/")
        
        error_msg = check_credentials(username, password)
        if error_msg:
            raise cherrypy.HTTPRedirect("/loginpage?from_page=" + from_page)
        else:
            cherrypy.session.regenerate()
            cherrypy.session[lybtools.SESSION_KEY] = cherrypy.request.login = username
            self.on_login(username)
            raise cherrypy.HTTPRedirect(from_page or "/")
    
    @cherrypy.expose
    def logout(self, from_page="/"):
        sess = cherrypy.session
        username = sess.get(lybtools.SESSION_KEY, None)
#        for key in sess.keys():
#            del sess[key]
#        sess[lybtools.SESSION_KEY] = None
        sess.regenerate()
        sess.delete()
        if username:
            cherrypy.request.login = None
            self.on_logout(username)
        raise cherrypy.HTTPRedirect("/")
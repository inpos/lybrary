#!/usr/bin/env python3
import sys
sys.path.insert(0, "/path/to/lybrary/root/dir")

from lybmods import lybrary, lybpqconn, lybpqsession
from lybmods.lybformauth import check_auth
from lybmods import lybcfg
import cherrypy
from flipflop import WSGIServer

cherrypy.log.screen = None
#cherrypy.log.access_file='/tmp/lybrary/logs/pyaccess.log'
#cherrypy.log.error_file='/tmp/lybrary/logs/pyerror.log'

lybpqconn.create_schema()
cherrypy.lib.sessions.PgsqlSession = lybpqsession.PgsqlSession
cherrypy.tools.auth = cherrypy.Tool('before_handler', check_auth)
cherrypy.tree.mount(lybrary.Root(), script_name='/lybrary.fcgi')
cherrypy.engine.autoreload.unsubscribe()
cherrypy.server.unsubscribe()
WSGIServer(cherrypy.tree).run()

# -*- coding: utf-8 -*-
from time import tzname
from lybmods.lybformauth import AuthController,  member_of,   any_of
from lybmods.lybclasses import Doc, Cat
import cherrypy
from  lybmods import lybtools
from  lybmods import lybhtdata
from lybmods import lybedit
from lybmods  import lybctl

class Root:
    
    _cp_config = {
        'tools.sessions.on': True,
        'tools.sessions.storage_type'  : 'pgsql',
        'tools.sessions.name' : 'PGSQLSes',
        'tools.sessions.timeout': 120,
        'tools.auth.on': True
    }
    auth = AuthController()
    mdict = lybtools.mdict
    from_page = '/'
    def __init__(self):
        self.edit = lybedit.Edit(self)
        self.ctl = lybctl.Ctl(self)
    @cherrypy.expose
    def index(self):
        self.from_page = '/'
        return self.buildhtml('Архив', lybhtdata.index_html)
    @cherrypy.expose
    def css(self):
        return lybhtdata.style
    @cherrypy.expose
    def poisk(self, search = None, catid = 0):
        if not search or search == '':
            cherrypy.HTTPRedirect("/")
        search.replace('<', '').replace('>', '').replace(';', '').replace(',', '')
        html_cont = '<div align="left">\n<table>\n{html}\n</table></div>'
        html = ''
        cat = Cat(0)
        res = cat.search(search)
        html += '<tr><td><h1>Найдено ' + str(len(res)) + ' документов</h1></td></tr>'
        for did in res:
            doc = Doc(did)
            catid = doc.cat.id
            html += '<tr><td><a href="/get_doc?catid=' + str(catid) + '&doc=' + str(did) + '">' + doc.name + '</a></td>\n<td>(' + self.path(did, doc = True) + ')</td></tr>\n'
        return self.buildhtml('Архив[Запрос: ' + search + ']', html_cont.format(html=html))
    
    @cherrypy.expose
    def loginpage(self, from_page='/'):
        self.from_page = from_page.replace('<', '').replace('>', '').replace(';', '').replace(',', '')
        username = cherrypy.session.get(lybtools.SESSION_KEY, None)
        if username:
            raise cherrypy.HTTPRedirect("/")
        else:
            return self.buildhtml('Архив [Получение доступа]', lybhtdata.login_body)
    @cherrypy.expose
    def denied(self):
        return self.buildhtml('Архив [Доступ закрыт]', lybhtdata.access_denied_body)
    def path(self, oid, doc = False, lcat = False):
        if doc:
            p = Doc(oid).path
        else:
            p = Cat(oid).path
        html = '' 
        for i in p:
            name = Cat(i).name
            if len(name) > 15: name = name[:15] + '...'
            if i > 0: q = '&raquo;'
            else: q = ''
            html += q + '<a href="/category?catid=' + str(i) + '" title="' + Cat(i).name + '"><small><i><b>[' + name + ']</b></i></small></a>'
        if p == []: q = ''
        else: q = '&raquo;'
        if not doc and not lcat: html += q + '<small><i><b>' + Cat(oid).name + '</b></i></small>'
        if lcat: html += q + '<a href="/category?catid=' + str(oid) + '"><small><i><b>[' + Cat(oid).name + ']</b></i></small></a>'
        return html
    @cherrypy.expose
    def category(self, catid = 0):
        catid = int(catid)
        category = Cat(catid)
        html = '<div align="left">' + self.path(catid) + '</div><div  align="center">\n<table>\n'
        if category.catcount: html += '<tr><td><h2>Подразделы:</h2></td>\n'
        for cat in category.categories:
            rec = '<td><b>[<a href="/category?catid=' + str(cat.id) + '" title="Подразделов: ' + str(cat.catcount) + '/Документов: ' + str(cat.doccount) + '">' + cat.name + '</a>]</b></td>\n'
            if any_of(member_of('admins'), member_of('editors'))():
                html += '<tr><form action="/edit/catedit" method="post">\n{rec}<input type="hidden" name="catid" value="'.format(rec = rec) + str(cat.id) + '">\n<td><input type="submit" name="submit" value="Переименовать"></td>\n<td><input type="submit" name="submit" value="Перенести"></td>\n<td><input type="submit" name="submit" value="Удалить"></td>\n</form></tr>\n'
            else:
                html += '<tr>{rec}</tr>'.format(rec = rec)
        if category.catcount and category.doccount: html += '<tr><td>***</td><td>***</td><td>***</td><td>***</td></tr>\n'
        if category.doccount: html += '<tr><td><h2>Документы:</h2></td>\n'
        for doc in category.documents:
            did = doc.id
            rec = '<td><a href="/get_doc?catid=' + str(catid) + '&doc=' + str(did) + '">' + doc.name + '</a></td>\n'
            if any_of(member_of('admins'), member_of('editors'))():
                html += '<tr><form action="/edit/docedit" method="post">\n{rec}<input type="hidden" name="catid" value="'.format(rec = rec) + str(catid) + '">\n<input type="hidden" name="doc" value="' + str(did) + '">\n<td><input type="submit" name="submit" value="Переименовать"></td>\n<td><input type="submit" name="submit" value="Редактировать"></td>\n<td><input type="submit" name="submit" value="Перенести"></td>\n<td><input type="submit" name="submit" value="Удалить"></td>\n</form></tr>\n'
            else:
                html += '<tr>{rec}</tr>'.format(rec = rec)
        html += '</table>\n</div>\n'
        if any_of(member_of('admins'), member_of('editors'))():
            html += '<div align="right">\n<form action="/edit/newdoc" method="post">\n<input type="hidden" name="catid" value="' + str(catid) + '">\n<input type="submit" value="Новый документ">\n</form>\n</div>\n'
            html += '<div align="right">\n<form action="/edit/upl" method="post">\n<input type="hidden" name="catid" value="' + str(catid) + '">\n<input type="submit" value="Загрузить документ">\n</form>\n</div>\n'
            html += '<div align="right">\n<form action="/edit/newcat" method="post">\nНовый раздел\n<input type="hidden" name="catid" value=' + str(catid) + '>\n<input type="text" name="catname">\n<input type="submit" value="Создать">\n</form>\n</div>\n'
        if catid != 0:
            parent = Cat(catid).parent
            html += '<div align="center"><a href="/category?catid=' + str(parent.id) + '"><i>&larr; Обратно в раздел "' + parent.name + '"</i></a></div>\n'
        title = 'Архив[Раздел: ' + category.name + ']'
        return self.buildhtml(title, html)
    @cherrypy.expose
    def get_doc(self, catid = 0, doc = None, plain = False):
        catid = int(catid)
        cat = Cat(catid)
        if not doc: return
        doc = int(doc)
        doco = cat[doc]
        txt = doco.text
        muser = doco.muser
        mtime = doco.mtime.strftime('%d.%m.%Y %H:%M:%S') + ' /' + tzname[0] + '/'
        if plain:
            return txt
        else:
            doct = '<div align="left">' + self.path(doco.id, doc = True) + '</div><div align="right"><a href="/category?catid=' + str(catid) + '">\n<i>&larr; Обратно в раздел "' + cat.name + '"</i>\n</a>\n</div>\n' + txt
            if any_of(member_of('admins'), member_of('editors'))():
                doct += '<div align="right"><form action="/edit/docedit" method="post">\n<input type="hidden" name="catid" value="' + str(catid) + '">\n<input type="hidden" name="doc" value="' + str(doc) + '">\n<input type="submit" name="submit" value="Переименовать">\n<input type="submit" name="submit" value="Редактировать">\n<input type="submit" name="submit" value="Перенести">\n<input type="submit" name="submit" value="Удалить">\n</form></div>\n'
            doct += '<div align="right">\nОтредактировано пользователем: <a href="/ctl/user?name=' + muser.name + '"><b>' + muser.dname + '[' + muser.name + ']</b></a>.</div>\n<div align="right">Дата редактирования: ' + mtime + '\n</div>\n'
            doct += '<br><div align="right"><a href="/category?catid=' + str(catid) + '">\n<i>&larr; Обратно в раздел "' + cat.name + '"</i>\n</a>\n</div>\n'
            return self.buildhtml('Архив[' + doco.name + ']', doct)
    @cherrypy.expose
    def getobj(self, lybsrcobj = None):
        obj = lybtools.getbin(cherrypy.session, lybsrcobj)
        cherrypy.response.headers["Content-Type"] = obj['type']
        return obj['body']
    @cherrypy.expose
    def menu_img(self):
        cherrypy.response.headers["Content-Type"] = 'image/png'
        return lybhtdata.m_i()
    def menupanel(self, mdict):
        menu = lybtools.menu_gen(mdict)
        menu += lybhtdata.form_minisearch
        username = cherrypy.session.get(lybtools.SESSION_KEY, None)
        if username:
            menu += lybhtdata.form_user.format(username=username)
        else:
            menu += lybhtdata.form_auth.format(from_page=self.from_page)
        return menu
    
    def buildhtml(self, title, doc):
        return lybhtdata.html.format(title=title, style='/css',
                                   body=lybhtdata.body.format(menu = self.menupanel(self.mdict), document = doc))


    

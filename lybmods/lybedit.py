# -*- coding: utf-8 -*-
from lybmods.lybformauth import member_of, any_of
from urllib.request import FancyURLopener
from lybmods.lybclasses import Cat
from random import random
from lybmods import lybshared
import lybmods.lybhtdata as lybhtdata
import cherrypy
import lybmods.lybtools as lybtools

class URLOpener(FancyURLopener):
    version = 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.6) Gecko/20100101 Firefox/10.0.6 Iceweasel/10.0.6'

class Edit:
    '''Управление хранилищем'''
    _cp_config = {
        'auth.require': [any_of(member_of('admins'),member_of('editors'))]
    }
    
    def __init__(self, root):
        self.root = root
    @cherrypy.expose
    def index(self):
        cherrypy.HTTPRedirect("/")
    @cherrypy.expose
    def nejs(self):
        return lybhtdata.ne_js()
    
    @cherrypy.expose
    def negif(self):
        response = cherrypy.response
        response.headers['Content-Type'] = 'image/gif'
        return lybhtdata.ne_gif()
    @cherrypy.expose
    def upl(self, catid = 0):
        catid = int(catid)
        cat = Cat(catid)
        catname = cat.name
        return self.root.buildhtml('Архив [Загрузка документа в архив]', lybhtdata.form_upload.format(catid = catid, catname = catname) + '<a href="/category?catid=' + str(catid) + '">\n<i>&larr; Обратно в раздел "' + catname + '"</i>\n</a>\n')
    @cherrypy.expose
    def upload(self, catid = 0, filein=''):
        if catid: catid = int(catid)
        url = filein
        try:
            res = URLOpener().open(url)
        except:
            cat = Cat(catid)
            catname = cat.name
            return self.root.buildhtml('Архив [Загрузка документа в архив]', lybhtdata.form_upload.format(catid = catid, catname = catname) + '<div class="document" style="color: red; ">Ошибка загрузки документа</div><div><a href="/category?catid=' + str(catid) + '">\n<i>&larr; Обратно в раздел "' + catname + '"</i>\n</a>\n</div>')
        return self.root.buildhtml('Архив [Обработка файла закончена]', self.fileproc(catid, res.url, lybtools.ctype(res.headers['Content-Type']), res.read()))
    @cherrypy.expose
    def tmpstore(self, lybsrcobj=None):
        sess = cherrypy.session
        
        cherrypy.response.headers["Content-Type"] = sess[lybsrcobj]['type']
        res = sess[lybsrcobj]['body']
        try:
            return res
        except:
            pass
    def fileproc(self, catid, url, ctype,  htfile):
        if ctype == 'text/html':
            return self.html(catid, url, htfile)
        if ctype == 'text/plain':
            htxt = self.txt(htfile)
            return self.html(catid, url, htxt)
    
    def txt(self, text):
        text = "".join(lybtools.edit_esc.get(c,c) for c in text)
        return text.replace('\n', '<br />\n')
    def html(self, catid, url, htfile, md = None, sub = False, ins = False):
        return lybshared.html(self, catid, url, htfile, md, sub, ins)
    def ne(self, catid, url = None, html = None, md = None, docname = "Новый документ"):
        return lybshared.ne(self, catid, url, html, md, docname)
    @cherrypy.expose
    def newcat(self, catid = 0, catname = None):
        catid = int(catid)
        category = Cat(catid)
        if not catname or catname == '':
            return self.root.buildhtml('Архив[Ошибка создания раздела]', '<p>Имя раздела не должно быть пустым</p>\n<div align="center"><a href="/category?catid=' + str(category.id) + '">\n<i>&larr; Обратно в раздел "' + category.name + '"</i>\n</a>\n</div>')
        catname = catname.strip()
        if category.newcat(catname):
            return self.root.category(catid = catid)
        else:
            return self.root.buildhtml('Архив[Ошибка создания раздела]', '<p>Ошибка создания раздела "' + catname + '"</p>\n<div align="center"><a href="/category?catid=' + str(category.id) + '">\n<i>&larr; Обратно в раздел "' + category.name + '"</i>\n</a>\n</div>')
    @cherrypy.expose
    def catrename(self, catid = None, catname = None):
        if catid: catid = int(catid)
        if not catname: return self.catedit(submit = 'Переименовать', catid = catid, err = '!!!Пустое имя раздела!!!')
        catname = catname.strip()
        cat = Cat(catid)
        parent = cat.parent
        for subc in parent.categories:
            if subc.name == catname: return self.catedit(submit = 'Переименовать', catid = catid, err = '!!!В разделе "' + parent.name + '" есть подраздел с именем "' + catname + '"!!!')
        if catname == cat.name:
            return self.catedit(submit = 'Переименовать', catid = catid, err = '!!!Исходное имя равно новому!!!')
        cat.setname(catname)
        return self.root.category(catid = parent.id)
    @cherrypy.expose
    def catdelete(self, catid = None):
        if catid: catid = int(catid)
        cat = Cat(catid)
        parent = cat.parent
        cat.delete()
        return self.root.category(catid = parent.id)
    @cherrypy.expose
    def catmove(self, catid = None, toid = None):
        if not catid: return
        if not toid: return self.catedit(submit = 'Перенести', catid = catid, err = '!!!Не выбран раздел!!!')
        catid = int(catid)
        toid = int(toid)
        cat = Cat(catid)
        tocat = Cat(toid)
        if catid == toid: return self.catedit(submit = 'Перенести', catid = catid, err = '!!!Нельзя перенести себя в себя!!!')
        if toid == cat.parent.id: return self.catedit(submit = 'Перенести', catid = catid, err = '!!!Раздел уже в этом месте!!!')
        if cat.name in [x.name for x in tocat.categories]: return self.catedit(submit = 'Перенести', catid = catid, err = '!!!В разделе "' + cat.parent.name + '" уже есть подраздел с таким именем!!!')
        cat.setparentid(toid)
        return self.root.category(catid = cat.parent.id)
    @cherrypy.expose
    def catedit(self, submit = None, catid = None, err = ''):
        if submit and catid:
            catid = int(catid)
            cat = Cat(catid)
            catname = cat.name
            parent = cat.parent
            if submit == 'Переименовать':
                html = '<div align="center"><form action="/edit/catrename" method="post"><input type="hidden" name="catid" value=' + str(catid) + '>Сменить имя раздела "' + catname + '" на <input type="text" name="catname" value="' + catname + '"><input type="submit" value="Готово"></form></div><div align="center"><a href="/category?catid=' + str(parent.id) + '"><i>&larr; Обратно в раздел "' + parent.name + '"</i></a></div>'
                title, document = ('Архив[Переименовать раздел "' + catname + '"]' + err, html)
            elif submit == 'Перенести':
                l = '<select name="toid">\n{lbody}</select>\n'
                lo = '<option value={id}>{name}</option>\n'
                lopts = ''
                def lgen(lopts, mod = '', cid = 0):
                    c = Cat(cid)
                    lopts += lo.format(id = cid, name = mod + c.name)
                    for subcat in c.categories:
                        if subcat.id == catid: continue
                        lopts = lgen(lopts, mod = mod + '...', cid = subcat.id)
                    return lopts
                lopts = lgen(lopts)
                sel = l.format(lbody = lopts)
                html = '<div align="center"><form action="/edit/catmove" method="post"><input type="hidden" name="catid" value=' + str(catid) + '>Переместить раздел "' + catname + '" в\n{sel}<input type="submit" value="Готово"></form></div><div align="center"><a href="/category?catid='.format(sel = sel) + str(parent.id) + '"><i>&larr; Обратно в раздел "' + parent.name + '"</i></a></div>'
                title, document = ('Архив[Переместить раздел "' + catname + '"]' + err, html)
            elif submit == 'Удалить':
                html = '<div align="center"><form action="/edit/catdelete" method="post"><input type="hidden" name="catid" value="' + str(catid) + '">Действительно удалить раздел "' + catname + '"?<br>Все хранящиеся в нём подразделы и документы будут перенесены в родительский раздел.<br><input type="submit" value="Удалить"></form><div align="center"><a href="/category?catid=' + str(parent.id) + '"><i>&larr; Обратно в раздел "' + parent.name + '"</i></a></div>'
                title, document = ('Архив[Удалить раздел "' + catname + '"]', html)
            return self.root.buildhtml(title, document)
    @cherrypy.expose
    def insert_doc(self, catid = 0, url = None, html = None, doc_name = '', md = None):
        return lybshared.insert_doc(self, catid, url, html, doc_name, md)
    @cherrypy.expose
    def docedit(self, catid = None, doc = None, submit = None, err = ''):
        if catid: catid = int(catid)
        if doc: doc = int(doc)
        if not doc or not submit: return
        cat = Cat(catid)
        doco = cat[doc]
        catname = cat.name
        docname = doco.name
        if submit == 'Редактировать':
            return self.root.buildhtml('Архив[Редактирование документа "' + docname + '"]', self.html(catid, '/', self.root.get_doc(doc=doc, catid=catid, plain=True), md = str(doc)))
        if submit == 'Переименовать':
                html = '<div align="center">\n<form action="/edit/docrename" method="post">\n<input type="hidden" name="catid" value=' + str(catid) + '>\n<input type="hidden" name="doc" value=' + str(doc) + '>\nСменить имя документа "' + docname + '" на <input type="text" name="doc_name" value="' + docname + '">\n<input type="submit" value="Готово">\n</form>\n</div>\n<div align="center">\n<a href="/category?catid=' + str(catid) + '">\n<i>&larr; Обратно в раздел "' + catname + '"</i>\n</a>\n</div>'
                title, document = ('Архив[Переименовать документ "' + doco.name + '"]' + err, html)
        elif submit == 'Удалить':
            shtml = '<div align="center">\nУдалить документ "' + docname + '"?\n<form action="/edit/docdelete" method="post">\n<input type="hidden" name="catid" value=' + str(catid) + '>\n<input type="hidden" name="doc" value="' + str(doc) + '">\n<input type="submit" value="Удалить документ">\n</form>\n<br>\n<a href="/category?catid=' + str(catid) + '">\n<i>&larr; Обратно в раздел "' + catname + '"</i>\n</a>\n</div>'
            title, document = ('Архив[Удалить Документ "' + doco.name + '"]' + err, shtml)
        elif submit == 'Перенести':
            if len(Cat(0).categories) == 0:
                shtml = '<div align="center">Других разделов нет\n<br><a href="/category?catid=' + str(catid) + '"><i>&larr; Обратно в раздел "' + catname + '"</i></a></div>'
            else:
                l = '<select name="toid">\n{lbody}</select>\n'
                lo = '<option value={id}>{name}</option>\n'
                lopts = ''
                def lgen(lopts, mod = '', cid = 0):
                    c = Cat(cid)
                    lopts += lo.format(id = cid, name = mod + c.name)
                    for subcat in c.categories:
                        lopts = lgen(lopts, mod = mod + '...', cid = subcat.id)
                    return lopts
                lopts = lgen(lopts)
                sel = l.format(lbody = lopts)
                shtml = '<div align="center">Перенести документ "' + docname + '"<form action="/edit/docmove" method="post">\n<input type="hidden" name="catid" value=' + str(catid) + '><input type="hidden" name="doc" value="' + str(doc) + '">в категорию ' + sel + ' ?<br><br><input type="submit" value="Перенести"></form>\n<br><a href="/category?catid=' + str(catid) + '"><i>&larr; Обратно в раздел "' + catname + '"</i></a></div>'
            title, document = ('Архив[Перенос документов]' + err, shtml)
        return self.root.buildhtml(title, document)
    @cherrypy.expose
    def docdelete(self, catid = None, doc = None):
        if not catid or not doc: return
        catid = int(catid)
        doc = int(doc)
        cat = Cat(catid)
        try:
            del cat[doc]
        except:
            doco = cat[doc]
            docname = doco.name
            return self.root.buildhtml('Архив[Документ "' + docname + '" не удалён]', '<div align="center">Документ "' + docname + '" не удалён.<br><a href="/category?catid=' + str(catid) + '"><i>&larr; Обратно в раздел "' + cat.name + '"</i></a></div>')
        return self.root.category(catid = catid)
    @cherrypy.expose
    def docrename(self, catid = None, doc = None, doc_name = None):
        if catid: catid = int(catid)
        if not doc_name or not doc: return self.docedit(submit = 'Переименовать', catid = catid, doc = doc, err = '!!!Пустое имя документа!!!')
        doc = int(doc)
        doc_name = doc_name.strip()
        cat = Cat(catid)
        doco = cat[doc]
        if doc_name == doco.name:
            return self.docedit(submit = 'Переименовать', catid = catid, doc = doc, err = '!!!Исходное имя равно новому!!!')
        for docs in cat.documents:
            if docs.name == doc_name: return self.docedit(submit = 'Переименовать', catid = catid, doc = doc, err = '!!!В разделе "' + cat.name + '" есть документ с именем "' + doc_name + '"!!!')
        doco.setname(doc_name)
        return self.root.category(catid = catid)
    @cherrypy.expose
    def newdoc(self, catid = 0):
        url = 'http://new.doc/' + (str(random() * int(random() * 10)) + str(random() * int(random() * 10)) + str(random() * int(random() * 10))).replace('.', '')
        return self.root.buildhtml('Архив[Новый документ]', self.fileproc(catid, url, 'text/html', '<body><br></body>'))
    @cherrypy.expose
    def docmove(self, catid = None, doc = None, toid = None):
        if not catid or not doc: return
        if not toid: return self.docedit(submit = 'Перенести', catid = catid, doc = doc, err = '!!!Не выбран раздел!!!')
        catid = int(catid)
        doc = int(doc)
        toid = int(toid)
        cat = Cat(catid)
        tocat = Cat(toid)
        doco = cat[doc]
        catname = cat.name
        tocatname = tocat.name
        docname = doco.name
        if catid == toid: return self.docedit(submit = 'Перенести', catid = catid, doc = doc, err = '!!!Документ "' + docname + '" уже в разделе "' + catname + '"!!!')
        if toid == catid: return self.docedit(submit = 'Перенести', catid = catid, doc = doc, err = '!!!Раздел уже в этом месте!!!')
        if doc in list(tocat.keys()): return self.docedit(submit = 'Перенести', catid = catid, doc = doc, err = '!!!В разделе "' + tocatname + '" уже есть документ с таким содержимым!!!')
        if tocat.docidbyname(doco.name): return self.docedit(submit = 'Перенести', catid = catid, doc = doc, err = '!!!В разделе "' + tocatname + '" уже есть документ с именем"' + docname + '"!!!')
        doco.setcatid(toid)
        return self.root.category(catid = catid)
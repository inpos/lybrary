# -*- coding: utf-8 -*-
import cherrypy
from lybmods.lybformauth import member_of, name_is, require
from lybmods.lybclasses import Users, Groups, Usr, Grp
import lybmods.lybtools as lybtools
import lybmods.lybhtdata as lybhtdata
class Ctl:
    _cp_config = {
        'auth.require': []
        }
    def __init__(self, root):
        self.root = root
    @cherrypy.expose
    def index(self):
        raise cherrypy.HTTPRedirect("/")
    @cherrypy.expose
    def user(self, name = None, err = ''):
        name = True and name or cherrypy.session.get(lybtools.SESSION_KEY, None)
        html = ''
        usr = Usr(name)
        dname = usr.dname
        grps = usr.groups
        if len(grps):
            html += '<tr><td><b>Пользователь "' + dname + '[' + name + ']" находится в следующих группах:</b></td></tr>'
            for grp in grps:
                if member_of('admins')():
                    html += '<tr><form action="/ctl/grpfromusr"><td></td><td><a href="/ctl/group?name=' + grp.name + '">' + grp.dname + '[' + grp.name + ']</a></td><input type="hidden" name="uname" value="' + name + '"><input type="hidden" name="gname" value="' + grp.name + '"><td><input type="submit" value="Удалить из этой группы"></td></form></tr>\n'
                else:
                    html += '<tr><td>' + grp.dname + '[' + grp.name + ']</td></tr>\n'
        else: html += '<tr><td><b>Пользователь "' + dname + '[' + name + ']"  не находится ни в каких группах</b></td></tr>'
        if member_of('admins')():
            l = '<select name="gname">\n{lbody}</select>\n'
            lo = '<option value={gname}>{dname}[{gname}]</option>\n'
            lopts = ''
            fg = usr.fgroups
            if len(fg):
                for g in usr.fgroups:
                    lopts += lo.format(gname = g.name, dname = g.dname)
                sel = l.format(lbody = lopts)
                html += '<tr>\n<form action="/ctl/grptousr">\n<td>Добавить пользователя в группу: <input type="hidden" name="uname" value="' + name + '">\n{sel}<input type="submit" value="Добавить">\n</td>\n</form>\n</tr>\n'.format(sel = sel)
        if member_of('admins')() or name_is(name)():
            html += '<tr><form action="/ctl/setpwd"><input type="hidden" name="name" value="' + name + '"><td>Новый пароль<input type="password" name="password"><input type="submit" value="Установить"></td></form></tr>'
        return self.root.buildhtml('Панель управления[Пользователь "' + name + '"]' + err, lybhtdata.user_body.format(name = name, groups = html))
    @cherrypy.expose
    def setpwd(self, name = None, password = ''):
        if password == '': return self.user(name = name, err = '!!!Пароль не может быть пустым!!!')
        name = True and name or cherrypy.session.get(lybtools.SESSION_KEY, None)
        if not member_of('admins')() and not name_is(name)(): raise cherrypy.HTTPRedirect("/denied")
        usr = Usr(name)
        usr.setpwd(password)
        return self.user(name, '<Пароль установлен>')
    @cherrypy.expose
    @require(member_of('admins'))
    def useredit(self, submit = None, name = None, err = ''):
        if submit and name:
            usr = Usr(name)
            dname = usr.dname
            if submit == 'Переименовать':
                html = '<div align="center"><form action="/ctl/renameuser" method="post"><input type="hidden" name="name" value=' + name + '>\nНовое имя пользователя\n<input type="text" name="newname" value="' + name + '">\nНовое отображаемое имя<input type="text" name="newdname" value="' + dname + '"><input type="submit" value="Готово"></form></div><div align="center"><a href="/ctl/users"><i>&larr; Обратно к списку пользователей</i></a></div>'
                title, document = ('Панель управления[Переименовать пользователя "' + name + '"]', html)
            elif submit == 'Удалить':
                html = '<div align="center"><form action="/ctl/deleteuser" method="post"><input type="hidden" name="name" value="' + name + '">Действительно удалить пользователея "' + name + '"?<br><input type="submit" value="Удалить"></form><div align="center"><a href="/ctl/users"><i>&larr; Обратно к списку пользователей</i></a></div>'
                title, document = ('Панель управления[Удалить пользователя "' + name + '"]', html)
            return self.root.buildhtml(title + err, document)
    @cherrypy.expose
    @require(member_of('admins'))
    def renameuser(self, name = None, newname = '', newdname = ''):
        if newname == '': return self.useredit('Переименовать', name, '!!!Имя пользователя не может быть пустым!!!')
        if newdname == '': newdname = newname
        name = True and name or cherrypy.session.get(lybtools.SESSION_KEY, None)
        usr = Usr(name)
        dname = usr.dname
        if name == newname and dname == newdname: return self.useredit('Переименовать', name, '!!!Данные не изменены!!!')
        if name != newname:
            if not usr.setname(newname):return self.useredit('Переименовать', name, '!!!Ошибка. Возможно пользователь с таким именем уже существует!!!')
        if dname != newdname:
            usr.setdname(newdname)
        return self.users()
    @cherrypy.expose
    @require(member_of('admins'))
    def deleteuser(self, name = None):
        if not name: return
        if name_is(name)(): return self.useredit('Удалить', name, '!!!Нельзя удалить своего же пользователея!!!')
        usr = Usr(name)
        if 'admins' in usr.groups and len(Grp('admins').members) == 1:
            return self.useredit('Удалить', name, '!!!Нельзя удалить единственного администратора!!!')
        try:
            usr.delete()
        except:
            pass
        return self.users()
    @cherrypy.expose
    @require(member_of('admins'))
    def users(self):
        usrs = Users()
        html = '<div  align="center">\n<table>\n'
        html += '<tr><td><b><u>Отображаемое имя|</u></b></td><td><b><u>|Имя пользователя</u></b></td>\n'
        for user in usrs.list:
            name = user.name
            dname = user.dname
            rec = '<td><a href="/ctl/user?name=' + name + '">' + dname + '</a></td><td><a href="/ctl/user?name=' + name + '">[' + name + ']</a></td>\n'
            html += '<tr><form action="/ctl/useredit" method="post">\n{rec}<input type="hidden" name="name" value="'.format(rec = rec) + name + '">\n<td><input type="submit" name="submit" value="Переименовать"></td>\n<td><input type="submit" name="submit" value="Удалить"></td>\n</form></tr>\n'
        html += '</table>\n</div>\n'
        html += '<div align="right">\n<form action="/ctl/newuser" method="post">\n<input type="submit" value="Создать пользователя">\n</form>\n</div>\n'
        return self.root.buildhtml('Панель управления[Пользователи]', html)
    @cherrypy.expose
    @require(member_of('admins'))
    def groups(self):
        grps = Groups()
        html = '<div  align="center">\n<table>\n'
        html += '<tr><td><b><u>Отображаемое имя|</u></b></td><td><b><u>|Имя группы</u></b></td>\n'
        for grp in grps.list:
            name = grp.name
            dname = grp.dname
            rec = '<td><a href="/ctl/group?name=' + name + '">' + dname + '</a></td><td><a href="/ctl/group?name=' + name + '">[' + name + ']</a></td>\n'
            if name == 'admins' or name == 'editors': html += '<tr>%s</tr>' % rec
            else: html += '<tr><form action="/ctl/groupedit" method="post">\n{rec}<input type="hidden" name="name" value="'.format(rec = rec) + name + '">\n<td><input type="submit" name="submit" value="Переименовать"></td>\n<td><input type="submit" name="submit" value="Удалить"></td>\n</form></tr>\n'
        html += '</table>\n</div>\n'
        html += '<div align="right">\n<form action="/ctl/newgroup" method="post">\n<input type="submit" value="Создать группу">\n</form>\n</div>\n'
        return self.root.buildhtml('Панель управления[Группы]', html)
    @cherrypy.expose
    @require(member_of('admins'))
    def newuser(self, err = ''):
        html = '<div  align="left">\n<table>\n'
        html += '<tr><form action="/ctl/createuser" method="post">\n<td>Имя пользователя<input type="input" name="name"></td>\n<td>Отображаемое имя<input type="input" name="dname"></td>\n<td>Пароль<input type="password" name="password"></td>\n<td><input type="submit" value="Создать"></td>\n</form></tr>\n'
        html += '</table>\n</div>\n'
        html += '<div align="right"><a href="/ctl/users">\n<i>&larr; Обратно в список пользователей</i>\n</a>\n</div>\n'
        return self.root.buildhtml('Панель управления[Пользователи]' + err, html)
    @cherrypy.expose
    @require(member_of('admins'))
    def newgroup(self, err = ''):
        html = '<div  align="left">\n<table>\n'
        html += '<tr><form action="/ctl/creategroup" method="post">\n<td>Имя группы<input type="input" name="name"></td>\n<td>Отображаемое имя<input type="input" name="dname"></td>\n<td><input type="submit" value="Создать"></td>\n</form></tr>\n'
        html += '</table>\n</div>\n'
        html += '<div align="right"><a href="/ctl/groups">\n<i>&larr; Обратно в список групп</i>\n</a>\n</div>\n'
        return self.root.buildhtml('Панель управления[Группы]' + err, html)
    @cherrypy.expose
    @require(member_of('admins'))
    def createuser(self, name = '', dname = '', password = ''):
        if name == '' or password == '': return self.newuser(err = '!!!Имя пользователя или пароль не могут быть пустыми!!!')
        if dname == '': dname = name
        usr = Usr(name)
        if usr.new(password, dname): return self.user(name)
        else: return self.newuser(err = '!!!Ошибка. Возможно пользователь с таким именем уже существует!!!')
    @cherrypy.expose
    @require(member_of('admins'))
    def creategroup(self, name = '', dname = ''):
        if name == '': return self.newuser(err = '!!!Имя группы не может быть пустыми!!!')
        if dname == '': dname = name
        grp = Grp(name)
        if grp.new(dname): return self.group(name)
        else: return self.newgroup(err = '!!!Ошибка. Возможно группа с таким именем уже существует!!!')
    @cherrypy.expose
    @require(member_of('admins'))
    def group(self, name = None, err = ''):
        if not name: return
        html = ''
        grp = Grp(name)
        dname = grp.dname
        members = grp.members
        if len(members):
            html += '<tr><td><b>В группе "' + dname + '[' + name + ']" находятся следующие пользователи:</b></td></tr>'
            for member in members:
                html += '<tr><form action="/ctl/usrfromgrp"><td></td><td><a href="/ctl/user?name=' + member.name + '">' + member.dname + '[' + member.name +  ']</a></td><input type="hidden" name="uname" value="' + member.name + '"><input type="hidden" name="gname" value="' + name + '"><td><input type="submit" value="Удалить из группы"></td></form></tr>\n'
        else: html += '<tr><td><b>В группе "' + dname + '[' + name + ']"  нет ни одного пользователя</b></td></tr>'
        l = '<select name="uname">\n{lbody}</select>\n'
        lo = '<option value={uname}>{udname}[{uname}]</option>\n'
        lopts = ''
        nm = grp.notmembers
        if len(nm):
            for u in nm:
                lopts += lo.format(uname = u.name, udname = u.dname)
            sel = l.format(lbody = lopts)
            html += '<tr>\n<form action="/ctl/usrtogrp">\n<td>Добавить в эту группу пользователя: <input type="hidden" name="gname" value="' + name + '">\n{sel}<input type="submit" value="Добавить">\n</td>\n</form>\n</tr>\n'.format(sel = sel)
        return self.root.buildhtml('Панель управления[Группа "' + name + '"]' + err, lybhtdata.group_body.format(name = name, groups = html))
    @cherrypy.expose
    @require(member_of('admins'))
    def groupedit(self, submit = None, name = None, err = ''):
        if submit and name:
            grp = Grp(name)
            dname = grp.dname
            if submit == 'Переименовать':
                html = '<div align="center"><form action="/ctl/renamegroup" method="post"><input type="hidden" name="name" value=' + name + '>\nНовое имя группы\n<input type="text" name="newname" value="' + name + '">\nНовое отображаемое имя<input type="text" name="newdname" value="' + dname + '"><input type="submit" value="Готово"></form></div><div align="center"><a href="/ctl/groups"><i>&larr; Обратно к списку групп</i></a></div>'
                title, document = ('Панель управления[Переименовать группу "' + name + '"]' + err, html)
            elif submit == 'Удалить':
                html = '<div align="center"><form action="/ctl/deletegroup" method="post"><input type="hidden" name="name" value="' + name + '">Действительно удалить группу "' + name + '"?<br><input type="submit" value="Удалить"></form><div align="center"><a href="/ctl/groups"><i>&larr; Обратно к списку групп</i></a></div>'
                title, document = ('Панель управления[Удалить группу "' + name + '"]', html)
            return self.root.buildhtml(title + err, document)
    @cherrypy.expose
    @require(member_of('admins'))
    def renamegroup(self, name = None, newname = '', newdname = ''):
        if newname == '': return self.groupedit('Переименовать', name, '!!!Имя группы не может быть пустым!!!')
        if not name or name =='' or name == 'admins' or name == 'editors': return
        if newdname == '': newdname = newname
        grp = Grp(name)
        dname = grp.dname
        if name == newname and dname == newdname: return self.groupedit('Переименовать', name, '!!!Данные не изменены!!!')
        if name != newname:
            if not grp.setname(newname): return self.groupedit('Переименовать', name, '!!!Ошибка. Возможно группа с таким именем уже существует!!!')
        if dname != newdname:
            grp.setdname(newdname)
        return self.group()
    @cherrypy.expose
    @require(member_of('admins'))
    def deletegroup(self, name = None):
        if not name or name =='' or name == 'admins' or name == 'editors': return
        grp = Grp(name)
        try:
            grp.delete()
        except:
            pass
        return self.groups()
    @cherrypy.expose
    @require(member_of('admins'))
    def grpfromusr(self, uname = '', gname = ''):
        if uname == '' or gname == '': return
        grp = Grp(gname)
        if gname == 'admins' and len(Grp('admins').members) == 1:
            return self.user(uname, '!!!Нельзя удалить единственного пользователя из группы администраторов!!!')
        grp.delmember(uname)
        return self.user(uname)
    @cherrypy.expose
    @require(member_of('admins'))
    def usrfromgrp(self, uname = '', gname = ''):
        if uname == '' or gname == '': return
        grp = Grp(gname)
        if gname == 'admins' and len(Grp('admins').members) == 1:
            return self.group(gname, '!!!Нельзя удалить единственного пользователя из группы администраторов!!!')
        grp.delmember(uname)
        return self.group(gname)
    @cherrypy.expose
    @require(member_of('admins'))
    def grptousr(self, uname ='', gname = ''):
        if uname == '' or gname == '': return
        grp = Grp(gname)
        if not grp.addmember(uname): return self.user(uname, '!!!Пользователь уже в группе "' + grp.dname + '[' + gname + ']"!!!')
        return self.user(uname)
    @cherrypy.expose
    @require(member_of('admins'))
    def usrtogrp(self, uname ='', gname = ''):
        if uname == '' or gname == '': return
        grp = Grp(gname)
        if not grp.addmember(uname): return self.group(gname, '!!!Пользователь "' + Usr(uname).dname + '[' + uname + ']"уже в этой группе!!!')
        return self.group(uname)

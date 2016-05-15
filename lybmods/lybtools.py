import lybmods.lybhtdata as lybhtdata
from base64 import b64encode, b64decode, encodestring, decodestring, urlsafe_b64encode, urlsafe_b64decode
import lybmods.lybcfg as lybcfg
from lxml import etree
from chardet import detect

SESSION_KEY = '_cp_username'
mdict = {
                 'Меню':[
                            [
                             'Хранилище',
                             '/category',
                             None
                             ],
                             [
                              'Панель управления',
                              '#',
                              {
                                'Пользователи':'/ctl/users',
                                'Группы': '/ctl/groups'
                               }
                              ]
                         ]
        }
edit_esc = {
     "&": "&amp;amp;",
     '"': "&amp;quot;",
     "'": "&amp;apos;",
     ">": "&amp;gt;",
     "<": "&amp;lt;",
     }
def menu_gen(mdict):
    m = ''
    sm = ''
    smi = ''
    for menu in list(mdict.keys()):
        if type(mdict[menu]) is list:
            for submenu in mdict[menu]:
                if type(submenu[2]) is dict:
                    for item in list(submenu[2].keys()):
                        smi = smi + lybhtdata.submenuitem.format(name = item, url = submenu[2][item])
                    sm = sm + lybhtdata.submenu.format(name = submenu[0], url = submenu[1],
                                                    submenuitem = lybhtdata.submenuitem_container.format(submenuitem = smi))
                    smi = ''
                else:
                    sm = sm + lybhtdata.submenuitem.format(name = submenu[0], url = submenu[1],
                                                    submenuitem = '')
            m = m + lybhtdata.menu.format(name = menu, submenu = sm)
            sm = ''
        else:
            m = m + lybhtdata.menu.format(name = menu, submenu = '')
    return lybhtdata.menu_container.format(menu = m)

def b64dec(self, data, ascii=False):
    if ascii:
        return urlsafe_b64decode(data)
    else:
        return b64decode(data)
def b64enc(data, ascii=False):
    if ascii:
        return urlsafe_b64encode(data)
    else:
        return b64encode(data)
def b64decstr(data):
    return decodestring(data)
def b64encstr(data):
    return encodestring(data)

def ctype(c_t):
    t = c_t.split(';')
    return t[0]

def htfile_tounicode(htfile):
    if type(htfile) is str:
        return htfile
    ct = etree.HTML(htfile).xpath('//meta/@http-equiv')
    enc = detect(htfile)['encoding']
    if ct != []:
        c_t = ct[0].getparent().attrib['content']
        if 'charset' in c_t:
            enc = c_t.split('charset')[1].strip().split('=')[1].strip().split(' ')[0]
    return str(htfile, enc, 'ignore')

def getbin(sess, hhash):
    cur = sess.db.cursor()
    cur.execute('SELECT type, body FROM %s WHERE hash = %%s;' % lybcfg.bin_table_name, (hhash,))
    res = cur.fetchone()
    return {'type': res[0], 'body': res[1].tobytes()}

qChkUserAndPwd = """\
SELECT COUNT(*) FROM auth_passwd
    WHERE username=%s AND password=%s;"""
qChkUserInGroup = """\
SELECT COUNT(*) FROM auth_membership AS m 
    WHERE m.uid=(
        SELECT id FROM auth_passwd AS p
            WHERE p.username=%s
        )
    AND m.gid=(
        SELECT id FROM auth_group AS g
            WHERE g.name=%s
        );"""
SESS_SCHEMA = """\
CREATE TABLE {sess} (
    id VARCHAR(40),
    expiration_time TIMESTAMP,
    CONSTRAINT {sess}_pkey PRIMARY KEY (id)
);
CREATE TABLE {sessdata} (
    sid VARCHAR(40),
    key VARCHAR,
    value BYTEA
);
CREATE INDEX {sessdata}_idx on {sessdata} USING btree(sid);
CREATE OR REPLACE FUNCTION del_{sessdata}() RETURNS trigger AS
'
BEGIN
    DELETE FROM {sessdata} where sid=old.id;
    RETURN old;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER on_{sess}_del
    AFTER DELETE
    ON {sess} FOR EACH ROW
    EXECUTE PROCEDURE del_{sessdata}();
""".format(sess = lybcfg.sess_table_name, sessdata = lybcfg.sess_data_table_name)

AUTH_SCHEMA = """\
CREATE TABLE {grp} (
    id serial NOT NULL, 
    name varchar(40) NOT NULL UNIQUE, 
    dname varchar(40) NOT NULL,
    CONSTRAINT group_pkey PRIMARY KEY (id)
);
CREATE TABLE {pwd} (
    id serial NOT NULL,
    username varchar(40) NOT NULL UNIQUE,
    dname varchar(40) NOT NULL,
    password varchar(40) NOT NULL,
    CONSTRAINT passwd_pkey PRIMARY KEY (id)
);
CREATE TABLE {mbrsh} (
    id serial NOT NULL,
    uid integer,
    gid integer,
    CONSTRAINT membership_pkey PRIMARY KEY (id)
);
CREATE OR REPLACE FUNCTION del_uid() RETURNS trigger AS
'
BEGIN
    DELETE FROM {mbrsh} where uid=old.id;
    RETURN old;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER on_{pwd}_del
    AFTER DELETE
    ON {pwd} FOR EACH ROW
    EXECUTE PROCEDURE del_uid();
CREATE OR REPLACE FUNCTION del_gid() RETURNS trigger AS
'
BEGIN
    DELETE FROM {mbrsh} where gid=old.id;
    RETURN old;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER on_{grp}_del
    AFTER DELETE
    ON {grp} FOR EACH ROW
    EXECUTE PROCEDURE del_uid();
INSERT INTO {pwd}
    (username, dname, password)
    VALUES ('admin', 'Администратор', 'dd94709528bb1c83d08f3088d4043f4742891f4f');
INSERT INTO {grp}
    (name, dname)
    VALUES ('admins', 'Администраторы');
INSERT INTO {grp}
    (name, dname)
    VALUES ('editors', 'Редакторы');
INSERT INTO {mbrsh}
    (uid, gid) 
    VALUES ((SELECT id FROM {pwd} WHERE username = 'admin'), (SELECT id FROM {grp} WHERE name = 'admins'));
""".format(grp = lybcfg.grp_table_name, pwd = lybcfg.pwd_table_name, mbrsh = lybcfg.mbrsh_table_name)

CAT_SCHEMA = """\
CREATE TABLE {cat} (
    id bigserial NOT NULL,
    name varchar(512) NOT NULL,
    parent bigint,
    CONSTRAINT {cat}_pkey PRIMARY KEY (id)
    );
CREATE OR REPLACE FUNCTION update_{cat}_in_{doc}() RETURNS trigger AS
'
BEGIN
    UPDATE {doc} SET catid = old.parent WHERE catid = old.id;
    UPDATE {cat} SET parent = old.parent WHERE parent = old.id;
    RETURN old;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER on_{cat}_del
    AFTER DELETE
    ON {cat} FOR EACH ROW
    EXECUTE PROCEDURE update_{cat}_in_{doc}();
CREATE INDEX name_idx ON {cat} USING gin(to_tsvector('russian', name));
""".format(cat = lybcfg.cat_table_name, doc = lybcfg.doc_table_name)
DOC_SCHEMA = """\
CREATE TABLE {doc} (
    id bigserial NOT NULL,
    name varchar(512) NOT NULL,
    catid bigint NOT NULL,
    muser varchar(40) NOT NULL,
    mtime timestamp without time zone DEFAULT now() NOT NULL,
    body text,
    fts_index tsvector,
    CONSTRAINT {doc}_pkey PRIMARY KEY (id)
    );
CREATE INDEX fts_idx on {doc} USING gin(fts_index);

CREATE OR REPLACE FUNCTION del_{docbin}() RETURNS trigger AS
'
BEGIN
    DELETE FROM {docbin} WHERE docid=old.id;
    RETURN old;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER on_{doc}_del
    AFTER DELETE
    ON {doc} FOR EACH ROW
    EXECUTE PROCEDURE del_{docbin}();
CREATE FUNCTION update_fts_index() RETURNS trigger AS $$
  BEGIN
    new.fts_index :=
      setweight(to_tsvector('pg_catalog.russian', coalesce(new.name,'')), 'A') ||
      setweight(to_tsvector('pg_catalog.russian', coalesce(new.body,'')), 'B');
    RETURN new;
  END
$$ LANGUAGE plpgsql;
CREATE TRIGGER fts_index_update
    BEFORE INSERT OR UPDATE
    ON {doc} FOR EACH ROW
    EXECUTE PROCEDURE update_fts_index();
""".format(doc = lybcfg.doc_table_name, docbin = lybcfg.docbin_table_name)
#CATDOC_SCHEMA = """\
#CREATE TABLE {catdoc} (
#    id serial NOT NULL,
#    docid bigint NOT NULL,
#    catid bigint NOT NULL,
#    CONSTRAINT {catdoc}_pkey PRIMARY KEY (id)
#    );
#CREATE OR REPLACE FUNCTION del_orphaned_{doc}() RETURNS trigger AS
#'
#BEGIN
#    PERFORM * FROM {catdoc} WHERE docid = old.docid;
#    IF NOT FOUND THEN
#        DELETE FROM {doc} where id=old.docid;
#        RETURN old;
#    END IF;
#    RETURN old;
#END
#'
#LANGUAGE plpgsql;
#CREATE TRIGGER on_{catdoc}_del
#    AFTER DELETE
#    ON {catdoc} FOR EACH ROW
#    EXECUTE PROCEDURE del_orphaned_{doc}();
#""".format(catdoc = lybcfg.catdoc_table_name, doc = lybcfg.doc_table_name)
BIN_SCHEMA = """\
CREATE TABLE {bin} (
    id bigserial NOT NULL,
    hash varchar(40) NOT NULL,
    type varchar(40) NOT NULL,
    body bytea,
    CONSTRAINT {bin}_pkey PRIMARY KEY (id, hash)
    );
""".format(bin = lybcfg.bin_table_name)
DOCBIN_SCHEMA = """\
CREATE TABLE {docbin} (
    id bigserial NOT NULL,
    binid bigint NOT NULL,
    docid bigint NOT NULL,
    CONSTRAINT {docbin}_pkey PRIMARY KEY (id)
    );
CREATE OR REPLACE FUNCTION del_orphaned_{bin}() RETURNS trigger AS
'
BEGIN
    PERFORM * FROM {docbin} WHERE binid = old.binid;
    IF NOT FOUND THEN
        DELETE FROM {bin} where id=old.binid;
        RETURN old;
    END IF;
    RETURN old;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER on_{docbin}_del
    AFTER DELETE
    ON {docbin} FOR EACH ROW
    EXECUTE PROCEDURE del_orphaned_{bin}();
""".format(docbin = lybcfg.docbin_table_name, bin = lybcfg.bin_table_name)
GRPCAT_ACCESS_SCHEMA = """\
CREATE TABLE {grpcat_access} (
    id bigserial NOT NULL,
    gid bigint NOT NULL,
    catid bigint NOT NULL,
    attr varchar(2),
    CONSTRAINT {grpcat_access}_pkey PRIMARY KEY (id)
    );
CREATE INDEX {grpcat_access}_idx on {grpcat_access} USING btree(gid, catid);
CREATE OR REPLACE FUNCTION del_orphaned_{grpcat_access}_on_del_{cat}() RETURNS trigger AS
'
BEGIN
    DELETE FROM {grpcat_access} WHERE catid=old.id;
    RETURN old;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER del_orphaned_{grpcat_access}_on_del_{cat}
    AFTER DELETE
    ON {cat} FOR EACH ROW
    EXECUTE PROCEDURE del_orphaned_{grpcat_access}_on_del_{cat}();
CREATE OR REPLACE FUNCTION del_orphaned_{grpcat_access}_on_del_{grp}() RETURNS trigger AS
'
BEGIN
    DELETE FROM {grpcat_access} WHERE gid=old.id;
    RETURN old;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER del_orphaned_{grpcat_access}_on_del_{grp}
    AFTER DELETE
    ON {grp} FOR EACH ROW
    EXECUTE PROCEDURE del_orphaned_{grpcat_access}_on_del_{grp}();
""".format(grpcat_access = lybcfg.grpcat_access_table, cat = lybcfg.cat_table_name, grp = lybcfg.grp_table_name)
GRPDOC_ACCESS_SCHEMA = """\
CREATE TABLE {grpdoc_access} (
    id bigserial NOT NULL,
    gid bigint NOT NULL,
    docid bigint NOT NULL,
    attr varchar(2),
    CONSTRAINT {grpdoc_access}_pkey PRIMARY KEY (id)
    );
CREATE INDEX {grpdoc_access}_idx on {grpdoc_access} USING btree(gid, docid);
CREATE OR REPLACE FUNCTION del_orphaned_{grpdoc_access}_on_del_{doc}() RETURNS trigger AS
'
BEGIN
    DELETE FROM {grpdoc_access} WHERE docid=old.id;
    RETURN old;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER del_orphaned_{grpdoc_access}_on_del_{doc}
    AFTER DELETE
    ON {doc} FOR EACH ROW
    EXECUTE PROCEDURE del_orphaned_{grpdoc_access}_on_del_{doc}();
CREATE OR REPLACE FUNCTION del_orphaned_{grpdoc_access}_on_del_{grp}() RETURNS trigger AS
'
BEGIN
    DELETE FROM {grpdoc_access} WHERE gid=old.id;
    RETURN old;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER del_orphaned_{grpdoc_access}_on_del_{grp}
    AFTER DELETE
    ON {grp} FOR EACH ROW
    EXECUTE PROCEDURE del_orphaned_{grpdoc_access}_on_del_{grp}();
""".format(grpdoc_access = lybcfg.grpdoc_access_table, doc = lybcfg.doc_table_name, grp = lybcfg.grp_table_name)

PWDCAT_ACCESS_SCHEMA = """\
CREATE TABLE {pwdcat_access} (
    id bigserial NOT NULL,
    pid bigint NOT NULL,
    catid bigint NOT NULL,
    attr varchar(2),
    CONSTRAINT {pwdcat_access}_pkey PRIMARY KEY (id)
    );
CREATE INDEX {pwdcat_access}_idx on {pwdcat_access} USING btree(pid, catid);
CREATE OR REPLACE FUNCTION del_orphaned_{pwdcat_access}_on_del_{cat}() RETURNS trigger AS
'
BEGIN
    DELETE FROM {pwdcat_access} WHERE catid=old.id;
    RETURN old;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER del_orphaned_{pwdcat_access}_on_del_{cat}
    AFTER DELETE
    ON {cat} FOR EACH ROW
    EXECUTE PROCEDURE del_orphaned_{pwdcat_access}_on_del_{cat}();
CREATE OR REPLACE FUNCTION del_orphaned_{pwdcat_access}_on_del_{pwd}() RETURNS trigger AS
'
BEGIN
    DELETE FROM {pwdcat_access} WHERE pid=old.id;
    RETURN old;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER del_orphaned_{pwdcat_access}_on_del_{pwd}
    AFTER DELETE
    ON {pwd} FOR EACH ROW
    EXECUTE PROCEDURE del_orphaned_{pwdcat_access}_on_del_{pwd}();
""".format(pwdcat_access = lybcfg.pwdcat_access_table, cat = lybcfg.cat_table_name, pwd = lybcfg.pwd_table_name)
PWDDOC_ACCESS_SCHEMA = """\
CREATE TABLE {pwddoc_access} (
    id bigserial NOT NULL,
    pid bigint NOT NULL,
    docid bigint NOT NULL,
    attr varchar(2),
    CONSTRAINT {pwddoc_access}_pkey PRIMARY KEY (id)
    );
CREATE INDEX {pwddoc_access}_idx on {pwddoc_access} USING btree(pid, docid);
CREATE OR REPLACE FUNCTION del_orphaned_{pwddoc_access}_on_del_{doc}() RETURNS trigger AS
'
BEGIN
    DELETE FROM {pwddoc_access} WHERE docid=old.id;
    RETURN old;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER del_orphaned_{pwddoc_access}_on_del_{doc}
    AFTER DELETE
    ON {doc} FOR EACH ROW
    EXECUTE PROCEDURE del_orphaned_{pwddoc_access}_on_del_{doc}();
CREATE OR REPLACE FUNCTION del_orphaned_{pwddoc_access}_on_del_{pwd}() RETURNS trigger AS
'
BEGIN
    DELETE FROM {pwddoc_access} WHERE pid=old.id;
    RETURN old;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER del_orphaned_{pwddoc_access}_on_del_{pwd}
    AFTER DELETE
    ON {pwd} FOR EACH ROW
    EXECUTE PROCEDURE del_orphaned_{pwddoc_access}_on_del_{pwd}();
""".format(pwddoc_access = lybcfg.pwddoc_access_table, doc = lybcfg.doc_table_name, pwd = lybcfg.pwd_table_name)

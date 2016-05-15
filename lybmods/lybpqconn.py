# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extensions
import lybmods.lybcfg as lybcfg
import lybmods.lybtools as lybtools

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
conn = psycopg2.connect(database=lybcfg.dbname, user=lybcfg.dbuser, password=lybcfg.dbpass, host=lybcfg.dbhost)
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

def create_schema():
    cur = conn.cursor()
    d = {
         lybcfg.pwd_table_name: lybtools.AUTH_SCHEMA,
         lybcfg.sess_table_name: lybtools.SESS_SCHEMA,
         lybcfg.cat_table_name: lybtools.CAT_SCHEMA,
         lybcfg.doc_table_name: lybtools.DOC_SCHEMA,
         lybcfg.bin_table_name: lybtools.BIN_SCHEMA,
         lybcfg.docbin_table_name: lybtools.DOCBIN_SCHEMA,
         lybcfg.grpcat_access_table: lybtools.GRPCAT_ACCESS_SCHEMA,
         lybcfg.grpdoc_access_table: lybtools.GRPDOC_ACCESS_SCHEMA,
         lybcfg.pwdcat_access_table: lybtools.PWDCAT_ACCESS_SCHEMA,
         lybcfg.pwddoc_access_table: lybtools.PWDDOC_ACCESS_SCHEMA
         }
    for k in d.keys():
        try:
            cur.execute('SELECT COUNT(*) FROM %s' % k)
        except:
            cur.execute(d[k])
    conn.commit()


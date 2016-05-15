'''Этот модуль предназначен для конвертации в C-код и последующей компиляции в исполняюмую библиотеку. Здесь находятся тяжёлые функции.'''

import cherrypy
from lxml import etree
from lybmods import lybtools
from urllib.request import FancyURLopener
from urllib.parse import urlencode
from urllib.parse import urljoin, parse_qs, urlsplit
from lybmods.lybclasses import Cat
from lybmods import lybhtdata
from base64 import decodestring
import re
import hashlib


class URLOpener(FancyURLopener):
    version = 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.6) Gecko/20100101 Firefox/10.0.6 Iceweasel/10.0.6'

def html(self, catid, url, htfile, md = None, sub = False, ins = False):
    htfile = lybtools.htfile_tounicode(htfile)
    body = etree.ElementTree(etree.HTML(htfile).xpath('//body')[0])
    sessdata = cherrypy.session
    strip_tags = ["script", "link"]
    etree.strip_elements(body, *strip_tags, with_tail=False)
    chg_tags = ["body", "a", "form", "input", "noscript"]
    etree.strip_tags(body, *chg_tags)
    etree.strip_tags(body, etree.Comment)
    #safe_tags = ['img']
    for elem in body.xpath('//*'):
        if elem.tag == 'body': elem.tag = 'old-body'
        attr = elem.attrib
        if elem.tag in chg_tags:
            etree.strip_attributes(elem, *attr)
        if "class" in attr:
            etree.strip_attributes(elem, "class")
        if "id" in attr:
            etree.strip_attributes(elem, "id")
        if "onclick" in attr:
            etree.strip_attributes(elem, "onclick")
        if "style" in attr:
            attr['style'] = re.sub('url\(.+\)', 'url()', attr['style'])
        #if elem.tag not in safe_tags and (elem.text is None or elem.text.strip() == '') and elem.getchildren() == []:
        #    elem.getparent().remove(elem)
        #    continue
        if "src" in attr:
            m = re.search('data:(\S+);base64,(.+)', attr['src'])
            if not m:
                srcurl = urljoin(url, attr['src'])
                srcobjquery = urlsplit(srcurl)[3]
                srcqdict = parse_qs(srcobjquery)
                if 'lybsrcobj' in list(srcqdict.keys()):
                    ohash = srcqdict['lybsrcobj'][0]
                    srcquerydata = {'lybsrcobj': ohash}
                    srcquery = urlencode(srcquerydata)
#                    if ins:
                    page = '/getobj?'
#                    else:
#                        page = '/edit/tmpstore?'
#                    if ohash not in sessdata:
#                        if md:
#                            cat = Cat(int(catid))
#                            doco = cat[int(md)]
#                            sessdata[ohash] = doco[ohash]
                    elem.set('src', page + srcquery)
                    continue
                try:
                    srcu = URLOpener().open(srcurl)
                except:
                    continue
                if srcu.code >= 400:
                    continue
                srcdata = srcu.read()
                cont_type = srcu.headers['Content-Type']
                srcftype = cont_type and lybtools.ctype(srcu.headers['Content-Type']) or 'none'
            else:
                srcdata = decodestring(m.group(2).encode('utf-8'))
                srcftype = m.group(1)
            srchashname = hashlib.sha1(srcdata).hexdigest()
            if srcftype == 'text/html':
                if elem.tag == 'img': continue
                srcdata = self.html(catid, srcu.url, srcdata, sub = True)
            if srchashname not in sessdata:
                sessdata[srchashname] = {'body': srcdata, 'type': srcftype}
            srcquerydata = {'lybsrcobj': srchashname}
            srcquery = urlencode(srcquerydata)
            if ins:
                page = '/getobj?'
            else:
                page = '/edit/tmpstore?'
            elem.set('src', page + srcquery)
    etree.strip_tags(body, 'old-body')
    ht_ml = etree.tounicode(body, method='html', pretty_print = True)
    if not sub and not ins:
        return self.ne(catid, url=url, html=ht_ml, md=md)
    else:
        return ht_ml

def insert_doc(self, catid = 0, url = None, html = None, doc_name = '', md = None):
    catid = int(catid)
    doc_name = doc_name.strip()
    cat = Cat(catid)
    catname = cat.name
    if md:
        md = int(md)
        modify_doc = '<input type="hidden" name="md" value="' + str(md) + '">'
    else:
        modify_doc = ''
    
    html = self.html(catid, '/', html, ins = True)
    if doc_name == '':
        return self.root.buildhtml('Архив [Укажи имя документа]', lybhtdata.nicedit_html1 + lybhtdata.nicedit_html2.format(docname=doc_name,
                                                                                                                           url=url,
                                                                                                                           modify_doc=modify_doc,
                                                                                                                           textarea=lybhtdata.nicedit_textarea.format(input_html=html), catid=catid,
                                                                                                                           catname = catname))
    did = cat.docidbyname(doc_name)
    if did and did != md:
        return self.root.buildhtml('Архив [Документ с таким именем в разделе "' + cat.name + '" существует]', lybhtdata.nicedit_html1 + lybhtdata.nicedit_html2.format(docname=doc_name,
                                                                                                                                          url=url,
                                                                                                                                          modify_doc=modify_doc,
                                                                                                                                          textarea=lybhtdata.nicedit_textarea.format(input_html=html), catid=catid,
                                                                                                                                          catname = catname))
    if md:
        cat[md] = { 'name': doc_name, 'body': html}
        did = md
    else:
        did = cat.insert({ 'name': doc_name, 'body': html})
    xdata = etree.HTML(html)
    if md:
        new_bin_list = [ parse_qs(urlsplit(x)[3])['lybsrcobj'][0] for x in xdata.xpath('//@src') if 'lybsrcobj' in parse_qs(urlsplit(x)[3])]
        old_bin_list = cat[did].bins
        list_to_del = list(set(old_bin_list) - set(new_bin_list))
        for bhash in list_to_del:
            del cat[did][bhash]
    for src in xdata.xpath('//@src'):
        srcquery = urlsplit(src)[3]
        try:
            src_obj = parse_qs(srcquery)['lybsrcobj'][0]
        except:
            continue
        try:
            obj = cherrypy.session[src_obj]
        except KeyError:
            continue
        cat[did][src_obj] = obj
    cherrypy.session.clear()
    args = {'doc':did, 'catid':catid}
    return self.root.get_doc(**args)

def ne(self, catid, url = None, html = None, md = None, docname = "Новый документ"):
    html = lybhtdata.nicedit_textarea.format(input_html=html)
    xhtml = etree.HTML(html).xpath('//textarea[@id=\'nicedit-js-area\']')[0]
    if md:
        docname = Cat(int(catid))[int(md)].name
        modify_doc = '<input type="hidden" name="md" value="' + md + '">'
    else:
        modify_doc = ''
    return self.root.path(int(catid), lcat = True) + '<br><br>' + lybhtdata.nicedit_html1 + lybhtdata.nicedit_html2.format(url=url,
                                                              catid=catid,
                                                              catname = Cat(int(catid)).name,
                                                              docname = docname,
                                                              modify_doc=modify_doc,
                                                              textarea=etree.tounicode(xhtml,
                                                                                      method="html",
                                                                                      pretty_print=True)
                                                              )

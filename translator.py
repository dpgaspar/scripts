__author__ = 'dpgaspar'
import sys
import re
import requests
import urllib
import mechanize
import ast


class GoogleTranslator():

    url = "http://translate.google.pt/translate_a/t?client=t&sl=%s&tl=%s&hl=pt-BR&sc=2&ie=UTF-8&oe=UTF-8&prev=btn&rom=1&ssel=0&tsel=0&q=%s"

    def __init__(self, babelfilepath, to_lang):
        self.babelfilepath = babelfilepath
        self.to_lang = to_lang
        

    def process2(self):
        f = open(self.babelfilepath)
        for line in f:
            allfile += line

        m = re.search('msgid "(.*?)"\n*msgstr "(.*?)"', line)
        if m:


    def process(self):
        f = open(self.babelfilepath)
        for line in f:
            m = re.search('msgid "(.*?)"', line)
            if m:
                msgid = m.group(1)
                for line in f:
                    m = re.search('msgstr "(.*?)"', line)
                    if m:
                        msgstr = m.group(1)
                        if msgstr == "":
                            for line in f:
                                if line == "\n": break
                            
                        print 'msgid "%s"' % (msgid)
                        ret_msgstr = ""
                        for item in  msgid.split("\n"):
                            ret_msgstr += self._translate(item)
                        print 'msgstr "%s"' % (ret_msgstr)
                        break
                    else:
                        msgid += line
            else:
                print line.rstrip('\n')

    def _translate(self, text, from_lang="en", to_lang="fr"):
        return "bon jour"

    def translate(self, text, from_lang="en"):
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        browser.addheaders = [('User-agent', 'chrome')]
        text = text.replace('"','')
        text = browser.open(self.url % (from_lang,self.to_lang,urllib.quote(text))).read().decode('UTF-8')
        m = re.search('^\[\[\["(.*?)",.*',text)
        return m.group(1)



    def dump(self):
        for item in self.babelitems:
            print item


b = GoogleTranslator(sys.argv[1], sys.argv[2])
b.process()

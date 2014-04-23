__author__ = 'dpgaspar'
import sys
import re
import requests
import mechanize

class BabelItem():
    msgid = ""
    msgstr = ""

    def __init__(self, msgid, msgstr):
        self.msgid = msgid
        self.msgstr = msgstr

    def __repr__(self):
        return "msgid: %s msgstr: %s" % (self.msgid, self.msgstr)


class GoogleTranslator():

    url = "http://translate.google.pt/translate_a/t?client=t&sl=%s&tl=%s&hl=pt-BR&sc=2&ie=UTF-8&oe=UTF-8&prev=btn&rom=1&ssel=0&tsel=0&q=%s"

    def __init__(self, babelfilepath):
        self.babelfilepath = babelfilepath
        self.babelitems = []


    def loadfile(self):
        f = open(self.babelfilepath)
        for line in f:
            line = line.rstrip()
            m = re.search('msgid "(.*)"', line)
            if m:
                msgid = m.group(1)
                for line in f:
                    line = line.rstrip()
                    m = re.search('msgstr "(.*)"', line)
                    if m:
                        msgstr = m.group(1)
                        if msgstr == "":
                            for line in f:
                                line = line.rstrip()
                                if line == "\n": break
                        print "msgid: %s" % (msgid)
                        print "msgstr: %s" % (self._translate(msgid))
                        break
                    else:
                        msgid += line
            else:
                print line

    def _translate(self, text, from_lang="en", to_lang="fr"):
        return "bon jour"

    def translate(self, text, from_lang="en", to_lang="fr"):
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        browser.addheaders = [('User-agent', 'chrome')]
        text = browser.open(self.url % (from_lang,to_lang,text)).read().decode('UTF-8')
        m = re.match('\[\[\["(.*[\"+0])".*\]', text)
        print m.group(1)



    def dump(self):
        for item in self.babelitems:
            print item


b = GoogleTranslator(sys.argv[1])
b.loadfile()
#b.translate("Hello")

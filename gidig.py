#!/usr/bin/env python
# based on http://jblevins.org/log/webpy-markdown

import web
import markdown
import re

templatespath = 'templates'
sourcepath = '../source/'
targetpath = '../'
sourcemarkup = '.md'
alwaysonsite_file = 'templates/alwaysonsite.md'
hash_separator = '__HASH_SEPARATOR__'

urls = (
    '/parser/(.*)', 'hashparser',
    '^/(.*)/$', 'redirect',
    '/(.*)', 'page',
)

render = web.template.render(templatespath)

# Application
app = web.application(urls, globals())

# Markdown
md = markdown.Markdown(output_format='html4')


class redirect:
    def GET(self, path):
        web.seeother('/' + path)


class hashparser:
    def GET(self, url):

        # find all hashtags in one file (from url)
        sourcefile = open( sourcepath + url + sourcemarkup , "r")
        hashtags = []
        for line in sourcefile:
            if  re.search('\S+#\S+', line):
                hashtags +=  re.findall('\S+#\S+', line) 
        sourcefile.close() 

        # handle every hashtag
        for hashtag in hashtags:
            thishash = hashtag.split('#')
            key = thishash[0]
            value = thishash[1]

            # read prosa-content from target file/key and delete old listing
            listerfile = open( sourcepath + key + sourcemarkup ,"a+")
            unlistedfile = []
            nowlisting = 0
            for num, line in enumerate(listerfile):
                if re.search(hash_separator, line):
                    nowlisting = 1                           ## TODO just end for 
                elif nowlisting == 1:
                    nowlisting = 1
                else :
                    unlistedfile.append(line)
            listerfile.close()
        
            # write prosa-content and new list
            listerfile = open( sourcepath + key + sourcemarkup ,"w")
            unlistedfile.append(hash_separator + '\n')
            unlistedfile.append( value + ': ' + url )
            listerfile.writelines(unlistedfile)
            listerfile.close()

        return url + ' parsed'

class page:
    def GET(self, url):
        # Handle index pages: path/ maps to path/index.txt
        if url == "" or url.endswith("/"):
            url += "index"

        lemma = url ## TODO param

        # Each URL maps to the corresponding .txt file in pages/
        content_file = sourcepath + lemma + sourcemarkup ## TODO param

        # Try to open the text file, returning a 404 upon failure
        try:
            f = open(content_file, 'r')
            a = open(alwaysonsite_file, 'r')

        except IOError:
            return web.notfound()

        # Read the entire file, converting Markdown content to HTML
        alwaysonsite = a.read()
        alwaysonsite = md.convert(alwaysonsite)

        content = f.read()
        content = md.convert(content)
        # Render the page.html template using the converted content

        content = render.headerfooter(lemma, alwaysonsite, content) ## all from config
        content = content

        f_html = open( targetpath + lemma ,"w")
        f_html.write( str(content) )
        f_html.close()

        return content


# http://webpy.org/cookbook/userauthbasic

if __name__ == '__main__':
    app.run()

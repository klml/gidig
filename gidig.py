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

urls = (
    '/parser/(.*)', 'hashparser',
    '/(.*)/', 'redirect',
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

        file = open('../source/klml.md', "r")

        conte = ""
        for line in file:
            if re.search('#', line):
                conte += line

        return url + conte

                #~ f_html = open( "../lister.md" ,"w")
                #~ f_html.write( line )
                #~ f_html.close()



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


if __name__ == '__main__':
    app.run()

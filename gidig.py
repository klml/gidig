#!/usr/bin/env python
# based on http://jblevins.org/log/webpy-markdown ;)

import web
import markdown


templatespath = 'templates'
sourcepath = '../source/'
targetpath = '../'
sourcemarkup = 'md'


urls = (
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

class page:
    def GET(self, url):
        # Handle index pages: path/ maps to path/index.txt
        if url == "" or url.endswith("/"):
            url += "index"

        # Each URL maps to the corresponding .txt file in pages/
        page_file = sourcepath + '%s.' %(url) + markup ## TODO param

        # Try to open the text file, returning a 404 upon failure
        try:
            f = open(page_file, 'r')

        except IOError:
            return web.notfound()

        # Read the entire file, converting Markdown content to HTML
        content = f.read()
        content = md.convert(content)
        # Render the page.html template using the converted content
        lemma = '%s' %(url) ## TODO param
        content = render.headerfooter(lemma, content) ## all from config
        content = content

        f_html = open( targetpath + lemma ,"w")
        f_html.write( str(content) )
        f_html.close()

        return content


if __name__ == '__main__':
    app.run()

#!/usr/bin/env python
# based on http://jblevins.org/log/webpy-markdown ;)

import web
import markdown

urls = (
    '/(.*)', 'page',
)

render = web.template.render('templates')

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
        page_file = 'source/%s.md' %(url) ## TODO param

        # Try to open the text file, returning a 404 upon failure
        try:
            f = open(page_file, 'r')

        except IOError:
            return web.notfound()

        # Read the entire file, converting Markdown content to HTML
        content = f.read()
        content = md.convert(content)
        content = render.headerfooter(content)

        # Render the page.html template using the converted content


        lemma_html = '%s.html' %(url) ## TODO param

        f_html = open( lemma_html ,"w")
        f_html.write( content )
        f_html.close()

        return 'sadsadsadsad'

        #~ return content


if __name__ == '__main__':
    app.run()

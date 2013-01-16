# gidig

cvs-lightweight-markup content framework

* edit git versioned markdown directory ('/md/')
** on filesystem
** just HTTP-PUT markdown from a textarea
* inotify triggers [autocommit.sh](script/autocommit.sh) for webedited changes or commit manual
* [post-commit](.git/hooks/post-commit) all new and changed to [markdown.sh](script/markdown.sh) and little bit templating to html

Works with a PUT enabled webserver (I use nginx)


<pre>
                               ┌──────────┐
                               │ web      │
      ┌─ http POST/writer.xx ─ │ server   │ ─┐
      │                        │          │  │
      │                        └──────────┘  │
      │                            │         │
      │                            │   GET   │
      │                            │         │
   ┌─────┐                     ┌─────────┐┌─────┐
   │     ├┐                    │         ││     │
   │ git │├┐   ┌─ markdown ────│ html    ││ html│
   │     │││ ──┤               │         ││     │
   │     │││   └─ templater ───│         ││     │
   └┬────┘││                   │-------- │└─────┘
    └┬────┘│ ─── indexer ──────│ * list  │
     └─────┘                   │ * lists │
                               │ * lis   │
                               │ * li    │
                               │         │
                               └─────────┘

</pre>


## TODO

* transclusion
* tag parser
* comments
** marken, mitschleifen und per jQuery rauswerfen und vorlegen?
* non autocommit with dircet access
* autostart autocommit
* site title
* robots.txt

### client
* webediting
** tagssyntaxer
** autocomplete
* TOC



## install

Although you can config all directories, te easiest way is to start in your web-directory (e.g. /var/www/example.com/

<code>
git clone git@github.com:klml/gidig.git
</code>


also create your <code>source/</code> directory here, versioning is here very useful, but not mandatory.
Trigger after every content-update `source2html.xx`

For an "post-update"-hook
<code>
exec sh ../gidig/source2html.sh
</code>

useful pages index.md and 404.md

config


## inspired by

* [rawk](https://github.com/kisom/rawk/)

## name

gidig is a mixture from

* w__i__k__i__
* __gi__t
* ticket
* and its an palindrome like radar ;)

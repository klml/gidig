# gidig

git-markdown content framework

* edit DVCS versioned markdown directory ('/md/')
  * on filesystem
  * just HTTP-PUT markdown from a textarea
* index diff from changeset on [outermarkdown](http://umija.org/dev%3Aoutermarkdown) (easy hashtags like 'prio#1') to files
* render alle fields with tenmplates in md
* [CRUD](http://en.wikipedia.org/wiki/Create,_read,_update_and_delete) source and html to DCVS- and webservers.

<pre>
 ┌─server (optional)─┐                ┌─ (web) server ────────┐
 │ ┌────────┐──────┐ │                │  ┌─────────┐┌─────┐   │
 │ │ git    ├┐     │ │                │  │         ││     │   │
 │ │        │├┐    │ │                │  │ html    ││ html│   │
 │ │--------│├┼─┐  │ │                │  │         ││     │   │
 │ │ * list │││ │  │ │                │  │         ││     │   │
 │ │ * lists│││ │  │ │                │  │-------- │└─────┘   │
 │ │ * lis  │││ │  │ │                │  │ * list  │          │
 │ └┬───────┘││ │  │ │                │  │ * list  │          │
 │  └┬───────┘│ │  │ │                │  │ * list  │          │
 │   └───┬────┘ │  │ │                │  └─────────┘          │
 │       │      │  │ │                │                       │
 │       │      │  │ │                │                       │
 └───────┼──────┼──┼─┘                └───────────────────────┘
         │      │  │                                   │       
         ↑      ↓  ↑                                   ↑       
         │      │  │                                   │       
         │      │  │     ┌─ CRUD ───────────────────┐  │       
         │      │  └─────│─ PUT/writer.php/py/js ───│──┘       
         │      │        └─────────────────────┬────┘          
         │      │                              └──────┐        
 ┌───────┼──────┼─── processing ──────────────────────┼───────┐
 │       │      │                                     │       │
 │       │      ├─── 1.) editing (webeditor) ─────────┤       │
 │       │      │                                     │       │
 │       │      ├──────────────────────────────────┐  │       │
 │       │      │   ┌─2.)──────────────────────┐   │  │       │
 │       └───────── │─────── indexer ──────────│───┘  │       │
 │                  │ diff                     │      │       │
 │              │   └──────────────────────────┘      │       │
 │              │                                     │       │
 │              │   ┌──3.)─────────────────────┐      │       │
 │              │   │      ┌─ markdown ────────│──────┤       │
 │              └───│──────┤                   │      │       │
 │                  │      └─ templater ───────│ ─────┘       │
 │                  └──────────────────────────┘              │
 └────────────────────────────────────────────────────────────┘
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


Although you can config all directories, the easiest way is to start in your web-directory, so you have all pages in this directory, or named sub-directories.
Only gidig and source (boths in configurable) are reserved for source-files and the gidig script.


<code>
/var/www/example.com$ tree
.
├── gidig
│   ├── config
│   ├── css
│   ├── gidig.php
│   ├── .....
│   └── tpl_header.html
├── source
│   ├── Ae.md
│   ├── ....
│   └── wdsh.md
├── index
├── klml
└── tmp
</code>




<code>
git clone git@github.com:klml/gidig.git
</code>

copy (`cp`) or move (`mv`) `config.exmpl` to `config`.


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

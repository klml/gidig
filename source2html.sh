#!/bin/bash
# trigger this after "post-update" (hook)
# exec sh ../gidig/source2html.sh
# or manual to recreate all files

. ./config

# get 
#if [ "CHGLEMMAS" != "" ]; then
#    CHGLEMMAS="$(git diff HEAD~1 --name-only | sed 's/\(.*\)\..*/\1/')" # use $markup !
#fi


for CHGLEMMA in $1;
    do
        cat $SCRIPTROOT/tpl_header.html > $WEBROOT/tmp  ## need kumul variable TODO
        # __TITLE__ # heading in first line
#        markdown $SOURCEROOT/$CHGLEMMA.$markupextension >> $WEBROOT/tmp
        cat $SCRIPTROOT/tpl_footer.html >> $WEBROOT/tmp

        cat $WEBROOT/tmp | sed -e "s|__LEMMA__|$CHGLEMMAS|" > $WEBROOT/$CHGLEMMA$WEBEXTENSION # put name in body etc

done

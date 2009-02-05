#!/bin/sh
set -e

# This scripts updates the Documentation part of the site from Yokadi master
# branch.

# FIXME: do not hardcode paths!
SRC_DIR=$HOME/src/yokadi/
WWW_DIR=$HOME/src/yokadi-pages/
DOC_FILE=$WWW_DIR/doc.markdown
DOC_FILE_TMPL=$WWW_DIR/doc.markdown.tmpl

cp $DOC_FILE_TMPL $DOC_FILE

for srcName in $(grep -o '[A-Za-z/]*\.markdown' $DOC_FILE_TMPL) ; do
    src=$SRC_DIR/$srcName
    title=$(head --lines=1 $src | sed 's/^# *//')

    name=$(basename $src)
    dst=$WWW_DIR/$name

    echo "---\ntitle: $title\nlayout: default\n---" > $dst
    tail --lines=+2 $src >> $dst

    nameHtml=$(echo $name | sed 's/markdown$/html/')

    sed -i "s|$srcName|[$title]($nameHtml)|" $DOC_FILE
done

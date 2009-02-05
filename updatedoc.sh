#!/bin/sh
set -e

# This scripts updates the Documentation part of the site from Yokadi master
# branch.

# FIXME: do not hardcode paths!
if [ $# -ne 2 ] ; then
    echo "Usage: $(basename $0) <path/to/yokadi/checkout> <path/to/yokadi.github.com/checkout>"
    exit 1
fi

SRC_DIR=$1
WWW_DIR=$2

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

# vim: set ts=4 sw=4 et:

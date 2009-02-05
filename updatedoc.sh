#!/bin/sh
set -e

# This scripts updates the Documentation part of the site from Yokadi master
# branch.

# FIXME: do not hardcode paths!
SRC_DIR=$HOME/src/yokadi/
WWW_DIR=$HOME/src/yokadi-pages/
DOC_FILE=$WWW_DIR/doc.markdown

echo "---\ntitle: Documentation\nlayout: default\n---" > $DOC_FILE

for src in $SRC_DIR/README.markdown $SRC_DIR/doc/*.markdown ; do
    title=$(head --lines=1 $src | sed 's/^# *//')

    name=$(basename $src)
    dst=$WWW_DIR/$name

    echo "---\ntitle: $title\nlayout: default\n---" > $dst
    tail --lines=+2 $src >> $dst

    nameHtml=$(echo $name | sed 's/markdown$/html/')

    echo "- [$title]($nameHtml)" >> $DOC_FILE
done

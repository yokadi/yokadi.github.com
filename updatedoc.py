#!/usr/bin/env python
import os
import re
import sys


gTitleRe = re.compile("^#", re.MULTILINE)
def copyDoc(title, src, dstDir):
    dst = open(os.path.join(dstDir, os.path.basename(src)), "w")

    print >>dst, """---
title: %s
layout: default
---
""" % title

    content = open(src).read()
    # Shift titles one level down because our template starts the document with
    # a level1 title
    content = gTitleRe.sub("##", content)
    print >>dst, content


def main():
    if len(sys.argv) != 3:
        print "Usage: updatedoc.py <path/to/yokadi/checkout> <path/to/yokadi.github.com/checkout>"
        return 1

    srcDir = sys.argv[1]
    wwwDir = sys.argv[2]
    docFileTmpl = os.path.join(wwwDir, "doc.markdown.tmpl")

    dstDoc = open(docFileTmpl.replace(".tmpl", ""), "w")

    linkRe = re.compile("\[(.*)\]\((.*)\)")

    for line in open(docFileTmpl).readlines():
        result = linkRe.search(line)
        if result:
            title, fileName = result.groups(0)
            copyDoc(title, os.path.join(srcDir, fileName), wwwDir)
            htmlFileName = os.path.basename(fileName).replace(".markdown", ".html")
            line = line.replace(fileName, htmlFileName)

        dstDoc.write(line)

    return 0


if __name__=="__main__":
    sys.exit(main())
# vi: ts=4 sw=4 et

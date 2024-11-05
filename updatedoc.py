#!/usr/bin/env python3
import os
import re
import sys

"""
Update local Markdown files from Yokadi README.md and files in the doc/
directory.
"""

DOC_HEADER = """---
title: %s
layout: default
---

"""


H1_RE = re.compile("^# (.*)\n\n?", re.MULTILINE)

# Matches a Markdown link of the form: [Title](fileName)
LINK_RE = re.compile(r"\[(.*)\]\((.*)\)")


def copyDoc(title, src, dstDir):
    with open(src) as fp:
        content = open(src).read()

    # Remove H1 title: it's provided by the YAML header
    content = H1_RE.sub("", content)

    with open(os.path.join(dstDir, os.path.basename(src)), "w") as fp:
        fp.write(DOC_HEADER % title)
        fp.write(content)


def main():
    if len(sys.argv) != 3:
        print("Usage: updatedoc.py <path/to/yokadi/checkout>"
              " <path/to/yokadi.github.com/checkout>")
        return 1

    srcDir = sys.argv[1]
    wwwDir = sys.argv[2]
    docFileTmpl = os.path.join(wwwDir, "doc.md.tmpl")

    dstDoc = open(docFileTmpl.replace(".tmpl", ""), "w")

    for line in open(docFileTmpl).readlines():
        result = LINK_RE.search(line)
        if result:
            title, fileName = result.groups(0)
            copyDoc(title, os.path.join(srcDir, fileName), wwwDir)

            # doc.md.tmpl contains links to .md files, but doc.md must contain
            # links to .html files
            htmlFileName = os.path.basename(fileName).replace(".md", ".html")
            line = line.replace(fileName, htmlFileName)

        dstDoc.write(line)

    return 0


if __name__ == "__main__":
    sys.exit(main())
# vi: ts=4 sw=4 et

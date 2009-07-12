---
title: Second release of Yokadi is out!
author: Sebastien
---
During the [Gran Canaria Desktop Summit](http://www.grancanariadesktopsummit.org/), there were a conspiracy of some
guys that were using text based tool to manages their tasks!

So we decided to make an 'Akademy' release. Here's the highlights:
- ability to assign keywords to a project
- shortened some commands (old ones still available but deprecated):
	- t_set_due => t_due
        - t_set_project => t_project
        - t_set_urgency => t_urgency
- changed keyword syntax: use @foo instead of -k foo
- added t_recurs command to define task recursion (weekly, monthly, yearly...)
- added full text search with t_list -s foo
- enhanced t_list display
- added purge command (t_purge) to remove old tasks
- added Windows support
- fixed install script to be more friendly to both users and packagers

We focus on adding new features while keeping the software easy to use et easy
to maintain. We hope you like it as much as we do.

[Grab it](download.html), have a look at the [README](README.html)
and start getting organized! Should anything go wrong, [let us know](contact.html).

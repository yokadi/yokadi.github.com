---
title: Second release of Yokadi is out!
author: Sebastien
---
During the [Gran Canaria Desktop Summit](http://www.grancanariadesktopsummit.org/), there were a conspiracy of some
guys who were using text based tool to manage their tasks!

So we decided to make an `Akademy` release. Here are the highlights:
- Ability to assign keywords to a project.
- Shortened some commands (old ones are still available but are considered deprecated):

  - t\_set\_due => t\_due
  - t\_set\_project => t\_project
  - t\_set\_urgency => t\_urgency

- Changed keyword syntax: use @foo instead of -k foo.
- Added t\_recurs command to define task recursion (weekly, monthly, yearly...)
- Added full text search with t\_list -s foo.
- Enhanced t\_list display.
- Added purge command (t\_purge) to remove old tasks.
- Added Windows support.
- Fixed install script to be more friendly to users and packagers.

We focused on adding new features while keeping the software easy to use and easy
to maintain. We hope you like it as much as we do.

[Grab it](download.html), have a look at the [README](README.html)
and start getting organized! Should anything go wrong, [let us know](contact.html).

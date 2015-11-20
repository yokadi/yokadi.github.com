---
layout: post
title: Spring, time to release 0.13.0!
author: Sebastien
---
The sun is shining, it's time to release new yokadi stuff!

Here are the highlights of the 0.13.0 release:
- cryptographic support to encrypt tasks title and description
- t_apply now accept id range (x-y)
- Special keyword __ can used in t_apply to affect all tasks previously select by t_list

Crypto stuff leads to optional new dependancy on the [Python Cryptographic Toolkit](http://www.pycrypto.org). But it you don't have it
yokadi will work as before, you will just have new crypto function deactivated.

[Grab it](/download.html), have a look at the [README](/README.html) that explain new crypto stuff and tasks range.
Keep organized! 

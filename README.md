RICOH THETA S API Tests
=======================

Uses [RICOH THETA S API v2](https://developers.theta360.com/en/docs/v2/api_reference/).
This is not compatible with the THETA m15 or earlier cameras.
For more information, check the [Unofficial and Unauthorized THETA S Hacking
Guide](http://codetricity.github.io/theta-s/index.html).

There are three programs that use the same sample library, `thetapylib`.

The three examples are:

1. pyTHETA: Python command line, the most fully developed.
2. deskTHETA: Python desktop example using Pygame library
3. Python desktop example using Kivy library

---

Requirements
------------

The examples use the python `requests` module instead of `urllib2`.  
To install `requests` do:

  $ pip install requests

Check out the [requests web site](http://docs.python-requests.org/) for
more information on installation and usage.

Go to the Pygame site to [download the Pygame binaries](http://pygame.org/download.shtml).

Code was tested with Python 2.7.

## Other Python Projects from the Community

* [Python library for interfacing with Open Spherical Camera (OSC) APIs](https://github.com/hpd/OpenSphericalCamera) by
[Haarm-Pieter Duiker](http://duikerresearch.com/about/)
* [Download media from command link with Python](https://github.com/theta360developers/python-download-rossgoderer) by
Ulrich Rossgoderer

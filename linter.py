#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Adam Altmejd
# Copyright (c) 2013 Adam Altmejd
# License: MIT
#

"""Uses chktex to lint LaTeX files."""

from SublimeLinter.lint import PythonLinter, util


class Chktex(PythonLinter):

    """ Provides an interface to use chktex in SublimeText with SublimeLinter3.

    Chktex uses stdin for input and stdout for output.
    Todo:
        - user settings
        - ignore some warnings
        - allow checking of latex scope in eg .Rnw (knitr) files
        - combine with lacheck?

    """

    syntax = ('latex', 'latexing', 'latexing (knitr)')
    selectors = {'latexing (knitr)': }

    cmd = 'chktex "-f%l:%c %k %m\n" '
    regex = (
        r'^(?P<line>\d+):(?P<col>\d+) '
        r'(?:(?P<error>Error)|(?P<warning>Warning)) '
        r'(?P<message>.+)'
    )
    error_stream = util.STREAM_STDOUT

    defaults = {

    }

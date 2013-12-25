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


class chktex(PythonLinter):

    """ Provides an interface to use chktex in SublimeText with SublimeLinter3.

    Chktex uses stdin for input and stdout for output.
    Todo:
        - user settings
        - ignore some warnings
        - allow checking of latex scope in eg .Rnw (knitr) files
        - combine with lacheck?

    """

    syntax = ('latex', 'latexing')
    selectors = {}

    cmd = 'chktex "-f%l:%c %k %m\n" '
    executable = None
    regex = (
        r'^(?P<line>\d+):(?P<col>\d+) '
        r'(?:(?P<error>Error)|(?P<warning>Warning)) '
        r'(?P<message>.+)'
    )

    multiline = False
    error_stream = util.STREAM_STDOUT

    line_col_base = (1, 1)
    tempfile_suffix = None
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    module = None
    check_version = False

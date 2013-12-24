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


class Latex(PythonLinter):

    """Provides an interface to chktex."""

    syntax = ('latex', 'latexing')
    cmd = 'chktex "-f%l:%c %k %m\n" '
    executable = None
    regex = (
        r'^(?P<line>\d+):(?P<col>\d+) '
        r'(?:(?P<error>Error)|(?P<warning>Warning)) '
        r'(?P<message>.+)'
    )
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_STDOUT
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    module = None
    check_version = False

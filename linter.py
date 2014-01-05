#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Adam Altmejd
# Copyright (c) 2013 Adam Altmejd
# License: MIT
#
# - Todo: make chktex ignore R code blocks in Knitr/Sweave environments instead
#   of linting scopes separately.

"""Uses chktex to lint LaTeX files."""

from SublimeLinter.lint import PythonLinter, util


class Chktex(PythonLinter):

    """ Provides an interface to use chktex in SublimeText with SublimeLinter3."""

    syntax = ('latex', 'latexing', 'latex (knitr)', 'knitr-rnw', 'latex beamer', 'latexing beamer')
    selectors = {
        'latex (knitr)': 'text.tex.latex.knitr.ing - meta.block.parameters.knitr - source.r.embedded.knitr',
        'knitr-rnw': 'text.tex.latex.knitr - meta.block.parameters.knitr - source.r.embedded.knitr'
    }

    cmd = 'chktex -wall "-f%l:%c %k %k %n: %m\n"'
    error_stream = util.STREAM_STDOUT
    regex = (
        r'^(?P<line>\d+):(?P<col>\d+) '
        r'(?:(?P<error>Error)|(?P<warning>Warning)) '
        r'(?P<message>.+)'
    )

    config_file = ('--localrc', 'chktexrc')
    defaults = {
        '--nowarn:,+': [22, 30],
        '--erroron:,+': [16]
    }
    inline_overrides = ('nowarn', 'erroron')
    comment_re = r'\s*%'

from SublimeLinter.lint import PythonLinter, util


class Chktex(PythonLinter):
    cmd = 'chktex -wall "-f%l:%c %k %k %n: %m\n"'
    error_stream = util.STREAM_STDOUT
    regex = (
        r'^(?P<line>\d+):(?P<col>\d+) '
        r'(?:(?P<error>Error)|(?P<warning>Warning)) '
        r'(?P<message>.+)'
    )
    defaults = {
        'selector': 'text.tex.latex - meta.block.parameters.knitr - source.r.embedded.knitr',
        '--nowarn:,+': [22, 30],
        '--erroron:,+': [16],
        '--inputfiles=': [0]
    }

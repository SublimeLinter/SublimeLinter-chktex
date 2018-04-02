SublimeLinter-chktex
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-chktex.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-chktex)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [ChkTeX](http://baruch.ev-en.org/proj/chktex/). It will be used with files that have use LaTeX (or LaTeXing) syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `chktex` is installed on your system. ChkTeX is available on [CTAN](http://www.ctan.org/pkg/chktex) and comes with e.g. [TeX Live](http://www.tug.org/texlive/) starting with TeX Live 2011, and available for many platforms.

If you are using a TeX distribution which does not include ChkTeX (for example MiKTeX) follow the instructions below to compile ChkTeX manually:

1. Make sure you don't have any [spaces in the path to MikTeX](http://stackoverflow.com/questions/30378183/cygwin-make-chktex-command-not-found)

2. Install [cygwin](http://cygwin.com/install.html) with the `make` and `gcc compiler` packages

3. Download [chktex](http://www.ctan.org/tex-archive/support/chktex) and save in home directory of cygwin (default is C:\cygwin\home\USER\)

4. In the cygwin bash, run
    ```
    cd c:
    cd cygwin64/home/USER
    cd chktex-1.7.2
    configure
    make
    make install
    ```


5. The resulting `chktex.exe` along with `cygwin1.dll` should now be saved in a directory which is registered in the PATH environment variable (for example %MiKTeX Install%\miktex\bin\ is appropriate)

In order for `chktex` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable).


## Settings
- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html

By default, SublimeLinter-chktex ignores Warning 22 (Comment displayed) and Warning 30 (Multiple spaces detected in output). It also sets Warning 16 (Mathmode is still on at end of LaTeX file) as an error.

Additional settings for `ckktex`:

- `nowarn`: A comma-separated list of warnings to ignore.
- `erroron`: A comma-separated list of warnings to output as errors.

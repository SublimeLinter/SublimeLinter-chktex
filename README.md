SublimeLinter-chktex
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-chktex.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-chktex)

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to [ChkTeX](http://baruch.ev-en.org/proj/chktex/). It will be used with files that have use LaTeX (or LaTeXing) syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
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

### Linter configuration
In order for `chktex` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once `chktex` is installed and configured, you can proceed to install the SublimeLinter-chktex plugin if it is not yet installed.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

2. When the plugin list appears, type `chktex`. Among the entries you should see `SublimeLinter-chktex`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

In addition to the standard SublimeLinter settings, SublimeLinter-chktex provides its own settings, which may also be [used inline](http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings) as overrides. For a full list of warnings see the [ChkTeX manual](http://ctan.uib.no/support/chktex/ChkTeX.pdf).

By default, SublimeLinter-chktex ignores Warning 22 (Comment displayed) and Warning 30 (Multiple spaces detected in output). It also sets Warning 16 (Mathmode is still on at end of LaTeX file) as an error.

|Setting|Description|Default|
|:------|:----------|:--------|
|nowarn|A comma-separated list of warnings to ignore. | [22,30] |
|erroron|A comma-separated list of warnings to output as errors. | [16] |

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!

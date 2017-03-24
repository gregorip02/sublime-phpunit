# WHAT PHPUNITKIT IS

[![Author](https://img.shields.io/badge/author-@gerardroche-blue.svg?style=flat-square&maxAge=86400)](https://twitter.com/gerardroche) [![Source Code](https://img.shields.io/badge/source-GitHub-blue.svg?style=flat-square&maxAge=86400)](https://github.com/gerardroche/sublime-phpunit) [![License](https://img.shields.io/badge/license-BSD--3-blue.svg?style=flat-square&maxAge=86400)](LICENSE) [![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-phpunit.svg?style=flat-square&maxAge=86400)](https://github.com/gerardroche/sublime-phpunit/stargazers) [![Latest version](https://img.shields.io/github/tag/gerardroche/sublime-phpunit.svg?style=flat-square&maxAge=86400&label=release)](https://github.com/gerardroche/sublime-phpunit/tags) [![Sublime version](https://img.shields.io/badge/sublime-v3.0.0-green.svg?style=flat-square&maxAge=86400)](https://sublimetext.com) [![Downloads](https://img.shields.io/packagecontrol/dt/phpunitkit.svg?style=flat-square&maxAge=86400)](https://packagecontrol.io/packages/phpunitkit)

PHPUNITKIT is a plugin that provides [PHPUnit](https://phpunit.de) support in [Sublime Text](https://sublimetext.com). It provides an abstraction over running tests from the command-line. It works best alongside other PHP development plugins such as [PHP Grammar], [PHP Snippets], and [PHP Completions].

![Screenshot](screenshot.png)

## OVERVIEW

* [Features](#features)
* [Commands](#commands)
* [Key Bindings](#key-bindings)
* [Configuration](#configuration)
* [Installation](#installation)
* [Contributing](#contributing)
* [Changelog](#changelog)
* [Credits](#credits)
* [License](#license)

## FEATURES

* Zero configuration required; Does the Right Thing™
* Fully customized CLI options configuration
* Supports [Composer]
* Supports colour test results (including failure diffs)
* Jump to next/previous test result failure via keybinding <kbd>F4</kbd>/<kbd>Shift+F4</kbd>
* Switch File (splits window and puts test case and class under test side by side)

## COMMANDS

All commands are prefixed with "PHPUnit: ".

Command | Description
--------|------------
Test Suite | Runs the whole test suite.
Test File | Runs all the tests in the current file test case.
Test Nearest | Runs the test nearest to the cursor. A multiple selection can used to used to run several tests at once.
Test Last | Runs the last test.
Switch File | Splits the window and puts nearest test case and class under test side by side.
Show Results |
Open Code Coverage |
Toggle Option |

## KEY BINDINGS

OS X | Windows / Linux | Command
-----|-----------------|------------
<kbd>Command</kbd>+<kbd>Shift</kbd>+<kbd>t</kbd> | <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>t</kbd> | Test Suite
<kbd>Command</kbd>+<kbd>Shift</kbd>+<kbd>r</kbd> | <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>r</kbd> | Test Nearest
<kbd>Command</kbd>+<kbd>Shift</kbd>+<kbd>e</kbd> | <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>e</kbd> | Test Last
<kbd>Command</kbd>+<kbd>Shift</kbd>+<kbd>.</kbd> | <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>.</kbd> | Switch File
<kbd>F4</kbd> | <kbd>F4</kbd> | Jump to next failure
<kbd>Shift</kbd>+<kbd>F4</kbd> | <kbd>Shift</kbd>+<kbd>F4</kbd> | Jump to previous failure

Vim/Vintage/Vintageous | Command
-----------------------|--------
<kbd>,</kbd><kbd>a</kbd> | Test Suite
<kbd>,</kbd><kbd>T</kbd> | Test File
<kbd>,</kbd><kbd>t</kbd> | Test Nearest
<kbd>,</kbd><kbd>l</kbd> | Test Last
<kbd>,</kbd><kbd>.</kbd> | Switch File

## CONFIGURATION

Key | Description | Type | Default
----|-------------|------|--------
`phpunit.options` | Command-line options to pass to PHPUnit. See [PHPUnit usage](https://phpunit.de/manual/current/en/textui.html#textui.clioptions) for an up-to-date list of command-line options. | `dict` | `{}`
`phpunit.keymaps` | Enable the default keymaps. | `boolean` | `true`
`phpunit.vi_keymaps` | Enable the default vi keymaps. | `boolean` | `true`
`phpunit.composer` | Enable [Composer] support. If a Composer installed PHPUnit executable is found then it is used to run tests. | `boolean` | `true`
`phpunit.save_all_on_run` | Enable writing out every buffer with changes in active window before running tests. | `boolean` | `true`
`phpunit.php_executable` | Use a custom PHP executable. | `string` | Uses PHP available on system path

### Composer

If a [Composer] installed PHPUnit executable is found then it is used to run tests, otherwise PHPUnit is assumed to be available via the system path.

To disable runinng tests via Composer installed PHPUnit: `Preferences > Settings`

```json
{
    "phpunit.composer": false
}
```

Or disable it per-project: `Project > Edit Project`

```json
{
    "settings": {
        "phpunit.composer": false
    }
}
```

### Options

If you want some CLI options to stick around use your [phpunit.xml](https://phpunit.de/manual/current/en/appendixes.configuration.html) file. Place it at the root of your project.

```
<?xml version="1.0" encoding="UTF-8"?>
<phpunit verbose="true" stopOnFailure="true">
    <php>
        <ini name="display_errors" value="1" />
        <ini name="xdebug.scream" value="0" />
    </php>
    <testsuites>
        <testsuite>
             <directory>tests</directory>
        </testsuite>
    </testsuites>
    <filter>
        <whitelist processUncoveredFilesFromWhitelist="true">
            <directory>src</directory>
        </whitelist>
    </filter>
</phpunit>
```

Or as Sublime Text global preferences: `Preferences > Settings`

```json
{
    "phpunit.options": {
        "v": true,
        "stop-on-failure": true,
        "no-coverage": true,
        "d": [
            "display_errors=1",
            "xdebug.scream=0"
        ]
    }
}
```

The above settings map to the following CLI Options passed to PHPUnit:

```
phpunit --stop-on-failure -d "display_errors=1" -d "xdebug.scream=0" -v --no-coverage
```

Or as per-project settings: `Project > Edit Project`

```json
{
    "settings": {
        "phpunit.options": {
            "v": true,
            "stop-on-failure": true,
            "no-coverage": true,
            "d": [
                "display_errors=1",
                "xdebug.scream=0"
            ]
        }
    }
}
```

The above settings map to the following CLI Options passed to PHPUnit:

```
phpunit --stop-on-failure -d "display_errors=1" -d "xdebug.scream=0" -v --no-coverage
```

## INSTALLATION

### Package Control installation

The preferred method of installation is [Package Control].

### Manual installation

1. Close Sublime Text.
2. Download or clone this repository to a directory named **`phpunitkit`** in the Sublime Text Packages directory for your platform:
    * Linux: `git clone https://github.com/gerardroche/sublime-phpunit.git ~/.config/sublime-text-3/Packages/phpunitkit`
    * OS X: `git clone https://github.com/gerardroche/sublime-phpunit.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/phpunitkit`
    * Windows: `git clone https://github.com/gerardroche/sublime-phpunit.git %APPDATA%\Sublime/ Text/ 3/Packages/phpunitkit`
3. Done!

## CONTRIBUTING

Your issue reports and pull requests are welcome.

### Debug messages

Debug messages are output to the Console (not the tests results output panel). Open the console: `Menu > View > Console` or click the icon in the bottom right of the status bar.

Debug messages are disabled by default. To enable them set an environment variable to a non-blank value e.g. `SUBLIME_PHPUNIT_DEBUG=y`. To disable them set unset it or set it to a blank value e.g. `SUBLIME_PHPUNIT_DEBUG=`.

For more information on environment variables read [What are PATH and other environment variables, and how can I set or use them?](http://superuser.com/questions/284342/what-are-path-and-other-environment-variables-and-how-can-i-set-or-use-them)

#### Linux

Sublime Text can be started at the Terminal with an exported environment variable.

```
$ export SUBLIME_PHPUNIT_DEBUG=y; subl
```

To set the environment permanently set it in `~/.profile` (requires restart).

```
export SUBLIME_PHPUNIT_DEBUG=y
```

Alternatively, create a [debug script (subld)](https://github.com/gerardroche/dotfiles/blob/1a27abed589f2fea9126a0496ef4d1cae0479722/src/bin/subld) with debugging environment variables enabled.

#### Windows

Sublime Text can be started at the Command Prompt with an exported environment variable.

```
> set SUBLIME_PHPUNIT_DEBUG=y& "C:\Program Files\Sublime Text 3\subl.exe"
```

To set the environment permanently set it as a *system* environment variable (requires restart).

1. Control Panel > System and Security > System > Advanced system settings
2. Advanced > Environment Variables
3. System variables > New...
4. Add Variable name `SUBLIME_PHPUNIT_DEBUG` with Variable value `y`
5. Restart Windows

### Running tests

To be able to run the tests enable plugin development. This will make the command "PHPUnit: Run all Plugin Tests" available in the Command Palette.

Preferences > Settings - User

```
{
    "phpunit.development": true
}
```

## CHANGELOG

See [CHANGELOG.md](CHANGELOG.md).

## CREDITS

Based initially on [maltize/sublime-text-2-ruby-tests](https://github.com/maltize/sublime-text-2-ruby-tests) and [stuartherbert/sublime-phpunit](https://github.com/stuartherbert/sublime-phpunit). And inspired by [janko-m/vim-test](https://github.com/janko-m/vim-test).

## LICENSE

Released under the [BSD 3-Clause License](LICENSE).

[Package Control]: https://packagecontrol.io/browse/authors/gerardroche
[PHP Grammar]: https://packagecontrol.io/browse/authors/gerardroche
[PHP Completions]: https://packagecontrol.io/browse/authors/gerardroche
[PHP Snippets]: https://packagecontrol.io/browse/authors/gerardroche
[PHPUnit]: https://packagecontrol.io/browse/authors/gerardroche
[Composer]: https://getcomposer.org

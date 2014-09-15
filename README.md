`$ termrule_`
=============

Tired of destroying the Enter key by creating a "void zone" in your terminal so that you can see the error that you're trying to debug? If yes, this is for you. `termrule` allows you to create colored horizontal rule in terminal. Use it in place of the old `<hr />` tag in terminal. This script is inspired from `hr.py` by euangoddard. Works on both Python 2.7 & 3.4. *The script is now accessed by `rl` instead of `tr` due to clashes*

### Installation:
` $ pip install termrule `

### Supported Colors:
Below is the list of all color names you can use, if an invalid color is entered, an `InvalidColorException` will be raised.
 - grey
 - red
 - green
 - yellow
 - blue
 - magenta
 - cyan
 - white

### Usage:
The `color` parameter is optional, if it is not passed, then the default the green color will be used.

#### Command Line:
```
usage: rl [-h] [--color COLOR] [symbol [symbol ...]]

positional arguments:
  symbol         Symbol for horizontal line

optional arguments:
  -h, --help     show this help message and exit
  --color COLOR  Color of the line
```
```
$ rl
#################################### # Till the end of terminal 

$ rl "&"
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
```
You can also create beautiful ASCII patterns
```
$ rl "#-#"
#-##-##-##-##-##-##-##-##-##-##-##- # Till the end of termnial 

$ rl "*-*" --color red
*-**-**-**-**-**-**-**-**-**-**-**- # Till the end of terminal in red color
```

#### Script:
```python
>>> from tr import TermRule
>>> r = TermRule()
>>> r.tr(["#", "-"], color="cyan")
##################################### # Till the end of terminal in cyan color
-------------------------------------
>>> r.tr(["^"])
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ # Till the end of terminal in default color
>>> r.tr(["@-@"])
@-@@-@@-@@-@@-@@-@@-@@-@@-@@-@@-@@-@@
```
### Tests:
Unitests is used as the testing library, run `python test_termrule.py` to see all tests pass :)

### Dependencies:
`termcolor` is the only dependency; it is used for colored outputs, and I hope you know that `python 2.7` or `python 3.4` is also required (isn't that obvious?)

### License:
`termrule` is distributed under MIT license, see `LICENSE` for more details


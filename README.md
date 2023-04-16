# Pypsorem
Pypsorem is a Python script that generates Lorem Ipsum text according to your needs. Whether you need paragraphs, words, lists, or bytes of placeholder text, Pypsorem can provide it for you quickly and easily.
This script has a Command-line Interface that provides a service API for [lipsum.com](https://lipsum.com), which you may or may not know as the go-to place to generate arbitrary dummy text whenever you need it. 
This Python code is also inspired by [node-lipsum](https://github.com/traviskaufman/node-lipsum), a NodeJS Module equivalent written in CoffeeScript.


# Installation

First of all, clone this repository
```Bash
git clone https://github.com/RMI78/Pypsorem
```

then run setup.py to build the package :
```Bash
python setup.py sdist bdist_wheel
```

and finally, install it via pip :
```Bash
pip install /path/to/dist/package_name-version.whl
```

# Usage

To use PyPsorem, simply run the pypsorem command followed by the arguments you want to use. PyPsorem accepts the following arguments:

    -v or --version: Displays the current version of PyPsorem and exits.
    -s or --start-with-lipsum: Whether or not your text starts with the classic "Lorem Ipsum" placeholder text. Defaults to False.
    -w or --what: The type of text you want to generate. Valid options are "paras" (paragraphs), "words", "lists", or "bytes". Defaults to "paras".
    -a or --amount: The number of text structures you want to generate. Defaults to 5.

For example, to generate 10 paragraphs of Lorem Ipsum text that start with the classic "Lorem Ipsum" placeholder, you would run the following command:
```Python
pypsorem -s -w paras -a 10
```
Pypsorem will then generate the text and print it to your console.
From here, you can pipe the output of Pypsorem to other softwares or appends to files

# License

Pypsorem is licensed under the MIT License. See the LICENSE file for more information.


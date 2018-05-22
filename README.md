Parse football statistic from [myscore.ua](http://myscore.ua/)
==============================================================

[![Python version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)

# Installation
```
git clone https://github.com/lerdem/myscore-parser.git
```
###### Dependencies
also install _[geckodriver](https://github.com/mozilla/geckodriver/releases/tag/v0.20.0)_
# Example
make file executable
```
chmod +x main.py
```
start parsing all result for championship season 17-18 run next line
```
./main.py --start yes https://www.myscore.ua/soccer/england/championship/results/ championship17-18
```

your target url - https://www.myscore.ua/soccer/england/championship/results/

your project name - championship17-18

# Restore
You can break running script any time, and restore project 
```
./main.py --restore yes https://www.myscore.ua/soccer/england/championship/results/ championship17-18
```

# Uninstallation
remove parser
```
rm -r myscore-parser/
```

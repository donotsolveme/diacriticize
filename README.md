# Diacriticize

A package that ḑ͌̓͜ ̧ͤ́ͫe̹͚͛̔ ̸̞̓ͩm͚̜̅́ ̷͉̽͊o̗͚̊̕ ͖̈ͧ̓l̴̢͈̋ ̲̰̅͏i̧̨̳͇ ̮̦̠͟s̢͒̎͌ ͉ͣͩ͢ḩ͙͍͌ ̵̤̿ͣe̡͑͊͊ ̯̪͙̅s̶ͬ͒̆ strings (also called *zalgo*)

## Usage
As a module:
```py
from diacriticize import diacriticize

out = diacriticize("input string")
```

Also includes a cli tool:
```bash
$ diacriticize -h
usage: diacriticize [-h] [--times TIMES] [--unsafe-range] input

combine input chars with random diacritical marks

positional arguments:
  input

options:
  -h, --help            show this help message and exit
  --times TIMES, -t TIMES
                        number of diacritical marks to combine (default: 4)
  --unsafe-range, -u    use characters not visible in common fonts
```

## Installation
```bash
$ pip install -U diacriticize
```

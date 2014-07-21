SiLoHa
======

Simple log handler

## Usage:

Import with:

```
from siloha import LogHandler
```

And get your log object:

```
log = LogHandler()
```

Log your stuff:

```
log.msg('Hi dude!')
```


## Options:
We can pass the following options to the object constructor:

* Set debug mode on:

```
debug=True
```

* Set log type colors:

```
msgColor=color
alertColor=color
warnColor=color
errorColor=color
```

* Set log type symbol

```
msgSym=symbol
alertSym=symbol
warnSym=symbol
errorSym=symbol
```

By default the symbols and colors are:

* [*] none

* [+] Yellow

* [>] Purple

* [!] Red

The available colors are:

* none

* white

* black

* cyan

* blue

* green

* yellow

* purple

* red

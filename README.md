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

## Log modes:

There are log messages, debug only messages and nested debug messages:

```
log.msg('This is a message')
log.alert('This is an alert message')
log.warn('This is a warn message')
log.error('This is an error message')

log.debug('This is a debug message')
log.dbgAlert('This is a debug alert message')
log.dbgWarn('This is a debug warn message')
log.dbgError('This is a debug error message')

log.dbgNested('This is a nested debug message')
log.dbgNestedAlert('This is a nested debug alert message')
log.dbgNestedWarn('This is a nested debug warn message')
log.dbgNestedError('This is a nested debug error message')
```
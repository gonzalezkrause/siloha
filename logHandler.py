#!/usr/bin/env python
# -*- coding: utf-8 -*-
##################################################################
# Simple Logger -- logHandler.py
# By José F. González Krause
# Licensed under MIT
##################################################################


class LogHandler(object):
   '''
   Simple Log Handler
   '''

   def __init__(self, **kw):
      super(LogHandler, self).__init__()
      # 30m - Black
      # 31m - Red
      # 32m - Green
      # 33m - Yellow
      # 34m - Blue
      # 35m - Purple
      # 36m - Cyan
      # 37m - White
      # 39m - No color
      # 0 - Normal
      # 1 - Bold

      self.colors = {
         'bold': ['\x1b[22m', '\x1b[1m'],
         'underline': ['\x1b[24m', '\x1b[4m'],
         'none': ['\x1b[39m', '\x1b[39m'],
         'white': ['\x1b[39m', '\x1b[37m'],
         'black': ['\x1b[39m', '\x1b[30m'],
         'cyan': ['\x1b[39m', '\x1b[36m'],
         'blue': ['\x1b[39m', '\x1b[34m'],
         'green': ['\x1b[39m', '\x1b[32m'],
         'yellow': ['\x1b[39m', '\x1b[33m'],
         'purple': ['\x1b[39m', '\x1b[35m'],
         'red': ['\x1b[39m', '\x1b[31m']
      }

      self.dbg = kw.get('debug', False)
      msgColor = kw.get('msgColor', 'none')
      alertColor = kw.get('alertColor', 'yellow')
      warnColor = kw.get('warnColor', 'purple')
      errorColor = kw.get('errorColor', 'red')
      msgSym = kw.get('msgSym', '*')
      alertSym = kw.get('alertSym', '+')
      warnSym = kw.get('warnSym', '>')
      errorSym = kw.get('errorSym', '!')

      self.logColor = {
         'msg': msgColor,
         'alert': alertColor,
         'warn': warnColor,
         'error': errorColor
      }

      self.logSymbol = {
         'msg': msgSym,
         'alert': alertSym,
         'warn': warnSym,
         'error': errorSym
      }


   def msg(self, msg):
      print('[{0}] {1}').format(self.logSymbol['msg'], msg)


   def alert(self, msg):
      print('{0}[{3}]{1} {2}').format(
         self.colors[self.logColor['alert']][1], 
         self.colors[self.logColor['alert']][0], 
         msg,
         self.logSymbol['alert']
      )


   def warn(self, msg):
      print('{0}[{5}] {1}{2}{3}{4}').format(
         self.colors[self.logColor['warn']][1],
         self.colors['underline'][1],
         msg,
         self.colors['underline'][0],
         self.colors[self.logColor['warn']][0],
         self.logSymbol['warn']
      )

      
   def error(self, msg):
      print('{0}[{3}]{1} {2}').format(
         self.colors[self.logColor['error']][1], 
         self.colors[self.logColor['error']][0], 
         msg,
         self.logSymbol['error']
      )


   #######################
   # Nested log messages #
   #######################
   def nestedMsg(self, msg):
      print('[{1}]\t└── {0}').format(msg, self.logSymbol['msg'])


   def nestedAlert(self, msg):
      print('{0}[{3}]{1}\t└── {2}').format(
         self.colors[self.logColor['alert']][1], 
         self.colors[self.logColor['alert']][0], 
         msg,
         self.logSymbol['alert']
      )


   def nestedWarn(self, msg):
      print('{0}[{5}]\t└── {1}{2}{3}{4}').format(
         self.colors[self.logColor['warn']][1],
         self.colors['underline'][1],
         msg,
         self.colors['underline'][0],
         self.colors[self.logColor['warn']][0],
         self.logSymbol['warn']
      )


   def nestedError(self, msg):
      print('{0}[{3}]{1}\t└── {2}').format(
         self.colors[self.logColor['error']][1],
         self.colors[self.logColor['error']][0],
         msg,
         self.logSymbol['error']
      )


   ################################################
   # Only used with debug=True, these methods are # 
   # extensions of the debug mode.                #
   ################################################
   def debug(self, msg):
      if self.dbg:
         print('[{1}] {0}').format(msg, self.logSymbol['msg'])
      else:
         return


   def dbgAlert(self, msg):
      if self.dbg:
         print('{0}[{3}]{1} {2}').format(
            self.colors[self.logColor['alert']][1], 
            self.colors[self.logColor['alert']][0], 
            msg,
            self.logSymbol['alert']
         )
      else:
         return


   def dbgWarn(self, msg):
      if self.dbg:
         print('{0}[{5}] {1}{2}{3}{4}').format(
            self.colors[self.logColor['warn']][1],
            self.colors['underline'][1],
            msg,
            self.colors['underline'][0],
            self.colors[self.logColor['warn']][0],
            self.logSymbol['warn']
         )
      else:
         return


   def dbgError(self, msg):
      print('{0}[{3}]{1} {2}').format(
         self.colors[self.logColor['error']][1], 
         self.colors[self.logColor['error']][0], 
         msg,
         self.logSymbol['error']
      )


   #########################
   # Nested debug messages #
   #########################
   def dbgNested(self, msg):
      if self.dbg:
         print('[{1}]\t└── {0}').format(msg, self.logSymbol['msg'])
      else:
         return


   def dbgNestedAlert(self, msg):
      if self.dbg:
         print('{0}[{3}]{1}\t└── {2}').format(
            self.colors[self.logColor['alert']][1], 
            self.colors[self.logColor['alert']][0], 
            msg,
            self.logSymbol['alert']
         )
      else:
         return


   def dbgNestedWarn(self, msg):
      if self.dbg:
         print('{0}[{5}]\t└── {1}{2}{3}{4}').format(
            self.colors[self.logColor['warn']][1],
            self.colors['underline'][1],
            msg,
            self.colors['underline'][0],
            self.colors[self.logColor['warn']][0],
            self.logSymbol['warn']
         )
      else:
         return


   def dbgNestedError(self, msg):
      if self.dbg:
         print('{0}[{3}]{1}\t└── {2}').format(
            self.colors[self.logColor['error']][1],
            self.colors[self.logColor['error']][0],
            msg,
            self.logSymbol['error']
         )
      else:
         return


if __name__ == '__main__':
   log = LogHandler(debug=True)

   log.msg('This is a message')
   log.alert('This is an alert message')
   log.warn('This is a warn message')
   log.error('This is an error message')

   print('\n=================')
   log.nestedMsg('This is a nested message')
   log.nestedAlert('This is a nested alert message')
   log.nestedWarn('This is a nested warn message')
   log.nestedError('This is a nested error message')
   
   print('\n=================')
   log.debug('This is a debug message')
   log.dbgAlert('This is a debug alert message')
   log.dbgWarn('This is a debug warn message')
   log.dbgError('This is a debug error message')
   
   print('\n=================')
   log.dbgNested('This is a nested debug message')
   log.dbgNestedAlert('This is a nested debug alert message')
   log.dbgNestedWarn('This is a nested debug warn message')
   log.dbgNestedError('This is a nested debug error message')
   
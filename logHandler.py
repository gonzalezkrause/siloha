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

   def __init__(self, debug=False):
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
         'black': ['\x1b[39m', '\x1b[30m'],
         'red': ['\x1b[39m', '\x1b[31m'],
         'green': ['\x1b[39m', '\x1b[32m'],
         'yellow': ['\x1b[39m', '\x1b[33m'],
         'blue': ['\x1b[39m', '\x1b[34m'],
         'purple': ['\x1b[39m', '\x1b[35m'],
         'cyan': ['\x1b[39m', '\x1b[36m'],
         'white': ['\x1b[39m', '\x1b[37m']
      }

      if 'debug':
         self.dbg = True
      else:
         self.dbg = False



   def msg(self, msg):
      print('[*] {0}').format(msg)


   def alert(self, msg):
      print('{0}[+]{1} {2}').format(
         self.colors['yellow'][1], 
         self.colors['yellow'][0], 
         msg
      )


   def warn(self, msg):
      print('{0}[>] {1}{2}{3}{4}').format(
         self.colors['purple'][1],
         self.colors['underline'][1],
         msg,
         self.colors['underline'][0],
         self.colors['purple'][0]
      )

      
   def error(self, msg):
      print('{0}[!]{1} {2}').format(
         self.colors['red'][1], 
         self.colors['red'][0], 
         msg
      )




   ################################################
   # Only used with debug=True, these methods are # 
   # extensions of the debug mode.                #
   ################################################
   def debug(self, msg):
      if self.dbg:
         print('[*] {0}').format(msg)
      else:
         return


   def dbgAlert(self, msg):
      if self.dbg:
         print('{0}[+]{1} {2}').format(
            self.colors['yellow'][1], 
            self.colors['yellow'][0], 
            msg
         )
      else:
         return


   def dbgWarn(self, msg):
      if self.dbg:
         print('{0}[>] {1}{2}{3}{4}').format(
            self.colors['purple'][1],
            self.colors['underline'][1],
            msg,
            self.colors['underline'][0],
            self.colors['purple'][0]
         )
      else:
         return


   def dbgError(self, msg):
      print('{0}[!]{1} {2}').format(
         self.colors['red'][1], 
         self.colors['red'][0], 
         msg
      )


   #########################
   # Nested debug messages #
   #########################
   def dbgNested(self, msg):
      if self.dbg:
         print('[*]\t└── {0}').format(msg)
      else:
         return


   def dbgNestedAlert(self, msg):
      if self.dbg:
         print('{0}[+]{1}\t└── {2}').format(
            self.colors['yellow'][1], 
            self.colors['yellow'][0], 
            msg
         )
      else:
         return


   def dbgNestedWarn(self, msg):
      if self.dbg:
         print('{0}[>]\t└── {1}{2}{3}{4}').format(
            self.colors['purple'][1],
            self.colors['underline'][1],
            msg,
            self.colors['underline'][0],
            self.colors['purple'][0]
         )
      else:
         return


   def dbgNestedError(self, msg):
      if self.dbg:
         print('{0}[+]{1}\t└── {2}').format(
            self.colors['red'][1],
            self.colors['red'][0],
            msg
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
   log.debug('This is a debug message')
   log.dbgAlert('This is a debug alert message')
   log.dbgWarn('This is a debug warn message')
   log.dbgError('This is a debug error message')
   
   print('\n=================')
   log.dbgNested('This is a nested debug message')
   log.dbgNestedAlert('This is a nested debug alert message')
   log.dbgNestedWarn('This is a nested debug warn message')
   log.dbgNestedError('This is a nested debug error message')
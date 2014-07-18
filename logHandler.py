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
         'bold':{True:'\x1b[1m',False:'\x1b[22m'},
         'black':{True:'\x1b[30m',False:'\x1b[39m'},
         'red':{True:'\x1b[31m',False:'\x1b[39m'},
         'green':{True:'\x1b[32m',False:'\x1b[39m'},
         'yellow':{True:'\x1b[33m',False:'\x1b[39m'},
         'blue':{True:'\x1b[34m',False:'\x1b[39m'},
         'purple':{True:'\x1b[35m',False:'\x1b[39m'},
         'cyan':{True:'\x1b[36m',False:'\x1b[39m'},
         'white':{True:'\x1b[37m',False:'\x1b[39m'},
         'underline':{True:'\x1b[4m',False:'\x1b[24m'}
      }

      if 'debug' in kw:
         self.dbg = kw['debug']
      else:
         self.dbg = False


   def msg(self, msg):
      print('[*] {0}').format(msg)


   def error(self, msg):
      print('{0}[!]{1} {2}').format(
         self.colors['red'][True], 
         self.colors['red'][False], 
         msg
      )


   def alert(self, msg):
      print('{0}[+]{1} {2}').format(
         self.colors['yellow'][True], 
         self.colors['yellow'][False], 
         msg
      )


   def warn(self, msg):
      print('{0}[*] {1}{2}{3}{4}').format(
         self.colors['purple'][True],
         self.colors['underline'][True],
         msg,
         self.colors['underline'][False],
         self.colors['purple'][False]
      )


   ################################################
   # Only used with debug=True, these methods are # 
   # extensions of the debug mode.                #
   ################################################
   def debug(self, msg):
      if self.dbg:
         print('[-] {0}').format(msg)
      else:
         return

   def dbgError(self, msg):
      print('{0}[!]{1} {2}').format(
         self.colors['red'][True], 
         self.colors['red'][False], 
         msg
      )



   def debNested(self, msg):
      if self.dbg:
         print('[-]\t└── {0}').format(msg)
      else:
         return


   def debNestedAlert(self, msg):
      if self.dbg:
         print('{0}[+]{1}\t└── {2}').format(s
            elf.colors['yellow'][True], 
            self.colors['yellow'][False], 
            msg
         )
      else:
         return


   def debAlert(self, msg):
      if self.dbg:
         print('{0}[+]{1} {2}').format(
            self.colors['yellow'][True], 
            self.colors['yellow'][False], 
            msg
         )
      else:
         return



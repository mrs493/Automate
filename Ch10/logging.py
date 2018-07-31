import logging

'''
logs can be catagrized into levels based on importance
these levels are shown below in order of importance,
aswell as how and when they are used in the format:
Level
Logging Function
Description

DEBUG
logging.debug()
The lowest level. Used for small details.
Usually you care about these messages
only when diagnosing problems.

INFO
logging.info()
Used to record information on general
events in your program or confirm that
things are working at their point in the
program.

WARNING
logging.warning()
Used to indicate a potential problem that
doesn’t prevent the program from working
but might do so in the future.

ERROR
logging.error()
Used to record an error that caused the
program to fail to do something.

CRITICAL
logging.critical()
The highest level. Used to indicate a fatal
error that has caused or is about to cause
the program to stop running entirely
'''

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
#only logs of the same or higher level as the level argument will be shown
'''
appears not to work in spyder, always shows debug and up
'''
#logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#passing a filename argument writes logs to a file rather than the terminal
'''
unless you're using spyder -_-
'''

#logging.disable(logging.CRITICAL)
#disables logging statements for logs of the given level and lower
'''
in spyder is remembered between runs, so commenting out alone will not re-enable all levels
need to either change argument to lower level and run, or comment out and reopen spyder
'''

logging.debug('Some debugging details.')

logging.info('The logging module is working.')

logging.warning('An error message is about to be logged.')

logging.error('An error has occurred.')

logging.critical('The program is unable to recover!')
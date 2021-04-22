# Perform Troubleshooting and Error Handling

# Вопрос: какая будет ошибка? В какой строке?

#a = 1 ; b = 2 ; c == a + b ;
"""
Error Handling\Lab1_6demo.py", line 5, in <module>
    a = 1 ; b = 2 ; c == a + b ;
NameError: name 'c' is not defined
"""
a = 1 ; b = 2 ; c = a + b ;
print(c)

# Ошибки времени выполнения
a1 = 53
b1 = 10
c1 = a1/b1  # ZeroDivisionError: division by zero

# Try to open a non-existent file and note the error generated
# publishingfile = open("np041215web.xml","r")

# Use a try / except statement to change the message generated
try:
    publishingfile = open("np041215web.xml","r")
except IOError: print('The file does not exist or is not available. Please verify the file name and try again.')

# Create the file and try opening it again.  Add an else clause to print a message when successful.
try:\
    publishingfile = open("np041215web.xml","r")
except IOError: print('The file does not exist or is not available.  Please verify the file name and try again.')
else:
    print('The file was opened successfully.')
    publishingfile.close()

# Use the raise statement to manually generate an error, then use it to test an except clause that responds to the error.
try:
    import numpy as np
    array1 = np.array([2,4,6,8,10])
    max1 = array1.max()
    raise ModuleNotFoundError
except ModuleNotFoundError: print("Please install the missing module and try again.")

# Add additional except clauses to see how the try statement behaves
try:
    import numpy as np
    array1 = np.array([2,4,6,8,10])
    max1 = array1.max()
    raise ModuleNotFoundError
    raise ValueError
except ModuleNotFoundError: print("Please install the missing module and try again.")
except (IOError, ValueError): print("Please make sure the required resource is available or specify the correct syntax.")
except KeyboardInterrupt: print("Please wait until the process is finished.")


# Include else and finally clauses\n",
try:
    import numpy as np
    array1 = np.array([2,4,6,8,10])
    max1 = array1.max()
    raise ModuleNotFoundError
except ModuleNotFoundError: print("Please install the missing module and try again.")
else:
        print("The operation was successful.")
finally:
        print("The end.")


# Use the logging module to create a log file that stores all 5 message levels.
# Record log entries to test it then view the file content
import logging, os, platform, datetime
timestring = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
logfile = 'python_' + timestring + '.log'
logging.basicConfig(filename=logfile, level=logging.DEBUG,format='%(asctime)s_%(levelname)s: %(message)s')
logging.debug('This is a debug message.')
logging.info('This is an info message.')
logging.warning('This is a warning message.')
logging.error('This is an eror message.')
logging.critical('This is a critical message.')
if platform.system() == 'Windows':
    os.system('type ' + logfile)
else:
    os.system('cat ' + logfile)




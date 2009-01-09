import os
import re
import pprint as pprint # for testing

def loadListFromFile (filename):
    """Loads a list of strings from file.  Will append to given list
    if asked."""
    retval = []
    filename = os.path.expanduser (filename)
    if not os.path.exists (filename):
        print "Error: '%s' file does not exist."
        raise RuntimeError, "Bad filename"
    source = open (filename, 'r')        
    for line in source.readlines():
        line = re.sub (r'#.+$', '', line) # remove comment characters
        line = line.strip()
        if len (line):
            retval.append (line)
    source.close()
    return retval


##############################################################################
## ######################################################################## ##
## ##                                                                    ## ##
## ######################################################################## ##
##############################################################################

    
if __name__ == "__main__":
    #############################################
    ## Load and save command line history when ##
    ## running interactively.                  ##
    #############################################
    import os, readline
    import atexit
    historyPath = os.path.expanduser("~/.pyhistory")


    def save_history(historyPath=historyPath):
        import readline
        readline.write_history_file(historyPath)
        if os.path.exists(historyPath):
            readline.read_history_file(historyPath)


    atexit.register(save_history)
    readline.parse_and_bind("set show-all-if-ambiguous on")
    readline.parse_and_bind("tab: complete")
    if os.path.exists (historyPath) :
        readline.read_history_file(historyPath)
        readline.set_history_length(-1)


    ############################
    # Example code starts here #
    ############################

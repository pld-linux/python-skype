#!/usr/bin/python
# ---------------------------------------------------------------------------------------------
#  Python / Skype4Py example that takes a skypename from command line parameter,
#  checks if that skypename is in contact list and if yes then starts a chat to that skypename.
#
#  Tested with  Skype4Py version 1.0.31.0 and Skype verson 2.0.0.72

import sys
import Skype4Py

# Let's see if we were started with a command line parameter..
try:
    CmdLine = sys.argv[1]
except:
    print 'Missing command line parameter'
    sys.exit()

# strip skype: prefix
if CmdLine[:6] == "skype:":
	CmdLine = CmdLine[6:]

# Creating Skype object and assigning event handlers..
skype = Skype4Py.Skype()

# Starting Skype if it's not running already..
if not skype.Client.IsRunning:
    print 'Starting Skype..'
    skype.Client.Start()

# Attatching to Skype..
print 'Connecting to Skype..'
skype.Attach()

# Checking if what we got from command line parameter is present in our contact list
Found = False
for F in skype.Friends:
    if F.Handle == CmdLine:
        Found = True
        print 'Chatting ' + F.Handle + '..'
        chat = skype.CreateChatWith(CmdLine);
        chat.OpenWindow()
        break

if not Found:
    print 'Call target not found in contact list'
    sys.exit()

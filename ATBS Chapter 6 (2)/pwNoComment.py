#! python3
# pw.py - An insecure password locker program


PASSWORDS = {'email': 'ocegueda22',
            'steam': 'pridetothegenocide',
            'hulu': 'laurel527'} 			

import sys, pyperclip
if len(sys.argv) < 2: 	                       
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
	
account = sys.argv[1]                           

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])		
    print('Password for ' + account + ' copied to the clipboard.')
else:
    print('There is no account named ' + account)
 


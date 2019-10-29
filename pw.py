#! python3
# pw.py - An inseure password locker program.

PASSWORDS = {'email': 'wqiU327UIudu8e2487u897672EN3 $##$5',
'phone': '24901383',
'fb': 'wu3m39es@44@#jsnJWJUWI3948D9ED8ssw'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
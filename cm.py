#!/usr/bin/env python
#file name : cm.py
#Copyright (c) Arun.K.R
#Creative Commons Attribution-Share Alike 3.0 Unported' <http://creativecommons.org/licenses/by-sa/3.0/>
#short for 'c'ontact 'm'anager
#This is the entry point to the program
#loads my own module cb.py which contains ContactBook class
#which is the base of our implementation
import cb
import sys

def showHelp():
	'''show help for cm program'''
	print '''Usage: cm OPTION(S) [CONTACT_NAME]
This program manages your contacts efficiently.

OPTIONS without CONTACT_NAME
-h		help
-v		version
-a		add contact
-l		list all contact's name

OPTIONS with CONTACT_NAME
-r 		remove contact
-m		modify contact
-c  	show specified contact

No two OPTIONS can be specified at a time.
example:
cm -l 		:lists all contact's name
cm -r Ragu	:removes contact of Ragu (if already there)'''

def showVer():
	'''prints version of program'''
	print '''cm (Contacts Manager) version 1.0
Copyright (C) 2008 Arun.K.R, MegaWare(tm) <www.megaware.co.nr>
This is free software.  You may redistribute copies of it under the terms of
the 'Creative Commons Attribution-Share Alike 3.0 Unported' <http://creativecommons.org/licenses/by-sa/3.0/>.\
There is NO WARRANTY, to the extent permitted by law.
Written by Arun.K.R <code333 at gmail dot com>'''

cv = cb.ContactBook() #creates an object of ContactBook class

argLn = len(sys.argv) # this helps to speed up a littile bit (from my C++  experiance.)
#this is because we don't need to calculate length again and again.
if argLn < 2 or argLn > 3:
	showHelp()
elif argLn == 2:
	op = sys.argv[1][1] #reads second argument without trailing '-'
	#ToDo : what if argument is like this "cm -hv" which is obviously false
	op = op.lower()
	if op == 'h' : #shows help
		showHelp()
	elif op == 'v': #shows version
		showVer()
	elif op == 'a': #add a contact
		name = str(raw_input('Enter Name : '))
		#ToDo: for the next two we can add more than one items of each
		#also we can check for validity.ie., email address and phone number are
		#in proper format. also any constraints for name should also needs to be implemented.
		email = str(raw_input('Enter email, <enter> for none : '))
		phone = str(raw_input('Enter phone, <enter> for none : '))
		if email == '\n': email = None
		if phone == '\n': phone = None
		cv.updateContact(name, email, phone)
	elif op == 'l': #print all contact's name
		cv.showNames()
	else: #invalied argument format
		print 'Invalied argument(s)'
		showHelp()
else: #there are 3 arguments
	op = sys.argv[1][1] #reads second argument without trailing '-'
	#ToDo : what if argument is like this "cm -cm" which is obviously false
	op = op.lower()
	name = sys.argv[2]
	if op == 'c': #show specified contcat
		cv.showContact(name)
	elif op == 'm': #modify given account
		#ToDo: for the next two we can add more than one items of each
		#also we can check for validity.ie., email address and phone number are
		#in proper format.
		print 'curent email is %s' % cv.getEmail(name)
		email = str(raw_input('Enter new email, <enter> for current : '))
		print 'current phone is %s' % cv.getPhone(name)
		phone = str(raw_input('Enter new phone, <enter> for current : '))
		if email == '\n': email = cv.getEmail(name)
		if phone == '\n': phone = cv.getPhone(name)
		cv.updateContact(name, email, phone)
	elif op == 'r': #remove a contact
		if cv.hasContact(name) == True:
			print '\n following contact will be permanantly removed'
			cv.showContact(name)
			if str(raw_input('do you want to continue (y/n): ')).lower() == 'y':
				cv.rmContact(name)
		else:
			print 'There is no contact in this <%s> name' % name
	else: #invalied argument format
		print 'Invalied arguments'
		showHelp()
#program ends here
#|ലോകത്തിലെല്ലാവര്ക്കും നന്മ വരട്ടെ|लोका समस्ता सुखिनॊ भवन्तु |

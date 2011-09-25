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
-h		Help
-v		Version
-n		New contact
-l		List all contact's name

OPTIONS with CONTACT_NAME
-r 		Remove contact
-m		Modify contact
-d  	Display contact
-a		Add info. to existing contact

No two OPTIONS can be specified at a time.
example:
cm -l 		:lists all contact's name
cm -r Ragu	:removes contact of Ragu (if already there)'''

def showVer():
	'''prints version of program'''
	print '''cm (Contacts Manager) version 2.0
Copyright (C) 2008 Arun.K.R, MegaWare(tm) <www.megaware.co.nr>
This is free software.  You may redistribute copies of it under the terms of
the 'Creative Commons Attribution-Share Alike 3.0 Unported' <http://creativecommons.org/licenses/by-sa/3.0/>.\
There is NO WARRANTY, to the extent permitted by law.
Written by Arun.K.R <code333 at gmail dot com>'''

def addToList(lst, itm):
	'''append an item 'itm' to list 'lst'

	care should be taken. ie., lst must be a list'''
	lst.append(itm)
	return lst

def isRepeated(customise):
	while True:
		itr = str(raw_input('Do you want to add %s (y/n) : ' % customise)).lower()
		if itr == 'y' or itr == 'n' :
			break
	return itr

cv = cb.ContactBook() #creates an object of ContactBook class

argLn = len(sys.argv) # this helps to speed up a littile bit (from my C++  experiance.)
#this is because we don't need to calculate length again and again.
if argLn < 2 or argLn > 3:
	showHelp()
elif argLn == 2:
	if len(sys.argv[1]) > 2 : #ie., '-' and OPTION, OPTION is always one character.
		showHelp()
	else:
		op = sys.argv[1][1] #reads second argument without trailing '-'
		op = op.lower()
		if op == 'h' : #shows help
			showHelp()
		elif op == 'v': #shows version number
			showVer()
		elif op == 'n': #add a new contact
			name = str(raw_input('Enter Name : '))
			#ToDo: we can check for validity.ie., email address and phone number are in proper format.
			email = []
			phone = []
			while True:
				tmp_email = str(raw_input('Enter email, <enter> for none : '))
				# I am surprised when I found during debugging face that tmp_email now contains '' not \n
				if tmp_email == '':
					tmp_email = ' '
					addToList(email, tmp_email)
					break #if the user choose to press <enter> ie., for none, why we ask to enter another one?
				addToList(email, tmp_email)
				if isRepeated('another email') == 'n' : break
			while True:
				tmp_phone = str(raw_input('Enter phone, <enter> for none : '))
				if tmp_phone == '':
					tmp_phone = ' '
					addToList(phone, tmp_phone)
					break #if the user choose to press <enter> ie., for none, why we ask to enter another one?
				addToList(phone, tmp_phone)
				if isRepeated('another phone') == 'n' : break
			cv.updateContact(name, email, phone)
		elif op == 'l': #print all contact's name
			cv.showNames()
		else: #invalied argument format
			print 'Invalied argument(s)'
			showHelp()
else: #there are 3 arguments
	if len(sys.argv[1]) > 2 :  #ie., '-' and OPTION, OPTION is always one character.
		showHelp()
	else:
		op = sys.argv[1][1] #reads second argument without trailing '-'
		op = op.lower()
		name = sys.argv[2]
		if cv.hasContact(name) == False:
			print 'No contact for name : %s ' % name
		elif op == 'c': #show specified contcat
			cv.showContact(name)
		elif op == 'm': #modify given account
			#ToDo: we can check for validity.ie., email address and phone number are in proper format.
			elst = cv.getEmail(name) #gets email list for given name
			while True:
				email_old = str(raw_input('Enter old email, <enter> for exit : '))
				if email_old == '' or elst.__contains__(email_old) :
					if email_old != '':
						email_new = str(raw_input('Enter new email : '))
						elst[elst.index(email_old)] = email_new
						if isRepeated('another email') == 'n': break
					else: break
				else:
					print 'Entered email is non-existing:'

			plst = cv.getPhone(name)
			while True:
				phone_old = str(raw_input('Enter old phone, <enter> for exit : '))
				if phone_old == '' or plst.__contains__(phone_old) :
					if phone_old != '':
						phone_new = str(raw_input('Enter new phone : '))
						plst[plst.index(phone_old)] = phone_new
						if isRepeated('another phone') == 'n': break
					else: break
				else:
					print 'Entered phone is non-existing:'

			cv.updateContact(name, elst, plst)
		elif op == 'r': #remove a contact
			if cv.hasContact(name) == True:
				print '\n following contact will be permanantly removed'
				cv.showContact(name)
				if str(raw_input('do you want to continue (y/n): ')).lower() == 'y':
					cv.rmContact(name)
			else:
				print 'There is no contact in this <%s> name' % name
		elif op == 'a': #adds info. to existing contact
			#ToDo: we can check for validity.ie., email address and phone number are in proper format.
			elst = cv.getEmail(name) #gets email list for given name
			if isRepeated('an email') == 'y':
				while True:
					email_new = str(raw_input('Enter new email : '))
					elst.append(email_new)
					if isRepeated('another email') == 'n': break

			plst = cv.getPhone(name)
			if isRepeated('a phone') == 'y':
				while True:
					phone_new = str(raw_input('Enter new phone : '))
					plst.append(phone_new)
					if isRepeated('another phone') == 'n': break

			cv.updateContact(name, elst, plst)
		else: #invalied argument format
			print 'Invalied arguments'
			showHelp()
#program ends here

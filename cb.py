#!/usr/bin/env python
#file name : cb.py
#Copyright (c) Arun.K.R
#Creative Commons Attribution-Share Alike 3.0 Unported' <http://creativecommons.org/licenses/by-sa/3.0/>
#short for 'c'ontact 'b'ook
#this module as it's doesn't do anything
#because I succeded in splitting source file into modules [ഞാനാരാ മോന്‍  ;-) ] 
#I doubt wether the first line is needed. I think don't since this is not a
#stand alone module. എതായാലും ഒരു വഴിക്ക്  പോണതല്ലെ, കിടന്നോട്ടെ :-)

import os.path
import cPickle as pkl

# class to represent a contact
class ContactBook:
	'''Each object of this class represent a contact book'''

	# A dictionary is used to keep contacts, and name is used as key
	# although this is not a good practice (because it can't be Primary Key)
	# we use it for simplicity. And is class variable.
	contacts = {}

	def __init__(self):
		''' loading of contacts already persisted occures here'''
		self.dbName = 'contacts.cm' #our persistance store
		#ToDo what if user installs this program and runs this program from different directories
		#contact will be created in those directories this effects program
		#so depending upon platform create a file in users home directory
		#in linux os.environ.get('HOME') will give just that. find windows's case also mac
		ContactBook.contacts.clear() #we starts program with an empty contact book
		if os.path.exists(self.dbName): #file already exists, ie., not first run
			try:
				self.f = file(self.dbName, 'rb') #open file for reading in binary mode
				ContactBook.contacts = pkl.load(self.f) #reads persisted contact book
			finally:
				self.f.close() #closes opened file handle
		else:	#this is first run of program
			print 'welcome to cm (contact manager) program'
			print ' '*5, 'written by Arun.K.R (using python)'
			print ' '*5, "with the aid of 'Byte of Python' by Swaroop.C.H'"
			print 'Thank You for using it'
		#initialization compleates here

	def __del__(self):
		''' before closing all existing contacts will be persisted'''
		try:
			self.f = file(self.dbName, 'wb') #open file to write in binary mode
			pkl.dump(ContactBook.contacts, self.f) #our contact book persisted.
		finally:
			self.f.close() #closes file handle.

	def updateContact(self, name, email, phone):
		'''To add a new contact or update an existing contact'''
		ContactBook.contacts[name] = [email, phone]
		#or ContactBook.contacts.update({name:[email, phone]})
		# I don't know any difference b/n the two

	def rmContact(self, name):
		'''removes entry corresponding to given name'''
		del ContactBook.contacts[name]
		#or ContactBook.contacts.pop(name) is also fine

	def showNames(self):
		'''used to list all contact's name'''
		for n in ContactBook.contacts.keys():
			print '%s \n ' % n

	def showContact(self, name):
		'''used to show a specific contact'''
		#note the 'self.hasContact()' if we call it as simply 'hasContact()' it'll fail.
		#ie., even a member function need to be called in this way.
		#A difference b/n C++, Java etc with Python
		if self.hasContact(name) == True:
			print 'name  : %s' % name
			tmp = ContactBook.contacts[name] #give phone and email of given name as a list
			print 'email : %s' % tmp[0] #fist item is email
			print 'phone : %s' % tmp[1] #second is phone

	def hasContact(self, name):
		'''look wether there is a contact for specified name'''
		#return True of there is given name, False otherwise
		return ContactBook.contacts.has_key(name)

	def getEmail(self, name):
		if self.hasContact(name) == True:
			#ContactBook.contacts[name] returns a list, of wich first item is email.
			return ContactBook.contacts[name][0]

	def getPhone(self, name):
		if self.hasContact(name) == True:
			#ContactBook.contacts[name] returns a list, of wich 2nd item is phone.
			return ContactBook.contacts[name][1]

#class definition ends here

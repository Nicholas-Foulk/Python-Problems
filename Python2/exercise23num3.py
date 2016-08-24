import urllib2 #this is a new library, lets see whats in this

try:  #try cases exist in python now, this is cool.
	urllib2.urlopen("http://google.com", timeout=2) #okay so this trys to open the url and handles all the details that come with that.
	print "working connection"
except urllib2.URLError:        #this is the exception if there an error is thrown back from the try case.
	print "No internet connection"

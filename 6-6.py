print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input('What\'s your name?')
name = original
if len(name) > 0 and name.isalpha():
    print name
else:
    print "empty"

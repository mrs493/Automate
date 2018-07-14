#regular expressions and re

import re

#\d corresponds to digit characters
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#pass the string search for to the compile function to create a regex object
#r is require as we want to pass the raw string to the object
#alternatively r can be ommited if all special characters are escaped, i.e. \\d
#in order to search for regular expression symbols (shown below) they must be escape
mo = phoneNumRegex.search('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')
#use the regex objects search method to search for its first instance in the passed string
print('Phone number found: ' + mo.group())
#the group method returns the matching text
print()

#placing parts of the string in brackets creates groups
#individual groups can be called by passing their number (starting from 1) to the group method
#0 calls the entire string, the same as when no number is passed
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group(2))
print('Area code: ' + mo.group(1))
print('Full number: ' + mo.group(0))
#the groups method returns a tuple of all groups
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)
print()

#the pipe character searches for either of the expressions
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())
print()

#placing the pipe in a group allows for several variations of that group to be searched for
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
print()

#placing a ? after a group means finding that group is optional
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
print()

#placing a * after a group means 0 or more of that group can be found
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
print()

#similarly a + searches for one or more of a group
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1)
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
print()

#curly braces following a group containing a number require that group be repeated that many times
#a range of repetitions can also be searched for using two numbers and a comma
#the search will then find any matches with the group repeated in the inclusive range of the two numbers
#either number can be left blank, in which case the corresponding limit is unbound
haRegex = re.compile(r'(Ha){2,}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2)
#in the case of mo1, HaHaHa is matched, even though HaHa is also a valid match
#search is greedy by default, and will always match the longest string possible
#the non-greedy version is followed by a question mark and matches the shortest string possible
#this can also be used to make the * and + regex symbols non-greedy
haRegex = re.compile(r'(Ha){2,}?')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
print()

#using the findall method instead of search will return every match in the string
#if the regex contains no groups, it will return a list of matching strings
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
#if the regex does have groups, instead the items in the list are tuples of the strings for the groups in each match
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
print()

'''
in addition to \d there are other shorthand codes for character classes, these are:
\d   the numbers from 0 to 9
\D   not numbers from 0 to 9
\w   any letter, number or an underscore ('word' characters)
\W   not letter, number or an underscore
\s   any space, tab or newline ('space' characers)
\S   not space, tab or newline ('space' characers)
'''

#it is also possible to define your own character class by placing the desirec characters in square brackets
#note that in square brackets, the regular expression symbols do not need to be escaped
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
#a hyphen can also be used to match a range of letters or numbers
#i.e. [a-eA-E3-6] will match upper and lower case letters from a to e, and numbers from 3 to 6
#is is possible to hyphen connect characters of different types (i.e. numbers and upper case letters)
#by using the fact that they are stored in the order number, upper case, lower case
#for example [4-d] are the numbers 4 to 9, all upper case letters and lower case a to d

#placing a caret (^) after a character class' opening bracket makes it a negative character class, which matches all characters not in it
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))
print()

#using a caret at the start of a regex requires the match to occur at the start of the string
#similarly, ending a regex with a dollar sign requires the match occur at the end
#using both together means that a match must be with the entire string and not a subset
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world!'))
print(beginsWithHello.search('He said hello.'))
print()

endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your number is forty two.'))
print()

wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890'))
print(wholeStringIsNum.search('12  34567890'))
print()

#the dot (.) character is the wildcard character, and will match any character except a newline
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
print()
#by using (.*) it is possible to all text
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))
#note that this is a greedy match by default, adding a ? to the end switches to the non-greedy version
#the difference between the two matches is demonstrated below
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<<To serve man> for dinner.>')
print(mo.group())
#note that the first match is always used with the search method
#so although <To serve man> is a shorter match, <<To serve man> comes first and so this is the match found
#the dot character can be made to include newlines by passing re.DOTALL as a second argument to re.compile()
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
print()

#similarly, by passing re.IGNORECASE, or re.I as a second argument to re.compile() will ignore case when matching
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())
print()

#the sub method can be used instead of the search method inorder to replace any matches found
#it is given two arguments, the first is the string to replace matches with and the second the string to be edited
#the method then returns the string with the substitutions made
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))
#you can also use text from any groups in the match for the substitution by using the escaped number of the group
#i.e. \1 for the first group, \2 the second and so on
namesRegex = re.compile(r'Agent (\w)\w+')
print(namesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
print()

#for more complex regex, the gegex expressions may get difficult to read
#in such cases, passing the second argument re.VERBOSE to re.compile() tells it to ignore whitespace and comments
#i.e. the complicated regex for a phone number below is made easier to read
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    \d{3} # first 3 digits
    (\s|-|\.) # separator
    \d{4} # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? # extension
    )''', re.VERBOSE)

#re.compile() is only able to take arguments
#In order to use multiple values the variables can be combined using a pipe character (a bitwise operator in this context)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
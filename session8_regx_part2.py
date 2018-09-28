# pattern validation 
# pattern extraction 

import re 

# s = "abcdabcdacacadede"
# r = re.compile("ab")
# l = re.findall(r,s)
# print(l)

# metachars :
# . = > mathch with anything 
# [a-z] [A-Z][a-zA-Z]=> char class
# digit [0-9] => digit class
# + => atleast one occurance if more allowed
# * => zero more occurance 
# ^ =>start of the string 
# $ => end of the string
# [a-z]{4} => 4 chars
# [0-9]{2,4} => 2 to 4 
# s = "abcde124"
# r = re.compile("^[a-z]{2,4}[0-9]+$")
# l = re.findall(r,s)
# print(l)

# s = "AAAAAABCDE1234A"
# r = re.compile(r"^[A-Z]{5}[0-9]{4}[A-Z]$")
# l = re.findall(r,s)
# print(l)

s = "12-02-2018"
# 32-13-2018
# dd-mm-yyyy
# r = re.compile(r"^([0-9]{2})-([0-9]{2})-([0-9]{4})$")
# # l = re.findall(r,s)
# # print(l)
# m = re.search(r,s)
# if m:
# 	print(m.group(2))
# else:
# 	print("pattern not found")
# Search returns a object of call match if pattern found 
# else None 

# s = "(+91)7123456789"
# s1 = "7123456789"

# l = re.findall("[A-Za-z]+[0-9]?","Python")
# print(l)

# r = re.compile(r"^(\(\+91\))?[6-9][0-9]{9}$")
# m = re.search(r,s1)
# if m:
# 	print(m.group())
# else:
# 	print("Pattern not found")


# url = "www.zekelabs.com"

# <a href="www.zekelabs.com">click here</a>

# s = "the code link is https://www.github.com, http://www.zekelabs.com"

# r = re.compile(r"https?://www\.[a-z0-9]+\.com")
# l = re.findall(r,s)
# print(l)

# for value in l:
# 	s = s.replace(value,"<a href={}>{}</a>".format(value,value))
# print(s)

# "the code link is <a href ="http://www.github.com">http://www.github.com</a>,
# <a href = "http://zekelabs.com">http://zekelabs.com</a>


s = "12-02-2018"
# 32-13-2018
# dd-mm-yyyy
# r = re.compile(r"^(?P<day>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})$")
# # # l = re.findall(r,s)
# # # print(l)
# m = re.search(r,s)
# if m:
# 	print(m.group("year"))
# else:
# 	print("pattern not found")
# Search returns a object of call match if pattern found 
# else None 


s = "(+91)7123456789"
# s1 = "7123456789"

# l = re.findall("[A-Za-z]+[0-9]?","Python")
# print(l)

# ?: : non caputuring group
# ?P<name> : named group

r = re.compile(r"^(?:\(\+91\))?([6-9]\d{9})$")
m = re.search(r,s)
if m:
	print(m.group(1))
else:
	print("Pattern not found")

# s = """ python3
# java8"""
# r = re.compile(r"[a-z]+[0-9]",flags = 2)
# l = re.findall(r,s)
# print(l)
# help(re)

# m = re.search(r,s)
# if m : 
# 	print(m.group())
# else:
# 	print("pattern not found")

# s = "Python1234$$$$"
# print(re.findall("[^A-Za-z]+",s))

# [a-zA-Z0-9] = > \w
# [^a-zA-Z0-9] => \W

# [0-9] => \d
# [^0-9] = > \D

# \s => space 
# \S => compliment of space 

# email address validation abc123@gmail.com
# date validation 
# ip valid 0.0.0.0 
# 		255.255.255.255

# ABC 4|4|2|3



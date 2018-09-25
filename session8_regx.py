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
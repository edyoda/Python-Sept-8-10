# Modes of opening the file :
# 1 r read 
# 2 r + 
# 3 w write 
# 4 w + 
# 5 a append 
# 6 a+

#read:
# fp = open(r"test2.txt","r")
# content = fp.read()
# print(content)

# content = fp.read()
# print(content)

# fp.close()

# fp = open(r"test2.txt","r")
# content = fp.read(20)
# print(content)

# content = fp.read()
# print(content)
# fp.close()


# fp = open(r"test2.txt","r")
# content = fp.readline()
# print(content)

# content = fp.readlines()
# print(content)

# fp.close()

# read() => str 
# read(20) => str 
# readline => str 
# readlines => list,each elemnt is one one line  


# fp = open("test3.txt","w+")
# print(fp.tell())
# fp.write("Add another line")
# print(fp.tell())
# fp.seek(0,0)
# print(fp.tell())
# content = fp.read()
# print(content)

# fp.close()

# read + write
# fp = open("test3.txt","r+")
# content = fp.read()
# print(content)
# print(fp.tell())
# fp.seek(0,2)
# print(fp.tell())
# fp.write("*****Add line 4")
# fp.close()

# fp = open("test3.txt","a+")
# print(fp.tell())
# fp.write("\nAdd this using append mode")
# fp.seek(0,0)
# content = fp.read()
# print(content)

# fp.close()
# fp = open("test2.txt",'r')
# for x in fp:
# 	print(x)

# fp.close()



# seek(offset,position)

# 0 => start of the file 
# 1 => current position 
# 2 => end of the file 

# seek(15,0)
# seek(15,0)


fp = open("test4.txt","r")
fp2 = open("test5.txt","w")
# content = fp.read()
# print(content)

for line in fp:
	elements = line.split(" ")
	# print(elements)
	reviews_str = elements[1].split("|")
	# print(reviews_str)
	sum = 0
	for value in reviews_str:
		sum = sum + int(value)

	fp2.write("{} {}\n".format(elements[0],sum/len(reviews_str)))
	# print(elements[0],sum/len(reviews_str))
fp.close()

# r : fp =>start,file not exist = > error , read 
# r+ : fp => start, file not exist => error , read + write 

# w : fp> start ,craete new file , write  
# w+ : fp : start , craete new file , write and read 

# a : fp -> last ,create a new file , write 
# a+ fp => last , create a new file , write + read 

# tell
# seek

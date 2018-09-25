# parameter passing techniques :
# 	1 Positional args 
# 	2 variable length positional *args => tuple 
# 	3 default val1 = 100
# 	4 keyword username= ,passsowrd 
# 	5 varaible length keyword keyword  **kwargs = > dict  
# 	6 unpacking *l ,** kwargs 

# def printVal():
# 	global num1
# 	print("Inside function",num1)
# 	num1 = 200
# 	print("After changing the value",num1)


# num1 = 100
# print("before function call",num1)
# printVal()
# print("after function call",num1)

# fact(5) = 5 * 4! 
# 			  4 * 3!
# 			  		3 * 2 !
# 			  			2 * 1!
# 			  				1

# def fact(num1):
# 	if num1 == 1:
# 		return 1
# 	else:
# 		return num1 * fact(num1 - 1)

# result = fact(5)
# print(result)


# fact(5) = return 5 * fact(4) = 5 * 24 = 120 
# 			return 4 * fact(3) = 4 * 6 = 24 
# 				return 3 * fact(2) = 3 * 2 = 6 
# 					return 2 * fact(1) => 2 * 1 = 2
# 						return 1



def binary_search(l,key):
	if not l:
		return False
	else:

		mid = len(l) // 2
		if key == l[mid]:
			return True
		elif key < l[mid]:
			return binary_search(l[:mid],key)
		else:
			return binary_search(l[mid+1:],key)

l = [10,20,30,40,50,60,70,80]
key = 600
result = binary_search(l,key)
print(result)

# binary_serach(l,key)
# 	binary_serach([60,70,80],key)
# 		binary_serach([80],key) = >True 
# 			True		
# 1 list should be sorted 
# 2 mid = len(l) / 2 
# 		if key == mid 70 == 50
# 					return True 
# 		else key < mid 

# 		key > mid 
# 			l = [60,70,80] key 70 
# 			mid = 70 70 == 80 
# 					return True

# 			if key < mid

# 			key > mid  
# 				80 key = 80	
# 				80 == 80 return True 
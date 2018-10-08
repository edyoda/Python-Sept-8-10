# class : data member methods 
# objectes

# paytm 
# 	no 
# 	email 
# 	aadhar no 
# 	password 

# 	recharge 
# 	pay bills 
# 	transfer money 

# object 

# Emp : 
# 	id 
# 	name 
# 	contact 
# 	email 
# 	sal 

# 	get_details 
# 	incr_sal 
# 	update_details 

# instance variable : each object will have its own set of variable 

class Emp:
	def __init__(self,id,name,email,sal):
		self.emp_id =  id
		self.emp_name = name
		self.email_emp = email 
		self.salary = sal 

	def get_details(self):
		return self.emp_id,self.emp_name,self.email_emp,self.salary		

	def set_dept(self,dept):
		
		self.dept = dept		

	def incr_sal(self,per=30):
		self.salary = self.salary + (self.salary*per)/100
		return self.salary

class Dept:
	def __init__(self,id,title):
		self.id = id
		self.title  = title

# hr = Dept(1,"HR")
# admin = Dept(2,"Admin")

# emp1 = Emp(101,"ABC","abc@gmail.com",75000)
# # Emp(emp1,101,"ABC","abc@gmail.com",75000)
# emp2 = Emp(102,"PQR","pqr@gmail.com",65000)
# emp3 = Emp(103,"XYZ","xyz@gmail.com",70000)
# emp4 = Emp(104,"RST","rst@gmail.com",50000)

# emps = [emp1,emp2,emp3,emp4]

# print(emp1.emp_id,emp1.emp_name,emp1.email_emp,emp1.salary)
# print(emp2.emp_id,emp2.emp_name,emp2.email_emp,emp2.salary)


# print(emp1.get_details())
# # Emp.get_details(emp1)


# print(emp2.get_details())

# emp1.set_dept(hr)
# emp2.set_dept(admin)
# emp3.set_dept(hr)
# emp4.set_dept(hr)

# print(emp1.dept.title)
# print(emp1.incr_sal(40))

# print(emp2.incr_sal())


# for emp in emps:
# 	print(emp.get_details())

# Author:
# 	id 
# 	author name 
# 	about author 
# Book 
# 	id 
# 	title 
# 	author
# 	price 

# ABC
# PQR
# XYZ
# RST 


# a
# b 
# c


# all the books written by a

class Author:
	def __init__(self,id,name,description):
		self.id = id
		self.name = name 
		self.description = description


class Book:
	def __init__(self,id,title,author,price):
		self.id = id 
		self.title = title
		# self.author = author 
		self.price = price 

	def get_details(self):
		return self.title,self.price

	def set_author(self,author):
		self.author = author

a = Author(1,"a","about me for a") 
b = Author(2,"b","about me for b")
c = Author(3,"c","about me for c")

# book1 = Book(101,"ABC",a,500) 
# book2 = Book(102,"PQR",b,600)
# book3=  Book(103,"RST",a,700)
# book4 = Book(104,"XYZ",c,800)

# book1 = Book(101,"ABC",500) 
# book2 = Book(102,"PQR",600)
# book3=  Book(103,"RST",700)
# book4 = Book(104,"XYZ",800)
# book1.set_author(a.name)


# books = [book1,book2,book3,book4]

# for book in books:
#  	if book.author.name  == 'a':
#  		print(book.get_details())



Student :

	roll_no 
	std  
	marks = [70,80,95,99,65]
 	attendence 

	percentage 

	result   40 < fail else attendence 75 < fail else pass 

	all the failed students 
	all the passed student 

	1 st rank and 2 nd rank 


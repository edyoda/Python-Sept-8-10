class Course:
    course_count = 0
    
    def __init__(self,id,name,desc,author,catagory):
        self.__id = id
        self.__name = name
        self.__desc = desc
        self.__author = author
        self.__catagory = catagory
        Course.course_count+=1
    
    
    def get_catagory(self):
        return self.__catagory
    
    def get_name(self):
        return self.__name
    
class Tutorial:
    
    tutorial_count = 0
    tutorials = []

    @classmethod
    def incr_count(cls):
        cls.tutorial_count+=1

    @classmethod
    def get_count(cls):
        return cls.tutorial_count
    
    @classmethod
    def add_tutorial(cls,obj):
        cls.tutorials.append(obj)

    @staticmethod
    def printVal(num1,num2):
        print(num1,num2)


    def __init__(self,id,name,content,course):
        self.__id = id
        self.__name = name
        self.__content = content
        self.__course = course
        
        Tutorial.incr_count()
        Tutorial.add_tutorial(self)
        # Tutorial.tutorials.append(self)
        
    def get_tutorial_name(self):
        return self.__name 
    
    def get_course(self):
        return self.__course 
    
    def set_tutorial_name(self,new_name):
        self.__name = new_name
    
    def get_details(self):
        return self.__id,self.__name
        
course1 = Course(1,"Python Basics","Learn Python Basics","ABC","Python")        
course2 = Course(2,"Python Advanced","Learn Python Advanced","ABC","Python")        
course3 = Course(3,"Data Science","Learn DS","ABC","Data Science")        
course4 = Course(4,"ML Basics","Learn ML Basics","ABC","Machine Learning")        

# print(course1.name)

tutorial1 = Tutorial(101,"Python Loops","For loop and While loop",course1)
tutorial2 = Tutorial(102,"Python List","List CRUD",course1)
tutorial3 = Tutorial(103,"NumPy","Numpy",course2)
tutorial4 = Tutorial(104,"Pandas","Pandas",course3)
tutorial5 = Tutorial(105,"Scikit","Scikit",course4)

# tutorials = [tutorial1,tutorial2,tutorial3,tutorial4,tutorial5]

# print(tutorial1.get_tutorial_name())
# tutorial1.set_tutorial_name("Loops Python")
# print(tutorial1.get_tutorial_name())

# for tutorial in tutorials:
#     if tutorial.get_course().get_catagory() == "Python":
#         print(tutorial.get_details())

# courses = {}
# for tutorial in tutorials:
#         if courses.get(tutorial.get_course().get_name()):
#             courses[tutorial.get_course().get_name()] +=1
#         else:
#             courses.setdefault(tutorial.get_course().get_name(),1)
        
# print(courses)        

# print(Tutorial.get_count())
# # print(Tutorial.tutorial_count)
# print(Tutorial.tutorials)

# Tutorial.printVal(10,20)
# tutorial1.printVal(100,200)


# s = "Python"
# print(type(s))
# s.index("P")

# class str:

#     def index(self,char)
#         return index


# fromkeys 

# d.get("Key")
# l = [10,20,30,40,50]
# d = dict.fromkeys(l)
# print(d)

# Django User class 

# User : username 
#        password 
#        first_name 
#        last_name 
#        email

# Profile:
#         username 
#         first_name
#         last_name
#         email 
#         contact number 
#         linkedin profile 
#         website 


class User:
    def __init__(self,username,password,fn,ln,email):
        self._username = username
        self.password = password
        self.first_name = fn 
        self.last_name = ln 
        self._email = email 

    def get_detail(self):
        return self._username,self.first_name,self.last_name,self._email

class Demo:
    def get_detail(self):
        return "Hi from demo class"


class Profile(Demo,User):
    def __init__(self,username,fn,ln,email,password,contact,linkedin,website):
       super().__init__(username,fn,ln,email,password)
       self.contact = contact
       self.linkedin = linkedin
       self.website = website

    def get_detail(self):
        t = User.get_detail(self)       
        return t,self.contact,self.linkedin,self.website 

user1 = User("abc123","abc@123","ab","c","abc@gmail.com")

profile1 = Profile("abc123","abc@123","ab","c","abc@gmail.com","876543123","www.linkedin/abc","www.abc.com")
print(profile1.__dict__)

# help(profile1)
# print(profile1.get_detail())

# Depth first left  to right algo 

# Demo  User 
# profile 

# print(user1._username)

# PEP 8 

# method overloding => two methods same name but diffrenet paraneters 
# 1 total no of parameter will be different 
# 2 different type of parameter 
# add(num1,num2,num3)
# add(num1,num2)

# add(int num1,int num2)
# add(int num1,float num2)

# add(*args)



# method overriding two methods same name same parameter but different implementattions

# encapsulation and abstarction : classes and objects  
# polymorphism : method overriding
# data hiding : public,private __ ,protected _ => by convetion

 






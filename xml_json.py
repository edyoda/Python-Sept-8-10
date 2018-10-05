# json :

# {key:value} => json object 			dict 
# " "									'' " " """ """
# [15,20,25,"Python"] =>array			list 
# number 10 15.255					int float 
# 									tuple 
# 									set

# # 									
# import json
# fp = open("test.json","r")
# content = fp.read()
# fp.close()
# # print(content)

# d = json.loads(content)
# # print(d,type(d))

# # print(d['glossary']['title'])
# d['glossary']['title'] = "new title for json"

# # print(d['glossary']['GlossDiv']['GlossList']['GlossEntry']['ID'])
# d['glossary']['GlossDiv']['GlossList']['GlossEntry']['ID'] = ('HTML','SGML')
# # print(d)

# j = json.dumps(d,indent = 4 )
# print(j)

# fp = open("test2.json","w")
# fp.write(j)
# fp.close()

# <html>

# </html>

# <note>
# 	<to email="abc@gmail.com">ABC</to>
# 	<from>PQR</from>
# 	<body> Hi </body>

# </note>

# xmltodict 
# etree 
# pip install xmltodict 
# import xmltodict 

# fp = open("test.xml","r")
# content = fp.read()
# fp.close()
# # print(content)
# d = xmltodict.parse(content)
# print(d['glossary']['title'])
# d['glossary']['title'] = "New title for xml"
# # print(d)

# # print(d['glossary']['GlossDiv']['GlossList']['GlossEntry']['@ID'])
# d['glossary']['GlossDiv']['GlossList']['GlossEntry']['@ID'] = "HTML"

# # print(d)

# x = xmltodict.unparse(d)
# print(x)

# fp = open("test2.xml","w")
# fp.write(x)
# fp.close()

# json :
# 	loads => json string to dict 
# 	dumps => dict => json 

# xmlto dict 
# 	parse => xml to dict 
# 	unparse => dict to xml 


import csv 
# reader 
# dict reader 
# writer 
# dict writer 

# fp = open("filename","r") 


with open("test6.csv","a+") as fp:
	# csv_fp = csv.reader(fp)
	# # print(csv_fp)
	# print(next(csv_fp))
	# for row in csv_fp:
	# 	print(row)

	# csv_fp = csv.DictReader(fp)
	# # print(csv_fp)
	# # print(next(csv_fp))
	# for row in csv_fp:
	# 	print(row)

	# csv_fp = csv.writer(fp,lineterminator="\n")
	# # csv_fp.writerow(["QWE","qwe@gmail.com","651324552"])
	# # csv_fp.writerow(["POI","POI@gmail.com","651124552"])
	# csv_fp.writerow(["RST","POI@gmail.com","651124552"])
	# csv_fp.writerows([["RST","POI@gmail.com","651124552"],
	# 	["UYT","POI@gmail.com","651124552"],
	# 	["TYU","POI@gmail.com","651124552"],
	# 	["POI","POI@gmail.com","651124552"]])

	# fields = ['Name','Email','Contact']
	# csv_fp = csv.DictWriter(fp,lineterminator="\n",fieldnames=fields)

	# csv_fp.writerow({"Name":"WEY","Contact":"54433333"})
	# csv_fp.writerows([["RST","POI@gmail.com","651124552"],
	# 	["UYT","POI@gmail.com","651124552"],
	# 	["TYU","POI@gmail.com","651124552"],
	# 	["POI","POI@gmail.com","651124552"]])


fp.close()

help(csv)

# writerow => list  
# writerows => [[][]]


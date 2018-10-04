# 1 Beautiful Soup => library 
# 2 Scrapy => framework 

# pip install BeautifulSoup4
# pip install requests

# http://wwww.zekelabs.com

# get :  get data from server => response html  
# post : send data to server => html 
# SEO Search engine optimization 

# pagerank 
# keywords
# keyword density
# inbound links 
# outbound links
# html5
# mobile optimized 
# social presence  

# <html>
# 	<head>
# 		<title>Sample title</title>
# 	</head>
# 	<body>
# 		<sections>
# 			<div id =' ' class="">
# 				<img src="path">
# 				<p>COntent</p>
# 				<a href ="google.com">click Here</a>
# 			</div
# 		</section>
# 	</body>

# </html>
import requests 
from bs4 import BeautifulSoup

response = requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Bangalore")
print(response.status_code)
# print(response.content)


soup = BeautifulSoup(response.content,"html.parser")
# print(soup)


# DOM tree 
# 					soup 
# 					html
# 			head 		body 
# 					section 	div P

# find 
# find_all


# prices = soup.find_all("div",attrs={"class":"m-srp-card__price"})
# print(prices[0].text)

# for price in prices:
# 	print(price.text)
print("----------Page 1 ----------------")
cards = soup.find_all("div",attrs={"class":"m-srp-card__container"})

for card in cards[:5]:
	price = card.find("div",attrs={"class":"m-srp-card__price"})
	# print(price.text)
	carpet_area = card.find("div",attrs={"class":"m-srp-card__summary__info"})
	# print(carpet_area.text)

	title = card.find("a",attrs={"class":"m-srp-card__title"})
	link = title.get("href")

	response2 = requests.get(link)
	# print(response2.status_code)
	# print(link)
	soup2 = BeautifulSoup(response2.content,"html.parser")
	super_area = soup2.find('span',attrs={'id':"coveredAreaDisplay"})
	if super_area:
		super_area_text = super_area.text
	else:
		super_area_text = None
	# print(super_area.text)
	title_text = title.text.replace("\n"," ")
	# print(title_text.strip(" "))

	output_text = "{} {} {} {}".format(title_text.strip(" "),carpet_area.text,price.text,super_area_text)
	print(output_text)


print("--------Page 2 ------------------")


payload = {
"propertyType_new":"10002_10003_10021_10022",
"city": 3327,
"mbTrackSrc": "homeSearchForm",
"searchType": 1,
"propertyType": "10002,10003,10021,10022",
"category": "S",
"page": 2,
"ltrIds": "37135469,37137229,36316913,31628459,35775147,35647279,37161547,36410767,34924657,34002751,33836989,37014165,34660657,36949791,20236698,37169509,35476813,35508537,33645591,35500143,36184143,36975103,21929323,36878073,30103997,36527847,17475128,34072951,37086683,37138757",
}



response = requests.post("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Bangalore",data = payload)
print(response.status_code)


soup = BeautifulSoup(response.content,"html.parser")
cards = soup.find_all("div",attrs={"class":"m-srp-card__container"})

for card in cards[:5]:
	price = card.find("div",attrs={"class":"m-srp-card__price"})
	# print(price.text)
	carpet_area = card.find("div",attrs={"class":"m-srp-card__summary__info"})
	# print(carpet_area.text)

	title = card.find("a",attrs={"class":"m-srp-card__title"})
	link = title.get("href")

	response2 = requests.get(link)
	# print(response2.status_code)
	# print(link)
	soup2 = BeautifulSoup(response2.content,"html.parser")
	super_area = soup2.find('span',attrs={'id':"coveredAreaDisplay"})
	if super_area:
		super_area_text = super_area.text
	else:
		super_area_text = None
	# print(super_area.text)
	title_text = title.text.replace("\n"," ")
	# print(title_text.strip(" "))

	output_text = "{} {} {} {}".format(title_text.strip(" "),carpet_area.text,price.text,super_area_text)
	print(output_text)



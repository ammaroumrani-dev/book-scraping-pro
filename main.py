import requests as req
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import csv
import string
import time
import pandas as pd

p=string.punctuation
b="..."+p
data=[]

base_url="http://books.toscrape.com/"

final_urls=[]

final_cat_names=[]

final_ratings=[]

price_symbols="$"

res=req.get(base_url)

soup=bs(res.text,"lxml")

cat_list=soup.find("ul", class_="nav").find("ul")

all_cat=cat_list.find_all("a")

for category in all_cat:
    link=urljoin(base_url, category['href'])
    

    name=category.text.strip()

    final_urls.append(link)
    final_cat_names.append(name)


#save information into csv file

with open("books.csv","w",newline='',encoding="utf-8-sig") as f:
    writer=csv.writer(f)

    #write header row
    writer.writerow(["title","price_gbp","price","rating","availability"])

    #loop through each category
    for link,cat_name in zip(final_urls,final_cat_names):
        print(f"Extrzcting data from {cat_name}")

        #res category page
        res_book=req.get(link)
        res_book.encoding="utf-8"
        #delay to avoid stressing the server
        #time.sleep(1)

        soup_book=bs(res_book.text,"lxml")

        #find all books in category
        books_list=soup_book.find_all("article",class_="product_pod")

        #limit to three book only
        count=0

        for book in books_list:
            
            #get book title
            title=book.find("h3").text.strip()

            #get rating
            rating_tag=soup_book.find("p",class_="star-rating")
            if rating_tag:

                rating=rating_tag.get("class")[1]
                final_ratings.append(rating)
                
            else:
                print("not found")

            #get avilability
            av=book.find("p",class_="instock").text.strip()
            im=book.find("img",class_="thumbnail")
            #clean title from punctuation
            clean_title=[clean for clean in title if clean not in b]

            final_title="".join(clean_title)
            print(final_title)
            

            c="."
            c_p=[clear for clear in p if clear not in c]
            p="".join(c_p)

            p=p+"Â£"

            #get book price
            price=book.find("p", class_="price_color").text.strip()
            clean_price=[pr for pr in price if pr not in p]
            final_price="".join(clean_price)

            data.append({
                "title": final_title,
                "price gbp": price_symbols,
                "price": final_price,
                "rating": rating,
                "availability": av,
            })
            
            
            
            #write row to csv
            writer.writerow([final_title,price_symbols,final_price,rating,av])

#save to excel
df=pd.DataFrame(data)

df.to_excel("books.xlsx", index=False)


print("file created")

            
            
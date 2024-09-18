from pre_code import starting_code
from convert_price import convert_price
from convert_rating import  convert_rating
import pandas as pd
bsoup = starting_code(url='https://books.toscrape.com/' , head= {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
})

def get_articles(article):
    title = article.find('h3').find('a')['title']
    text_price = article.find("p" , attrs= {"class" : "price_color"}).text
    price = float(convert_price(text_price))
    text_rating = article.find('p', attrs= {'class' : 'star-rating'}).attrs['class'][1]
    rating = convert_rating(text_rating)

    all_articles = {
        'title' : title ,
        'price' : price ,
        'rating' : rating
    }
    return all_articles

articles = bsoup.find_all('article' , attrs= {"class" : "product_pod"})


all_data = [get_articles(ar) for ar in articles]
pd_all_data = pd.DataFrame(all_data)
print(pd_all_data)

all_data_rating = pd_all_data.groupby('rating')
print(all_data_rating['price'].sum())

all_data_rating = pd_all_data.groupby('rating')
print(all_data_rating['price'].mean())

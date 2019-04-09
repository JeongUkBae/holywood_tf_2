from selenium import webdriver
from bs4 import BeautifulSoup
ctx = '../crawler/chromedriver'
driver = webdriver.Chrome(ctx)

driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.prettify())

all_divs = soup.find_all('div',attrs={'class':'tit3'})
arr = [div.a.string for div in all_divs]
for i in arr:
    print(i)


import requests
import bs4

res = requests.get('http://olympus.realpython.org/dice')
# print(res.text)

soup = bs4.BeautifulSoup(res.text, 'lxml')
hello = soup.select('title')

print(hello[0].getText())






# import mechanicalsoup
#
# browser = mechanicalsoup.Browser()
# page = browser.get("http://olympus.realpython.org/dice")
# tag = page.soup.select("#result")[0]
# result = tag.text
#
# print(f"The result of your dice roll is: {result}")
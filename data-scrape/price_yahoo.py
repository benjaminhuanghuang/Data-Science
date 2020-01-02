import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from datetime import date


def fetchPrice(symbol):
  url = 'https://finance.yahoo.com/quote/{}'.format(symbol)
  response = requests.get(url)
  soupe = bs(response.content,"html.parser")

  price = soupe.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text

  return price


if __name__ == '__main__':
  print(fetchPrice('AAPL'))
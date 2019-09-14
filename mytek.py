import requests
from bs4 import BeautifulSoup
import smtplib
import time

x = input('Chnwa el soum ely tehb tehoto ka target?: ')
URL= input('het lien o lazem ykon men www.mytek.ctn = ')

headers={
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}


def check_price():
  page = requests.get(URL, headers=headers)

  soup1 = BeautifulSoup(page.content, "html.parser")

  soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
  title = soup2.find(itemprop= "name").get_text()
  price = soup1.find(itemprop="price").get_text()
  converted_price = (float(price[0:5].translate({ord(' '): None})))
  

  if(converted_price < float(x)):
     send_mail()
  print(title.strip())
  print(converted_price)


  
def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('hiallnigas@gmail.com', 'mdvctlwdusutqxby')

  subject = "Price is fall down"
  body = f'ahlan , \n  el produit taaek cava wsel lel {x}\n odekhel tfaqed l produit taaek mena {URL}'

  msg = f"Subject: {subject}\n\n{body}"
  server.sendmail(
      'hiallnigas@gmail.com',
      'jemaii.ghassen1@gmail.com',
      msg
  )  
  print("THE EMAIL IS SENT!")
  server.quit()


while(True):
    check_price()
    time.sleep(60)
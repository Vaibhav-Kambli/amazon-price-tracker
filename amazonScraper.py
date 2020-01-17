"""
amazonScraper.py
Author name: Vaibhav Kambli

Description: Python code to automatically notify user via email when the price of a particular item in amazon's website
or the user's wishlist drops.

"""

#imports
#-------------------------------------------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup
import smtplib
import time


#-------------------------------------------------------------------------------------------------------------
#url and browser's user agent

#url for your desired product (Echo dot 3rd gen in this case) 
URL = "https://www.amazon.ca/Echo-Dot-3rd-gen-Charcoal/dp/B07PDHT5XP/ref=br_msw_pdt-4?_encoding=UTF8&smid=A3DWYIK6Y9EEQB&pf_rd_m=A3DWYIK6Y9EEQB&pf_rd_s=&pf_rd_r=CETY6YNMWE9RPKS91SAZ&pf_rd_t=36701&pf_rd_p=8b68a462-b908-4cf4-b9b4-0c036da526cd&pf_rd_i=desktop"

user_agent = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}


#-------------------------------------------------------------------------------------------------------------
#function to get product price

def price_checker():

    page = requests.get(URL, headers=user_agent)

    soup1 = BeautifulSoup(page.content, 'html.parser')

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")      #get html text of the link

    title = soup2.find(id="productTitle").get_text().strip()    #get title of the prouct

    price = soup2.find(id="priceblock_ourprice").get_text()     #get price of the product

    numeric_price = float(price[5:10])                          #gets only numeric value from the price

    if(numeric_price < 48):                                     #set the price for the prouct you want to get notified for
        send_email()



#-------------------------------------------------------------------------------------------------------------
#function to send email 

def send_email():

    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls() 
  
    # Authentication 
    s.login("sender_email_id", "sender_email_id_password") #Specify your email id and password

    #email's subject and body messages
    subject = "Price reduced!"
    body = 'Check the link https://www.amazon.ca/Echo-Dot-3rd-gen-Charcoal/dp/B07PDHT5XP/ref=br_msw_pdt-4?_encoding=UTF8&smid=A3DWYIK6Y9EEQB&pf_rd_m=A3DWYIK6Y9EEQB&pf_rd_s=&pf_rd_r=CETY6YNMWE9RPKS91SAZ&pf_rd_t=36701&pf_rd_p=8b68a462-b908-4cf4-b9b4-0c036da526cd&pf_rd_i=desktop'
    
    #formatted message to be sent 
    message = f"Subject: {subject}\n\n{body}"
    
    # sending the mail 
    s.sendmail("sender_email_id", "receiver_email_id", message) 
    
    # terminating the session 
    s.quit() 

#-------------------------------------------------------------------------------------------------------------
#main

while(True):
    price_checker()
    time.sleep(86400)   #check every 24 hours


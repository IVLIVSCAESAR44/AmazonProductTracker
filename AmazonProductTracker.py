import bs4
import pandas as pd
from selenium import webdriver
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import time

Available=[]
PotentialDelist=[]


def tracker(url):
      # to prevent script from crashing when there isn't a price for the product
    try:
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        driver.get(url)
        time.sleep(1)
        html = driver.page_source
        soup  = bs4.BeautifulSoup(html,features ='lxml')
        buybox = soup.find('span', class_ = 'tabular-buybox-text').get_text()
        
        if buybox == 'Amazon.com':
            Available.append("{0}".format(buybox))
            driver.quit()
        else:
            PotentialDelist.append("{0} may be delisted, please verify ".format(url))
            driver.quit()  

    except Exception as e:
        PotentialDelist.append("{0} may be delisted, please verify ".format(url))
        driver.quit()
        print(e)
        
df=pd.read_csv('CSV File name')
for i in range(0,len(df["URL"])):
    tracker(df["URL"][i])

print(PotentialDelist)    


Availablestr= ''.join(Available)
PotentialDeliststr= ''.join(PotentialDelist)

recipients = ['InsertEmail', 'InsertEmail']

if len(PotentialDelist) >= 1:        
    msg = MIMEMultipart()       
    msg['Subject'] = 'Potential Delisting for ' + datetime.date.today().strftime("%B %d, %Y") + ', please verify the below URLs'
    msg['From'] = 'SenderEmail'
    msg['To'] = 'InsertEmail, InsertEmail'
    message = 'URL'
    msg.attach(MIMEText(PotentialDeliststr))   
    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('SenderEmail', 'SenderPassword')
    mailserver.sendmail('SenderEmail', recipients, msg.as_string())
    mailserver.quit()        
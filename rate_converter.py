# Extract data from the given URL. Copy the URL, after selecting the desired location.
# Scrape the data with the help of requests and the Beautiful Soup module.
# Convert that data into HTML code.
# Find the required details and filter them.

import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text


def get_info():
    try:
        htmldata = getdata("https://finance.yahoo.com/quote/usdinr=X?ltr=1")
        soup = BeautifulSoup(htmldata, 'html.parser')
        mydatastr = ''
        for table in soup.find_all("div", class_="D(ib) Va(m) Maw(65%) Ov(h)"):
            mydatastr += table.get_text()
        list_data = mydatastr.split()
        temp = list_data[0].split("-")
        rate.set(temp[0])
        inc.set(temp[1])
        per_rate.set(list_data[1])
        time.set(list_data[3])
        result.set("sucess")
    except:
        result.set("Oops! something wrong")

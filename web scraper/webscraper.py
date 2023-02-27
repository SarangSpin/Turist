import requests
from bs4 import BeautifulSoup
import csv
from googlesearch import search
import pymongo
import time




client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = client.destinations


searchtype = input("List(2) or single entry(1): ")

def operation(searchtype):      
    if (searchtype=='1'):
        x = input("Enter the search: ")
        for i in search(x + ' wikipedia', num_results=1):
            url = i
        print(url)
        result = requests.get(url, headers = {'User-agent': 'Hello'}).content
        content = BeautifulSoup(result, 'html.parser')
        description = []
        name = content.find('span', class_="mw-page-title-main").text
        description_raw = content.find_all('p', class_="")
        for u in range(5):
            for z in description_raw[u].find_all('sup'):
                z.decompose()
            description.append(description_raw[u].text +'\n')
        description = "\n".join(description)
        description.replace('/n', '')
        print(name)
        if(content.select_one('.geo-dec')):
            location = content.select_one('.geo-dec').text
            print(location)
        category = []
        time.sleep(1)
        for l in search(x + ' www.britannica.com', num_results=1):
                urlx = l
        rx = requests.get(urlx, headers = {'User-agent': 'Hello'}).content
        content = BeautifulSoup(rx, 'html.parser')
        category = content.find('div', class_='topic-identifier font-16 font-md-20').text.split(',')
        answer = {
            'name': name,
            'description': description,
            'location': location,
            'category': category
        }
        db.places.insert_many([answer])
        
    elif (searchtype=='2'):
        y = input("Enter the search: ").split(',')
        for x in y:
            for i in search(x + ' wikipedia', num_results=1):
                url = i
            print(url)
            result = requests.get(url, headers = {'User-agent': 'Hello'}).content
            content = BeautifulSoup(result, 'html.parser')


            answer = {}
            location = ""
            description = []
            name = content.find('span', class_="mw-page-title-main").text
            description_raw = content.find_all('p', class_="")
            for u in range(5):
                for z in description_raw[u].find_all('sup'):
                    z.decompose()
                description.append(description_raw[u].text + '/n')
            description = "\n".join(description)
            description.replace('/n', '')
            print(name)
            if(content.select_one('.geo-dec')):
                location = content.select_one('.geo-dec').text
                print(location)
            category = []
            time.sleep(1)
            for l in search(x + ' www.britannica.com', num_results=1):
                urlx = l
            rx = requests.get(urlx, headers = {'User-agent': 'Hello'}).content
            content = BeautifulSoup(rx, 'html.parser')
            category = content.find('div', class_='topic-identifier font-16 font-md-20').text.split(',')
            print(category)
            answer = {
            'name': name,
            'description': description,
            'location': location,
            'category': category
            }
            db.places.insert_many([answer])
    else:
        raise Exception(TypeError)

try:
    operation(searchtype)
except Exception as exc: 
    print(exc)
import requests
from bs4 import BeautifulSoup
import csv
import googlesearch

for i in googlesearch.search("qutub", num_results=10):
    print(i)
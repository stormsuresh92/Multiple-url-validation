
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


urls = open('inputurls.txt', 'r')
url = urls.readlines()
for url in tqdm(url):
	try:
		response = requests.get(url.strip())
		status = response.status_code
		soup = BeautifulSoup(response.content, 'html.parser')
		cont = soup.title.text
		wr = open('validated urls.tsv','a')
		wr.write(str(status)+'\t'+str(cont)+'\t'+str(url.strip())+'\n')
	except:
		wr.write(str(status)+'\t'+str(cont)+'\t'+str(url.strip())+'\n')
        
print('Url validation completed')


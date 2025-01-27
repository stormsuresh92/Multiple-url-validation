import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from time import sleep

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
}

with open('inputurls.txt', 'r') as urls:
    url_list = urls.readlines()

with open('validated1_urls.csv', 'a') as wr:
    # Write column headers
    wr.write('Status_Code,Title,URL\n')

    for url in tqdm(url_list):
        try:
            response = requests.get(url.strip(), headers=headers, timeout=10)
            sleep(3)
            status = response.status_code
            soup = BeautifulSoup(response.content, 'html.parser')
            cont = soup.title.text
        except Exception as e:
            status = 'Error'
            cont = str(e)
        
        wr.write(f'{status},{cont},{url.strip()}\n')

print('URL validation completed')


from urllib import request, error
from bs4 import BeautifulSoup


with request.urlopen('https://akipress.org') as resp:
    data = resp.read()
    soup = BeautifulSoup(data, 'html.parser')
    items = soup.find_all('a', attrs={'class': 'newslink'})
    for item in items:
        link = item.get('href')
        title = item.get_text()
        if 'turmush.kg' in link:
            with request.urlopen('https:'+link) as file:
                data1 = file.read()
                soup1 = BeautifulSoup(data1, 'html.parser')
                des = soup1.find_all('p')
                for i in des:
                    text = i.get_text()
                    with open(title + '.txt', 'a',encoding='utf-8') as file2:
                            file2.write(text)
                            print('done')



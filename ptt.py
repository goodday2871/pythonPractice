from bs4 import BeautifulSoup
import requests
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
req = requests.Session()
f = open('file.txt', 'w')

payload = {
    'from': '/bbs/Gossiping/index.html',
    'yes': 'yes'
}


for i in range(3):
    r1 = req.post(
        'https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html', data=payload)
    r2 = req.get(url)
    soup = BeautifulSoup(r2.text, 'html.parser')
    sel = soup.select('div.title a')
    u = soup.select('div.btn-group.btn-group-paging a')
    print('url 為', ' ', url)
    for s in sel:
        print('https://www.ptt.cc'+s['href'], s.text)
        f.write(str('https://www.ptt.cc'+s["href"]) + "  " + s.text+"\n")
    url = 'https://www.ptt.cc' + u[1]['href']

f.close()

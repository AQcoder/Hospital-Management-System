import requests
import bs4
all_para=""
r=requests.get('https://en.wikipedia.org/wiki/Jupiter')
soup=bs4.BeautifulSoup(r.text,'html5lib')
headers=[]
for url in soup.find_all("h3"):
    headers.append(url.text)
i = len(headers) - 1
counter = 0
while counter <= i:
    if headers[counter].endswith('\t'):
        headers.pop(counter)
        counter -= 1
    counter += 1
    i = len(headers) -1
for iteri in range(len(headers)):
    deet = soup.find('h3', text=headers[iteri])
    for para in deet.find_next_siblings():
        if para.name == "h2" or para.name == "h3":
            break
        elif para.name=='p':
            all_para += para.get_text()
            all_para += '\n'
print(all_para)

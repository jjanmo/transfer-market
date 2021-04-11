# BeautifulSoup Practice

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.114 Safari/537.36'}

url = 'https://www.transfermarkt.com/'

r = requests.get(url, headers=headers)
print(r.status_code)

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>"""

soup = BeautifulSoup(html_doc, 'html.parser')

# p 태그 정보 가져오기 (처음 나오는 것 한 개)
# 1)
print(soup.p)
# 2)
print(soup.find('p'))

# a 태그에 있는 'href' 속성값 가져오기 (처음 나오는 것 한 개)  // soup.TAG['attribute'] or soup.find('TAG')['attribute']
print(soup.a['href'])
print(soup.find('a')['href'])

# a 태그에 있는 텍스트 가져오기 (처음 나오는 것 한 개)
print(soup.a.text)
print(soup.a.get_text())
print(soup.find('a').text)

# a 태그에 있는 요소들 모두 가져오기
print(soup.find_all('a'))

# 두번째 a태그에 있는 정보 가져오기
print(soup.find_all('a')[1])

# a 태그에 있는 'href' 속성값 모두 가져오기
a_list = soup.find_all('a')
for a in a_list:
    print(a['href'])

# a 태그이면서 class가 sister인 값 모두 찾아오기
print(soup.find_all('a', class_='sister'))
print(soup.find_all('a', {'class': 'sister'}))

# a태그이면서 id가 link3인 요소들 모두 찾기
print(soup.find_all('a', {'id': 'link3'}))

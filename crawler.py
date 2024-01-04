import requests
url = "https://www.index.hu"
response = requests.get(url)
# A weboldal HTML tartalmának kiolvasása
html_content = response.text
# print(html_content)

from bs4 import BeautifulSoup
# HTML tartalom feldolgozása BeautifulSoup segítségével
soup = BeautifulSoup(html_content, 'html.parser')

h2s = soup.find_all('h2') # Az összes H2 címke kiválasztása

with open('milan_horvath_index.txt', 'w') as f:
    for x in h2s:
        h2 = h2s.pop()
        print("*******************")
        f.write("*******************\n")
        #  print(h2)
        a_link = h2.find('a')
        if a_link is None:
            print("!!!!!!!!!!!!!!!!!!")
            f.write("!!!!!!!!!!!!!!!!!!\n")
            a_text = h2.getText();
        else:
            a_text = a_link.getText();
        print(a_text)
        f.write(a_text + "\n")


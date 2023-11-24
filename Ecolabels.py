#paints: GreenGuard, Green Seal, Master Painters Institute Green Performance Standard, LEED v4

///////////////////////////////////////////////////////////////////////////////////////////////////

import requests
from bs4 import BeautifulSoup

# Make a GET request to the website
url = "https://www.ecolabelindex.com/ecolabels/"
page = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(page.content, "html.parser")

# Find the relevant information on the page
# Replace with the specific tags and attributes that contain the data you want to scrape
ecolabels = soup.find_all("div", class_="ecolabel")

# Extract the data for each ecolabel
data = []
for ecolabel in ecolabels:
    name = ecolabel.find("h3").text
    description = ecolabel.find("p").text
    data.append({
        "Name": name,
        "Description": description
    })

# Print the extracted data
for item in data:
    print(item["Name"])
    print(item["Description"])
    print("\n")

//////////////////////////////////////////////////////////////////////////////////////////////////
<h4 class="cuddle"><a  href="/ecolabel/wholesome-food-association">Wholesome Food Association</a></h4>
                    <p>The Wholesome Food Association local symbol scheme is a low-cost. </p>

//////////////////////////////////////////////////////////////////////////////////////////////////

import requests
from bs4 import BeautifulSoup # add this

response = requests.get('https://www.ecolabelindex.com/ecolabel/forest-stewardship-council-fsc-forest-management-certification')

main_page = response.text
print(main_page)

# add this 
soup = BeautifulSoup(yc_web_page, 'html.parser')

article_tag = soup.find(name="h4", class_='cuddle')
article_title = article_tag.get_text()

article_link = article_tag.get('href')
article_des = soup.find(name="p").get_text()

result = {
  "title": article_title,
  "link": article_link,
  "point": article_des
}

print(result)

///////
labels = soup.find_all(name="h4", class_='cuddle')
for i in labels:
  label_title = i.get_text()
  print(label_title)
//////

alexandra@utrechtinc.nl

Alexandra Purewal



import bs4
import requests

# response = requests.get("https://news.ycombinator.com/")
# response.raise_for_status()
with open("news.html", "r") as f:
    html = f.read()
soup = bs4.BeautifulSoup(html, 'html.parser')

tags = soup.select(selector="span.titleline a")

scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(scores)
largest = max(scores)
largest_index = scores.index(largest)
print(largest_index)

print(tags[largest_index * 2 - 1])


# with open("website.html", 'r') as f:
#     html = f.read()
#
# soup = bs4.BeautifulSoup(html, 'html.parser')
#
# all_anchors = soup.find_all(name="a")
# for tag in all_anchors:
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section = soup.find(name="h3", class_="heading")
# print(section)
#
# company_url = soup.select_one(selector="#name")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)


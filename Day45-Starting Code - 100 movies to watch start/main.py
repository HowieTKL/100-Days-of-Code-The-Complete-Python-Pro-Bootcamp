import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
with open("movies.html", "r") as file:
    html = file.read()
# print(html)
soup = BeautifulSoup(html, "html.parser")

tags = soup.find_all(name="h3", class_="title")
movies = [tag.text for tag in tags]
movies.reverse()
with open("movies.txt", "w") as f:
    for movie in movies:
        f.write(f"{movie}\n")

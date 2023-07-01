import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/search/title?title_type=feature&sort=num_votes,desc&count=10"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
movies = soup.find_all("div", class_="lister-item mode-advanced")
for movie in movies:
  title = movie.find("h3").text
  rating = movie.find("div", class_="ratings-bar").find("span", class_="rating-value").text
  print(title, rating)

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []

for article in articles:
    text = article.getText()
    link = article.get("href")
    article_texts.append(text)
    article_links.append(link)

article_votes = [int(vote.getText().split()[0]) for vote in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_votes)

max_votes = max(article_votes)
max_index = article_votes.index(max_votes) + 1

print(max_votes)
print(max_index)

print(article_texts[max_index])
print(article_links[max_index])

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.p)
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
# all_paragraphs = soup.find_all(name="p")
# # print(all_paragraphs)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find_all(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
#
# company_url = soup.select_one(selector="p a")

from bs4 import BeautifulSoup
import requests

def parse_vox(page_count):
    results = []
    for page in range(1, page_count+1):
        url = f"https://www.vox.com/technology/archives/{page}"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        links_titles = soup.select(".c-entry-box--compact__title>a")
        authors = soup.select(".c-byline__author-name")
        dates = soup.find_all("time")
        for i in range(len(links_titles)):
            results.append(
                {
                    'title': links_titles[i].text,
                    'link': links_titles[i]['href'],
                    'author': authors[i].text,
                    'date': dates[i].text.replace('\n', '')
                }
            )

    return results

pages = parse_vox(5)
for i in pages:
    print(f"""
    Title: {i['title']}
    Link: {i['link']}
    Author: {i['author']}
    Date: {i['date']}
    """)

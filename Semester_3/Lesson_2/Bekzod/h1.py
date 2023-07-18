import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

# parsing
def parser_vox():
    result=[]
    url=f'https://www.vox.com/technology/archives'
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    titles=soup.find_all(class_='c-entry-box--compact__title')
    author_title=soup.select(".c-byline")
    times=[time.get_text().rstrip().lstrip() for time in soup.select('time')]
    for id, title in enumerate(titles):
        if author := author_title[id].find(class_="c-byline__author-name"):
            author=author.string.split()[0]
            
            result.append({
                'title':title.a.string,
                'link': title.a['href'],
                'author':author,
                'datatime':times[0],
                })
            times.pop(0)
    pprint(result)
    with open('data.json','w') as f:
        json.dump(result,f)
parser_vox()


# Codewars
# def divisors(n):
#     result=[]
#     for i in range(1,n //2+1):
#         if n % i == 0:
#             result.append(i)
#     result.append(n)
#     return len(result)


# print(divisors(4))


# test.assert_equals(divisors(1), 1) 
# test.assert_equals(divisors(4), 3)
# test.assert_equals(divisors(5), 2)
# test.assert_equals(divisors(12), 6)
# test.assert_equals(divisors(30), 8)
# test.assert_equals(divisors(4096), 13)



# def friends(x):
#     return list(filter(lambda i: len(i)==4,x ))
# print(friends(["Ryan", "Kieran", "Mark",]))


# def duplicate_count(text):
#     return len(set(list(filter(lambda x: text.lower().count(x) >= 2 , text.lower()))))
"""
    Explanation
    result=[]
    for i in text.lower():
        if text.lower().count(i) >= 2:
            result.append(i)
    return len(set(result))
"""


# print(duplicate_count("abcdeaB"))
# print(duplicate_count("abcde"))
# print(duplicate_count('Abcdeac'))
# print(duplicate_count("Indivisibilities"))
# print(duplicate_count(""))



# def comp(array1,array2):
#     lst1=sorted(set(array1))
#     lst2=sorted(set(array2))
#     newlst=[]    
#     for i in lst1:
#         newlst.append(i**2)
#     if newlst == lst2:
#         return True
#     return False


# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# print(comp(a1,a2))
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
# print(comp(a1,a2))
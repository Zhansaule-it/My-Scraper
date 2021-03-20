from bs4 import BeautifulSoup
import requests

#  function take a repository array of dict and transform it and return it into a CSV string
def format(repositories_data):
    CSVstring = "deverloper,repository_name,nbr_stars\n"
    for i in range(len(repositories_data)):
        CSVstring +="".join((repositories_data[i]['deverloper'])+","+(repositories_data[i]['repository_name'])+","+(repositories_data[i]['nbr_stars'])+"\n")
    print(CSVstring)
    return CSVstring

# function take an array of the repository row and return an array of dictionary
def transform(html_repos):
    res = []
    for i in range(0,len(html_repos)-2,3): 
         res.append({'deverloper': html_repos[i], 'repository_name': html_repos[i+1], 'nbr_stars': html_repos[i+2]})
    format(res)
    return res

# function extract data about repostories from html code and return it
def extract(page):
    soup = BeautifulSoup(page.text, "lxml")
    name_project= []
    star = []
    art = soup.find_all('article',class_="Box-row")
    for tag in art:
        name_project.append(tag.find_all('h1',class_="h3 lh-condensed")[0].text.strip("\n").strip().split("/"))
       # star.append(tag.find_all('a',class_="")[0].text.strip("\n").strip())
    # the name of class of tag "a" sometimes changes, previously name was "muted-link d-inline-block mr-3"
    all_data = []
    for i in range(len(name_project)):
        all_data.append(name_project[i][0].strip())
        all_data.append(name_project[i][1].rstrip().strip("\n").strip())
        all_data.append(star[i])
    transform(all_data)
    return all_data

# function get request from giving url and return it
def request_github_trending(url):
    response = requests.get(url)
    extract(response) 
    return response

url = 'https://github.com/trending'
request_github_trending(url)

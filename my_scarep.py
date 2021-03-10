def format(repositories_data):
    res = "deverloper,repository_name,nbr_stars\n"
    for i in range(len(repositories_data)):
        res +="".join((repositories_data[i]['deverloper'])+","+(repositories_data[i]['repository_name'])+","+(repositories_data[i]['nbr_stars'])+"\n")
    print(res)
def transform(html_repos):
    res = []
    for i in range(0,len(html_repos)-2,3): 
         res.append({'deverloper': html_repos[i], 'repository_name': html_repos[i+1], 'nbr_stars': html_repos[i+2]})
    format(res)
def extract(page):
    from bs4 import BeautifulSoup
    import requests
    soup = BeautifulSoup(page.text, "lxml")
    name_project= []
    star = []
    art = soup.find_all('article',class_="Box-row")
    for tag in art:
        name_project.append(tag.find_all('h1',class_="h3 lh-condensed")[0].text.strip("\n").strip().split("/"))
        star.append(tag.find_all('a',class_="muted-link d-inline-block mr-3")[0].text.strip("\n").strip())
    all_data = []
    for i in range(len(name_project)):
        all_data.append(name_project[i][0].strip())
        all_data.append(name_project[i][1].rstrip().strip("\n").strip())
        all_data.append(star[i])
    #print(all_data)
    transform(all_data)
def request_github_trending(url):
    import requests
    response = requests.get(url)
    extract(response) 
url = 'https://github.com/trending'
request_github_trending(url)

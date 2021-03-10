# My-Scraper
Project get return a CSV of the TOP 25 trending repository from Github
*def request_github_trending(url) it  return the result of Request.
*def extract(page) in order to find_all instances of html code of repository rows and return it. 
*def transform(html_repos) taking an array of all the instances of html code of the repository row.
It will return an array of hash following this format: [{'deverloper': NAME, 'repository_name': REPOS_NAME, 'nbr_stars': NBR_STARS}, ...]
*def format(repositories_data) taking a repository array of hash and transform it and return it into a CSV string. Each columns will be separated by , and each lines by \n
The columns will be Developer, Repository Name, Number of Stars

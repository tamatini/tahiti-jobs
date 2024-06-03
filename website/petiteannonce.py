from src.utils import scrapper
from src.models import jobModel

url = "https://www.petites-annonces.pf/annonces.php?c=28"

get_soup = scrapper.get_soup
get_session = scrapper.get_session

soup = get_soup(get_session(url))


def jobs_url():
    jobsUrl = []
    jobs = soup.find_all("a", class_="lda")
    for job in jobs:
        jobsUrl.append("https://www.petites-annonces.pf/"+job["href"])
    return jobsUrl


def job_list():
    jobsList = []
    for job_url in jobs_url():
        soup = get_soup(get_session(job_url))
        job = soup.find("div", id="det")
        title = job.find("h3", attrs={'class': None}).text
        print(title)


def save_job():
    for job_url in jobs_url():
        print(job_list())
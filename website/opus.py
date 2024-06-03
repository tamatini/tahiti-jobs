from src.utils import scrapper
from src.models import jobModel

url = "https://opus.recruitee.com"

get_soup = scrapper.get_soup
get_session = scrapper.get_session

soup = get_soup(get_session(url+"/offres-demploi"))


def jobs_url():
    jobsUrl = []
    jobs = soup.find_all("div", class_="sc-uzptka-1")
    for job in jobs:
        jobsUrl.append(url+job.find("a")["href"])
    return jobsUrl


def job_list():
    jobsList = []
    for job_url in jobs_url():
        soup = get_soup(get_session(job_url))
        job = soup.find("main", class_="sc-73r8cv-0")
        jobTitle = job.find("h1", class_="sc-crgk9f-2").text
        jobLocation = job.find("span", class_="sc-qfruxy-1").text
        jobDescription = job.findAll("div", class_="sc-1fwbcuw-0")[0].text
        jobQualifications = job.findAll("div", class_="sc-1fwbcuw-0")[1].text
        jobsList.append(jobModel.job(jobTitle, job_url, jobLocation, jobDescription, jobQualifications))
    return jobsList

def save_job():
    for job in job_list():
        job.save()
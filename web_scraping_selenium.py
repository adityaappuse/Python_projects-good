from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

#Using microsoft edge access the naukri website homepage
os.environ["PATH"] += r"C:/Selenium drivers"
driver = webdriver.Edge()
url1 = "https://www.naukri.com/python-jobs-in-india?k=python&l=india&experience=0&nignbevent_src=jobsearchDeskGNB"
driver.get(url1)
try:
    WebDriverWait(driver,30).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME,"styles_job-listing-container__OCfZC")  #Element filtration steps
        )   
    )
    

    html = driver.page_source


    soup = BeautifulSoup(html,"html.parser")
    job_details = soup.find("div",class_= "styles_job-listing-container__OCfZC")
    job_rows = job_details.find_all("div",class_="srp-jobtuple-wrapper")

    #find locations
    
    #show each column information in the job table
    for each_column in job_rows:
        anchor = each_column.find("span",class_="locWdth")
        locations = anchor.get("title")
        #find post_day
        post_day =each_column.find("span",class_="job-post-day")

        if "bengaluru" in locations.lower() or "bangalore" in locations.lower() and "1 Day ago" in post_day:
            print("\n",locations)
            #gives the job title
            job_name = each_column.find("a",class_="title")
            print("Job Name: ",job_name.text)

            #gives the rating
            rating = each_column.find("span",class_="main-2")
            try:
                print("Rating: ",rating.text,end ="\t")
            except:
                print("Not available")

            #Checks the experience required is fresher
            experience = each_column.find("span",class_="exp-wrap")
            print("Experience: ",experience.text)
            #It has a title with locations
            # location_details = each_column.find_all("span",class_="title")
            # for locations in location_details:
            #     print("Locations: ",locations,end="\t")
            try:
                skillset = each_column.find("ul",class_="tags-gt")
                skills = skillset.find_all("li",class_="dot-gt tag-li")
                print("Skills:",end = "\n\t")
                for each_skill in skills:
                    print(each_skill.text,end="\t")
            except Exception as e:
                print(e)    

            job_href = job_name.get("href")
            print("\nLink : ",job_href)
            
            
            #find the links to direct page
            

        # job_post_day = each_column.find("span",class_ ="job-post-day")
        # if(job_post_day.text == "1 Day Ago"):
        #     job_name = each_column.find("a",class_="title")
        #     company_name = each_column.find("a",class_ = "comp-name mw-25")
        #     experience = each_column.find("span",class_="expwdth")
        #     rating = each_column.find("a",class_="rating")
        #     Skills = each_column.find("ul",class_="tags-gt")
        #     print("Job Title is ",job_name.text)
        #     print("Company_name is ",company_name.text)
        #     print("The experience required is ",experience.text)
        #     print("Rating of the company is ",rating.text)
        #     print("The skills required are",Skills.text)
except Exception as e:
    print(e)
    print("The page was closed . Restarting....")
    driver.quit()
    driver =webdriver.Edge()
   
finally:
    driver.quit

# job_list = WebDriverWait(driver,30).until(
#     EC.presence_of_element_located(
#          (By.CLASS_NAME,"styles_job-listing-container__OCfZC") , #Element filtration steps
#     )   
# )

#to do list
#find company name somehow
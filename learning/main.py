from dotenv import load_dotenv 
from crewai import Crew
from langchain_openai import AzureChatOpenAI
import openai
from openai import AzureOpenAI
from tasks import ResumeshortlistingTasks
from agents import resumeAgents
import os


def main():
    load_dotenv()

    """"azure_oai_endpoint=os.getenv("https://bits-interns.openai.azure.com/")
    OPENAI_API_KEY=os.getenv("be2fa5bef41f4252bc9a56364e75986d")
    azure_oai_model="gpt-4"
    azure_deployment="Interns-deployment"""

    print("## Welcome to the resume shortlisting model")
    print('-------------------------------')
    job_listing= input("What is the job listing?\n")
    resume=[]
    i=1
    t='t'
    while(t=='t'):
        k=input("Enter resume of candidate number "+str(i)+"?\n")
        resume.append(k)
        i+=1
        t=input("enter t to enter one more resume\n")

    tasks = ResumeshortlistingTasks()
    agents = resumeAgents()
    
    # create agents
    compatibility_checker = agents.compatibility_checker()
    analyst_checker = agents.analyst_checker()

    
    # create tasks
    research_job = tasks.research_job(analyst_checker, job_listing)
    research_each_resume = tasks.research_each_resume(analyst_checker,resume)
    yesorno = tasks.yesorno(compatibility_checker, job_listing,resume)
    
    #research_job.context = [job_listing]
    #research_each_resume.context = [resume]
    yesorno.context=[research_job,research_each_resume]
    
    crew = Crew(
      agents=[
        compatibility_checker,
        analyst_checker,
      ],
      tasks=[
        research_job,
        research_each_resume,
        yesorno
      ]
    )
    
    result = crew.kickoff()
    
    print(result)
    
if __name__ == "__main__":
    main()
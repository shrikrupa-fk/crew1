from textwrap import dedent 
from crewai import Agent 
from langchain_openai import AzureChatOpenAI
llm = AzureChatOpenAI(
   openai_api_version="2024-02-01",
   azure_deployment="test",
   azure_endpoint="https://bits-interns.openai.azure.com/",
   api_key="be2fa5bef41f4252bc9a56364e75986d",
   model="gpt-4o",
)
class resumeAgents():
    def compatibility_checker(self):
      return Agent(
        role="Compatibility checker",
        goal='Go through job listing and the resume of each candidate and check if its a match.',
        backstory=dedent("""\
          As a Compatiblity checker, your mission is to finalise 5 most suitable candidates for the particular job listing
        Check for skill match. Check for the years of experience required. """),
        verbose=True,
        llm=llm
      )
      
    def analyst_checker(self):
      return Agent(
        role='Analyst',
        goal='Analyze the given text and identify role required, key skills needed, years of experience.',
        backstory=dedent("""\
            As an Analyst, your analysis will identify key skills,
            and potential filters that will help the hiring process become more efficient and smooth,
            identify key skills that seperates a candidate from the rest."""),
        verbose=True,
        llm=llm
      )

from crewai import Task
from textwrap import dedent
from langchain_openai import AzureChatOpenAI
llm = AzureChatOpenAI(
   openai_api_version="2024-02-01",
   azure_deployment="test",
   azure_endpoint="https://bits-interns.openai.azure.com/",
   api_key="0874561ae99a4f6886e7e53f575ff19a",
   model="gpt-4o",
)
class ResumeshortlistingTasks():
    def research_job(self,agent,job_listing):
        return Task(
            description=dedent(f"""\
            Conduct comprehensive research on the job listing and the key skills required
            .Gather information on the technical languages required for the job. Note the years of experience listed.
            Summarise what the role is.

            Job listing: {job_listing}"""),
            expected_output=dedent("""\
            A detailed report summarizing key findings about the job posting. It should contain, role expected
            ,years of experience and languages required"""),
        async_execution=True,
        agent=agent,
        llm=llm
        )
    def research_each_resume(self,agent,resume):
        return Task(
            description=dedent(f"""\
				Analyze the resume. Look for listed key skills. Look for languages known. Look for 
                years of experiences. Check if the job listing matches the candidates profile. The number of years of
                experience of the candidate must be greater or equal to the years listed on the profile."

				Resumes: {resume}"""),
			expected_output=dedent("""\
				Give the key skills of the applicant. Which languages they know. How many years of experience."""),
			async_execution=True,
			agent=agent,
            llm=llm               
            )
    def yesorno(self, agent, job_listing, resume):
        return Task(
			description=dedent(f"""\
				Compare the job listing with the resumes of each individual candidate. If the skills mentioned by the candidate and the skills required on the job listing are similar or the same.

				job listing: {job_listing}
				resume: {resume}"""),
			expected_output=dedent("""\
				Get the email ids of the 5 most applicable candidates from the list of resumes containing 10 candidates' resumes.
                put the email ids of the 5 shortlisted candidates in another list called FINAL ROUND and output it."""),
			agent=agent,
            llm=llm
		)

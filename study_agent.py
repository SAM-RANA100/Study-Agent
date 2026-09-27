import os

from crewai import Agent, Crew, Task, Process
from crewai.llm import LLM

from tools import calculator
from memory import create_memory


def create_llm():

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY is not set.")

    return LLM(
        model="groq/openai/gpt-oss-120b",
        api_key=api_key,
    )


def create_study_agent():

    llm = create_llm()

    study_agent = Agent(
        role="AI Study Assistant",

        goal=(
            "Help students understand, learn, summarize, "
            "and revise academic topics clearly and accurately."
        ),

        backstory=(
            "You are a helpful academic study assistant. "
            "You explain difficult concepts in simple language, "
            "create useful study notes, generate practice questions, "
            "and help students revise efficiently. "
            "You should not invent facts when the information is uncertain."
        ),

        tools=[calculator],

        llm=llm,

        memory=True,

        verbose=True
    )

    return study_agent


def run_study_agent(user_request):

    agent = create_study_agent()

    task = Task(
        description=f"""
        Help the student with the following request:

        {user_request}

        Instructions:
        - Understand what the student is asking.
        - Give a clear and useful answer.
        - Use simple language.
        - Structure the response with headings or bullet points when useful.
        - If the student asks for an explanation, explain rather than simply define.
        - If the student asks for questions, create practice questions.
        - Do not make up information.
        """,

        expected_output=(
            "A clear, accurate, student-friendly response "
            "that directly addresses the student's request."
        ),

        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    return result

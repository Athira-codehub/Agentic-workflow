import os
from crewai import Agent
from tools import tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True,
                             temperature=0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY"))


#Creating a senior research agent with memory and verbose mode

news_researcher = Agent(role="Senior Researcher",
                   goal = "Uncover ground breaking technologies in {topic}",
                   llm=llm,
                   verbose=True,
                   memory=True,
                   backstory = (
                       "Driven by curiosity , you want to explore and share knowledge to the world"
                   ),
                   tools=[tool],
                   allow_delegation=True
                   )

#creating write agent with custom tools responsibe in writing news
news_writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about topic',
    verbose='True',
    memory='True',
    backstory='you create enganging narratives that bring new discoveries to light',
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
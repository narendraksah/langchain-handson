from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

llm = ChatGoogleGenerativeAI(temperature=0.0, model="gemini-2.5-flash-lite")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-handson: react-search-agent!")
    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="Search for 3 job postings for AI engineer using langchain in Banglore, India on linkedin and list their details."
            )
        }
    )
    print(result)


if __name__ == "__main__":
    main()

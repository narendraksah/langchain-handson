from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch


class Source(BaseModel):
    """Schema for a source used by the agent"""

    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer: str = Field(description="The Agent's answer to the query")
    sources: List[Source] = Field(
        default_factory=list, description="List of sources used to generate answer"
    )


llm = ChatGoogleGenerativeAI(temperature=0.0, model="gemini-2.5-flash-lite")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


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

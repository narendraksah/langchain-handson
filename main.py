import asyncio
from dotenv import load_dotenv
from langchain.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters

load_dotenv()
llm = ChatGoogleGenerativeAI(temperature=0.0, model="gemini-2.5-flash-lite")

stdio_server_param = StdioServerParameters(
    command="python",
    args=[
        "C:/Users/platformengineering/Desktop/LCHandsOn/langchain-handson/servers/math_server.py"
    ],
)


async def main():
    async with stdio_client(stdio_server_param) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("Session initialized")
            tools = await load_mcp_tools(session)

            agent = create_agent(llm, tools)

            result = await agent.ainvoke(
                {"messages": [HumanMessage(content="What is 52 + 2 * 6?")]}
            )

            print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())

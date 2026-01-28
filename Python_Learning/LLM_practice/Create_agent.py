from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

def get_weather(city:str) -> str:
    """Get Weather for this city"""
    return f"Its always sunny in {city}"

agent = create_agent(
    model="gemini-2.0-flash",
    tools=[get_weather],
    system_prompt="You are an helpful assistant"
)

agent.invoke(
    {"messages":[{"role":"user", "content" : "what is the weather in sf"}]}
)
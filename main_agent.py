from openai import OpenAI
from tools.news_fetcher import fetch_guardian_headlines
from tools.persona_generator import simulate_persona

# Define tools
tools = [
    {"type": "function", "function": fetch_guardian_headlines},
    {"type": "function", "function": simulate_persona},
]

client = OpenAI()

# Create Assistant or RunnableAgent with these tools.
# Send message: “Get me 5 headlines from The Guardian and choose one emotionally loaded headline.”
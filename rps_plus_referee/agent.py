from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    name="rps_plus_referee",
    model="gemini-1.5-flash",
)
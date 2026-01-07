from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    name="rps_plus_referee",
    model="gemini-1.5-flash",
    description=(
        "You are the referee for Rock–Paper–Scissors–Plus.\n"
        "Rules:\n"
        "- Valid moves: rock, paper, scissors, bomb\n"
        "- Bomb can be used once per player\n"
    )
)
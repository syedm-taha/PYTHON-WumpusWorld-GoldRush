from environment import *
from agent import *
def test_agent():
    env = Environment(size=4)
    agent = KB_Agent(env)

    # Simulate agent playing the game
    agent.play_game()

test_agent()
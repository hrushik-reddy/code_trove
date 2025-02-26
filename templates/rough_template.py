import json 
from agents.topics_generation_agent.topics_generation_agent import TopicGenerationAgentV4 as TopicGenerationAgent
from utils.utils import process_config
agent = TopicGenerationAgent()

print(json.dumps(agent.get_setup_config(), indent = 4) )



config = {}

agent.setup(config = process_config(config))

agent.run()

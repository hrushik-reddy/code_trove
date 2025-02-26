from agents.google_calendar_agent.google_calendar_agent import GoogleCalendarAgent
import json
print(json.dumps(GoogleCalendarAgent.get_setup_config(), indent=4)

config = {}

from agents.google_calendar_agent.google_calendar_agent import GoogleCalendarAgent
from utils.utils import process_config
processed_config=process_config(config=rough_config, sub_level="tools")
agent=GoogleCalendarAgent()
agent.setup(config=processed_config, data = {
    "concierge_id": "be05476a-45f2-4545-9915-797b0112b8f5",
    "request_id": "requestId-fcbff7d7-edb1-48af-a2fa-182661334c17",
    "agent_name": "CreativeEmailAgent",
    "agent_id": "676296735f2a37fc59d47fd6",
    "agent_url": "https://ea55-205-254-168-145.ngrok-free.app/utility/creative-email-agent/",
    "agent_arguments": {
        "user_query": "Send an email stating that the email agent is working perfectly.",
        "user_email": "yash.mathur@techolution.com",
        "user_name": "Yash Mathur",
        "recipient_email": "mohak.khatri@techolution.com",
        "recipient_name": "Mohak Khatri"
    },
    "chat_history": [],
    "question": "Can you send a mail to \"mohak.khatri@techolution.com\", my email id is: \"yash.mathur@techolution.com\" stating that the email agent is working perfectly.",
    "prompt": "",
    "modelType": "google",
    "preview_id": "techolution-dummyassistant-0ca72249-ff5a-44f0-9d2a-e319f4fe2702",
    "orchByPassed": False
}
)
print(agent.run(user_email="rithuraj.nambiar@techolution.com", user_query="what meets do i have today?"))

import os
from asyncio import run

from dotenv import load_dotenv
from icecream import ic

from ua_alarm import Client as UkraineAlertApiClient

# Clear the console screen
os.system('cls' if os.name == 'nt' else 'clear')

load_dotenv()
client = UkraineAlertApiClient(os.getenv("UA_ALARM_API_KEY"))

# Run the main function
if __name__ == '__main__':
    try:
        # run(client.get_alerts())
        # history = run(client.get_region_history(12))

        # history = history[0].alarms[0].alertType
        # ic(client.refactor_alert_type(history))
        # ic(run(client.get_regions()))
        ic(run(client.get_alerts()))
        # run(client.alert_loop(12, True))

    except KeyboardInterrupt:
        exit()

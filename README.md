### Installing

## pip

``` bash
pip install -r requirements.txt -y
```

## poetry

``` bash
poetry install
```

## UA_ALARM

> Elegant, modern and asynchronous UkraineAlarm API framework in Python

``` python
from ua_alarm import Client as UkraineAlertApiClient
import os
from aiohttp.client_exceptions import ClientConnectorError
from asyncio import sleep, run

# Clear the console screen
os.system('cls' if os.name == 'nt' else 'clear')

api_token = "YOUR_API_KEY"
client = UkraineAlertApiClient(api_token)


async def main():
    # Example usage: Get a list of alerts
    alerts = await client.get_alerts()
    print(alerts)

alert_changed_time = ""

async def alert_loop():
    """
    A loop that continuously monitors for changes in the alert state for a specific region.

    The loop fetches region alerts using the UkraineAlert API and checks for changes in the last update time.
    If a change is detected, it prints information about the active alert, if any.

    Note: The loop sleeps for 30 seconds between iterations.

    Raises:
        ClientConnectorError: If there's a connection issue during API request.

    Global Variables:
        alert_changed_time (str): A global variable to store the timestamp of the last alert change.

    API Token:
        The API token is hardcoded for demonstration purposes.

    API Client:
        An instance of UkraineAlertApiClient is used to interact with the UkraineAlert API.
    """
    global alert_changed_time

    # Continuously monitor for changes in the alert state
    while True:
        try:
            # Fetch region alerts (region_id=28)
            data = await client.get_region_alerts(28)

            # Extract the last update time from the fetched data
            changed_str = data[0].lastUpdate

            # Check if there's a change in the alert state
            if not changed_str == alert_changed_time:
                alert_old_changed_time = alert_changed_time
                alert_changed_time = changed_str

                # Skip if duration less than or equal to 10 seconds
                if alert_old_changed_time:
                    if int((alert_changed_time - alert_old_changed_time).total_seconds()) <= 10:
                        continue

                    # Extract information about active alerts, if any
                    active_alerts = data[0].activeAlerts

                    # Construct a text message based on the active alert status
                    if active_alerts:
                        text = f"{active_alerts[0].type}\n\n‼️ Оголошено тривогу"
                    else: 
                        text = "Відбій тривоги"

                    # Print the alert information
                    print(text)

        # Continue to the next iteration if there's a connection issue
        except ClientConnectorError:
            pass

        # Sleep for 30 seconds before checking for changes again
        await sleep(30)


# Run the main function
if __name__ == '__main__':
    try:
        run(main())
    except KeyboardInterrupt:
            exit()
```

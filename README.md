# UA_ALARM 🚨
> Elegant, modern and asynchronous UkraineAlarm API framework in Python

## About

### UK

**Імплементує [api.ukrainealarm.com](https://api.ukrainealarm.com/swagger/index.html), який повертає інформацію про
повітряні тривоги в Україні.**

**Потребує API-ключ. Подавайте запит на отримання через форму на [api.ukrainealarm.com](https://api.ukrainealarm.com/).**

### EN

**Implements [api.ukrainealarm.com](https://api.ukrainealarm.com/swagger/index.html) API that returns info about Ukraine
air raid alarms.**

**Request API key via form on [api.ukrainealarm.com](https://api.ukrainealarm.com/).**
> About text was copied from [github.com/PaulAnnekov/ukrainealarm](https://github.com/PaulAnnekov/ukrainealarm)

## Installing

### pip

``` bash
pip install ua_alarm
```

### poetry

``` bash
poetry add ua_alarm
```

### Example

```python
from ua_alarm import Client as UkraineAlertApiClient
import os
from aiohttp.client_exceptions import ClientConnectorError
from asyncio import sleep, run

# Clear the console screen
os.system('cls' if os.name == 'nt' else 'clear')

api_token = "YOUR_API_KEY"
client = UkraineAlertApiClient(api_token)

# Run the main function
if __name__ == '__main__':
    try:
        run(client.get_alerts())
    except KeyboardInterrupt:
        exit()
```
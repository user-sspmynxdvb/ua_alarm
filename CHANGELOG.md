# Changelog

## [v1.3.4]() - 04.12.2023

### Improved
- **functions: __init__, _make_request**
- **files: client.py**

### Added
- **libraries: from asyncio import run**

### More info
- **__init__: added run(self._make_request("GET", self._ALERTS_ENDPOINT))**
- **_make_request: `if response.status != 200: raise Exception("Invalid API token")`**


## [v1.3.3](https://github.com/user-sspmynxdvb/ua_alarm/tree/bb6e4f60d6362467e61cb3dd6b24b7d3beed668c) - 29.11.2023

### Improved
- **code: Code format**

### Added
- **variables: Links have been moved to constants**

### Removed
- **functions: get_region_alerts**

### More info
- **removed function get_region_alerts, functionality has been moved to get_alerts**

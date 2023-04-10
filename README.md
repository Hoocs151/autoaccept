# Auto Accept for League of Legends

This script is used for auto accepting ready checks in League of Legends. It works by detecting the LeagueClientUx.exe process and retrieving the authentication key and port number to send a POST request to the ready check accept endpoint.

## Requirements

- Python 3.x
- `requests` library
- `base64` library
- `os` library
- `time` library
- `urllib3` library
- `logging` library

## Usage

- Make sure League of Legends is running.
- Run the script in the terminal using `python auto_accept.py`
- The script will automatically accept any ready checks that appear.

## Notes

- This script is for educational purposes only and should not be used to gain an unfair advantage in the game.
- The script may not work if Riot Games changes the authentication method or endpoint for ready check acceptance.

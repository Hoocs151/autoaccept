# League of Legends Auto Accept

This Python script automates the process of accepting match invitations in League of Legends client.

## Prerequisites

- Python 3.x
- Requests library (`pip install requests`)

## Usage

1. Make sure League of Legends client is running.
2. Run the Python script.
3. The script will continuously monitor for match invitations and automatically accept them.

## How it works

The script utilizes the Riot Games API to monitor for match invitations. It retrieves the necessary authentication key and port from the LeagueClientUx process using `wmic` command in Windows. Then, it sends a POST request to the `/lol-matchmaking/v1/ready-check/accept` endpoint with the obtained authorization header to accept match invitations.

## Disclaimer

This script interacts with the League of Legends client and uses its API. Use it responsibly and at your own risk. The script author is not responsible for any actions taken with this script.

## Troubleshooting

- If the script fails to run, make sure League of Legends client is running and try again.
- Ensure that the necessary dependencies are installed.

## Contributions

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or create a pull request.

import os
import base64
import requests
import time
import urllib3
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

KEYWORD = "LeagueClientUx.exe"
ACCEPT_ENDPOINT = "/lol-matchmaking/v1/ready-check/accept"
DELAY = 1

BASIC = "Basic"
AUTH_PREFIX = "riot:"
ACCEPT_HEADER = {"Accept": "application/json"}

logging.basicConfig(level=logging.INFO, format='%(message)s')
LOGGER = logging.getLogger(__name__)


def get_key_and_port():
    try:
        command = f"wmic process where \"caption=\'{KEYWORD}\'\" get Caption,Processid,Commandline"
        result = os.popen(command).read()
        key = result.split("remoting-auth-token=")[1].split('"')[0]
        port = result.split("app-port=")[2].split('"')[0]
        return key, port
    except:
        LOGGER.error("startKhông thể lấy được key và port")
        return None, None


def run_auto_accept():
    key, port = get_key_and_port()
    if key is None or port is None:
        LOGGER.error(
            "Không thể chạy auto accept, hãy chắc chắn rằng League of Legends đang chạy")
        return
    auth = f"{AUTH_PREFIX}{key}"
    auth_byte = auth.encode('ascii')
    auth_bsf_bytes = base64.b64encode(auth_byte)
    auth_encoded = auth_bsf_bytes.decode('ascii')
    LOGGER.info("Auto accept đang chạy.")
    while True:
        try:
            r = requests.post(url=f"https://127.0.0.1:{port}{ACCEPT_ENDPOINT}",
                              headers={
                                  'Authorization': f"{BASIC} {auth_encoded}", **ACCEPT_HEADER},
                              verify=False,
                              data='')
            if r.status_code == 204:
                os.system('cls' if os.name == 'nt' else 'clear')
                LOGGER.info("Auto accept đang chạy.")
            time.sleep(DELAY)
        except:
            LOGGER.error("Không thể chấp nhận trận đấu")
            break
    LOGGER.info("Auto accept đang chạy..")


if __name__ == "__main__":
    run_auto_accept()

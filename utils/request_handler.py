import time
import requests
from utils.logging import setup_logger

logger = setup_logger('request_handler')

def fetch_data(url: str, params: dict, max_retries: int = 3, sleep_time: int = 1) -> dict:
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                logger.info(f"Successfully fetched data from {url}")
                return response.json()
            else:
                logger.info(f"Attempt {attempt + 1} failed with status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error while fetching data: {e}")

        time.sleep(sleep_time)

    logger.error(f"Failed to fetch data after {max_retries} attempts")
    return None
import requests
import time
import logging

FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('Luna supply')

session = requests.session()
URL = "https://fcd.terra.dev/v1/circulatingsupply/luna"


def get_circulating_supply():
    response = session.get(URL)
    return int(response.json())


while True:
    supply_1 = get_circulating_supply()
    time.sleep(60)
    supply_2 = get_circulating_supply()
    logger.warning(f'Current supply:{supply_2}')
    if supply_2 - supply_1 > 0:
        logger.warning(f'🆘 ️Different: {(supply_2 - supply_1)} New Tokens')
    elif supply_2 - supply_1 < 0:
        logger.warning(f'🆘 ️Different: {(supply_2 - supply_1)} Burned Tokens')

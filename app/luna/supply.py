import requests
import time
import logging
import locale

locale.setlocale(locale.LC_ALL, 'en_US')
FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('Luna supply')

session = requests.session()
URL = "https://fcd.terra.dev/v1/circulatingsupply/luna"


def get_circulating_supply():
    response = session.get(URL)
    return int(response.json())


def main():
    prev_supply = 0
    while True:
        time.sleep(2)
        supply = get_circulating_supply()
        logger.warning(f'Current supply:{locale.format_string("%d", supply, grouping=True)}')
        if supply - prev_supply > 0:
            logger.warning(
                f'🆘 ️Different: {locale.format_string("%d", (supply - prev_supply), grouping=True)} New Tokens')
        elif supply - prev_supply < 0:
            logger.warning(
                f'🆘 ️Different: {locale.format_string("%d", (supply - prev_supply), grouping=True)} Burned Tokens')
        prev_supply = supply


if __name__ == '__main__':
    main()

import logging
import os

import requests
from lxml import html

_logger = logging.getLogger(__name__)


class Acsk:
    _certificate = os.path.join(
        os.path.split(os.path.dirname(os.path.realpath(__file__)))[0],
        'crtl'
    )

    def __init__(self):
        self._download_acsk_0()

    def _save_certificate(self, url, name):
        _logger.info(url)
        if not os.path.isfile(os.path.join(self._certificate, name)):
            responce = requests.get(url)
            if responce.status_code == 200:
                open(
                    os.path.join(self._certificate, name),
                    'wb').write(responce.content)
            else:
                _logger.error(responce.status_code)

    def _download_acsk_0(self):
        url = 'https://acskidd.gov.ua%s'
        tree = html.fromstring(requests.get(url % '/certs-crls').content)

        for href in tree.xpath('//a[@class="columntext"]'):
            _logger.info(href.get("href").split('/')[-1])
            try:
                self._save_certificate(
                    url % href.get("href"),
                    href.get("href").split('/')[-1]
                )
            except Exception:
                pass


if __name__ == '__main__':
    aa = Acsk()

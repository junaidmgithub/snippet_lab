import os
import urllib3
import logging
from tqdm import tqdm
from io import BytesIO

logger = logging.getLogger(__name__)
NO_PROGRESS_BAR = False


def download_zip(url: str) -> BytesIO:
    """Download data from url."""
    logger.warning('starting download.\n'
                   'Download may take a few minutes.')

    # disable warnings so that we don't need a cert.
    # see https://urllib3.readthedocs.io/en/latest/advanced-usage.html for more
    urllib3.disable_warnings()

    with urllib3.PoolManager() as http:
        # Get data from url.
        # set preload_content=False means using stream later.
        data = http.request('GET', url, preload_content=False)

        try:
            total_length = int(data.headers['content-length'])
        except (KeyError, ValueError, AttributeError):
            total_length = 0

        process_bar = tqdm(
            total=total_length,
            file=os.devnull if NO_PROGRESS_BAR else None,
        )

        # 10 * 1024
        _data = BytesIO()
        for chunk in data.stream(10240):
            _data.write(chunk)
            process_bar.update(len(chunk))
        process_bar.close()

    logger.warning('\ndownload done.')
    return _data


URL = 'https://storage.googleapis.com/chromium-browser-snapshots/Linux_x64/588429/chrome-linux.zip'
download_zip(URL)

import urllib.request
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed


class ThreadPoolWorker:

    def __init__(self, max_workers=5):
        self.pool = ThreadPoolExecutor(max_workers=max_workers)
        self.futures = list()

    def submit(self, func, *args, **kwargs):
        self.futures.append(self.pool.submit(func, *args, **kwargs))

    def map(self, func, *args, **kwargs):
        for _args in zip(*args):
            self.submit(func, *_args, **kwargs)

    def show_progress(self):
        process_bar = tqdm(total=len(self.futures))
        for _ in as_completed(self.futures):
            process_bar.update(1)
        process_bar.close()


def source_urls():
    urls = []
    for PAGE_NO in range(1, 39):
        BASE_URL = f'https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-{PAGE_NO}.html'
        urls.append(BASE_URL)
    return urls

URLS = source_urls()

def download_html(url):
    page_no = abs(int(url[-7:-5]))
    urllib.request.urlretrieve(url, f"{page_no}.html")


tpw = ThreadPoolWorker(max_workers=38)
tpw.map(download_html, URLS)
tpw.show_progress()

print('Done')

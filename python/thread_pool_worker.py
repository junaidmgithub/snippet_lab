import requests
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
        for future in as_completed(self.futures):
            #print(future.result())
            process_bar.update(1)
        process_bar.close()

# Test

img_urls = [
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623210949/download21.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211125/d11.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211655/d31.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212213/d4.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212607/d5.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623235904/d6.jpg',
]

def download_image(img_url):
    img_bytes = requests.get(img_url).content

tpw = ThreadPoolWorker()

# Usage 1
tpw.submit(download_image, img_urls[0])
# Usage 2
tpw.map(download_image, img_urls[1:])

tpw.show_progress()

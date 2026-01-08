import requests
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed


semaphore = threading.Semaphore(2)

def download_image(url, name):
    with semaphore:
        response = requests.get(url)
        with open(name, "wb") as f:
            f.write(response.content)
        return name


urls = [
        ("https://ru.pinterest.com/pin/860328335043004175/", "img1.png"),
        ("https://ru.pinterest.com/pin/320388961011668421/", "img2.png"),
        ("https://ru.pinterest.com/pin/1058557087429247986/", "img3.png"),
    ]

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [
        executor.submit(download_image, url, name)
        for url, name in urls
    ]

    for future in as_completed(futures):
        print("Загружен:", future.result())
from random import randint
from requests import get
from clint.textui import progress

def download_file(url, filename):
    with open(filename, 'wb') as f:
        r = get(url, stream=True,  headers={
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
            "Referer": "https://www.radiojavan.com/",
            "Host": "host2.rj-mw1.com"
        })
        total_length = int(r.headers['content-length'])
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()
        print("Finished")

url = input("Enter Url : ")

url = url.split("/")[5].split("?")[0]
download_file(
    f"https://host2.rj-mw1.com/media/mp3/mp3-128/{url}.mp3", f"{url}-{randint(0,10)}.mp3")

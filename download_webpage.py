import os
import sys
import re
import requests
from tqdm import tqdm
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from datetime import datetime

def savePage(url, date):
    def savenRename(soup, assetsFolder, session, url, tag, inner, total_size, bar):
        if not os.path.exists(assetsFolder):
            os.makedirs(assetsFolder)
        for res in soup.findAll(tag):
            if res.has_attr(inner):
                try:
                    filename, ext = os.path.splitext(os.path.basename(res[inner]))
                    filename = re.sub('\\W+', '', filename) + ext
                    fileurl = urljoin(url, res.get(inner))
                    filepath = os.path.join(assetsFolder, filename)
                    res[inner] = os.path.join(os.path.basename(assetsFolder), filename)
                    if not os.path.isfile(filepath): # was not downloaded
                        with open(filepath, 'wb') as file:
                            filebin = session.get(fileurl, stream=True)
                            for data in filebin.iter_content(chunk_size=1024):
                                bar.update(len(data))
                                file.write(data)
                except Exception as exc:
                    pass
    
    session = requests.Session()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    response = session.get(url, headers=headers, stream=True)

    redirect_url = response.url
    date_time_part = redirect_url.split('/')[-5]
    parsed_datetime = datetime.strptime(date_time_part, '%Y%m%d%H%M%S')
    formatted_datetime = parsed_datetime.strftime('%Y-%m-%d %H:%M:%S')
    folder_datetime = parsed_datetime.strftime('%Y_%m_%d_%H_%M_%S')

    input_url_part = url.split('/')[-2]
    input_time = input_url_part[8:]

    if url != response.url and input_time != "000000":
        print(f'The snapshot for that time doesn\'t exist. Downloading snapshot: {formatted_datetime} instead.')
    
    
    soup = BeautifulSoup(response.text, "html.parser")

    current_dir = os.getcwd()
    formatted_date = datetime.strptime(date, '%Y%m%d').strftime('%Y-%m-%d')
    url_folder_name = url.split('/')[-1].replace('/', '_')
    downloadFolder = os.path.join(current_dir, 'Downloads', url_folder_name, folder_datetime)
    assetsFolder = os.path.join(downloadFolder, 'Assets')

    if os.path.exists(downloadFolder):
        print(f"The snapshot '{formatted_date}' for URL '{url}' already exists. You can find the webpage at {downloadFolder}")
        return

    total_size = int(response.headers.get('content-length', 0))
    # print(url)
    with tqdm(total=total_size, unit='B', unit_scale=True, desc=f'Downloading Snapshot ({formatted_datetime})', ncols=80) as bar:
        tags_inner = {'img': 'src', 'redirect_url': 'href', 'script': 'src'}
        for tag, inner in tags_inner.items():
            savenRename(soup, assetsFolder, session, url, tag, inner, total_size, bar)
        with open(os.path.join(downloadFolder, f'{formatted_date}.html'), 'wb') as file:
            file.write(soup.prettify('utf-8'))

    print(f"Download finished. You can find the snapshot at {downloadFolder}")


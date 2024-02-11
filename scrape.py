import re
import os
import time
import requests
from prettytable import PrettyTable, ALL
from requests_html import HTMLSession
from datetime import datetime
from bs4 import BeautifulSoup

def scrape(search_url, cond=None):
    session = HTMLSession()
    if cond == 'New':
        url = f'https://web.archive.org/web/20240000000000*/{search_url}'
    else:
        url = search_url
    try:
        response = session.get(url)
        response.html.render(sleep=6, timeout=50)
        session.close()
        return response

    except Exception as e:
        print(f"An error occurred: {e}")
        session.close()
        return None

def termResults(response):
    if response is not None:
        table = PrettyTable(["Link", "Desc", "Web Pages", "Images", "Audio", "VID/GIF"])
        links = response.html.find('.result-item-heading')
        descs = response.html.find('.snippet')
        url_types = response.html.find('.urls-types')
        types = [element.find('b') for element in url_types]
        for link, desc, numbers in zip(links, descs, types):
            table.add_row([link.text, desc.text] + [web.text for web in numbers[::4]] + [img.text for img in numbers[1::4]] + [aud.text for aud in numbers[2::4]] + [vid.text for vid in numbers[3::4]])
        
        print(table)
        
def getInfo(response):
    if response is not None:
        result_details_elements = response.html.find('.captures-range-info')

        for info_element in result_details_elements:
            info_text = info_element.text
            return info_text

def month_name_to_number(month_name):
    try:
        date_object = datetime.strptime(month_name, "%B")
    except ValueError:
        date_object = datetime.strptime(month_name, "%b")
    return date_object.month

def is_between_dates(start_date, check_date, end_date):
    if start_date <= check_date <= end_date:
        return True
    else:
        return False

def makeUrl(info, url, date, time):
    parts = info.split('between')

    if len(parts) == 2:
        date_range = parts[1].split('and')
        start_date = date_range[0].strip()
        end_date = date_range[1].strip()

        start_parts = start_date.split(' ')
        start_year = int(start_parts[-1])
        start_month = int(month_name_to_number(start_parts[0][:3].upper()))
        start_day = int(start_parts[1].rstrip(','))
        start_date_full = int(f"{start_year:04d}{start_month:02d}{start_day:02d}")

        end_parts = end_date.split(' ')
        end_year = int(end_parts[-1].rstrip('.'))
        end_month = int(month_name_to_number(end_parts[0][:3].upper()))
        end_day = int(end_parts[1].rstrip(','))
        end_date_full = int(f"{end_year:04d}{end_month:02d}{end_day:02d}")

    if date:
        checkDate = is_between_dates(start_date_full, int(date), end_date_full)

        if checkDate is True:
            if time:
                snapshot_url = f'https://web.archive.org/web/{date}{time}/{url}'
            else:
                snapshot_url = f'https://web.archive.org/web/{date}000000/{url}'
            return snapshot_url
        else:
            print("Date Invalid.")

def find(terms, url):
    table = PrettyTable(["Matches"])
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pattern = re.compile(r'>\s*(.*?)\s*<')
    matches = [match.group(1).strip() for match in pattern.finditer(str(soup))]
    result_matches = {term: [match for match in matches if term in match] for term in terms}

    for term, term_matches in result_matches.items():
        if term_matches:
            print(f'\nMatches for "{term}":')
            for match in term_matches:
                print(f'• {match}')
        else:
            print(f'\nNo matches found for "{term}".')






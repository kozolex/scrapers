import time
import requests
from slugify import slugify
from bs4 import BeautifulSoup


class PageScrapper:

    def __init__(self, url):

        self.url = url
        self.last_page = self.get_last_page_number()

        print(f"Total number of pages: {self.last_page}")

    def get_last_page_number(self):
        #page = self.read_page_content(self.url)
        #last_page_element = page.find("a", {"title": "ostatnia strona"})
        return int(2)

    def find_advertisements(self):

        for page_number in range(self.last_page + 1):

            print(f"Page {page_number+1}/{self.last_page} processing...")

            page = self.read_page_content(self.url + str(page_number))
            advertisements = page.findAll("a", {"class": "text-lg text-primary"})

            data = self.parse_advertisement(advertisements)
            print(data)
            time.sleep(1)

    def parse_advertisement(self, url):

        data = {}

        page = self.read_page_content(url)
        container = page.find('div', {'class': 'card-body '})

        data['nazwa'] = container.find('a', {'class': 'text-lg text-primary '}).get_text().strip()
        #data['email'] = container.find('div', {'class': 'class="col-lg-4"'}).get_text().strip()
        #data['typ'] = container.find('div', {'class': 'col-lg-4 col-md-6'}).get_text()


        return data

    def read_page_content(self, url):
        page = requests.get(url)
        return BeautifulSoup(page.content, "html.parser")


URL = 'https://rspo.men.gov.pl/?rspo_search_criteria%5Bregon%5D=&rspo_search_criteria%5Brspo%5D=&rspo_search_criteria%5Bwojewodztwo%5D=14&rspo_search_criteria%5Bpowiat%5D=&rspo_search_criteria%5Bgmina%5D=&rspo_search_criteria%5Bmiejscowosc%5D=&rspo_search_criteria%5Bop_typ%5D=&rspo_search_criteria%5Bop_wojewodztwo%5D=&rspo_search_criteria%5Bop_powiat%5D=&rspo_search_criteria%5Bop_gmina%5D=&rspo_search_criteria%5Borgan%5D=&rspo_search_criteria%5Bor_typ%5D=&rspo_search_criteria%5Bor_wojewodztwo%5D=&rspo_search_criteria%5Bor_powiat%5D=&rspo_search_criteria%5Bor_gmina%5D=&rspo_search_criteria%5Brejestrujacy%5D=&rspo_search_criteria%5Btyp%5D%5B%5D=14&rspo_search_criteria%5Btyp%5D%5B%5D=15&rspo_search_criteria%5Btyp%5D%5B%5D=19&rspo_search_criteria%5Btyp%5D%5B%5D=16&rspo_added%5Bzawod%5D=&rspo_added%5Bspecjalnosc%5D=&rspo_added%5Bspecjalizacja%5D=&rspo_search_criteria%5Bsearch%5D='
scraper = PageScrapper(URL)
scraper.find_advertisements()

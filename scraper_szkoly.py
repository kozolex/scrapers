import time
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
#war-maz
my_url = 'https://rspo.men.gov.pl/?rspo_search_criteria%5Bregon%5D=&rspo_search_criteria%5Brspo%5D=&rspo_search_criteria%5Bwojewodztwo%5D=14&rspo_search_criteria%5Bpowiat%5D=&rspo_search_criteria%5Bgmina%5D=&rspo_search_criteria%5Bmiejscowosc%5D=&rspo_search_criteria%5Bop_typ%5D=&rspo_search_criteria%5Bop_wojewodztwo%5D=&rspo_search_criteria%5Bop_powiat%5D=&rspo_search_criteria%5Bop_gmina%5D=&rspo_search_criteria%5Borgan%5D=&rspo_search_criteria%5Bor_typ%5D=&rspo_search_criteria%5Bor_wojewodztwo%5D=&rspo_search_criteria%5Bor_powiat%5D=&rspo_search_criteria%5Bor_gmina%5D=&rspo_search_criteria%5Brejestrujacy%5D=&rspo_search_criteria%5Btyp%5D%5B0%5D=14&rspo_search_criteria%5Btyp%5D%5B1%5D=15&rspo_search_criteria%5Btyp%5D%5B2%5D=19&rspo_search_criteria%5Btyp%5D%5B3%5D=16&rspo_search_criteria%5Bsearch%5D=&rspo_added%5Bzawod%5D=&rspo_added%5Bspecjalnosc%5D=&rspo_added%5Bspecjalizacja%5D=&sort=dzialalnosc.nazwa&direction=asc&page='
#podlasie
my_url = 'https://rspo.men.gov.pl/?rspo_search_criteria%5Bregon%5D=&rspo_search_criteria%5Brspo%5D=&rspo_search_criteria%5Bwojewodztwo%5D=10&rspo_search_criteria%5Bpowiat%5D=&rspo_search_criteria%5Bgmina%5D=&rspo_search_criteria%5Bmiejscowosc%5D=&rspo_search_criteria%5Bop_typ%5D=&rspo_search_criteria%5Bop_wojewodztwo%5D=&rspo_search_criteria%5Bop_powiat%5D=&rspo_search_criteria%5Bop_gmina%5D=&rspo_search_criteria%5Borgan%5D=&rspo_search_criteria%5Bor_typ%5D=&rspo_search_criteria%5Bor_wojewodztwo%5D=&rspo_search_criteria%5Bor_powiat%5D=&rspo_search_criteria%5Bor_gmina%5D=&rspo_search_criteria%5Brejestrujacy%5D=&rspo_search_criteria%5Btyp%5D%5B0%5D=14&rspo_search_criteria%5Btyp%5D%5B1%5D=15&rspo_search_criteria%5Btyp%5D%5B2%5D=19&rspo_search_criteria%5Btyp%5D%5B3%5D=16&rspo_search_criteria%5Bsearch%5D=&rspo_added%5Bzawod%5D=&rspo_added%5Bspecjalnosc%5D=&rspo_added%5Bspecjalizacja%5D=&sort=dzialalnosc.nazwa&direction=asc&page='
#pomorze
my_url ='https://rspo.men.gov.pl/?rspo_search_criteria%5Bregon%5D=&rspo_search_criteria%5Brspo%5D=&rspo_search_criteria%5Bwojewodztwo%5D=11&rspo_search_criteria%5Bpowiat%5D=&rspo_search_criteria%5Bgmina%5D=&rspo_search_criteria%5Bmiejscowosc%5D=&rspo_search_criteria%5Bop_typ%5D=&rspo_search_criteria%5Bop_wojewodztwo%5D=&rspo_search_criteria%5Bop_powiat%5D=&rspo_search_criteria%5Bop_gmina%5D=&rspo_search_criteria%5Borgan%5D=&rspo_search_criteria%5Bor_typ%5D=&rspo_search_criteria%5Bor_wojewodztwo%5D=&rspo_search_criteria%5Bor_powiat%5D=&rspo_search_criteria%5Bor_gmina%5D=&rspo_search_criteria%5Brejestrujacy%5D=&rspo_search_criteria%5Btyp%5D%5B0%5D=14&rspo_search_criteria%5Btyp%5D%5B1%5D=15&rspo_search_criteria%5Btyp%5D%5B2%5D=19&rspo_search_criteria%5Btyp%5D%5B3%5D=16&rspo_search_criteria%5Bsearch%5D=&rspo_added%5Bzawod%5D=&rspo_added%5Bspecjalnosc%5D=&rspo_added%5Bspecjalizacja%5D=&sort=dzialalnosc.nazwa&direction=asc&page='

#kuj-pom
my_url ='https://rspo.men.gov.pl/?rspo_search_criteria%5Bregon%5D=&rspo_search_criteria%5Brspo%5D=&rspo_search_criteria%5Bwojewodztwo%5D=2&rspo_search_criteria%5Bpowiat%5D=&rspo_search_criteria%5Bgmina%5D=&rspo_search_criteria%5Bmiejscowosc%5D=&rspo_search_criteria%5Bop_typ%5D=&rspo_search_criteria%5Bop_wojewodztwo%5D=&rspo_search_criteria%5Bop_powiat%5D=&rspo_search_criteria%5Bop_gmina%5D=&rspo_search_criteria%5Borgan%5D=&rspo_search_criteria%5Bor_typ%5D=&rspo_search_criteria%5Bor_wojewodztwo%5D=&rspo_search_criteria%5Bor_powiat%5D=&rspo_search_criteria%5Bor_gmina%5D=&rspo_search_criteria%5Brejestrujacy%5D=&rspo_search_criteria%5Btyp%5D%5B0%5D=14&rspo_search_criteria%5Btyp%5D%5B1%5D=15&rspo_search_criteria%5Btyp%5D%5B2%5D=19&rspo_search_criteria%5Btyp%5D%5B3%5D=16&rspo_search_criteria%5Bsearch%5D=&rspo_added%5Bzawod%5D=&rspo_added%5Bspecjalnosc%5D=&rspo_added%5Bspecjalizacja%5D=&sort=dzialalnosc.nazwa&direction=asc&page='
data = {}

#file CSV
filename = 'szkoly_kujaw_pom.csv'
f = open(filename, 'w')
heders = 'nazwa,email,www,typ,miasto\n'
f.write (heders)

for number_page in range(1, 62):

    #Client
    URL = my_url+str(number_page)
    uClient = uReq(URL)
    #print(URL)
    page_html = uClient.read()

    #html parser
    page_soup = soup(page_html, 'html.parser')
    pages = 40

    containers = page_soup.findAll('div', {'class': 'card-body'})
    print(len(containers))

    #container = containers[1]
    for id in range(1, len(containers)):
        name = containers[id].find('a', {'class': 'text-lg text-primary'}).get_text().replace("\n", "")
        email = containers[id].findAll('div', {'class': 'col-lg-4'})[4].text.replace(" ", "").replace("\n", "")
        www = containers[id].findAll('div', {'class': 'col-lg-4'})[5].text.replace(" ", "").replace("\n", "")
        school_type = containers[id].findAll('div', {'class': 'col-lg-4'})[6].text.replace('Typ: ', '').replace("\n", "")
        city = containers[id].findAll('div', {'class': 'col-lg-12'})[1].text.strip().replace(" ", ""). split()[-1].replace("\n", "")

        result = name + ',' + email + ',' + www + ',' + school_type + ',' + city + '\n'
        #print(name)
        f.write(result)

    #time.sleep(1)
f.close
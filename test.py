import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup

link = "https://forum.mir4global.com/rank?ranktype=1&worldgroupid=22&worldid=137&classtype=&searchname=&loaded=1"

with webdriver.Chrome() as driver:
    driver.get(link)

    # datalist = []
    
    # show_more = driver.find_element(by=By.ID, value="btn_morelist")
    show_more = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btn_morelist")))
    driver.execute_script("arguments[0].click();",show_more)

    # for elem in driver.find_elements(by=By.CLASS_NAME, value="ranking_table"):
    for elem in WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "ranking_table"))):
        data = [item.text for item in elem.find_elements(by=By.CLASS_NAME, value="text_right")]
        # datalist.append(data)
        print(data)

# df = pandas.DataFrame(datalist)
# print(df)

# r = requests.get('https://forum.mir4global.com/rank?ranktype=1&worldgroupid=22&worldid=137&classtype=&searchname=&loaded=1')
# soup = BeautifulSoup(r.text, 'html.parser')

# league_table = soup.find('table', class_ = 'ranking_table')

# for team in league_table.find_all('tbody'):
#     rows = team.find_all('tr')
#     for row in rows:
#         pl_team = row.find('td', class_ ='text_right')
#         # pl_team = pl_team['data-long-name']
#         # points = row.find_all('td', class_ = 'standing-table__cell')[9].text
#         # print(pl_team, points)
#         print(pl_team)

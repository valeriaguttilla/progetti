import WebdriverWrapper
import random
import csv
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def main():
    movies = []
    wait_duration = 4  # seconds
    min_wait = 10  # seconds
    max_wait = 20  # seconds

    search_result = 0  # 0: single sub, 1: many movies, 2: many languages

    with open(
        "movies.csv",
        'r',
        newline="",
        encoding="utf-8"
    ) as fh:
        r = csv.reader(fh, delimiter=';', quotechar='"')

        while (True):
            row = next(r, None)
            if row is None:
                print("EOF")
                break
            movies.append(row[0].lower() + ' (' + row[1] + ')')

    wdw = WebdriverWrapper.WebdriverWrapper()
    driver = wdw.get_driver()
    target_url = 'https://www.opensubtitles.org/en/search/subs'

    not_found_list = []
    language_not_found = []
    count = 0

    driver.get(target_url)

    for movie in movies:
        count += 1
        search_result = 0  # 0: single sub, 1: many movies, 2: many languages
        print(count, ") ", movie)

        search_text_elem = driver.find_element_by_css_selector("#search_text")
        search_text_elem.clear()
        search_text_elem.send_keys(movie)

        submit_elem = driver.find_element_by_css_selector("#search_submit")
        print("search...")
        time.sleep(random.randint(min_wait, max_wait))
        submit_elem.submit()

        # search results

        # check result: many or only one
        many = False
        results_table_elem = driver.create_web_element(1)
        try:
            results_table_elem = WebDriverWait(driver, wait_duration).until(
                EC.visibility_of_element_located(
                    (By.ID, "search_results")
                )
            )
            many = True
        except  NoSuchElementException:  # only one
            pass
        except TimeoutException:
            pass

        if many:  # check: many movies or many languages
            firt_row_th_elems = results_table_elem.find_elements_by_css_selector("tr:first-child > th")

            if (firt_row_th_elems[1].get_attribute("class") == "head"):  # many movies
                search_result = 1
            else:  # many languages
                search_result = 2

        # case 1: many movies
        if search_result == 1:  # find the exact match
            found = False
            href = ''
            result_elems = driver.find_elements_by_css_selector("strong > a")
            for e in result_elems:
                if (e.text.replace('\n', ' ').lower() == movie):  # check
                    found = True
                    href = e.get_attribute("href")
                    # print("first result elem:", href)
                    break

            # many results but not contain what searched
            if (not found):
                not_found_list.append(movie)
                print("movie NOT FOUND")
                continue

            if href != '':
                print("get exact match page...")
                time.sleep(random.randint(min_wait, max_wait))
                driver.get(href)  # go to case 2

                try:
                    results_table_elem = WebDriverWait(driver, wait_duration).until(
                        EC.visibility_of_element_located(
                            (By.ID, "search_results")
                        )
                    )
                    search_result = 2
                except NoSuchElementException:
                    search_result = 0
                except TimeoutException:
                    search_result = 0

        # case 2: many languages
        if search_result == 2:
            sub_lang_elems = results_table_elem.find_elements_by_css_selector("tr")
            english_found = False
            href = ''
            for i in sub_lang_elems:
                try:
                    eng_elem = i.find_element_by_css_selector("a[title=English]")
                    href_elem = i.find_element_by_css_selector("strong > a")
                    href = href_elem.get_attribute("href")
                    english_found = True
                    break
                except NoSuchElementException:
                    pass

            if (not english_found):
                language_not_found.append(movie)
                print("English sub NOT FOUND")
                continue

            print("get eng sub page...")
            time.sleep(random.randint(min_wait, max_wait))
            driver.get(href)

        # case 0: subtitle page
        try:
            sub_elem = driver.find_element_by_css_selector("#moviehash > a")
            print("download...")
            time.sleep(random.randint(min_wait, max_wait))
            sub_elem.click()
        except NoSuchElementException:
            print("Error on finding download link ")

    print("Movies NOT FOUND:", not_found_list)
    print("Eng subs NOT FOUND:", language_not_found)
    return


if __name__ == "__main__":
    main()
import csv
from selenium import webdriver
from time import sleep
from random import uniform
from selenium.common.exceptions import NoSuchElementException


target_url = 'https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films'


print("Open a browser and navigate to {0} ...".format(target_url))



driver = webdriver.Chrome('/Users/valeriaguttilla/Desktop/MASTER/_Tools/chromedriver')
driver.get(target_url)

print("Retrieving the country page URLs...")

movies = driver.find_elements_by_css_selector('table.sortable > tbody > tr')
print(len(movies))

list_movies =[]
movies_non_l =[]
for thing in movies:
    element = thing.find_elements_by_css_selector('td')
    print(element)
    if len(element)>0:
        try:
            label = element[0].find_element_by_css_selector('small').text
            title = element[1].find_element_by_css_selector('i > a')
            url = title.get_attribute('href')
            titlestr = title.text
            list_movies.append([str(label), str(titlestr), url])
            #print(label, titlestr, url)
        except NoSuchElementException:
            pass

for i in range (300, len(list_movies)):

    if list_movies[i][0] == 'L': #or list_movies[i][0] == 'L':
        with open("{}.csv".format(str(list_movies[i][1])), "w", encoding="utf-8") as handle:
            file_writer = csv.writer(handle, delimiter=' ')
            print('.......finding plot movie {}.......'.format(list_movies[i][1]))
            target_url = (list_movies[i][2])
            driver = webdriver.Chrome('/Users/valeriaguttilla/Desktop/MASTER/_Tools/chromedriver')
            driver.get(target_url)
            movies = driver.find_elements_by_css_selector('div.mw-parser-output > *')
            plot = ''
            found = False
            for thing in movies:
                if found == False:
                    result_elements = thing.find_elements_by_id('Plot')
                    if len(result_elements) <= 0:
                        continue
                    else:
                        found = True

                else:
                    if thing.tag_name == 'p':
                        plot += (thing.text + ' ')

                    else:
                        break
            file_writer.writerow(plot.split())
    #
    #
    # else:
    #     movies_non_l.append(list_movies[i][1])
        print('movie {} not in category'.format(list_movies[i][1]))
        continue



print(movies_non_l)



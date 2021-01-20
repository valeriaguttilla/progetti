from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import *
import random
import string
from sys import exit


def stripURL(original_url):
    parsed_original_url = urlparse(original_url)
    stripped_url = parsed_original_url.netloc
    return(str(stripped_url))


def randomString(stringLength=5):
    letters = string.ascii_lowercase
    return ''.join(random.sample(letters, stringLength))



def check_opening_url(url_to_be_checked):
    u_open = urlopen(str(url_to_be_checked))
    if u_open.status == 200:
        return (1)
    else:
        return (2)




dictionary_urls = {}

while True:
    try:
        x = input ("\n\nIf you have an URL and you want its shortened version select 1, "
                   "if you already have the shortened version of an URL and you would like to go to the corresponding website press 2, to terminate the program press any other key   ")
        if x == '1':
            original_url = input("Write the URL    ")
            opening_status=check_opening_url(original_url)
            if opening_status == 1:
                    print("\n\nVery well, the URL is working. Wait to get the shortened version")
                    print('Working.......\n')

                    if original_url in dictionary_urls.values():
                        for key, value in dictionary_urls.items():
                            if str(original_url) == str(value):
                                print("URL already in our database. Shortened URL:   ", key)
                    else:
                        stripped_url = stripURL(original_url)
                        final_url = stripped_url + '/' + randomString()
                        dictionary_urls[final_url] = original_url
                        print('Your final URL is: {}'.format(final_url))




        elif x == '2':
            original_url = (input("Write the URL    "))
            if original_url in dictionary_urls.keys():
                print('URL already in our database, here is the original version:  ', dictionary_urls[original_url])
            else:
                print("Error 404: URL not in our database!")
                continue

            x2 = input('If you want to start again press 1, to end the program press any other key.')
            if x2 == '1':
                continue
            else:
                print('\n\nClosing the program...\n')
                print('Goodbye!')
                exit()

        else:
            print("See you soon!")
            exit()

    except ValueError:
        print("Error 404. The URL is not working, please try again.")
        continue
    except HTTPError:
        print("Error 404. The URL is not working, please try again.")
        continue
    except URLError:
        print("Error 404. The URL is not working, please try again.")
        continue




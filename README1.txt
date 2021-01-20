

**Describe the algorithm you used to shorten the URL in a short comment at the beginning of your code**


To shorten a URL the function urlparse can be used. It comes from urllib, an extensible library for working with URLs and what it does is splitting the URL into its six different components: scheme://netloc/path;parameters?query#fragment. 

-parsed_original_url = urlparse(original_url)

Since we’re interested in the part of the URL comprised between the http or https, the scheme and before the path, we can select it with the .netloc. 

-stripped_url = parsed_original_url.netloc

I deemed it easier to write a function to shorten URLs. The function takes an URL and returns its shortened version, as explained above. 

def stripURL(original_url):
    parsed_original_url = urlparse(original_url)
    stripped_url = parsed_original_url.netloc
    return(str(stripped_url))

****************************************



** The basic reasoning behind the code: 

The code either takes a URL and gives the user the shortened version or the other way around. 


** How it actually works:

The code starts by defining two other functions, along with the first one previously presented.

One function allows to add 5 ascii lowercase random letters to a string.


def randomString(stringLength=5):
    letters = string.ascii_lowercase
    return ''.join(random.sample(letters, stringLength))


Another checks whether the URL provided is actually working, once again taking the function urlopen from the urllib extensible library. Since the code returned when a URL is working is the 200, the check is made on that value. Returning 1 in case the URL works and 2 in case it doesn't can be later used in the main part of the code, when the function is called. 


def check_opening_url(url_to_be_checked):
    u_open = urlopen(str(url_to_be_checked))
    if u_open.status == 200:
        return (1)
    else:
        return (2)



The code starts by asking the customer whether he/she wants a shortened version of an URL or already has a shortened version and wants the original form.

        x = input ("\n\nIf you have an URL and you want its shortened version select 1, "
                   "if you already have the shortened version of an URL and you would like to go to the corresponding website press 2, to terminate the program press any other key")

	** If the customer has the original form, in order to provide the simplified version, the code first checks if the URL is actually working, with the function check_opening_url previously defined. 

if x == '1':
            original_url = input("Write the URL    ")
            opening_status=check_opening_url(original_url)
            if opening_status == 1:
                    print("\n\nVery well, the URL is working. Wait to get the shortened version")
                    print('Working.......\n')



Note that exceptions are risen if the URL provided is not written in the right format or it's not possible to open it. 


    except ValueError:
        print("Error 404. The URL is not working, please try again.")
        continue
   except HTTPError:
        print("Error 404. The URL is not working, please try again.")
        continue
  except URLError:
        print("Error 404. The URL is not working, please try again.")
        continue



After checking the URL is working another check is made to ensure the URL is not already in the database. The database is formed by a dictionary, named dictionary_urls and where both the original URL and the shortened version are added every time a new URL is entered and its shortened version created. Note that in the dictionary the original URL works as the value and the shortened version as the key. 
*In case the URL written by the user is in the database/dictionary, the already-generated shortened URL is provided.


  if original_url in dictionary_urls.values():
                        for key, value in dictionary_urls.items():
                            if str(original_url) == str(value):
                                print("URL already in our database. Shortened URL:   ", key)


*In case the URL was not already in the database a new one is created, given to the user and added to the dictionary. 



   else:
                        stripped_url = stripURL(original_url)
                        final_url = stripped_url + '/' + randomString()
                        dictionary_urls[final_url] = original_url
                        print('Your final URL is: {}'.format(final_url))





	** If the customer has the shortened version of an URL and wants the original form, the code checks whether the shortened URL is saved as a key in the dictionary and in case it is the user is given the original URL. 



 elif x == '2':
            original_url = (input("Write the URL    "))
            if original_url in dictionary_urls.keys():
                print('URL already in our database, here is the original version:  ', dictionary_urls[original_url])



In case the shortened URL is not present in the dictionary the user is asked whether he/she prefers to terminate the program of provide another URL.
 

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



****************************************

**FULL CODE**



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



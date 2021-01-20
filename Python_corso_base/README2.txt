
** The basic reasoning behind the code: 

A customer should be able to upload a quiz or play with one. The quiz repository starts empty and allows users to play only when a quiz is uploaded. 


** How it actually works:

It starts by defining two functions which will be extremely useful in the main code. 


1) 


The first one is to allow users to upload a quiz: def insert_quiz()


-First users are reminded that files need to have specific requirements:

            user_file = input("\n\nATTENTION: \n\n1)check that the file is in the app's directory \n\n2)check it is in a JSON format  "
                                "\n\n3)check the JSON has the following format:"
                                "\n\n{\nquestion: 'this is my questiion'\nA: apple\nB: banana\nC: carrot\nD: donuts\n}\n\nWrite the name of your file   ")

-The file uploaded by the user is then opened and read with the loads method to read JSON files. The method reads the string from the file, parses the JSON data and populates a dictionary. 

quizfile_file = open(user_file)
            quizfile_str = quizfile_file.read()
            quizfile_data = json.loads(quizfile_str)


-In order to check that the file is in the correct format an example is provided, which will be checked against the user's uploaded file.

dictionary_example = {'question': '1', 'A': '2', 'B': '3', 'C': '4', 'D': '5', 'answer': '6', 'scores': '7'}
          
-The file is checked in its entirety and in case is not provided in the right format, the user is asked whether he/she wants to upload another one or terminate the program.


    file_not_ok = 0
            for m in range(1, len(quizfile_data)):
                if (quizfile_data[m].keys()) != dictionary_example.keys():
                    file_not_ok = (input(print(
                        "\n\n File is not in the right format!\n\nThe file needs to be structured as follows:"
                        "\n'question', 'A', 'B', 'C', 'D', 'answer', 'scores'"
                        "\n\n{\nquestion: 'this is my questiion'\nA: apple\nB: banana\nC: carrot\nD: donuts\n}"
                        "\n\n""Do you have another file? Press 1 to go back to the main menu or any other key to exit the program")))
                    if file_not_ok == '1':
                        break
                    else:
                        print('\n\nSee you soon!')
                        exit()



-If the format is correct then the file is uploaded as a dictionary and added to the variable named quizfile_data.



else:
                    print('Very well, file correctly uploaded!')
                    return quizfile_data




-Exceptions are risen in case the file is not a JSON or is not found in the directory where the app (the Python's coding file) is.



  except ValueError:
            print('File format is not a JSON.\nIf you have a JSON file, try again!')
            exit()
  except FileNotFoundError:
            print("File not found. It needs to be in the same directory as the app.\nCheck again!")
            exit()




2) 


The second function allows the user to actually play: def quiz_game. Note that it takes as argument the uploaded file from function 1). 



-The quiz presents the user with 10 questions randomly polled from the ones in the file.



   for d in range(1, 11):
            random_number = (randint(1, len(quizfile_data)))



-It specifies which in the file is the question and which the multiple-choice answers, so as to present them to the user playing. 


	    question = (quizfile_data[random_number]['question'])
            answ_a = (quizfile_data[random_number]['A'])
            answ_b = (quizfile_data[random_number]['B'])
            answ_c = (quizfile_data[random_number]['C'])
            answ_d = (quizfile_data[random_number]['D'])
            print("'Question {}: {} \n Answer A: {} \n Answer B: {} \n Answer C:{} \n Answer D:{}".format(d, question ,answ_a, answ_b, answ_c, answ_d))




-It then asks the user for an answer, allowing him/her to choose between A,B,C or D. 

            user_answer = input('A, B, C o D? ')



-If the user answered correctly the game tells him/her and prints the right answer and adds the scores for the question to the total scores for the game. Note that for simplicity the letter provided by the user as the answers are considered case insensitively.


            if user_answer.lower() == ((quizfile_data[random_number]['answer']).lower()):
                print('\nThe answer is correct: ',(quizfile_data[random_number]['answer']))
                scores += (quizfile_data[random_number]['scores'])



-The user is also informed about how many points he/she was given for having answered correctly.


                if quizfile_data[random_number]['scores'] == 1:
                    print('Very well, this question was worthed one point!\n\n')
                else:
                    print('Very well, this question was worthed {} points!\n\n'.format(quizfile_data[random_number]['scores']))



-In case the answer was wrong, the right answer is still displayed and the game keeps going.

            else:
                print('\nWrong answer!\nThe correct answer was:  {}\n\n'.format(quizfile_data[random_number]['answer']))




-At the end of the game, after having answered the 10 questions, the user is given the final score.


        if scores == 0:
            print("You didn't get any point, try again!")
        elif scores == 1:
            print('\n\nYou scored one point!\n\n')
        else:
            print('\n \nWell done, you scored {} points!\n\n'.format(scores))
        user_input = input('To start again press enter, to exit press u\n\n')
        if user_input == 'u':
            print('\n\nGoodbye!')
            exit()





** The main code asks the user whether he/she wants to upload a quiz, play one or exit the program


user_type = int(input('If you have a quiz and you want to upload it press 1, to play press 2, to exit press 2   '))


-If the user wants to upload a game, function 1 is called


if user_type == 1:
            quizfile_data=insert_quiz()


-If the user wants to play a game function 2 is called and if there are no quizzes already available an error message is printed and the user is redirected to the beginning.


elif user_type == 2:
            if len(quizfile_data) == 0:
                print('Unfortunately there are no games at this moment in our database! Do you have a quiz and you want to upload it?')


-If the user wants to quit then the application exits. 


        elif user_type == 3:
            print('\n\nSee you soon!')
            exit()


-In case the users writes a number different from 1,2,3 or selects any other keys he/she is asked to try again. 

        else:
            print('You have to choose between 1,2 and 3. Try again!')
            continue
    except ValueError:
        print('You have to choose between 1,2 and 3. Try again!')
        continue



****************************************

**FULL CODE**


import sys
import json
from random import randint


def insert_quiz():

    while True:
        try:
            user_file = input("\n\nATTENTION: \n\n1)check that the file is in the app's directory \n\n2)check it is in a JSON format  "
                                "\n\n3)check the JSON has the following format:"
                                "\n\n{\nquestion: 'this is my questiion'\nA: apple\nB: banana\nC: carrot\nD: donuts\n}\n\nWrite the name of your file   ")

            quizfile_file = open(user_file)
            quizfile_str = quizfile_file.read()
            quizfile_data = json.loads(quizfile_str)

            dictionary_example = {'question': '1', 'A': '2', 'B': '3', 'C': '4', 'D': '5', 'answer': '6', 'scores': '7'}
            file_not_ok = 0

            for m in range(1, len(quizfile_data)):
                if (quizfile_data[m].keys()) != dictionary_example.keys():
                    file_not_ok = (input(print(
                        "\n\n File is not in the right format!\n\nThe file needs to be structured as follows:"
                        "\n'question', 'A', 'B', 'C', 'D', 'answer', 'scores'"
                        "\n\n{\nquestion: 'this is my questiion'\nA: apple\nB: banana\nC: carrot\nD: donuts\n}"
                        "\n\n""Do you have another file? Press 1 to go back to the main menu or any other key to exit the program")))
                    if file_not_ok == '1':
                        break
                    else:
                        print('\n\nSee you soon!')
                        exit()
                else:
                    print('Very well, file correctly uploaded!')
                    return quizfile_data
            if file_not_ok == '1':
                break

        except ValueError:
            print('File format is not a JSON.\nIf you have a JSON file, try again!')
            exit()
        except FileNotFoundError:
            print("File not found. It needs to be in the same directory as the app.\nCheck again!")
            exit()
    return quizfile_data


def quiz_game(quizfile_data):
    user_input = ''
    while user_input != 'u':
        scores = 0
        for d in range(1, 11):
            random_number = (randint(1, len(quizfile_data)))
            question = (quizfile_data[random_number]['question'])
            answ_a = (quizfile_data[random_number]['A'])
            answ_b = (quizfile_data[random_number]['B'])
            answ_c = (quizfile_data[random_number]['C'])
            answ_d = (quizfile_data[random_number]['D'])
            print("'Question {}: {} \n Answer A: {} \n Answer B: {} \n Answer C:{} \n Answer D:{}".format(d, question ,answ_a, answ_b, answ_c, answ_d))

            user_answer = input('A, B, C o D? ')
            if user_answer.lower() == ((quizfile_data[random_number]['answer']).lower()):
                print('\nThe answer is correct: ',(quizfile_data[random_number]['answer']))
                scores += (quizfile_data[random_number]['scores'])
                if quizfile_data[random_number]['scores'] == 1:
                    print('Very well, this question was worthed one point!\n\n')
                else:
                    print('Very well, this question was worthed {} points!\n\n'.format(quizfile_data[random_number]['scores']))
            else:
                print('\nWrong answer!\nThe correct answer was:  {}\n\n'.format(quizfile_data[random_number]['answer']))
        if scores == 0:
            print("You didn't get any point, try again!")
        elif scores == 1:
            print('\n\nYou scored one point!\n\n')
        else:
            print('\n \nWell done, you scored {} points!\n\n'.format(scores))
        user_input = input('To start again press enter, to exit press u\n\n')
        if user_input == 'u':
            print('\n\nGoodbye!')
            exit()


quizfile_data={}


while True:
    try:
        user_type = int(input('If you have a quiz and you want to upload it press 1, to play press 2, to exit press 2   '))
        if user_type == 1:
            quizfile_data=insert_quiz()
        elif user_type == 2:
            if len(quizfile_data) == 0:
                print('Unfortunately there are no games at this moment in our database! Do you have a quiz and you want to upload it?')
                continue
            else:
                quiz_game(quizfile_data)
        elif user_type == 3:
            print('\n\nSee you soon!')
            exit()
        else:
            print('You have to choose between 1,2 and 3. Try again!')
            continue
    except ValueError:
        print('You have to choose between 1,2 and 3. Try again!')
        continue



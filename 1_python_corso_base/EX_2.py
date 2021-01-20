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
                    print('Very well, this question gave you one point!\n\n')
                else:
                    print('Very well, this question gave you {} points!\n\n'.format(quizfile_data[random_number]['scores']))
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
        user_type = int(input('If you have a quiz and you want to upload it press 1, to play press 2, to exit press 3   '))
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

import random
import tkinter




def explosive_num():

    # print(('-------------------'*2+'\n')*2)
    # print('Welcome the Ultimate-password game\n')
    # print(('-------------------'*2+'\n')*2)
    interval_1 = int(input('Minimum number: '))
    interval_2 = int(input('Maximum number: '))


    # print('-------------------------'*1)
    # print('Let\'s get started!!!!!')
    # print('The interval is betwwen', interval_1,'and', interval_2)
    # print('-------------------------'*1)


    bingo = random.randint(interval_1+1,interval_2-1)
    guess = int(input('First player: '))


    while True:
        if guess < interval_1 or guess > interval_2:
            print('-------------------')
            print('The number is out of the interval, please enter the number in the interval') 
        else:
            if guess == bingo:
                print(('-------------------'*5+'\n')*3)
                print('!!!!!!!Boom!!!!!!!')
                print('Bingo, the game is over !!!!\n')
                print(('-------------------'*5+'\n')*3)
                break
            if guess < bingo:
                interval_1 = guess
            elif guess > bingo: 
                interval_2 = guess 
        print('-------------------')
        print('From', interval_1, 'to', interval_2 )
        guess = int(input('Next player: '))

    exit_variable = input('Do you wanna play again?(Y/N): ')

    return exit_variable



        # if type(guess) != int:
        #     print('PLEASE GIVE A NUMBER NOT OTHERS')


def out_game(var):
    


    if var == 'Y' or var == 'y':
        out_game(UP_game())
    elif var == 'N' or var== 'n':
        pass
    else :
        print('Enter the wrong')
        var = str(input('Do you wanna play again?(Y/N): '))
        return out_game(var)



out_game(UP_game())




        

        


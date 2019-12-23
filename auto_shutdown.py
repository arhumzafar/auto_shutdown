import os

def what_mode(text, function_type):
    loop_3 = True

    while loop_3:

        print(text)
        timer = input().strip()

        try:
            timer_int = int(timer)
            os.system(f'shutdown -{function_type} -t {timer_int * 60}')
            loop_3 = False

        except ValueError:
            print('Your input has to be a number!')

loop_1 = True

while loop_1:
    loop_2 = True

    print('If you want to shut down your computer please enter <s + Enter>\n'
          'If you want to restart your computer please enter <r + Enter>\n'
          'If you want to put your computer into sleep mode enter <h + Enter>\n'
          'If you want to exit enter <e + Enter>\n')

    mode = input().strip()

    if mode == 's':
        what_mode('In how many minutes would you like to shut down your computer?\n', mode)

    elif mode == 'r':
        what_mode('In how many minutes would you like to restart your computer?\n', mode)

    elif mode == 'h':
        what_mode('In how many minutes would you like to put your computer in sleep mode?\n', mode)

    elif mode == 'e':
        loop_2 = False
        break

    else:
        loop_2 = False
        print('You have to enter <s> or <r> or <h>')

    while loop_2:

        print('If you want to exit enter <e + Enter>\n'
              'If you want to cancel enter <c + Enter>\n')

        user_input = input().strip()

        if user_input == 'e':
            loop_1 = False
            loop_2 = False
            break

        elif user_input == 'c':
            print('The process was successfully canceled!')
            os.system(f'shutdown -a')
            loop_2 = False

        else:
            print('Your input has to be <e> or <c>')
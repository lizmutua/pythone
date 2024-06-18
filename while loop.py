# box=0
# while (box < 10):
#     box= box +1
#     print(box)

"""white guess a dice progrma that that 
randomly initialize dice variable with a value between [1,6]
please ask the user to guess the number until he gets it right"""

# guess=int(input('pliz put in number between[1,6]'))
# correct_num=5
# game=False
# while(guess<=6 and game== False):
#     if guess== correct_num:
#         print('yay, you have won the game')
#         game=True
#     else:
#         print('sorry,try again')
#         guess=int(input('pliz put in number between[1,6]'))
        
# import random
# guess=int(input('pliz put in number between[1,6]'))
# correct_num=random.randint(1,6)
# game=False
# while(guess<=6 and game== False):
#     if guess== correct_num:
#         print('yay, you have won the game')
#         game=True
#     else:
#         print('sorry,try again')
#         guess=int(input('pliz put in number between[1,6]'))

fibon=[0,1]
while (len(fibon)<10):
            sum=fibon[-1]+fibon[-2]
            fibon.append(sum)
            print(fibon)
               
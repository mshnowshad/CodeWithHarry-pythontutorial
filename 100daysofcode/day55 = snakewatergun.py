print()

print('======================================> this is a snake water gun <===========================')
print()


'''

এই গেমটি দুইজন খেলোয়াড়ের মধ্যে খেলা হয়, একজন আপনি এবং অন্যজন কম্পিউটার। খেলাটি খুবই সাধারণ, তবে মজার!

ধাপ ১: পছন্দ নির্বাচন

প্রথমে, আপনাকে আপনার পছন্দটি নির্বাচন করতে হবে। তিনটি অপশন রয়েছে:
সাপ: সাপ পানিকে খায়।
পানি: পানি বন্দুককে নিভিয়ে দেয়।
বন্দুক: বন্দুক সাপকে গুলি করে।
ধাপ ২: কম্পিউটারের পছন্দ

আপনি আপনার পছন্দ নির্বাচন করার পরে, কম্পিউটার র্যান্ডমভাবে সাপ, পানি বা বন্দুকের মধ্যে একটি নির্বাচন করবে।
ধাপ ৩: ফলাফল

এবার ফলাফল নির্ধারণ করা হবে আপনার এবং কম্পিউটারের পছন্দ অনুযায়ী:

ড্র: যদি আপনি এবং কম্পিউটার একই পছন্দ নির্বাচন করেন, তাহলে খেলাটি ড্র হবে।

আপনি জিতেছেন: যদি আপনার পছন্দ কম্পিউটারের পছন্দকে পরাজিত করে (উপরের তালিকা অনুযায়ী), তাহলে আপনি জিতেছেন।

কম্পিউটার জিতেছে: যদি কম্পিউটারের পছন্দ আপনার পছন্দকে পরাজিত করে, তাহলে কম্পিউটার জিতেছে।


ধাপ ৪: পুনরায় খেলা

ফলাফল দেখার পরে, আপনি আবার খেলতে পারেন বা গেমটি শেষ করতে পারেন।
কি মজা আছে?

এই গেমটি খুবই সাধারণ, তবে এটি অনেক মজার হতে পারে কারণ আপনি কখনো জানেন না আপনি বা কম্পিউটার জিতবেন! এটি আপনার বন্ধুদের সাথেও খেলতে পারেন, কে কতবার জিতেছে তা রেকর্ড করে রাখুন এবং দেখুন কে সেরা খেলোয়াড়!

আশা করি এখন আপনি সাপ-পানি-বন্দুক গেমটি বুঝতে পেরেছেন। যদি আর কোন প্রশ্ন থাকে, তাহলে জিজ্ঞেস করুন!






# গেমের মূল নিয়ম:

> সাপ: সাপ পানিকে খায়, অর্থাৎ যদি একজন সাপ দেখায় এবং অন্যজন পানি দেখায়, তাহলে সাপ দেখানো খেলোয়াড় জিতে যায়।

> পানি: পানি বন্দুককে নিভিয়ে দেয়, অর্থাৎ যদি একজন পানি দেখায় এবং অন্যজন বন্দুক দেখায়, তাহলে পানি দেখানো খেলোয়াড় জিতে যায়।

> বন্দুক: বন্দুক সাপকে গুলি করে, অর্থাৎ যদি একজন বন্দুক দেখায় এবং অন্যজন সাপ দেখায়, তাহলে বন্দুক দেখানো খেলোয়াড় জিতে যায়।



 



'''



# import random

# while True:
    
#     player_action = input('#> as you like (snake = s , water = w , gun = g) enter this any value of conditon : ')


#     possible_action = ['s','w','g']


#     computer_action = random.choice(possible_action)



#     print('#> computer choice is : ',computer_action)

#     if player_action == computer_action:
#         print('# Game is Dro')
#     elif player_action == 's' and computer_action == 'w':
#         print('#>> congratulation! You win!')

#     elif player_action == 'w' and computer_action == 'g':
#         print('#>> congratulation! You win!')
#     elif player_action == 'g' and computer_action == 's':
#         print('#>> congratulation! You win!')
#     else:
#         print('# You lose . Computer is win!')
#     play_agian = input(">> ARE you play Again (y or n): ")
#     if play_agian == 'n':
#         break
        



# print('Thanks for playing!')



print()

print()

print('=++++++++++++ i am own created __+++++++++++++\n')




import random


while True:
    userinput = input('> Enter the name of you catch : (gun,snake,water) - ')

    optionforsecondplayer = ['gun','water','snake']

    secondplayer = random.choice(optionforsecondplayer)
    print(f'\n #Second player catch is \'{secondplayer}\' ')
    print()
    
    
    if userinput == 'gun' and secondplayer == 'snake':
        print('congratulation! You win.')
    elif userinput == 'snake' and secondplayer == 'water':
        print('Congratulation! You win .')
    elif  userinput == 'water' and secondplayer == 'gun':
        print('Congratulation! You win .')
    elif secondplayer == userinput:
        print('#>>>>>>>>Game is dro now <<<<<<<<<<')
    else:
        print('\n #Second Player is win now')

    print()
    
    playagin = input('>Are you play again? enter the (yes or no) : ')
    print()
    
    if playagin != 'yes':
        break
    
    print()
    
print('++++++++++++++++++>>>>>>>>>>>>> Thanks for play this game<<<<<<<<<<<<<<++++++++++++++++++++')

print()




































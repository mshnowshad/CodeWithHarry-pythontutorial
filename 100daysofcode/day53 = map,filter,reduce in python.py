print()

print("============================> Map < ==================================")


def functio(n):
    return 2*n
# print(functio(2))



ll =[1,2,3,4,5,6,7,8,9,10]

# new = []

# for item in ll:
#     new.append(functio(item))
    
# print(new)

##> same as


# nel = list(map(functio, ll))   #> 'map' used because for loop na chalaiya sort niyom a use kora jay
# print('> map list : ', nel)


print("=========> MAP explain with AI <++++++++++++++++++++")

'''
map function কি?

এটি Python-এর একটি অন্তর্নির্মিত function যা একটি নির্ধারিত function-কে iterable-এর প্রতিটি উপাদানে প্রয়োগ করে।
এটি একটি iterator প্রদান করে যা প্রতিটি উপাদানের রূপান্তরিত ফলাফল ধারণ করে।
কিভাবে কাজ করে?

Function এবং Iterable নির্ধারণ করুন:

আপনি যে function-টি প্রয়োগ করতে চান সেটি নির্ধারণ করুন।
যে iterable-এর উপর function-টি প্রয়োগ করতে চান সেটি নির্ধারণ করুন (যেমন: list, tuple, string)।
map function-টি কল করুন:

map(function, iterable) এই syntax-টি ব্যবহার করে map function-টি কল করুন।
Iterator গ্রহণ করুন:

map function একটি iterator প্রদান করে।
iterator-টি তে প্রতিটি উপাদানের রূপান্তরিত ফলাফল থাকে।
ফলাফল বের করুন:

iterator-টি থেকে ফলাফল পেতে list(), tuple(), বা অন্য কোনো উপযুক্ত function ব্যবহার করুন।
উদাহরণ:

"""
# একটি list-এর প্রতিটি সংখ্যার বর্গ নির্ণয়
def square(x):
  return x * x

numbers = [1, 2, 3, 4]
squared_numbers = map(square, numbers)  # iterator তৈরি হয়েছে
print(list(squared_numbers))  # ফলাফল: [1, 4, 9, 16]

"""
গুরুত্বপূর্ণ বিষয়:

map function-টি lazy evaluation ব্যবহার করে। অর্থাৎ, ফলাফলগুলি প্রয়োজন না হওয়া পর্যন্ত প্রকৃতপক্ষে গণনা করা হয় না।
map function-টি একাধিক iterable-এর সাথে ব্যবহার করা যেতে পারে।
map function-টি lambda function-এর সাথেও ব্যবহার করা যেতে পারে।
ব্যবহার:

Iterable-এর উপাদানগুলিকে রূপান্তর করতে।
Iterable-এর উপাদানগুলির উপর নির্দিষ্ট ক্রিয়াকলাপ সম্পাদন করতে।
কোডের সংক্ষিপ্ততা এবং readability বৃদ্ধি করতে।



'''







print('====================================> filter <=================================')



# def fileter_fileter(c):
#     return c>3


# newl = list(filter(fileter_fileter,ll))

# print("> filter list : ", newl)  #> "filter" mane 'fileter_fileter' function er condition use kore output dibe
# print()



print('======> filter explain with AI <+++=====')


'''


Filter function কি?

এটি Python-এর একটি অন্তর্নির্মিত function যা একটি iterable থেকে নির্দিষ্ট শর্ত পূরণকারী উপাদানগুলিকে আলাদা করে একটি নতুন iterator তৈরি করে।
এটি একটি প্রদত্ত function-এর সাহায্যে উপাদানগুলিকে যাচাই করে এবং যেসব উপাদানের জন্য function-টি True ফলাফল দেয়, সেগুলোকে নতুন iterator-এ অন্তর্ভুক্ত করে।
কিভাবে কাজ করে?

Function এবং Iterable নির্ধারণ করুন:

আপনি যে শর্ত প্রয়োগ করতে চান সেই শর্তকে প্রতিনিধিত্বকারী function-টি নির্ধারণ করুন।
যে iterable-এর উপর filter প্রয়োগ করতে চান সেটি নির্ধারণ করুন (যেমন: list, tuple, string)।
Filter function-টি কল করুন:

filter(function, iterable) এই syntax-টি ব্যবহার করে filter function-টি কল করুন।
Iterator গ্রহণ করুন:

filter function একটি iterator প্রদান করে।
iterator-টি তে কেবলমাত্র শর্ত পূরণকারী উপাদানগুলো থাকে।
ফলাফল বের করুন:

iterator-টি থেকে ফলাফল পেতে list(), tuple(), বা অন্য কোনো উপযুক্ত function ব্যবহার করুন।
উদাহরণ:


"""
# একটি list থেকে জোড় সংখ্যাগুলো আলাদা করা
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)  # iterator তৈরি হয়েছে
print(list(even_numbers))  # ফলাফল: [2, 4, 6]

"""

গুরুত্বপূর্ণ বিষয়:

filter function-টিও lazy evaluation ব্যবহার করে। অর্থাৎ, উপাদানগুলি প্রয়োজন না হওয়া পর্যন্ত যাচাই করা হয় না।
filter function-টি lambda function-এর সাথেও ব্যবহার করা যেতে পারে।
ব্যবহার:

Iterable-এর উপাদানগুলিকে নির্দিষ্ট শর্তের ভিত্তিতে ফিল্টার করতে।
প্রয়োজনীয় উপাদানগুলির একটি subset তৈরি করতে।
কোডের সংক্ষিপ্ততা এবং readability বৃদ্ধি করতে।


'''







print('==================================> Reduce <==================================')


# from functools import reduce

# # def new_function(a,v):
# #     return a + v

# new_function2 = lambda b,c : b+c 
# # Userlist = [1,2,3,4,5,6,7,8,9,20]  #> list er bodole "list, tuple, string" use kora jay

# # reducecopylist = reduce(new_function,Userlist)  #> 'def' function use na kore "lambda function" use kora jay >same as
# reducesum = reduce(new_function2,Userlist)
# print(">> Your all sum is = ", reducesum)


print("+++++++++++++> Reduce explain with Ai <=++++++++++++++++++++")

'''

reduce" একটা উচ্চ পর্যায়ের ফাংশন, যা একটা iterable এর উপাদানগুলোকে ধাপে ধাপে এক করে ফেলে। এটা "functools" মডিউলে থাকে।

কাজের ধারা:

functools থেকে reduce এনো:
Python
from functools import reduce
Use code with caution. Learn more
আপনার অপারেশন ফাংশন লেখুন:
এই ফাংশন দুটো আর্গুমেন্ট নেবে এবং তাদের উপর কাজ করবে।

reduce কল করুন:

> result = reduce(function, iterable, initializer=None)


function: উপাদানগুলোতে প্রয়োগ করা ফাংশন।
iterable: কমানোর জন্য উপাদানের সিরিজ।
initializer: (ঐচ্ছিক) শুরুর মান।

কমানোর ধাপ:

যদি initializer দেওয়া থাকে, তাহলে প্রথমবার function কল করার সময় এটাকে প্রথম আর্গুমেন্ট হিসেবে ব্যবহার করা হয়।
iterable এর প্রথম দুইটি উপাদান function এ আর্গুমেন্ট হিসেবে পাঠানো হয়।
function এর ফলাফল পরবর্তী কলের জন্য প্রথম আর্গুমেন্ট হিসেবে ব্যবহার করা হয়, সাথে সাথে iterable এর তৃতীয় উপাদানটিও দেওয়া হয়।
এই প্রক্রিয়া চলে, যতক্ষণ না সব উপাদান ব্যবহার হয়ে যায়।
function এর শেষ কলের ফলাফল ফিরিয়ে দেওয়া হয়।
উদাহরণ:


"""
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # আউটপুট: 24

"""


গুরুত্বপূর্ণ বিষয়:

এটা প্রায়ই যোগফল, গুণফল, সর্বোচ্চ বা সর্বনিম্ন মান খুঁজে পাওয়ার মতো কাজে ব্যবহার করা হয়।
এটা যেকোনোiterable এর সাথে ব্যবহার করা যায়, যেমন list, tuple, string, ইত্যাদি।
reduce এ দেওয়া ফাংশন associative এবং commutative হওয়া উচিত, যাতে ঠিক ফলাফল পাওয়া যায়।
অনেক সময় লিস্ট কম্প্রিহেনশান বা জেনারেটর এক্সপ্রেশন এর মতো পদ্ধতি "reduce" এর চেয়ে বেশি "Pythonic" মনে হয়।










'''








































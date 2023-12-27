print()




print("----------------------------Enumerate Function in Python ----------------------")



"""

#পাইথনে enumerate ফাংশনটি হলো একটি বিল্ট-ইন ফাংশন, যেটি একটি ইটারেটর রিটার্ন করে।
 এই ইটারেটরটি আপনাকে একই সাথে দুটি জিনিস দেয়:

 >> একটি কাউন্টার: এটি একটি সংখ্যা, যা ইটারেট করা শুরু হওয়ার পর থেকে কতবার লুপ চলেছে তা নির্দেশ করে।
   প্রথমবার লুপ চলার সময় কাউন্টারটি ০ হয়, দ্বিতীয়বার ১ হয়, ইত্যাদি।

 >> একটি উপাদান: এটি ইটারেট করা হচ্ছে এমন কালেকশনের (যেমন, লিস্ট, টিউপল, ইত্যাদি) থেকে একটি উপাদান


"""
print()




# mark = [10,20,30,430,50,60]

# indexs = 0

# for mar in mark:
#     print(mar)

#     if indexs == 3:  
#         print("harry,awesome!") #> now this line is not printed






print("########### AnOther type ##########")


print()




marks = [10,20,30,430,50,60]





for index2,mark in enumerate(marks):
    print(mark)
    if index2 == 3:
        print("I am Nowshad")






print()


print('=================================> Enumerate Function <=======================')
print()

"""
> লুপের মধ্যে ইনডেক্স এবং মান একসাথে ব্যবহার করা যায়।
> কোডকে আরও সংক্ষিপ্ত এবং সহজবোধ্য করা যায়।    
    
    
    
    """







# index = 0
marks = [20,50,40,60,34,32,31,50,90,70]
marks.sort()
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print('harry')
#     index +=1

###> same as:



for index,mark in enumerate(marks): #> ইনডেক্স এবং মান উভয়ই পেতে enumerate ব্যবহার করুন
    print(mark)
    if index == 2:  #> পাইথনের এনুমারেট ফাংশনটি একটি ইটারেটর রিটার্ন করে যা প্রতিটি উপাদানের সাথে তার ইনডেক্স জুড়ে দেয়।
        print('> You passed, congratulation!')







# print()



# numbers = [11,22,33,44,55,66,77,88,99,100]

# for index,number in enumerate(numbers):
#     number = number + 1
    
#     if index == 4:  #> index na lekle 'if' kaj korbe na
#         print('congratulations!')
        
#     print(number)
    


























print()















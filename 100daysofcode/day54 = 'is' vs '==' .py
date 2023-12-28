print()



print("=================>========'is'  and '==' er comparison <========================")

#> ধরুন আপনার কাছে দুটি বাক্স রয়েছে, যার প্রতিটিতে একই ধরনের ছয়টি আইটেম রয়েছে। বাক্সগুলি দেখতে একই রকম হলেও, তারা আলাদা আলাদা বাক্স। "is" অপারেটরটি দুটি বাক্সের তুলনা করার মতো

#> "==" অপারেটরটি বাক্সের ভিতরে আইটেমগুলির তুলনা করার মতো।




a = 4

b = '4'

print('>> a2 is b2 : ',a is b) #return False
print('>> a2 ==  b2 : ',a == b) #return False


print()



a2 = 101
b2 = 101

print('>> a2 ==  b2 : ',a2 == b2)  #return True 
print('>> a2 is b2 : ',a2 is b2)  #return True


print()




a3 = 'i am a bad boy'
b3 = 'i am a bad boy'
 
print('>>> a3 is b3 : ', a3 is b3)   #return True 
print('>>> a3 == b3 : ', a3 == b3)      #return True 
 



print()




a4 = [1,2,3,4,5,10]
b4 = [1,2,3,4,5,10]

print('>>>> a4 is b4 : ', a4 is b4)  #return False  because  a4 is b4 False রিটার্ন করে কারণ a4 এবং b4 মেমরির ভিন্ন ভিন্ন অবস্থান নির্দেশ করে।
print('>>>> a4 == b4 : ', a4 == b4 )  #return True 



print()



print("hello world")


print()



# import random

# randomnumber = random.randint(1,20)

# user = int(input('#> Enter the random number  of 1 to 20 : '))

# if randomnumber == user:
#     print()



















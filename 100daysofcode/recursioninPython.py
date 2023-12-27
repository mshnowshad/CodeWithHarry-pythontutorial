print()



print("=================================== Recursion in Python ====================================")

print()


#>>>>>  পাইথনে রিকার্শন একটা অদ্ভুত কিন্তু শক্তিশালী টেকনিক, যেখানে একটা ফাংশন নিজেকেই বারবার আহ্বান করে। মনে করুন একটা গমলা পেঁয়াজ আছে, তার ভিতরে আরেকটা পেঁয়াজ, তার ভিতরে আবার আরেকটা, এভাবে। রিকার্শনও ঠিক এমন, একটা ফাংশন নিজেকেই বারবার ডেকে, নিজের কাজের ছোট ভার্সন সমাধান করে।                                                                                                                                                                                                                                                                      চলুন একটা উদাহরণ দিয়ে বুঝি। ধরুন, আমরা ফেক্টোরিয়াল হিসাব করতে চাই। ফেক্টোরিয়াল মানে একটা সংখ্যার গুণনফল, তার আগের সবগুলো পজিটিভ পূর্ণসংখ্যাকে দিয়ে। যেমন, 5! = 5 * 4 * 3 * 2 * 1 = 120। " ! = <factorial> "

print()





def ফেক্টোরিয়াল(n):
  if n == 0 or n ==1:

    return 1
  else:
    return n * ফেক্টোরিয়াল(n-1)

a = ফেক্টোরিয়াল(int(input(">>Enter the elment: ")))


print(">> Your factorial number is ; " , a)

print()








# print("=============================== Quiz of Fibunacci Series ==================================")

# print()






# def fubunacci(x): #>>>> "x " is a cholok

    
#     if x==0 :
#         return 0
#     elif x==1:
#         return 1
#     else:
#         return (x-1) + (x-2)
    

# a = int(input("enter the number of elemnent: "))
# print()

# fubnumber = fubunacci(a)

# print("> Your Element is ; ", a)
# print()


# print('>>> Your Fibunacci number is = ' , fubnumber )  #> 



# print()












# # print("=============================== Used of Ai bard===============================")


# # def fubunacci(x):
# # #   x = int(input("Enter the number of elements: "))
# #   if x == 0:
# #     return 0
# #   elif x == 1:
# #     return 1
# #   else:
# #     return x-1 + x-2

# # # Call the function and get the result
# # fib_number = fubunacci(int(input("Enter the number of elements: ")))

# # # Print the result
# # print(">>> Your Fibonacci number is: ", fib_number)

















# print()
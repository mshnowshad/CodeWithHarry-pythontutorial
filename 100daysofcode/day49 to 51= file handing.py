# print()

print("=================================================> this is a introduction of file handing<========================================================")
"""
> file = open(filename, mode)    
    
#ফাইল বন্ধ করা
> file.close()



    """
print()

print('================================> "with" Statement< ============================================')
print()

with open('tipforpython.txt','r') as f:  ##> ei rokom sort kore leka jay. 'with' statement aniya
    n1 = f.read() #>'f.read()' er poriborthe jotho gula function ase "file handing" sob use korthe parbo
    print(n1)
    # f.close  #>> ei statement use  na korle o autometic 'f.close()' hoy mane "close" hoye jay because 'with' statement use kora oise
    print()   







# print("==============> \"w \" - Write - will overwrite any existing content <========================")
# print()

# # a = open('tipforpython.txt','w')
# # a.write('\n hello my name is nowshed')

# print()



# print("=======================> writelines method < =======================================")
# print()

# #>> writelines() মেথড ব্যবহার করে আপনি একসাথে একাধিক স্ট্রিং (লাইন) কে একটি ফাইলে লিখতে পারবেন।


# with open('tipforpython2.txt','w') as writelinemethod:
#     linetoline = ['line = 1 \n','line = 2 \n','line = 3 \n', 'line = 4']#>> যেসব স্ট্রিং ফাইলে লিখতে চান, সেগুলোকে একটি লিস্টে রাখুন।
     
#     writelinemethod.writelines(linetoline)
    
    
    







# print("======================> \"a\" - Append - will append to the end of the file <===================================")
# print()

# # append1 = open('tipforpython.txt','a')   
# # append1.write('my name is Python File Handing.')  #> jotho bar run korbo thotho bar 'append' oithe thakbo 

# # print()





# print('====================> "r" - Read - Default value. Opens a file for reading, error if the file does not exist <====================')
# print()


# c = open('tipforpython.txt','r')

# print(c.read())

# print()









# print('=============================> read(), readlines() and other methods < =======================================')
# print()


# with open('tipforpython.txt','r') as lop:
    
#     # read1 = lop.readlines()
#     # for i in read1:
#         # print(i)
        
        
#     #>> other option nise tho deko hehe
    
#     read2 = lop.readline() #> ei 'lop.readline() ' method use na korle '>while' loop colthe thakbe 
#     while True:
        
#         if not read2: #> 'lop.readline()' use na korle ei 'if' statement is not working!
#             break
#         print(read2)
    
        
        
        
        
print('==================================> seek(), tell() and other functions < =======================================')

print()


'''





# ফাইলের শুরু থেকে 5 বাইট পড়া
data = file.read(5)
print(data)



# বর্তমান অবস্থান জানা
position = file.tell()


# ফাইলের শেষে যাওয়া
file.seek(0, 2) #> ফাইলের মধ্যে কারেন্ট পজিশন পরিবর্তন করার জন্য seek() ফাংশন ব্যবহার করা হয়।

'''
















# print("=============> exercise < =============+++++++++++++++")

# print()

# # with open('tipforpython2.txt','a') as f:
# #     a = f.write('\n my name is exercise. thank you')
    
    

# with open('tipforpython2.txt','r') as r:
#         print(r.read())
#     # print()

    
    









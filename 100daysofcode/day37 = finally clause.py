print("")


print("============================================= Finaly Clause =============================================")

print()


"""
Python-এ finally clause হলো একটি বিশেষ কোড ব্লক যা সবসময় execute হয়,
 try block-এ কোনো সমস্যা হোক বা না হোক। এটাকে আপনি কাজ শেষ করার গ্যারান্টি হিসেবে মনে করতে পারেন।

  #ak kothay output show hothe hobe
  
"""















# def fun1():
    

#     try:
#         l = [1,3,4]
#         i = int(input('enter the index: '))
#         print(l[i])
#         return 1

#     except:
#         print('some error ................')
#         return 0




#     finally:  #> ei key word mane print hothe hobei 
#         print("i am always executed..")
#     # print('i am always showed')   #> functioner bithor thakle return method use thakle ei line printed oithonay but finally key word er bithor thakle print oibo


# x = fun1()
# print(x)














print()










def function():
    try:
        a = ['harry','hablu', 'nowshad', 'riyad','nabil']
        in1 = int(input('enter the index you show: '))
        print(a[in1])
        print()
        return 1

    except:
        print('#You some wrong .........')
        print()
        return 'Please try again .'
    
    finally:
        print('>> I am always executed and thank you .<<')
        print()


        
hi = function()  #> ei jaygay variable na dorle 'return' method kaj korbe nay ba show hobe na 

print(hi)
























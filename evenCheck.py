# def even_num():
#     a=int(input("Enter the number\n"))
#     for i in range(1,a,1):
#         # if i%2==0:
#             # i=i+1
#             # print("The even number is = ",d)
#         return i
# d=even_num()
# print("The even number is = ",d)
# #


def even():  
    sum=[]
    a=int(input("Enter the range\t"))
    for i in range(1,a,1):
         if(i%2==0):
          sum.append(i)
    return sum 
# ti=[1,2,3,4,5,6,7,8,9]    
d=even()
print(d)

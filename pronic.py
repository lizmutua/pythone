

# #Task 1,numbers divisible by 7 and multiple of 5. Meaning that the number is divisible by 7 and 5. So we got the product of 7 and 5=35
# X=int(input('enter number 1\n'))
# Y=int(input('enter number 2\n'))
# def ma_th(a,b):#function to check numbers divisible by 35. a and b are local variables
#     bes=[]#list to be formed
#     for i in range(a,b):#the range is got from users input X and Y
#         if i%35==0:#check if the numbers are divisible
#             bes.append(i)
#     print(bes)#print the numbers divisible by 35
# ma_th(X,Y)

#Task 2,Pronic_number based on users input
X=int(input('enter a number\n'))#ask a user to enter a number
def pronic(num):#function that checks if the number is pronic or not. num is a local variable
    list11=[]
    list33=[]
    list44=[]
    for i in range(0,num):#the range is from 0 stops at num(number entered by a user)
        list11.append(i)
    print(list11)#print the list
 
    list33=list11#assign list33, the elements of list11
    for i in range(0,len(list33)-1):#range is from 0 till length of list33 minus 1. We are getting indexes here i.e positions of the elements in the list
        prod=list33[i]*list33[i+1]#0,1,2,3,4,5,6,7,8,9 list33[0]*list33[1]
        list44.append(prod)
    Y=list44
    print(Y)
    if num in Y:
        print('pronic')
    else:
        print('not pronic')
pronic(X)
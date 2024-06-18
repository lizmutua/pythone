# #  FIND MAX OF THE LIST

# def find_maximum(lst):
#     if len(lst) > 0:
#         maximum_value = max(lst)
#         print(f"The maximum value in the list is: {maximum_value}")
#     else:
#         print("The list is empty.")

# # Example usage
# my_list = [3, 7, 1, 9, 4,10,11,20]
# find_maximum(my_list)


# def Max():
#      ary=[2,4,7,4,23,5,1,4,8,9]
#      a=max(ary)
#      print(a)
# Max()


# AVERAGE

# arx2=[4,7,1,5,11,53,12,46,84,23]
# def average(arrx,n):
#     i=0
#     sum=0
#     while i<n:
#         sum+=arrx[i]
#         i+=1
#     print(sum)
#     print(n)
#     av_num=float(sum/n)
#     print('The average is',av_num)
# average(arx2,len(arx2))


# import statistics
# def average():
#     arx2=[4,7,1,5,11,53,12,46,84,23]
#     print(statistics.mean([4,7,1,5,11,53,12,46,84,23] ))
# average()



#  LIST IN REVERSE
# list1=[2,6,7,45,23,53,14,45,89,5]
# def revers():
#      list1.sort(reverse=1)
#      print(list1)
# revers()


# # 
# def compare():
# #creating list 1
#     l1=[]
#     print('**Enter 00 to mark end of list**')
#     x=int(input('Enter values for list 1 '))
#     l1.append(x)
#     while x!=00:
#         x=int(input('Enter values for list 1 '))
#         l1.append(x)
#         if x==00:
#             break
        
# #creating list 2
#     l2=[]
#     print('**Enter 00 to mark end of list**')
#     y=int(input('Enter values for list 2 '))
#     l2.append(y)
#     while y!=00:
#         y=int(input('Enter values for list 2 '))
#         l2.append(y)
#         if y==00:
#             break  
#     print('\n')
#     print('List1:',l1)
#     print('List2:',l2)
# #comparing the lists
#     if len(l1)!=len(l2):
#         print('False''\nLists must be of the same size')
#     else:
#         for i in range(0,len(l1)):
#             if l1[i]<l2[i]:
#                 print('True')
#                 print(l1[i],'Is less than',l2[i])
            
# compare()


# def compare_lists(list1, list2):
#     if len(list1) != len(list2):
#         print("False (Lists are not the same length)")
#         return

#     result = all(element1 < element2 for element1, element2 in zip(list1, list2))
    
#     print(result)

# # Example usage
# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 8]

# compare_lists(list1, list2)



#  SWAP

 
# #5 Swapping 2 elements using index of a list
# n=int(input('Enter number of elements: '))#number of elements
 
# list3=[]
# def ls3(list3,m):
#         for num in range(0,m):
#             num=int(input(f'Enter number {num}: '))
#             list3.append(num)
#         print('Before',list3)
#     #ls3(list3,m)
# print('\n')
# def swap(list3):#function to swap
#     x=int(input('Enter position1 to swap: '))
#     y=int(input('Enter position2 to swap: '))
#     i=list3[y]
#     list3[y]=list3[x]
#     list3[x]=i
#     print('After',list3)    
# ls3(list3,n)
# swap(list3)



# def swap_elements(lst, index1, index2):
#     if 0 <= index1 < len(lst) and 0 <= index2 < len(lst):
#         # Swap elements at index1 and index2
#         lst[index1], lst[index2] = lst[index2], lst[index1]
#         print(f"Swapped elements at indices {index1} and {index2}: {lst}")
#     else:
#         print("Invalid indices. Please provide valid indices within the list range.")

# # Example usage
# my_list = [1, 2, 3, 4, 5]

# # Swap elements at index 1 and index 3
# swap_elements(my_list, 1, 3)



 #5 Swapping 2 elements using index of a list
# n=int(input('Enter number of elements: '))#number of elements
 
# list3=[]
# def ls3(list3,m):
#         for num in range(0,m):
#             num=int(input(f'Enter number {num}: '))
#             list3.append(num)
#         print('Before',list3)
    #ls3(list3,m)
#print('\n')

# def swap(list3,m):#function to swap
#     for num in range(0,m):
#         num=int(input(f'Enter number {num}: '))
#         list3.append(num)
#     print('Before',list3)
 
#     x=int(input('Enter position1 to swap: '))
#     y=int(input('Enter position2 to swap: '))
#     # i=list3[y]
#     # list3[y]=list3[x]
#     # list3[x]=i
#     list3[x],list3[y]=list3[y],list3[x]#swap
#     print('After',list3)    
# #ls3(list3,n)
# swap(list3,n)



#  Concat list
# def concat(list1, list2):
#     result = list1 + list2
   
#     print(result)
 
# # Example usage
# list1 = [7, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9]
 
# concat(list1, list2)



# # 
# def last_index_of_value(lst, value):
#     try:
#         last_index = len(lst) - 1 - lst[::-1].index(value)
#         print(f"The last index of the value {value} is: {last_index}")
#     except ValueError:
#         print(f"The value {value} is not found in the list. Last index: -1")

# # Example usage
# my_list = [74, 85, 102, 99, 101, 85, 56]
# search_value = 85

# last_index_of_value(my_list, search_value)


# ... DIfference btwn max and min plus 1
# def calculate_range(lst):
#     min_value = min(lst)
#     max_value = max(lst)
#     data_range = max_value - min_value + 1

#     print(f"The range of values in the list is: {data_range}")

# # Example usage
# my_list = [36, 12, 25, 19, 46, 31, 22]

# calculate_range(my_list)


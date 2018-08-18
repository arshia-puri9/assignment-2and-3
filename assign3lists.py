#LISTS
#answer1:
#user defined inputs:
a=input("enter first input for the list\n")
b=input("enter second input for the list\n")
c=input("enter third  input for the list\n")
d=input("enter fourth input for the list\n")
list=[a,b,c,d]
print(list)

#answer2: adding the given list to the above list
list_1=['goggle",facebook",microsoft,"tesla']
#list here refers to the list in ques1
print(list + list_1)

#answer3:
colours=['red','yellow','red','green'] #given list
#to count no of times red occurs in the list
print("Count of red in the list is",colours.count('red'))

#answer4:
num_list=[10,23,5,11,27,9]
num_list.sort();
print("Sorted list in ascending order is",num_list)

#answer5:
A=[2,5,7,9]
B=[4,6,11]
C=A + B
C.sort();
print(C)

#answer6:
C=[2,4,5,6,7,9,11] #above given list
count_even=0;
count_odd=0;
for i in C:
    if(i%2==0):
       count_even=count_even+1
    else:
        count_odd=count_odd+1  
      
print("no of even numbers is",count_even)
print("no of odd numbers is",count_odd)




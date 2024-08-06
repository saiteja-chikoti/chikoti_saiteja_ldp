n = int(input())        #size of the array from user
a = list(map(int,input().split()))      #elements of array from user

total_moves= (n // 2) + (n % 2)    #calculating total moves of Alice
curr_moves = total_moves #keep track of moves left

even = sum(1 for x in a if x % 2 == 0)   #calculating count of even numbers
odd = n - even     # calculating count of odd numbers 

while True:            
    if curr_moves < 0:        #if no moves left Bob will win
        print("Bob")
        break
                             #In total_moves we may have even and odd numbers
                             #consider all num acquired in curr_moves to be even and remaining total_moves- curr_moves to be odd

    val1 = 2*curr_moves - 1  #To get even numbers in "curr_moves" we need atleast 2*curr_moves-1 even num in list 

    rem_moves=total_moves- curr_moves    #calculate rem_moves
    val2 = 2*rem_moves                   #To get odd numbers in "rem_moves" we need atleast 2*rem_moves odd num in list

    if even >= val1 and odd >= val2:     #check if list have the enough items to win alice 
        print("Alice")
        break
                             
    val1 = 2*curr_moves         #consider all num acquired in curr_moves to be odd and remaining total_moves- curr_moves to be even here
    rem_moves=total_moves- curr_moves    
    val2 = 2*rem_moves-1

    if even >= val1 and odd >= val2:
        print("Alice")
        break

    curr_moves -= 2



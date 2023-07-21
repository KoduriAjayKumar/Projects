'''
This Python project generates a magic square of odd order (n x n) using the Siamese method. 
A magic square is a square matrix in which the sum of each row, column, and diagonal is the same constant value.
The user is prompted to enter an odd number 'n' for the size of the matrix, and the program generates the magic square,
displaying the matrix and the constant sum of rows/columns/diagonals.
'''
def magic_sqaure(n):
    MagicSquare = []
    for i in range(n):
        L = []
        for j in range(n):
            L.append(0)
        #print(*L) gives the same output of below 5 lines of code
        MagicSquare.append(L) #Gives an nested list: [[0,0,0],[0,0,0],[0,0,0]]
   
    i = n//2
    j = n -1   # Condition 1 
    
    num = n*n
    count = 1
    
    while(count <= num):
        if (i ==-1 and j == n):
             i = 0
             j = n-2  # Condition 4
        else:
            if i <0 : # conditon 2 row is becoming -1
                 i = n-1
            if j == n: # Condition column value exceeding. 
                 j = 0
                   
        if(MagicSquare[i][j]!=0 ):
             i = i+1
             j = j-2   # Codition 3
             continue  # Continue to check above coditions of while loop from frist without going down.
        
        else:
            MagicSquare[i][j] = count
            count += 1
            
            i = i-1
            j = j+1
            
            
    for i in range(n):
        for j in range(n):
            print(MagicSquare[i][j] , end = " ")
        print()
    print()    
    print("Sum of each row/column/diagonal of above Magic Square(matrix) =", n*(n**2+1)/2)
    print()

   
def exit():
    print("Press 1 to continue \nPress 0 to exit")
    print()
    a = int(input())
    if a == 0 :
        print("Over")
    else:
        k = int(input("please enter a odd number 'n' for the size of matrix n*n :"))
        print()
        while (k%2 == 0):
            print("please enter a 'odd' number.")
            k = int(input("please enter a odd number 'n' for the size of matrix n*n :"))
        magic_sqaure(k)          
        exit()
        print()
    
k = int(input("please enter a odd number 'n' for the size of matrix n*n :"))
while (k%2 == 0):
    print("please enter a 'odd' number.")
    k = int(input("please enter a odd number 'n' for the size of matrix n*n :"))
print()
magic_sqaure(k)          
exit()
    
    
   
        
   














'''
given non-zero positive odd integer n, create an n-by-n magic square    
'''

# Initialize 

# compute magic square
    # initial row = top row
    # initial column = middle column

# output magic square


def odd_magic_square(n):
    if(n%2 == 1): # if n is odd, make a magic square. if it isn't odd (even), output such.

        # initialize
        square = [[0 for j in range(n)] for i in range(n)] # n by n square filled with zeros
        r = 0 # initial row is the top-most row
        c = int( n/2 ) # initial column is the middle column (not sure why it rounds up instead of flooring)
        ''' 
            start at square[r][c]
            Iteration:
                Case Analysis:
                    - if r is 0, we need to move to the bottom-most row (r = n-1)
                    - if c is n-1, we need to move to the left-most column (c = 0)
                    - if a cell is already taken, we need to move down 1 row
                    
            
        '''
        # compute magic square
        for i in range(n*n): # we have to traverse every square once
            past_r = r # storing the current value of which row we're in for after r is changed

            square[r][c] = i+1
            if(r==0): # if we're on the top row, move to the bottom row
                r = n-1
            else:
                r -= 1

            if(c==n-1): # if we're on the right-most column, move to the left-most column
                c = 0
            else:
                c += 1
            
            if(square[r][c] != 0): # condition to move down a row

                if(past_r == n-1): # if the previous row was on the bottom, set the current row to the top row, else set the row to be directly below the previous row
                    r = 0 
                else: 
                    r = past_r + 1 

                if(c == 0): # if the current column is the left-most column, move to the right-most column
                    c = n-1
                else:
                    c -= 1

        # output magic square
        for k in range(n):
            print(square[k])

    else:
        print("n must be an odd, positive integer")
        

odd_magic_square(5)


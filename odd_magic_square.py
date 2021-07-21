'''
given non-zero positive odd integer N, create an N-by-N magic square    
'''


# Initialize
n = 5
square = [[0 for j in range(n)] for i in range(n)]   # initially filled with sentinels

# def initialize(n):
    # number = n
    # if(n>0 and n%2==1): # if n is greater than zero and odd
        
    #     for c in range(1, n+1): # filling in the center (n by n) with zeroes
    #         for r in range(1, n+1):    
    #             square[r][c]= 0
    #     for
    # else:
    #     print("invalid input. n must be a positive, nonzero odd integer")





# compute magic square
    # if N is odd, start at the cell of the middle column at the top row
    # initial row = top row
    # initial column = middle column
r = 0
c = int( n/2 )

def compute_square(square):
    ''' let <r, c> equal the current row and column of the square s.t.


        start at square[r][c]
        Case Analysis:
            - if r is 0, we need to move to the bottom-most row
            - if c is n-1, we need to move to the left-most column
        
    '''
    


# output magic square
def output_square():
    for k in range(n): # just to see what it's like before computing the magic square
        print(square[k])

# initialize(n)
square[r][c] = 1
square[r+1][c] = 2
output_square()

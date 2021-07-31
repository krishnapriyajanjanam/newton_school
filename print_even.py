# recursion solution to printing even numbers
def print_even(x):
    if(x%2!=0):
        x-=1
    if(x>2):
        print_even(x-2)
        print(x, end=' ')
    else:
        print(x,end=' ')

x=int(input())
print_even(x)
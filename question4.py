# Question 4

memory = {}
def memoize_fibo(f):

    def inner(num):
        if num not in memory:
            memory[num] = f(num)
        return memory[num]
 
    return inner


@memoize_fibo
def fibo(n):
    if n<=1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

terms = input("Enter the nth term: ")
for i in range(int(terms)):
    print(fibo(i))



def sum_of_numbers(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_of_numbers(lst[1:])

print(sum_of_numbers([23, 44, 5, 67, 1, 1, 2, 4, 5]))
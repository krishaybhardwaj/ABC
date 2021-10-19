def fibonacci(x):
    count = 0
    term_1 = 0
    term_2 = 1
    while count < x:
        print(term_1)
        term_x = term_1 + term_2
        term_1 = term_2
        term_2 = term_x
        count+=1
    return count
print(fibonacci(7))


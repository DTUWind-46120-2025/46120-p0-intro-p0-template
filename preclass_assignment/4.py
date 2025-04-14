def fibonacci_stop(max_value):
    fib_seq = [1,1]
    while fib_seq[-1]+fib_seq[-2] <=max_value:
        fib_seq.append(fib_seq[-1]+fib_seq[-2])
    print(fib_seq)

fibonacci_stop(30)
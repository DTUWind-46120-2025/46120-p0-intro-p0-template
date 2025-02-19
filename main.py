from functions import greet, goldilocks, square_list, fibonacci_stop, clean_pitch
def main():
    "test greet"
    greet("Alice")
    "test goldilocks"
    print("\nGoldilocks Test:")
    goldilocks(132)
    goldilocks(141)
    goldilocks(160)
    print("\nSquared List:", square_list([1, 2, 3, 4, 5]))
    print("\nFibonacci Sequence:", fibonacci_stop(100))
    print("\nCleaned Pitch Angles:", clean_pitch[10, -5, 95, 45])
 
if __name__ == "__main__":
    main()
    
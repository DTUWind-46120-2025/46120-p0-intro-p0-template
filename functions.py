preclass_assignment/functions.py
def greet (name):
    print('Hello', name)
    
greet ('world')

def goldilocks (bed_length):
    if bed_length > 150:
        print('Too large!')
    elif bed_length < 140:
        print('Too small!')
    else:
        print('Just right!')

goldilocks (139)
goldilocks (140)
goldilocks (151)
goldilocks (150)

def square_list(numbers):
    return [num ** 2 for num in numbers]
print(square_list([1,2,3,4,5]))

square_list([1,2,3])


def fibonacci_stop(max_value):
    if max_value < 1:
        return []  # Return an empty list if max_value is less than 1

    fibonacci_numbers = [1, 1]  # Start with the first two Fibonacci numbers

    while True:
        next_fib = fibonacci_numbers[-1] + fibonacci_numbers[-2]  # Sum of last two numbers
        if next_fib > max_value:  # Stop if the next number exceeds max_value
            break
        fibonacci_numbers.append(next_fib)  # Add the next Fibonacci number to the list

    return fibonacci_numbers

# Example usage:
max_value = int(input("Enter the maximum value for Fibonacci sequence: "))
print(fibonacci_stop(max_value))

fibonacci_stop(30)

def clean_pitch(pitch_angles, status_signals):
    cleaned_angles = []  # List to store cleaned values

    for pitch, status in zip(pitch_angles, status_signals):
        if (pitch < 0 or pitch > 90) and status > 0:
            cleaned_angles.append(-999)  # Mark bad values
        else:
            cleaned_angles.append(pitch)  # Keep good values unchanged

    return cleaned_angles

# Example usage:
pitch_angles = [10, 85, -5, 95, 40, 100, 70]
status_signals = [0, 0, 1, 0, 0, 2, 1]  # 1 or greater indicates a malfunction


cleaned_data = clean_pitch(pitch_angles, status_signals)
print(cleaned_data)

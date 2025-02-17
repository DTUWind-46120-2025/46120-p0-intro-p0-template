#%%
#1. write a simple function
def greet(name):
        print(f"Hello, {name}!")
greet('world')

#%%
# 2. If/else statements
def goldilocks(length):
        if 140<length<150:
            print("Just right :)")
        if  length<140:
            print ("Too small!")
        else:
            print ('Too large!')
goldilocks (145)

#%%
# 3. For loops
def square_list(numbers):
    return [x ** 2 for x in numbers]
numbers = [1, 2, 3]
squared_numbers = square_list(numbers)
print(squared_numbers)

#%%
# 4. While loops
def fibonacci_stop(max_value):
    if max_value < 1:
        return []
    
    fib_sequence = [1, 1]
    while True:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        if next_value > max_value:
            break
        fib_sequence.append(next_value)
    
    return fib_sequence
max_value = 10
print(fibonacci_stop(max_value))  

#%%
# 5.Logical operators
def clean_pitch(measurements, status):
    cleaned_list = []
    for i in range(len(measurements)):
        if 0 <= measurements[i] <= 90:
            cleaned_list.append(measurements[i])
        elif status[i] > 0:
            cleaned_list.append(-999)
        else:
            cleaned_list.append(measurements[i])
    return cleaned_list
measurements = [-1,2,6,95]
status = [1,0,0,0]
cleaned_measurements = clean_pitch(measurements, status)
print(cleaned_measurements)
# %%

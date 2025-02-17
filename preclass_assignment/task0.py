#1 Write simple function

def greet(name):
    print(f"Hello, {name}!")

# Call the function
greet("Tessa")


#2 If/else statement
def goldilocks(BedSize):
    if BedSize < 140:
        print("Too small!")
    elif BedSize > 150:
            print("Too big!")
    else:
            print("Just right. :)")

goldilocks(139)
goldilocks(140)
goldilocks(151)
goldilocks(150)

#3 For loops
def square_list(numbers):
      squared_numbers = []
      for num in numbers:
            squared_numbers.append(num**2)
      
      return squared_numbers

print(square_list([1,2,3]))

#While loops
def fibonacci_stop(max_value):
      fibonacci_numbers = [1,1]
      while True:
            next_number= fibonacci_numbers[-1] + fibonacci_numbers[-2] #sum of last two numbers
            if next_number > max_value:
                  break
            fibonacci_numbers.append(next_number)
      return fibonacci_numbers

print(fibonacci_stop(30))



#Logical operators
def clean_pitch(pitch_angles, status_signals):
      cleaned_data =[]
      for angle, status in zip(pitch_angles, status_signals):
            if (angle <0 or angle >90) and status >0:
                  cleaned_data.append(-999)
            else:
                  cleaned_data.append(angle)
      return cleaned_data


angle = [-1, 3, 6, 95]  # "raw" pitch angles
status = [1, 0, 0, 0]  # status signals
print(clean_pitch(angle, status)) 

#if you want to iterate through two lists at the same time 
list_a = [1,2,3]
list_b=['a','b','c']
for tup in zip(list_a,list_b):
      item_a, item_b = tup
      print(item_a,item_b)

#fetch and pull on GitHub (fetch is you only take info from the ohter branch, and pull 
#is that you also implement that, so a pull is a fetch followed by a merge)
#pull request = branch to a branch
#gitignore = file ending patterns that you tell git to ignore

#copy that lives in user space that you live in (fork), and branch is your own
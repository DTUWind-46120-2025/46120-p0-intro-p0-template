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
def square_list(X):
    result=[]
 
    for i in X:
        value=np.sqrt(i)
        result.append(value)
 
    print(result)
square=square_list([1,4,9])

#%%
# 4. While loops
def fibonacci_stop(max_value):
    fib = [1, 1]
    while (n := fib[-1] + fib[-2]) <= max_value:
        fib.append(n) # append the new value to the list
    return fib if max_value >= 1 else []
 
#fib[-1]: This accesses the last element in the list.
#fib[-2]: This accesses the second-to-last element in the list.
# call the function where max_value = 30
print(fibonacci_stop(30))  

#%%
# 5.Logical operators
def clean_pitch(x,state):
    clean_pitch=[]
    for i ,k in zip(x,state):
        if (i<0 or i>90 ) and k==1:
            clean_pitch.append(-999)
        else:
            clean_pitch.append(i)
           
    return clean_pitch
x=[-1,2,6,95]
state=[1,0,0,0]
clean_pitch(x,state)
# %%

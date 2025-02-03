"""Demonstrate functions for preclass assignment."""
import functions as fxn

print('Exercise 1\n')
fxn.greet('world')

print('\nExercise 2\n')


fxn.goldilocks(139)
fxn.goldilocks(140)
fxn.goldilocks(151)
fxn.goldilocks(150)

print('\nExercise 3\n')

print(fxn.square_list([1, 2, 3]))

print('\nExercise 4\n')

print(fxn.fibonacci_stop(30))

print('\nExercise 5\n')

x = [-1, 2, 6, 95]
status = [1, 0, 0, 0]
x = fxn.clean_pitch(x, status)
print(x)

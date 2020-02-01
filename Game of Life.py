# Write your code here :-)
starting_population = [
[False , False , False , False, False, False, False, False],
[False , False , False , False, True, False, False, False],
[False , False , False , True, True, True, False, False],
[False , False , False , False, True, False, False, False]
]

next_population= [
[False , False , False , False, False, False, False, False],
[False , False , False , False, False, False, False, False],
[False , False , False , False, False, False, False, False],
[False , False , False , False, False, False, False, False]
]

def print_population():
    for i in range(0,4):
        print(starting_population[i])
print_population()

count_True = 0
nabor_looking_at = 0
def countTrue():
    global count_True
    global nabor_looking_at
    if nabor_looking_at == True:
        global count_True
        count_True = count_True + 1
# 1. Any live cell with fewer thqn two lines
# nabors 2
# cell

for y in range(2,3):
    for x in range(3,4):
#1
#print(starting_population[y][x])
#north south nabors
#2
#print(starting_population[y-1][x])
        nabor_looking_at = starting_population[y-1][x]
        countTrue()
#3
        nabor_looking_at = starting_population[y+1][x]
        countTrue()

# east south nabors
#4
        nabor_looking_at = starting_population[y][x-1]
        countTrue()
#5
        nabor_looking_at = starting_population[y][x+1]
        countTrue()
#daganals
# north west
#6
        nabor_looking_at = starting_population[y-1][x-1]
        countTrue()
#7
        nabor_looking_at = starting_population[y-1][x+1]
        countTrue()
#east south
#6
        nabor_looking_at = starting_population[y+1][x-1]
        countTrue()
#7
        nabor_looking_at = starting_population[y+1][x+1]
        countTrue()
print(count_True)
if count_True < 2:
    print(1)
    starting_population[y][x] == False
if count_True == 2 or count_True == 3:
    print(2)
if count_True > 3:
    print(3)




print_population()

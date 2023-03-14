from random import randint
play = 1
while play == 1:
    value_1 = randint(1,10)
    value_2 = randint(1,10)
    print("The problem is: ", value_1, "x", value_2, "=" )
    a = int(input("Answer:"))
    if a == value_1 * value_2:
        print("Correct!")
    else:
        print("That ir not correct. Correct answer is: ", value_1 * value_2)




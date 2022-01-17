import secrets, time

dice = int(input("What dice do you need rolled?: "))
counter = int(input("Enter number of rolls: "))

while counter >0:
    # Getting systemRandom class instance out of secrets module
    secretsGenerator = secrets.SystemRandom()

    # secure random integer numbers

    random_number = secretsGenerator.randint(1, dice)
    print(dice, " Sided Dice: ", random_number)
    counter = counter-1

    time_duration = 2
    time.sleep(time_duration)

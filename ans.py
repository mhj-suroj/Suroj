#Question 1
f = open("algorithm.txt", "w")
f.write("Step1: Input the number (n) till which the fibonacci series will run\n\nStep2: "
        "Let assign variable a equal to 1 and b equal to 2\n\nStep3: "
        "Add variable a and b and assign it to variable c\n\nStep4: "
        "Display the value of c\n\nStep5: "
        "Assign the value of b to variable a\n\nStep6: "
        "Assign the value of c to variable b\n\nStep7: "
        "Subtract one from n and store it to variable n\n\nStep8: "
        "if the value of n is not zero then go back to the third step\n\nStep9: "
        "Display fibonacci numbers till n numbers")
f.close()


#Question 2
a, b = 1, 2
total = 0
while True:
    a, b = b, a + b
    if b >= 4000000:
        break
    if b%2 == 0:
        total += b
print(total)
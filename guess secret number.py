secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
number=int(input("Enter large number:"))
n=True
while n==True:
    if number==secret_number:
        print("Well done, muggle! you are free now")
        n=False
    else:
        print("Ha ha! You're stuck in my loop!")
        number=int(input("Enter large number:"))

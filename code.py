import time
import random
print("Welcome to Blackjack!")
time.sleep(1)
print("Do you want me to explain the rules?")
time.sleep(1)
rules_decision = input("Enter Y for yes and N for no. ").title()
while rules_decision != "Y" and rules_decision != "N":
    print("Please input either Y or N.")
print("bye")
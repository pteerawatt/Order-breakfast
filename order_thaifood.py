import time
import sys

def print_pause(message_to_print):
    print(message_to_print)
    sys.stdout.flush()
    time.sleep(3)

def valid_input(prompt,option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response

def intro():
    print_pause("Hello! I am Peteboxes, the ThaiHouse Bot")
    print_pause("We have the best padthai in town, and you can choose from two choices of meat.")
    print_pause("The first is organic grass fed beef.")
    print_pause("The second is cage free chicken")

def get_order():
    response = valid_input("Would you like beef or chicken in your padthai?\n", "beef", "chicken")
    if "beef" in response:
        print_pause("Beef it is!")
    elif "chicken" in response:
        print_pause("Chickens it is!")
    print_pause("Your order will be ready shortly")
    order_again()

def order_again():
    response = valid_input("Would you like another padthai? Please say yes or no.\n", "yes", "no")
    if "no" in response:
        print_pause("OK, goodbye!")
    elif "yes" in response:
        print_pause("Very good, I'm Happy to take your order.")
        get_order()

def order_food():
    intro()
    get_order()

order_food()

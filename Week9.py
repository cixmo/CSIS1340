import array

receipts = array.array('d', [])

print("Welcome to the receipt program!")

while True:
    user_input = input("Enter the value for the seat ['q' to quit]: ")
    if user_input.isalpha():
        if user_input == 'q':
            print('*****Total: $' + ("%.2f" % sum(receipts)))
            break
        else:
            print("I'm sorry, but '"+ user_input +"' isn't valid. Please try again.")
            continue
    user_input = user_input.replace(',', '')
    user_input = float(user_input)
    receipts.append(user_input)
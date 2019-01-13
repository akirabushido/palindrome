while True:
    palindrome = input("Please write a setence or enter 'quit' to exit: ").lower()
    reverse= palindrome[::-1]
    if palindrome.lower() == 'quit':
        break
    elif reverse.replace(" ","") == palindrome.replace(" ",""):
        print("It's a palindrome!")
    else:
        reverse != palindrome
        print("Sorry not a palindrome.")
   
print("Thank you for playing!")        

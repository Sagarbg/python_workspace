import caesar_art

# Todo-1: Create a function called encrypt() that takes original_text and shift_amount as 2 inputs.

# Todo-2: Inside the 'encrypt' function, shift each letter of the original_text forwards in the alphabet by the shift_amount and print the encrypted text.

# You can use the built-in Python index() function to find out the position of an item in a a list e.g.
# fruits = [4, 55, 64, 32, 16, 32]
# x = fruits.index(32)

# e.g. If we have the following value:

# plaint_test = "hello"
# shift_amount = 1

# The final encrypted output shoud be:
# Here is the encoded result: ifmmp

# Where each of the letters of the 'hello' is shifted up by 1.

# Todo-3: Call the encrypt() function and pass in the user inputs. You should be able to test the code and encrypt a message.

# Todo-4: What happens if you try to shift z forwards by9? Can you fix the code? 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(caesar_art.logo)

def caeser(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        # shift_amount *= -1 will convert into negative sign
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet) #0-25
            output_text += alphabet[shifted_position]
    
    print(f"Here is the {encode_or_decode}d result: {output_text}")

shoud_continue = True

while shoud_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caeser(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'. \n").lower()
    if restart == "no":
        shoud_continue = False
        print("Goodbye..")




from tkinter import *
from Crypto.PublicKey import RSA

# Generate an RSA key pair (public and private key)
key = RSA.generate(2048)

# Get the public key for encryption
public_key = key.publickey()

# Encrypt the plaintext using the public key
def encrypt(plaintext):
    ciphertext = public_key.encrypt(plaintext.encode(), 32)[0]
    return ciphertext.hex()
private_key = RSA.import_key(open('private.pem').read())

# Decrypt the ciphertext using the private key
def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)
    plaintext = private_key.decrypt(ciphertext)
    return plaintext.decode()

root = Tk()
root.geometry("400x450")
root.title(" DES ")

def Take_input1():
	INPUT = inputtxt.get("1.0", "end-1c")
	print(INPUT)
	user_input=(str(INPUT))
	encrypted_text = encrypt(user_input)
	Output.insert(END, str(encrypted_text))
def Take_input2():
	INPUT = inputtxt.get("1.0", "end-1c")
	print(INPUT)
	user_input=(str(INPUT))
	encrypted_text = user_input
	plaintext = decrypt(encrypted_text)
	Output.insert(END, plaintext)
	
inputtxt = Text(root, height = 10,
				width = 25,
				bg = "light yellow")

Output = Text(root, height = 5,
			width = 25,
			bg = "light cyan")

Display1 = Button(root, height = 2,
				width = 20,
				text ="Encrypt",
				command = lambda:Take_input1())
Display2 = Button(root, height = 2,
				width = 20,
				text ="Decrypt",
				command = lambda:Take_input2())

inputtxt.pack()
Display1.pack()
Display2.pack()
Output.pack()

mainloop()
Output.delete("1.0", "end")


from tkinter import Tk   
from tkinter.filedialog import askopenfilename

method = input("decrypt/encrypt:")
encrypt_list = "./Encrypted_files.txt"
decrypt_list = "./Decrypted_files.txt"
file_path = "C:/Users/William Sanefski/Documents/Development_Projects/Python_Projects/"
def encrypt_file():

    Tk().withdraw()
    filename = askopenfilename()

    newfile = file_path + input("Enter Filename: ")
    encryption_file = open(newfile, "w")

    with open(filename, "r") as myfile:
        data = myfile.read()

    data = data[::-1]
    encryption_file.write(data)
    with open(encrypt_list, 'a+') as encryptval:
        encryptval.write("\n" + filename + "\n")
 
    print("File has been encrypted")
    encryption_file.close()
    

def decrypt_file():
    Tk().withdraw()
    filename = askopenfilename()
       
    with open(filename, "r") as myfile:
        data = myfile.read()
    decrypt_file = open(filename, "w")    
    data = data[::-1]
    decrypt_file.write(data)

    with open(decrypt_list, 'w+') as decryptval:
        decryptval.write("\n" + filename + "\n")

    decrypt_file.close()
    print("File has been decrypted!")



if method == "decrypt":
    decrypt_file()
elif method == "encrypt":
    encrypt_file()
else:
    print("You did not choose the right method please try again!")
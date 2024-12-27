
from art import text2art
import  time

print("Hello there this is MrWolf Tool logo maker!!!")
print("Made by MrW0lf of BruteBytes")

text = input("Type in your logo text : ")
arty = text2art(text)
print("This is your logo")
print(arty)

question = input("Do you want to save your logo in a file[y/N] :")

if question == "y" :
    file = open("wolfart.txt", "w")
    file.write(arty)
    file.close()
    print("Logo has been saved in current directory")
elif question == "N" or "n":
    print("File not saved")

import random
import requests

i = 1



while i < 6:
    val = int(input("inputkan angka : "))
    if val == 5 :
        print("benaar")
        break
    else:
        print("try")
        i +=1
        if i == 6:
            print("kesempatan habis")
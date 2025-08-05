import random



print("Selamat datang di Tebak Angka")


while True:
    i=0
    target = random.randint(1,10)
    chance = int(input("Masukkan jumlah kesempatan yang anda inginkan : "))
    while i < chance:
        val = int(input("inputkan angka : "))
        if val == target :
            print("Selamat Anda benar")
            break
        else:
            print("Coba Lagi")
            i +=1
            if i == chance:
                print("Kesempatan habis")
                print("Angka yang benar adalah : ", target)
                
    choice = input("Tekan Y untuk bermain lagi, tekan tombol lainnya jika ingin mengakhiri : ").lower()
    if choice != 'y':
        print("Goodbye!")
        break
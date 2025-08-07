import random



print("Selamat datang di Tebak Angka")


while True:
    i=0
    chance = int(input("Masukkan jumlah kesempatan yang anda inginkan : "))
    lower_limit = int(input("Masukkan limit bawah : "))
    upper_limit = int(input("Masukkan limit atas : "))
    target = random.randint(lower_limit, upper_limit)
    while i < chance:
        val = int(input("Inputkan angka : "))
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
import sys
# PROGRAM CONVERTER MATA UANG

# 1 Rp = 0,00007 usd, 1 usd = rp 14,347.35  
# 1 rp = 0,000059 euro, 1 euro = 16,191.75 rp
# 1 rp = 0,00045 yuan, 1 yuan = 2,220.11 rp
# 1 rp = 0,000051 poundsterling, 1 poundsterling = 19,737.89 rp
# 1 rp = 0,000094 sgd, 1 sgd = 10,668,93 rp

# ALGORITMA : program nanya user buat masukin nilai rupiah berapa, ditanya 

# define 
nilaiRupiah = []
nilaiUsd = []
nilaiEuro = []
nilaiYuan = []
nilaiPounds = []
nilaiSgd = []
kursUsd = float(0.00007)
kursEuro = float(0.000059)
kursYuan = float(0.00045)
kursPounds = float(0.000051)
kursSgd = float(0.000094)


# nilaiRupiah = [10000,20000,30000,40000,50000])

def rpValue():

    def appendArray(inputVar):
        if inputVar >=0 and inputVar <= 1000000000000000000:
            nilaiRupiah.append(inputVar)


    a = True
    while(a):                      
        print()
        print("  Masukkan nilai tanpa tanda nominal apapun ")
        print("            contoh : 10000             ")   
        input1 = int(input("Masukkan nilai rupiah ke-1 : "))
        appendArray(input1)

        input2 = int(input("Masukkan nilai rupiah ke-2 : "))
        appendArray(input2)

        input3 = int(input("Masukkan nilai rupiah ke-3 : "))
        appendArray(input3)

        input4 = int(input("Masukkan nilai rupiah ke-4 : "))
        appendArray(input4)

        input5 = int(input("Masukkan nilai rupiah ke-5 : "))
        appendArray(input5)
        
        a = False

def irToUsd():
    rpValue()
    for i in range(len(nilaiRupiah)):
        convertUsd = nilaiRupiah[i] * kursUsd
        nilaiUsd.append(convertUsd)
        print()
        print("====================================================")     
        print (f"Rp {nilaiRupiah[i]} sama dengan Usd {nilaiUsd[i]} ")
            
    del nilaiRupiah[:]
    del nilaiUsd[:]

    a = True
    while(a):
        print()
        print(" Ketik 'Ya' untuk kembali ke menu utama ")
        decision = input("Input : ")
        if (decision == 'YA' or decision == 'ya' or decision == 'yA'):
            sys.exit(home())
        else:
            print("error. Input sesuai perintah")

def irToEuro():
    rpValue()
    for i in range(len(nilaiRupiah)):
        convertEuro = nilaiRupiah[i] * kursEuro
        nilaiEuro.append(convertEuro)
        print()
        print("====================================================")     
        print (f"Rp {nilaiRupiah[i]} sama dengan Euro {nilaiEuro[i]} ")
            
    del nilaiRupiah[:]
    del nilaiEuro[:]

    a = True
    while(a):
        print()
        print(" Ketik 'Ya' untuk kembali ke menu utama ")
        decision = input("Input : ")
        if (decision == 'YA' or decision == 'ya' or decision == 'yA'):
            sys.exit(home())
        else:
            print("error. Input sesuai perintah")
    
def irToYuan():
    rpValue()
    for i in range(len(nilaiRupiah)):
        convertYuan = nilaiRupiah[i] * kursYuan
        nilaiYuan.append(convertYuan)
        print()
        print("====================================================")     
        print (f"Rp {nilaiRupiah[i]} sama dengan Yuan {nilaiYuan[i]} ")
            
    del nilaiRupiah[:]
    del nilaiYuan[:]

    a = True
    while(a):
        print()
        print(" Ketik 'Ya' untuk kembali ke menu utama ")
        decision = input("Input : ")
        if (decision == 'YA' or decision == 'ya' or decision == 'yA'):
            sys.exit(home())
        else:
            print("error. Input sesuai perintah")

def irToPoundsterling():
    rpValue()
    for i in range(len(nilaiRupiah)):
        convertPounds = nilaiRupiah[i] * kursPounds
        nilaiPounds.append(convertPounds)
        print()
        print("====================================================")     
        print (f"Rp {nilaiRupiah[i]} sama dengan Poundsterling {nilaiPounds[i]} ")
            
    del nilaiRupiah[:]
    del nilaiPounds[:]

    a = True
    while(a):
        print()
        print(" Ketik 'Ya' untuk kembali ke menu utama ")
        decision = input("Input : ")
        if (decision == 'YA' or decision == 'ya' or decision == 'yA'):
            sys.exit(home())
        else:
            print("error. Input sesuai perintah")

def irToSgd():
    rpValue()
    for i in range(len(nilaiRupiah)):
        convertSgd = nilaiRupiah[i] * kursSgd
        nilaiSgd.append(convertSgd)
        print()
        print("====================================================")     
        print (f"Rp {nilaiRupiah[i]} sama dengan Sgd {nilaiSgd[i]} ")
            
    del nilaiRupiah[:]
    del nilaiSgd[:]

    a = True
    while(a):
        print()
        print(" Ketik 'Ya' untuk kembali ke menu utama ")
        decision = input("Input : ")
        if (decision == 'YA' or decision == 'ya' or decision == 'yA'):
            sys.exit(home())
        else:
            print("error. Input sesuai perintah")

def home():
    print("================================")
    print("   CONVERTER NILAI MATA UANG    ")
    print("================================")
    print(" ")
    print(" ~ Pilihan Mata Uang : ")
    print(" 1. convert IR to USD ")
    print(" 2. convert IR to Euro ")
    print(" 3. convert IR to Yuan ")
    print(" 4. convert IR to Poundsterling ")
    print(" 5. convert IR to SGD ")
    print(" 6. Exit ")

    print(" Masukkan nomor untuk melakukan pengubahan mata uang ")
    print()
    x = True
    while(x):
        inputOpt = int(input("Nomor Pilihan : "))
        if inputOpt == 1:
            irToUsd()
            x = False
        
        elif inputOpt == 2:
            irToEuro()
            x = False
        
        elif inputOpt == 3:
            irToYuan()
            x = False
        
        elif inputOpt == 4:
            irToPoundsterling()
            x = False
        
        elif inputOpt == 5:
            irToSgd()
            x = False
        
        elif inputOpt == 6:
            print()
            print("Penelusuran selesai.")
            sys.exit(0)
        else:
            print(" Nomor pilihan tidak tersedia")

if __name__ == '__main__':
    home()
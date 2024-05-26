def hitung_kecepatan():
    print("hitungan kecepatan")
    jarak = float(input("masukan jarak (km): "))
    waktu = float(input("masukan waktu (km/jam): "))
    kecepatan = jarak/waktu
    print("kecepatan adalah: ", kecepatan, "m/s\n")

def luas_segitiga():
    print("hitungan segitiga")
    alas = float(input("masukan alas: "))
    tinggi = float(input("masukan tinggi: "))
    luas = 0.5 * (alas * tinggi)
    print("luas segitiga adalah: ", luas, "\n")

def luas_balok():
    print("hitungan luas balok")
    panjang = float(input("masukan panjang: "))
    lebar = float(input("masukan lebar: "))
    tinggi = float(input("masukan tinggi: "))
    luas = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
    print("luas balok adalah: ", luas, "\n")

def luas_bola():
    print("hitungan luas bola")
    r = float(input("masukan jari-jari: "))
    luas = 4 * 3.14 * (r**2)    
    print("luas bola adalah: ", luas, "\n")

while True:
    userinput = int(input(
        "pilih rumus yang akan dipakai: \n\n1.hitung kecepatan\n2.luas_segitiga\n3.luas_balok\n4.luas bola\n\n0.keluar program\n\nmasukan nomor: "))
    if(userinput == 1):
        hitung_kecepatan()
    elif(userinput == 2):
        luas_segitiga()
    elif(userinput == 3):
        luas_balok()
    elif(userinput == 4):
        luas_bola()
    else:
        break

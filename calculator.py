def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    while True:
        print(" Simple Calculator")
        print("1. Hitung Faktorial")
        print("2. Penjumlahan")
        print("3. Pengurangan")
        print("4. Keluar")
        
        pilihan = input("Pilih operasi (1/2/3/4): ")
        
        if pilihan == '1':
            angka = int(input("Masukkan angka untuk menghitung faktorial: "))
            hasil = factorial(angka)
            print(f"Faktorial dari {angka} adalah {hasil}")
        elif pilihan == '2':
            angka1 = float(input("Drop First Number: "))
            angka2 = float(input("Drop Second Number: "))
            hasil = angka1 + angka2
            print(f"Hasil penjumlahan: {hasil}")
        elif pilihan == '3':
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
            hasil = angka1 - angka2
            print(f"Hasil pengurangan: {hasil}")
        elif pilihan == '4':
            print("Terima kasih telah menggunakan kalkulator ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()

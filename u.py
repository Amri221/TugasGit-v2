kondisi = True
dataSiswa = []
while kondisi:                                   
    pilihan = input('''
=====================================================
  Selamat Datang di Program Sederhana dengan Python 
=====================================================
1. Persegi Panjang
2. Rata rata Nilai
3. Cek Bilangan Ganjil atau genap
4. Jumlah huruf vokal
5. Keluar
==================================
Masukkan pilihan kamu: ''')


    if pilihan == '1':
        panjang = float(input("\nMasukan Panjang: "))
        lebar = float(input("Masukan Lebar: "))

        luas = panjang*lebar
        keliling = 2 * (panjang+lebar)

        print("\nLuas Persegi Panjang \t\t:",luas)
        print("Keliling Persegi Panjang\t:",keliling)
    
    elif pilihan == '2':
        n = int(input("\nBanyaknya Nilai: "))

        print() #Membuat baris baru
        Nilai = []
        jum = 0

        for i in range(0, n):
           temp = int(input("Masukkan Nilai ke-%d: " % (i+1)))
           Nilai.append(temp)
           jum += Nilai[i]
           rata2 = jum / n
        print("\nRata-rata  = %0.2f" % rata2)

    elif pilihan == '3':
        x = int(input('Masukkan Bilangan: '))
        print(x,'adalah bilangan', 'genap' if (x % 2 == 0) else 'ganjil')
    
    elif pilihan == '4':
        teks = input("Masukkan Teks: ").lower()
        huruf_vokal={
            'a': 0,
            'i': 0,
            'u': 0,
            'e': 0,
            'o': 0,
        }
        total_huruf_vokal = 0

        for karakter in teks:
            if karakter in ['a', 'i', 'u', 'e', 'o']:
                huruf_vokal[karakter] += 1

        print(f'Total karakter: {len(teks)}')
        print(f'Total huruf vokal: {total_huruf_vokal}')
        print(f'''\
            a -> {huruf_vokal['a']})
            i -> {huruf_vokal['i']})
            u -> {huruf_vokal['u']})
            e -> {huruf_vokal['e']})
            o -> {huruf_vokal['o']})\
            ''')

    elif pilihan == '5':
     kondisi=False
      
while True:
    print("""
    [1] Toplama
    [2] Çıkarma
    [3] Bölme
    [4] Çarpma
    [5] Kuvvet Alma
    [Q] Çıkış
    """)
    işlem = input("Yapmak İstediğiniz işlemi Seçiniz: ")
    sayı_1 = int(input("Bir Sayı Giriniz: "))
    sayı_2 = int(input("Bir Sayı Giriniz: "))
    if işlem == "1":
        def toplama():
            toplam = (sayı_1 + sayı_2)
            print(f"Sonuç: {toplam}")
        toplama()
    elif işlem == "2":
        def çıkarma():
            çıkar = (sayı_1 - sayı_2)
            print(f"Sonuç: {çıkar}")
        çıkarma()
    elif işlem == "3":
        def bölme():
            böl = (sayı_1 / sayı_2)
            print(f"Sonuç: {böl}")
        bölme()
    elif işlem == "4":
        def çarpma():
            çarp = (sayı_1 * sayı_2)
            print(f"Sonuç: {çarp}")
        çarpma()
    elif işlem == "5":
        def kuvvet_alma():
            kuvvet = (sayı_1 ** sayı_2)
            print(f"Sonuç: {kuvvet}")
        kuvvet_alma()
    elif işlem == "q" or işlem == "Q":
        print("Çıkış Yapıldı...")
        break
    else:
        print("Hatalı Tuşlama Yaptınız...")
        break

    
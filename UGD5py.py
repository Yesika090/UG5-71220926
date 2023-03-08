def ganti_kata(kalimat, cari, ganti):
    # split kalimat menjadi list kata-kata
    kata_kalimat = kalimat.split()
    
    for i in range(len(kata_kalimat)):
        if kata_kalimat[i] == cari:
            kata_kalimat[i] = ganti
    
    kalimat_baru = " ".join(kata_kalimat)
    
    print(kalimat_baru)
kalimat = input("Masukkan kalimat: ")
cari = input("Kata yang ingin diganti: ")
ganti = input("Kata pengganti: ")
ganti_kata(kalimat, cari, ganti)
s



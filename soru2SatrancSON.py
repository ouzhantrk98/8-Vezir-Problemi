# -*- coding: utf-8 -*-
"""
Created on Fri May 14 23:50:44 2021

@author: oguzhan
"""

import random
import copy
import time


#satranç tahtasını oluşturan fonksiyon
def satrancTahtasiOlustur():
    rows,cols = 8,8
    arr = [[0 for x in range(rows)] for y in range(cols)] 
    
    
    for i in range(len(arr)):
    
        random_sayi = random.randint(0,7)
        
        tabloyuolustur(arr[i],random_sayi)
    
    
    #oluşturulan satranç tahtasını döndürelim...
    return arr
        
    #array_cakisma = satrancTahtasindaCakismaSayisiniBul(arr)
    
    #selectbestnode(array_cakisma,arr,0,0,0)

#rastgele her sütuna bir vezir yerleştiren fonksiyon
def tabloyuolustur(arr,sayi):
    
    arr[sayi] = 1
        

#satranç tahtasında olan toplam çakışma sayısını bulan fonksiyon
def cakismaSayisi(o_anki_satranc_tahtasi):
    
    konum_listesi = [0]*8 #8 tane vezir var çünkü
    
    cakisma_sayisi = 0
    
    say = len(konum_listesi)
    
    
    #vezilerin konumlarını bulalım
    
    for i in range(len(o_anki_satranc_tahtasi)):
        
        for j in range(len(o_anki_satranc_tahtasi[i])):
            
            if(o_anki_satranc_tahtasi[i][j] == 1):
                
                konum_listesi[i] = j

    
    while say>1:
        
        for j in range(1,say):
        
            if((konum_listesi[0] - j == konum_listesi[j]) or (konum_listesi[0] == konum_listesi[j]) or (konum_listesi[0] + j) == konum_listesi[j]):
                
                cakisma_sayisi += 1
        
        konum_listesi.pop(0)
        say-=1
    
    return cakisma_sayisi
    
#her vezirin gidebileceği 56 farklı yer için çakışma sayılarını bulan fonksiyon
def satrancTahtasindaCakismaSayisiniBul(array):
    
    rows,cols = 8,7
    array_cakisma = [[0 for x in range(cols)] for y in range(rows)] 
    
    arrayCopy = copy.deepcopy(array)
    
    #Vezir yalnızca satır bazında ve üst ve alt çaprazlar bazında çakışma yaşayabilir.
    #bunun için her veziri sütun boyu her kareye hareket ettirip 
    #Her konumda oluşan çakışma sayısını fonksiyon ile bulduruyoruz.
    for i in range(len(arrayCopy)):
        
        for j in range(len(arrayCopy[i])):
            
            if(arrayCopy[i][j] == 1):
                
                arrayCopy[i][j] = 0
                
                for k in range(j):
                    
                    arrayCopy[i][k] = 1
                    array_cakisma[i][k] = cakismaSayisi(arrayCopy)
                    arrayCopy[i][k] = 0
                    
                for m in range(j+1,len(arrayCopy)):
                    
                    arrayCopy[i][m] = 1
                    array_cakisma[i][m-1] = cakismaSayisi(arrayCopy)
                    arrayCopy[i][m] = 0
                
                arrayCopy[i][j] = 1
    
    return array_cakisma

#56 farklı hamle içerisinde her vezi için gidebilinen en iyi konumu seçen
#Yalnızca 1 tane olacak, fonksiyn
def selectbestnode(array_cakisma,node,satir_indeksi,hangi_satirda,hangi_sutunda,hamle_sayisi):
    
    #Her sütun için en düşük çakışma sayısı değeri ve sütunda bulunduğu indeks...
    #İlk değer minimum değer. İkincisi bulunduğu indeks
    dusuk_degerler = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    min_deger = 0
    
    nodeCopy = copy.deepcopy(node)
    
    for i in range(len(array_cakisma)):
        
        min_deger = array_cakisma[i][0]
        
        for j in range(len(array_cakisma[i])):
            
            if(array_cakisma[i][j] < min_deger):
                min_deger = array_cakisma[i][j]
                satir_indeksi = j
            
        dusuk_degerler[i][0] = min_deger
        dusuk_degerler[i][1] = satir_indeksi

    
    #min i tekrar tanımlayalım...
    min_deger = dusuk_degerler[0][0]
    for k in range(len(dusuk_degerler)):
        
        if(dusuk_degerler[k][0] < min_deger):
            
            min_deger = dusuk_degerler[k][0]
            hangi_satirda= k
            hangi_sutunda= dusuk_degerler[k][1]

    #Şimdi burada listeyi değiştirip yeniden yazdırmamız lazım 
    #daha sonra hill climbing fonksiyonunu yazacağız..

    kucukMu = False
    #Array deki vezirin konumunu değiştiren kod...
    #cakışma array i 8x7 lik olduğu için önce en küçük çakışmanın olduğu indeks
    #mevcut çakışmanın olduğu indeksten küçükse aynı şekilde yazıyoruz.
    #Değilse sütun değerini bir arttırıp veziri oraya koyuyoz
    #Çünkü mevcut vezirin konumunu sildik çakışma array inde
    for i in range(len(nodeCopy[hangi_satirda])):
        
        if(nodeCopy[hangi_satirda][i] == 1):
            nodeCopy[hangi_satirda][i] = 0
            
            if hangi_sutunda < i:
                kucukMu = True
    
    if(kucukMu):
        nodeCopy[hangi_satirda][hangi_sutunda] = 1
        hamle_sayisi+=1
    else:
        nodeCopy[hangi_satirda][hangi_sutunda+1] = 1
        hamle_sayisi+=1

    
    
    #Oluşan satranç tahtasını döndürelim...
    return nodeCopy,hamle_sayisi
    
#Şimdi hill climbing fonksiyonunu yazalım...

def hill_climbing(hamle_sayisi):
    
    node = satrancTahtasiOlustur()
    i =0
    while i<40:
        
        #Bu durumda amaca ulaşılmıştır.
        if(cakismaSayisi(node) == 0):
            return node,hamle_sayisi
        
        array_cakisma = satrancTahtasindaCakismaSayisiniBul(node)
        en_iyi_durum,hamle_sayisi = selectbestnode(array_cakisma,node,0,0,0,hamle_sayisi)
        
        if(cakismaSayisi(en_iyi_durum) < cakismaSayisi(node)):
            
            node = en_iyi_durum
        else:
            
            return [[0]],hamle_sayisi
        i+=1

def programi_calistir(liste,i):
    
    
    random_restart_sayisi = 0
    yapilan_hamle_sayisi = 0
    
    baslangic_zamani = time.monotonic()
    node,hamle_sayisi = hill_climbing(yapilan_hamle_sayisi)
    yapilan_hamle_sayisi=hamle_sayisi
    while(len(node) == 1):
        
        node,hamle_sayisi = hill_climbing(yapilan_hamle_sayisi)
        yapilan_hamle_sayisi=hamle_sayisi
        random_restart_sayisi+=1
        
    
    print("Çözüm ", (i+1))
    for m in range(len(node)):
        
        for n in range(len(node[m])):
            print(node[n][m]," ",end='')
        print()
    
    
    liste[i][0] = random_restart_sayisi
    liste[i][1] = yapilan_hamle_sayisi
    liste[i][2] = time.monotonic() - baslangic_zamani
    

def calistir():
    
    #Tüm durumların bilgilerini yazdırmak için listeye atalım...
    rows,cols = 25,3
    liste = [[0 for x in range(cols)] for y in range(rows)]
    
    
    
    i=0
    while i<25:
        
        programi_calistir(liste,i)
        i+=1
        
    print("\n\n")
    
    print("Random restart sayısı",end='')
    print("    Yapılan yer değiştirme Sayısı",end='')
    print("    İşlem süresi saniye cinsinden")
    
    say = 0
    for i in liste:
        print((say+1),") \t\t",i[0],end='')
        print("\t\t\t\t\t\t\t",i[1],end='')
        print("\t\t\t\t\t\t  %.4f sn" % (i[2]))    
        say+=1
    
    #25 başarılı çalıştırmanın ortalamasını veren kod..
    
    say = 0
    hamle_sayisi_ort = 0.0
    islem_suresi_ort = 0.0
    random_restart_ort = 0.0
    
    #i[0]: random restart sayısı
    #i[1]: Başarılı çalıştırmada vezirlerin yaptığı toplam hamle sayısı
    #i[2]: İşlem süresi saniye cinsinden
    for i in liste:
        random_restart_ort+=i[0]
        hamle_sayisi_ort+=i[1]
        islem_suresi_ort+=i[2]
    
    print("Ortalama hamle sayısı: %.2f" % (hamle_sayisi_ort/25))
    print("Ortalama random restart sayısı: %.2f" % (random_restart_ort/25))
    print("Ortalama işlem süresi: %.5f sn" % (islem_suresi_ort/25))
    
    
calistir()#Tüm kodu çalıştıran fonksiyon


    


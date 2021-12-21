# 8-Vezir-Problemi
8 vezir problemini hill climbing algoritması ile çözer

## Amaç
Bizden hill climbing algoritmasını kullanarak 8 vezir problemini çözmemiz isteniyor. Local minimum gibi hill climbing algoritmasının takıldığı durumlarda 8 vezir satranç tahtasında olacak şekilde rastgele vezirleri yeni konumlarına dağıtmamız isteniyor. 
Kural: Vezirler sadece kendi sütunlarında 56 farklı hamle yapabilirler. Satır boyunca veyahut çapraz boyunca hareket edemezler. 

## Programın Özellikleri
Yazılan program her çözümde satranç tahtasını konsol çıktısı olarak resmeder. Bunu yaparken vezirlerin gösterimi için 1 değerini kullanır. Ayrıca 25 farklı çözüm için yapılan rastgele yeniden başlatma sayısı (local maksimumda takıldığında) başarılı çalıştırmada (8 vezirin hiç çakışmadığı konumlara yerleştirildiği çalıştırma) yapılan hamle sayısı ve çözümü bulmak için bilgisayarın harcadığı süreyi saniye cinsinden konsolda tablo olarak gösterilecek şekilde yazdırır. 
Program çözümü bulurken önce vezilerin 56 farklı kareye gidebilmesi bilgisinden yararlanarak. Her vezir için kendi sütunundaki tüm karelerde bulunduğunda çakışma sayısı kaç oluyor bunu bulur. Bunları bir diziye atar. Bu dizi içerisinden en az çakışma değerine sahip vezirlerden bir tanesi (diyelim 8 çakışma değerine sahip 3 vezir varsa) bir tanesini seçer. (Her zaman ilk rastlanan en iyi değer seçiliyor) 
Döngüsel olarak satranç tahtasında 0 çakışmaya inesiye dek en iyileme işlemi devam eder. Local minimumda program restartlanır. 

## Programın Konsol Çıktıları
![Konsol Çıktıları 1](https://i.hizliresim.com/bxtk3ek.jpg)

![Kontrol Çıktıları 2](https://i.hizliresim.com/kdndqk0.jpg)

## Genel Tablo
![Genel Tablo](https://i.hizliresim.com/sno4eye.jpg)

## Ortalama Değerler
Program ortalama olarak 10-30 arası random restart ve 50-100 arası hamleyle sonucu bulur. Ortalama geçen süre 0.1 sn ile 0.01 sn arasında. Burada 4 farklı çalıştırma için ortalama değerler verilmiştir. 

![Ortalama Değerler](https://i.hizliresim.com/4mvuyfl.jpg)
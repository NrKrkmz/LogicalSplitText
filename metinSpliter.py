import random

def metinGirdisi():
    girilenMetin = input('Metni Buraya Girin = ')
    return girilenMetin # Metin Burada Belirlendi

def metinBolucu(metin):
    return metin.split('.') # Metni noktalarına göre ayırdık

def listeToStr(liste):
    yazı = ''
    for cumle in liste:
        yazı += cumle + '.'
    
    return yazı

def dosyaOlustur(dosyaNumarası, metin):
    dosyaİsmi = str(dosyaNumarası) # Dosya numarasını stringe çeviriyorum
    dosya = open(dosyaİsmi, 'w') # dosya ismini ve açılış formatını kullanarak dosyamızı açıyoruz
    dosya.write(metin) # Metnimizi dosyaya kaydediyoruz

def dosyaVar():
    kullanılanDosyalar = [] # Aynı dosyayı tekrar kullanmayalım diye tutuyoruz
    dosyaSayısı = int(input('Var Olan Son Dosya Numarasını Giriniz = ')) # Kullanıcı toplam dosya sayısını girmiş oluyor
    kontrol = 0 # Randomdan gelen dosya kullanılanlarda var mı diye bakıyorum
    sonucDosyası = open('SonucDosyam', 'w')
    
    kontrol = True
    while kontrol:
        kullanılanDosyaSayı = len(kullanılanDosyalar)
        
        if kullanılanDosyaSayı <= dosyaSayısı: 
            randomSayı = random.randint(0, dosyaSayısı)
            randomSayı = str(randomSayı)
            print('RANDOM SAYI = ', randomSayı)

            print('-----------------------')
            dosya = open(randomSayı, 'r')
            metin = dosya.read()

            print('METİN -->', metin)
            if randomSayı not in kullanılanDosyalar:
                kullanılanDosyalar.append(randomSayı)
                sonucDosyası.write(metin + ' ')
                print("kullanılanDosyalar", kullanılanDosyalar)
        else:
            kontrol = False

def dosyaYok():
    metin = metinGirdisi()
    metinListe = metinBolucu(metin)
    parca1 = [] # Metnin ilk parçasını temsil eden liste
    kelimeSayisi = 0 # Kelime sayısını kontrol ediyoruz
    sayac = 0 # Dosya numarasını ayarlamak için tuttuğumuz değişken

    for cumle in metinListe: # Metin Listesi içindeki cümlelerde dönüyorum
        cumleler = cumle.split(' ') # Cümleyi boşluklarına göre ayırıp cümledeki kelime sayısını buldum
        cumledekiKelimeSayisi = len(cumleler) # Cümledeki kelime sayısını tutuyorum
        parca1.append(cumle) # Cumleyi metin parçasına ekliyorum
        kelimeSayisi += cumledekiKelimeSayisi # Sınırlanmış kelime sayısını kontrol etmek için ayrı bir değişkende cümledeki kelime sayısını toplayarak sınırı kontrol ediyorum

        if kelimeSayisi >= 5: # Bu sınır aşılmadıysa
            dosyaOlustur(sayac, listeToStr(parca1)) # Metin parçası stringe dönüştürülüp dosya oluşturmaya yollanıyo
            parca1 = [] # Dosya oluşturulduktan sonra liste boşaltılıyor ki yeni dosyaya zemin hazırlansın
            sayac += 1 # Dosya numarasının da değişmesi için sayaç artırıldı
            kelimeSayisi = 0 # Yeni sınırı belirlemek için kelime sınırı sıfırlandı 

    if len(metinListe[-1].split(' ')) < 5:
        parca1.append(metinListe[-1]) # Listede kalan son eleman da dosyaya eklendi

    dosyaVar()

def main():
    dosyaVarmıYokmu = int(input('METİNLER VAR MI ?  YOKSA GİRİLECEK Mİ ?\n------VARSA --> 1\n------YOKSA --> 2'));

    if dosyaVarmıYokmu == 1:
        dosyaVar()
    elif dosyaVarmıYokmu == 2:
        dosyaYok()
    else:
        main()

main()
        
/**
 * created by cicek on Apr 13, 2020 00:43
 */

/*
160401002 - Bayram Çiçek

Konu : dynamic array – amortized cost
Teslim tarihi : 14 nisan 15:00 , hem sisteme hemde github a yüklenecek
Yüksek düzey bir dilde ( java, c# gibi ) dizi yapısını kullanan ve sadece:

    1. Append ( en sona eklenecek)
    2. Remove ( en son eklenen silinecek )
        methodlarını ieren bir class tanımlayıp her bir metod için programın main
        methodu içinde 5 tane örnek çağrım bir program yazınız. Tanımladığınız class
        içerisindeki array yapıdan kaynaklı overflow hatası vermemelidir.
        Bu günkü derste konuştuğumuz gibi tanımladığınız class da n,capacity ve array
        yapısını oluşturmak ve gerekli olduğu zaman çağrılan resize() fonksiyonun
        yazmalısınız.
        Rapor v.s. yazmanız gerekmiyor, kodunuzu gerekli yerlere comment ler
        ekleyerek son halini sisteme ve github hesabınıza haftaya kadar yüklemiş
        olursunuz
 */

/* karmaşıklık amortized cost olarak O(1),  */
public class DynamicArray {

    protected int uzunluk, capacity;
    protected int[] ilkDizi;

    public DynamicArray() {
        /* Create an empty array */
        this.uzunluk = 0;  // count actual elements
        this.capacity = 1;  // default array capacity

        /* 1 elemanlı bir yapı oluştur */
        ilkDizi = new int[capacity];

    }

    public int arraySize() {
        try {
            // ilkDizi'nin bellekte kapladığı yeri geri gönder.
            if (this.ilkDizi.length == 0)
                return 1;
            else
                return this.ilkDizi.length;

        } catch (Exception e) {
            System.out.println("hata" + e);
            return -1;
        }
    }

    public int arrayLength() {
        try {
            return this.uzunluk;

        } catch (Exception e) {
            System.out.println("hata" + e);
            return -1;
        }
    }

    public void append(int number) {
        // uzunluk -> kaç tane eleman var.
        // capacity -> toplam boyut

        /* uzunluk ve kapasite eşit ise diziyi genişlet */
        if (this.uzunluk == this.capacity) {
            this.resize(2 * this.capacity);
        }
        this.ilkDizi[uzunluk] = number;
        this.uzunluk += 1;
    }

    public void remove() {
        // direkt uzunluğu 1 azalttım
        this.uzunluk -= 1; // 1 azalttık

        // uzunluk, kapasitenin yarısına eşitse diziyi küçült
        if (this.uzunluk == this.capacity / 2) {
            this.resize(this.capacity / 2);
        }
    }

    public void resize(int c) {
        int[] yeniDizi = new int[c];

        System.out.println("şu an amortized cost işlemi... ");

        for (int i = 0; i < this.uzunluk; i++) {
            // mevcut elemanları yeni oluşturulan diziye kopyala
            yeniDizi[i] = this.ilkDizi[i];
            System.out.println("şu an move işlemi ...");
        }

        // yeniDizi'nin pointer'ını ilkDizi'nin pointer'ının üzerine yaz
        this.ilkDizi = yeniDizi;
        this.capacity = c;
    }


    public static void main(String[] args) {
        // nesne oluştur
        DynamicArray nesne = new DynamicArray();

        // ilk kapasite ve uzunluk göster
        System.out.printf("Uzunluk : %d\n" +
                        "Kapasite: %d\n\n",
                nesne.arrayLength(),
                nesne.arraySize());

        // eleman ekle
        for (int k = 0; k < 17; k++) {
            nesne.append(17);
        }

        /*
        5 defa eleman ekle için çıktı:

        Kapasite: 1
        Uzunluk : 0

        şu an amortized cost işlemi...
        şu an move işlemi ...
        şu an amortized cost işlemi...
        şu an move işlemi ...
        şu an move işlemi ...
        şu an amortized cost işlemi...
        şu an move işlemi ...
        şu an move işlemi ...
        şu an move işlemi ...
        şu an move işlemi ...

        Kapasite: 8
        Uzunluk : 5

        Process finished with exit code 0
         */

//        // 2049 defa eleman ekle
//        for (int k = 0; k < 2049; k++) {
//            nesne.append(-34);
//        } // ekleme örnekleri çoğaltılabilir
//        /* çıktı: Kapasite: 4096 Uzunluk : 2049  */

        // son kapasite ve uzunluk göster
        System.out.printf("\nUzunluk : %d\n" +
                        "Kapasite: %d\n\n",
                nesne.arrayLength(),
                nesne.arraySize());

        /* silme işlemi */

        // son elemanı sil
        for (int k = 0; k < 5; k++) {
            nesne.remove();
        }

        // son kapasite ve uzunluk göster
        System.out.printf("\nUzunluk : %d\n" +
                        "Kapasite: %d\n",
                nesne.arrayLength(),
                nesne.arraySize());

        /*
        5 defa son elemanı sil için çıktı:

        Uzunluk : 17
        Kapasite: 32

        şu an amortized cost işlemi...
        şu an move işlemi ...
        şu an move işlemi ...
        şu an move işlemi ...
        şu an move işlemi ...
        şu an move işlemi ...
        şu an move işlemi ...
        şu an move işlemi ...
        şu an move işlemi ...
        şu an move işlemi ...
        şu an move işlemi ...
        şu an move işlemi ...
        şu an move işlemi ...
        şu an move işlemi ...
        şu an move işlemi ...
        şu an move işlemi ...
        şu an move işlemi ...

        Uzunluk : 12
        Kapasite: 16

        Process finished with exit code 0
         */
    }
}

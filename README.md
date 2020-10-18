<h1><b>NVIDIA JETSON NANO İLE NESNE TAKİBİ</b></h1>
<b>1- NVIDIA JETSON NANO KARTI </b>
<br></br>
<p>NVIDIA Jetson Nano,  NVIDIA şirketinin geliştirmiş olduğu geliştirme kartıdır.
NVIDIA Jetson Nano geliştirme kartı, modern yapay zeka uygulamalarını  küçük  boyutta,  yüksek güçte ve düşük maliyette çalıştırmak için hesaplama performansını sunar. Yapay zeka uygulama geliştiricileri   artık görüntü sınıflandırma, nesne algılama, segmentasyon ve ses işleme gibi uygulamaları, yüksek maliyet ve yüksek donanımsal özelliklere gerek duymadan Jetson Nano geliştirme kartı ile yapabilmektedir ve sadece bu işlemleri yaparken yalnızca 5 watt güç harcamaktadır.</p>
<br>
<p>Örneğin; Jetson Nano, modern yapay zeka algoritmalarını hızlı bir şekilde çalıştırmak için 472 GFLOP sunar. Bu nedenle derin öğrenmede kullanılan birden çok sinir ağını paralel olarak çalıştırıp yüksek çözünürlüklü birkaç sensörü eş zamanlı olarak işleyerek uygulamalar üretebilirsiniz.</p>
<br></br>
<b>2- NVIDIA JETSON NANO KARTI GİRİŞ/ÇIKIŞ ÖZELLİKLERİ</b>
<br></br>
<p>NVIDIA Jetson kartının ön kısmında micro USB ve power jack girişleri bulunmaktadır. Bu girişler sayesinde geliştirme kartımıza enerji verebiliyoruz. Ayrıca micro USB girişine bilgisayarınıza bağlayıp monitör gibi dış birimlere gerek duymadan kullanabilirsiniz. 1 adet HDMI girişi bulunmaktadır. Bu giriş ile geliştirme kartını ekrana bağlayabilirsiniz ve bu durumdan dolayı NVIDIA firması Jetson Nano kartını bilgisayar gibi kullanabilme imkanı sunmaktadır. Bir başka giriş olarak Ethernet girişi bulunmaktadır. NVIDIA Jetson Nano geliştirme kartında WIFI modulü bulunmamaktadır Bu durumdan dolayı geliştirme kartınızı internete bağlamak için Ethernet girişini kullanmalısınız. Eğer WIFI ile bağlanmak istiyorsanız WIFI modulü almanız gerekmektedir. Son olarak 4 tane USB 3.0 girişi bulunmaktadır. USB giriş sayısı diğer geliştirme kartlarına göre fazla olmasından dolayı projelerinizde avantaj sağlamaktadır. Kartın üst tarafında ısınmaları minumum düzeye indirmek amacıyla soğutucu bulunmaktadır.</p>
<br></br>
<p>NVIDIA Jetson Nano kartının üzerinde 40 tane GPIO (General Purpose Input Output)  pini bulunmaktadır. Bu pinlerde 2 tane 5 volt girişi (vcc), 2 tane 3.3 volt girişi 8 tane toprak (GND) girişi bulunmaktadır. Aynı zamanda Jetson Nano geliştirme kartı haberleşme pinlerine sahiptir ve bu haberleşme pinleri ile diğer geliştirme kartları, mikrodenetleyiciler veya sistemler ile haberleşme yapılabilmektedir. Bu sayede Jetson Nano geliştirme kartı ile endüstriyel projeler yapabilme imkanınız bulunmaktadır.</p>
<br></br>
<b>3- NVIDIA JETSON NANO KARTI DONANIMSAL ÖZELLİKLERİ</b>
<br></br>
<b>3.1 GPU</b>
<p>GPU kavramından bahsedecek olursak; bilgisayar üzerinde görüntülenmekte olan yazı ve grafiklerin oluşturulması sırasında ekran ve işlemci arasında görev yapmakta olan dönüştürücülerdir. GPU; her bir piksel için ne yapılacağının kararını vermektedir. NVIDIA firması Jetson Nano geliştirme kartına GPU donanımı koyarak yüksek matematiksel işlemlerin yapılabilmesini sağlamışlardır. Nvidia Jetson Nano Kartı "Nvidia Maxwell 128 CUDA Çekirdeği"'ne sahiptir.</p>
<br></br>
<b>3.2 CPU</b>
<p>Merkezi işlem birimi olarak adlandırılan ve terminolojik kısaltması CPU olan işlemciler, milyonlarca transistörün silikon bir çip üzerinde birleştirilmesi ile meydana gelmektedir.
Aritmetik ve mantıksal işlem yapma yeteneğine sahip olan işlemciler, kısaca bilgisayarların verileri işleyen ve yazılım komutlarını gerçekleştiren bölümü olarak ifade edilebilir. NVIDIA Jetson Nano geliştirme kartı CPU’da ARM mimarisini kullanmaktadır. Verimliliği yüksek olmasından ve maliyeti düşük olmasından dolayı tablet, telefon vb. elektronik aletlerde kullanılmaktadır. Nvidia Jetson Nano Kartı "4-Core ARM A57 1.43 GHz"'e sahiptir. </p>
<br></br>
<b>3.3 BELLEK</b>
<p>Rastgele erişimli hafıza mikroişlemcili sistemlerde kullanılan bir tür veri deposudur. RAM; bilgisayar, ekran kartı ve birçok mikroişlemci modülünün içinde daimi olarak yer alan bir parçadır. Bilgisayarlar genellikle o an üzerinde çalıştıkları programlar ve işlemlerle ilgili bilgileri RAM diye adlandırılan bu hafıza bölümünde tutarlar. Nvidia Jetson Nano Kartı "   4 GB 64 Bit LPDDR4 | 25.6 GB/s"'ye sahiptir. </p>
<br></br>
<b>4- NVIDIA JETSON NANO KARTI KURULUM</b>
<br></br>
<b>4.1 GEREKLİ MALZEMELER</b>
<p>Nvidia Jetson Nano Kartının kurulumunu yapabilmek için şu malzemelere ihtiyaç vardır;       
ssss
</p>


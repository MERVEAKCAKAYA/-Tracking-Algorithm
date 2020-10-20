` 
	def pre_process(img):
	#Görüntüden yükseklik ve genişlik değerleri alınır.
	height, width = img.shape
 
	#Logaritma işlemi yapılır.
	img = np.log(img + 1)

	#Görüntü standardize edilir.
	img = (img - np.mean(img)) / (np.std(img) + 1e-5)

	# Hanning pencere fonksiyonu kullanılır
	window = window_func_2d(height, width)
    
	#Bu çerçeve görüntü üzerine uygulanır.
	img = img * window
    
	return img
`

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
<p>Nvidia Jetson Nano Kartının kurulumunu yapabilmek için şu malzemelere ihtiyaç vardır;   </p>
<li>Nvidia Jetson Nano Kart</li>
<li>64 GB Micro SD Kart</li>
<li>Nvidia Jetson Nano Kart Adaptörü</li>
<li>Mönitör</li>
<li>Ethernet Kablosu</li>
<li>HDMI Kablosu</li>
<li>Klavye, Mouse</li>
<br></br>
<b>4.2 GEREKLİ PROGRAMLAR</b>
<p>Nvidia Jetson Nano Kartının kurulumunu yapabilmek için şu programlara ihtiyaç vardır;   </p>
<li>SD Card Formatter</li>
<li>balenaEtcher</li>
<br></br>
<b>4.3 KURULUM ADIMLARI</b>
<br></br>
<p><b>Adım 1: </b>İlk olarak Jetson Nanoya işletim sistemi yüklemek gereklidir. SD karta işletim sistemini yüklemeden önce format atmalısınız. Bu sebeple bilgisayarınıza SD Card Formatter programını yükleyiniz. Bunun için aşağıdaki linki kullanarak bilgisayarınıza bu programı indiriniz.</p>
<p><li>https://www.sdcard.org/downloads/formatter/eula_windows/</p>
<p><b>Adım 2: </b>Bilgisayarınıza 64 GB boyutundaki SD kartınızı takınız ve SD Card Formatter programını çalıştırınız. Programı çalıştırınca ekrana aşağıdaki resimde görülen sekme gelecektir. Burada select card bölümünden sd kartınızı seçiniz ve Format butonuna basınız. Biraz bekledikten sonra sd kartınıza format atıldığına dair bildirim gelecektir. Kartı bilgisayarınızdan çıkarmadan diğer adımlara geçiniz. </p>
<img src="https://developer.nvidia.com/sites/default/files/akamai/embedded/images/jetsonNano/gettingStarted/Jetson_Nano-Getting_Started-Windows-SD_Card_Formatter.png"></img>
<br></br>
<p><b>Adım 3: </b>Sd karta işletim sistemini yüklemek için bilgisayarınıza balenaEtcher programını yükleyiniz. Bunun için aşağıdaki linki kullanarak bilgisayarınıza bu programı indiriniz. </p>
<p><li>https://www.balena.io/etcher/</p>
<p><b>Adım 4: </b>Bu adımda sd karta yüklenecek işletim sistemi indirilecektir. Bunun için aşağıdaki linke tıklayarak indirme işlemini başlatınız. Dosya boyutu büyük olduğundan bu işlem uzun sürebilir. İndirme işlemi sonucunda .zip dosyası inecektir. Kesinlikle bu dosyayı zipten çıkarmayınız. Sd karta .zip haliyle yüklenmesi gerekmektedir. </p>
<p><li>https://developer.nvidia.com/jetson-nano-sd-card-image</p>
<p><b>Adım 5: </b>Bilgisayarınızda 64 GB boyutundaki SD kartınızın takılı olduğunu kontrol ediniz ve ardından balenaEtcher programını çalıştırınız. Programı çalıştırınca ekrana aşağıdaki resimde görülen sekme gelecektir. Burada select image bölümüne tıklayınız ve daha önceden bilgisayarınıza indirmiş olduğunuz .zip halinde olan jetson nano card image'i seçiniz. Select drive bölümünde bilgisayarınıza takılı olan 64 GB boyutundaki sd kartı seçiniz. Artık Flash butonuna basmaya hazırsınız. Flash butonuna basınız ve işletim sistemi sd karta yazılmaya başlasın.  </p>
<img src="https://developer.nvidia.com/sites/default/files/akamai/embedded/images/jetsonNano/gettingStarted/Jetson_Nano-Getting_Started-Windows-Etcher.png"></img>
<br></br>
<p><b>Adım 6: </b>Bu işlemler sırasında ekrana aşağıdaki gibi uyarı sekmeleri gelecektir. Bunların hepsini tek tek kapatınız. </p>
<img src="https://developer.nvidia.com/sites/default/files/akamai/embedded/images/jetsonNano/gettingStarted/Jetson_Nano-Getting_Started-Windows-Etcher_Cancel.png"></img>
<br></br>
<p><b>Adım 7: </b>Sd karta işletim sistemi yükleme işlemi başarıyla bittiğinde artık sd kart kullanıma hazırdır. Sd kartınızı bilgisayarınızdan çıkarabilirsiniz. Çıkarttığınız sd kartı Jetson Nano kartına takınız. Ardından HDMI, Ethernet, Klavye, Mouse ve güç adaptörü bağlantısını yapınız. </p>
<img src="https://developer.nvidia.com/sites/default/files/akamai/embedded/images/jetsonNano/gettingStarted/Jetbot_animation_500x282_2.gif"></img>
<br></br>
<p><b>Adım 8: </b>Tüm adımları doğru bir şekilde yaptıysanız mönitöre akan yazıların gelmesi gerekmektedir. Biraz bekledikten sonra sistem ayarlarının yapılacağı ekranla karşılaşacaksınız. Buradan şifrenizi, isminizi, bölgenizi vb. şeyleri seçeceksiniz. Ardından aşağıdaki gibi ekran görüntüsüyle karşılaşacaksınız. Bu kurulum adımlarını başarılı bir şekilde tamamladığınızı göstermektedir.</p>
<img src="https://miro.medium.com/max/2728/1*8dx4DOn86dsWs-4Iy74uxg.png"></img>
<br></br>
<p><b>Adım 9: </b>Masaüstünde sağ tık yapıp open terminal seçeneğine tıklayınız. Açılan terminale sudo apt-get update yazıp enter'a basınız. Sizden şifre isteyecektir. Sistem ayarları sırasında belirlediğiniz şifreyi girip enter'a basınız. Güncelleme işleminin bitmesini bekleyiniz. İşlem bittikten sonra terminali kapatabilirsiniz. Artık Jetson Nano Geliştirme Kartını kullanabilirisiniz.</p>

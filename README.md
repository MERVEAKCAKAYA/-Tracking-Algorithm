![title](C:/Users/merve/Desktop/MARKDOWN/k/1.png)
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
<p>https://www.balena.io/etcher/</p>
<p><b>Adım 4: </b>Bu adımda sd karta yüklenecek işletim sistemi indirilecektir. Bunun için aşağıdaki linke tıklayarak indirme işlemini başlatınız. Dosya boyutu büyük olduğundan bu işlem uzun sürebilir. İndirme işlemi sonucunda .zip dosyası inecektir. Kesinlikle bu dosyayı zipten çıkarmayınız. Sd karta .zip haliyle yüklenmesi gerekmektedir. </p>
<p>https://developer.nvidia.com/jetson-nano-sd-card-image</p>
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
<br></br>
<b>5- MOSSE TAKİP ALGORİTMASI</b>

<p>MOSSE, basit şablonlardan daha iyi performans gösteren ve giriş görüntülerini ideal çıktılarıyla eşleyen korelasyon filtreleri oluşturur. Bu, arka plan ile etkileşimi azaltır ve daha iyi performans sağlar. MOSSE filtreleri, bir nesnenin aydınlatma, ölçek, poz ve şeklindeki değişikliklere karşı dayanıklıdır. Bir nesne, filtreyi başlatmak için seçilir. Etiketleme için nesneyi seçtikten sonra nesnenin çevresine bir pencere çizilir. Bu pencere başlatma sırasında şablonu ve takip sırasında takip penceresini temsil eder. Takip sırasında filtreyi başlatmak ve güncellemek için şablon kırpılır. Filtreyi başlatmadan ve nesneyi izlemeden önce videonun her karesinde bir ön işleme adımı gerçekleştirilir. 
Ön işleme adımından elde edilen şablon, Fourier alanına dönüştürülür. Sonrasında filtreyi başlatmak ve güncellemek için yapay bir çıktı üretilir. Yapay çıktı da Fourier alanına dönüştürülür ve filtre Fourier alanında hesaplanır. Korelasyonun çıktısı, izleme sırasında videonun sonraki karelerinde nesnenin yeni konumunu bulmak için uzamsal alana geri dönüştürülür.
Korelasyon çıktısındaki maksimum değere karşılık gelen konum hedefin yeni konumunu gösterir. Daha sonra bu yeni konuma bağlı olarak gerçek zamanlı bir güncelleştirme gerçekleştirilir. Tüm bu işlemler, hesaplamaları daha hızlı yapabilmek için Fourier alanında gerçekleştirilir.
</p>
<p>Bir takipçinin başlatılması için aşağıdaki adımlar gereklidir:</p>
<p>1- Bir şablon elde etmek ve bu şablonu ön işlemeden geçirmek
</p>
<p>2- Bir yapay hedef oluşturmak </p>
<p>3- Hem önceden işlenmiş şablonu hem de yapay hedefi uzamsaldan Fourier etki alanına dönüştürmek</p>

<b>5.1 ÖN İŞLEME</b>
<br></br>
<p>MOSSE filtresi ile takip algoritması, iki ana bileşenden oluşur : filtreyi başlatma ve nesneyi takip etme. Filtreyi başlatma veya takip işlemi öncesinde videonun her karesi üzerinde bir ön işleme (preprocessing) gerçekleştirilir. 

Ön işleme adımları aşağıda açıklanmıştır:</p>

<li>Şablon, grayscale bir görüntüye dönüştürülür.</li>
<li>Bir önceki adımdan elde edilen şablonda aşağıdaki denklem kullanılarak log dönüşümü gerçekleştirilir

x= ln(x+ 1)</li>
<li>x giriş görüntülerinin piksel değerleridir. Log işlevi, ışık efektlerini azaltmak ve kontrastı artırmak için uygulanır.</li>
<li>Şablonun piksel değerleri, standardizasyon işlemine sokulur ve şablon kenara yakın piksel değerlerini yavaş yavaş sıfıra düşüren bir kosinüs penceresi ile çarpılır.
</li>
<li>Standardizasyon, aydınlatmadaki değişimin etkilerini azaltmada ve videonun farklı kareleri arasındaki aydınlatma tutarlılığının korunmasında fayda sağlar.</li>
<li>Önceki adımda elde edilen şablon uzamsal etki alanından Fourier etki alanına dönüştürülür. Fourier dönüşümü, bir sinyali sinüs ve kosinüs bileşenlerine ayrıştırmak için kullanılır. Görüntü analog bir sinyal değildir, bu nedenle görüntü için ayrı bir Fourier dönüşümü (FFT) kullanılır. Bu dönüştürmenin çıktısı Fourier veya frekans etki alanında görüntüyü temsil eder. Bu işlemin python kodu aşağıda verilmiştir.</li>


```
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

def window_func_2d(height, width):
	#Bu fonksiyon cosinus penceresini oluşturmak için kullanılır.
	#Hanning fonksiyonu ile pencere için gerekli değerler oluşturulur.
	win_col = np.hanning(width)
	win_row = np.hanning(height)

	#Satır ve sütun değerleri hanning den gelen değerler kullanılarak maskelenir.
	mask_col, mask_row = np.meshgrid(win_col, win_row)

	#Pencere oluşturulur.
	win = mask_col * mask_row
	return win

```
<br></br>
<b>5.2 YAPAY HEDEF</b>
<p>Yapay hedef, izlenecek nesnenin konumunda Gaussian tepe noktasına sahip ve yapay olarak oluşturulmuş bir görüntüdür. Yapay bir hedef giriş görüntüsünü, filtre oluşturmak için ilgili korelasyon çıkışıyla eşlemek için kullanılır. Aşağıdaki denklem hedef görüntüyü yapay hedef haline getirmek için kullanılır.
</p>
<p>İlk görüntüde bir hedef belirleniyor ve pencere içine alınıyor, ikinci görüntü de ise hedefin merkezi Gaussian tepe noktası olarak kullanılıyor ve bir yapay hedef oluşturuluyor. Bu işlemin python kodu aşağıda verilmiştir. </p>

```
def _get_gauss_response(self, img, gt):

    	#Görüntüden yükseklik ve genişlik değerleri alınır.
    	height, width = img.shape
    	# 2d boyutlu bir ızgara oluşturmak için gerekli x ve y değerleri alınır.
    	xx, yy = np.meshgrid(np.arange(width), np.arange(height))

    	# Hedefin merkez koordinatları alınır.
    	center_x = gt[0] + 0.5 * gt[2]
    	center_y = gt[1] + 0.5 * gt[3]

   	 
    	# Formüldeki üs değeri hesaplanır.
    	dist = (np.square(xx - center_x) + np.square(yy - center_y)) / (2 * self.sigma)

    	# e üzeri dist değeri bulunur.
    	response = np.exp(-dist)
 	 
    	# Min-Max normalizasyonu yapılır.
    	response = linear_mapping(response)
 
    	return response

```

<br></br>
<b>5.3 TAM FİLTRE (EXACT FİLTER)</b>
<p>Filtrenin başlatıldığı bir şablonla ilişkilendirildiğinde tam bir filtre, nesnenin konumunda güçlü bir tepe ve diğer tüm konumlarda sıfır değerleri üretir. Tam filtre, giriş görüntüsünü hedef çıkış görüntüsüne tam olarak dönüştürebilmesi nedeniyle bu adı alır. Başlatma verileri bir çift eğitim görüntüsünden, bir şablondan ve bir yapay hedeften oluşur. Tam filtreyi oluşturmak için aşağıdaki adımlar izlenir :
</p>
<p>1- Yapay hedef, Hızlı Fourier Dönüşümü kullanılarak Fourier alanına dönüştürülür. Python dilinde numpy paketindeki np.fft.fft2 () fonksiyonu görüntüleri Fourier etki alanına dönüştürmek için kullanılır.</p>
<p>2- Tam filtreyi elde etmek için aşağıdaki denklem kullanılır:
</p>
<p>3- H*, frekans alanındaki filtrenin kompleks bir eşleniğidir. F, Fourier etki alanındaki önceden işlenmiş şablondur.G, Fourier alanındaki yapay hedef görüntüsüdür ve F*, F'nin kompleks bir eşleniğidir. Element-wise çarpma ⊙ sembolü ile gösterilir.  sıfıra bölmeyi önlemek için kullanılır ve çok küçük bir değer ifade eder.
</p>
<p>Bu işlemin python karşılığı aşağıda verilmiştir. Kod içerisinde Ai değeri formüldeki pay kısmını gösterirken Bi değeri paydayı göstermektedir. Sonrasında H*değeri bulunurken Ai / Bi işlemi yapılmaktadır. </p>

```
def _pre_training(self, fi, G):
   	 
    	#fi değişkeninin eşleniği alınır.
    	fiC=np.conjugate(fi)

    	#Formüldeki Ai bulunur.
    	Ai = G * fiC
   	 
    	#Formüldeki Bi bulunur.
    	Bi = fi * fiC
   	 
    	return Ai, Bi

```
<p>Bu kısıma kadar yapılan işlemler takipçinin başlatması için gereklidir. Tüm bu işlemlerin yazıldıldığı başlatma fonksiyonun python kodu aşağıda verilmiştir.</p>

```
def __init__(self,frame,roi,sigma,lr):

    	#Alınan ilk kare init-img değişkenine atanır.
    	self.init_img = frame

    	#Sigma değeri belirlenir.
    	self.sigma=sigma

    	#Öğrenme katsayısı(learning rate) belirlenir.
    	self.lr=lr

    	#Görüntü griye döndürülür.
    	init_frame = cv2.cvtColor(self.init_img, cv2.COLOR_BGR2GRAY)

    	#Görüntü float32 tipine dönüştürülür.
    	self.init_frame = init_frame.astype(np.float32)
   	 
    	#Seçilen hedefi içine alan pencere init_gt değişkenine atanır.
    	init_gt = roi

    	#Pencere int64 tipine dönüştürülür.
    	self.init_gt = np.array(init_gt).astype(np.int64)

    	#Yapay hedef için gerekli gauss dağılımı fonksiyonu çalıştırılır.
    	self.response_map = self._get_gauss_response(self.init_frame, self.init_gt)
   	 
    	#Gauss dağılımından hedefimizin bulunduğu pencere çıkartılır ve g değişkenine atanır.
    	g = self.response_map[self.init_gt[1]:self.init_gt[1]+self.init_gt[3], self.init_gt[0]:self.init_gt[0]+self.init_gt[2]]
   	 
    	#g değişkeni fourier alanına dönüştürülür. (İşlemlerin daha hızlı çalışması için her değişken fourier alanına dönüştürülür)
    	self.G = np.fft.fft2(g)

    	#Hedefimizin bulunduğu pencere tüm resimden kesilir ve fi değişkenine atanır.
    	self.fi = self.init_frame[self.init_gt[1]:self.init_gt[1]+self.init_gt[3], self.init_gt[0]:self.init_gt[0]+self.init_gt[2]]
   	 
    	#fi değişkeni ön işlemeden geçirilir.
    	self.fi = pre_process(self.fi)

    	#fi değişkeni fourier alanına dönüştürülür.
    	self.fi = np.fft.fft2(self.fi)

    	#Ai ve Bi değerleri bulunur
    	self.Ai, self.Bi = self._pre_training(self.fi, self.G)

    	#Seçilen alanın x y ve w h değerleri pos dizisine alınır.
    	self.pos = self.init_gt.copy()

    	#Yine aynı alanın (x,y) ve ((x+w),(y+h)) değerleri clip_pos dizisine alınır.
    	self.clip_pos = np.array([self.pos[0], self.pos[1], self.pos[0]+self.pos[2], self.pos[1]+self.pos[3]]).astype(np.int64)

```

<br></br>
<b>5.4 GÜNCELLEME VE TAKİP</b>
<p>Takipçi, filtreyi başlattıktan sonra hedefi izlemeye başladığında, her kare için hedefin yeni bir konumu elde edilir. Hareketli bir izleme penceresi için pencerenin merkezi, her yeni kare için elde edilen nesnenin yeni konumu ile güncellenir. Hedefin yeni x - y koordinatları izleme penceresinin yeni merkezi olur. 
Hedefin yeni konumunun öğrenilmesi için aşağıdaki formülden yararlanılır :

Yeni gelen kare için hedef pencere ön işlemeden geçirilir ve yeni birFi bulunur. Önceki adımlarda Gi / Fi işlemi yapılarak H*değeri bulunmuştu. Sonrasında bu değişkenler denklemde yerine yazılır ve G değeri (FFT den geçirilirmiş gauss dağılımı) elde edilir. Bu değer üzerinden tekrar FFT uygulanır ve gauss dağılımının yeni kare için güncellenmiş hali elde edilir. Bu dağılımın maksimum değeri takip penceresinin yeni merkezini verir. 

</p>
<p>Takip penceresi yeni konumuna getirildikten sonra Fi değeri bu konum için tekrar hesaplanır ve aşağıdaki denklemler kullanılarak takip filtresi güncellenir :

η öğrenme oranıdır. Bu oran ile son karelere daha fazla ağırlık verilir ve önceki karelerin etkisinin zamanla azalması sağlanır. Bu oran denemeler sonucunda 0.125 olarak belirlenmiştir. 

Bu işlemin python kodu aşağıda verilmiştir.
</p>

```

def update(self,frame):

    	#Güncel kare alınır ve current_frame değişkenine atanır.
    	current_frame = frame

    	#Kare griye dönüştürülür.
    	frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    	frame_gray = frame_gray.astype(np.float32)

    	#Formülden Hi değeri (tam filtre) bulunur.
    	Hi = self.Ai / self.Bi
    	height, width = self.fi.shape
   	 
    	#Önceki takip pencerisi yeni kare üzerinden alınır ve fi değişkenine atanır.
    	fi = frame_gray[self.clip_pos[1]:self.clip_pos[3], self.clip_pos[0]:self.clip_pos[2]]

    	#Yeni fi değeri ön işlemeden geçirilir ve fourier alanına dönüştürülür.
    	self.fi = np.fft.fft2(pre_process(fi))

    	#Formülden Gi değeri bulunur.
    	Gi = Hi * self.fi

    	#Gi değeri üzerinden ters fft ve normalizasyon yapılarak gauss dağılımı elde edilir.
    	gi = linear_mapping(np.fft.ifft2(Gi))
   	 
    	#Dağılımın maksimum değeri alınır
    	max_value = np.max(gi)
   	 
    	#Yeni dağılımın tepe noktası bulunur ve merkez noktası ile arasındaki fark dx ve dy değişkenlerine atanır.
    	max_pos = np.where(gi == max_value)
    	dy = int(np.mean(max_pos[0]) - gi.shape[0] / 2)
    	dx = int(np.mean(max_pos[1]) - gi.shape[1] / 2)
   	 
    	# Koordinatlar güncellenir.
    	self.pos[0] = self.pos[0] + dx
    	self.pos[1] = self.pos[1] + dy

    	# Yeni koordinatlar kare dışına taşmayacak şekilde clip_pos değişkenine atanır. [xmin, ymin, xmax, ymax]
    	self.clip_pos[0] = np.clip(self.pos[0], 0, current_frame.shape[1])
    	self.clip_pos[1] = np.clip(self.pos[1], 0, current_frame.shape[0])
    	self.clip_pos[2] = np.clip(self.pos[0]+self.pos[2], 0, current_frame.shape[1])
    	self.clip_pos[3] = np.clip(self.pos[1]+self.pos[3], 0, current_frame.shape[0])
    	self.clip_pos = self.clip_pos.astype(np.int64)

    	# Yeni fi değeri bulunur.
    	fi = frame_gray[self.clip_pos[1]:self.clip_pos[3], self.clip_pos[0]:self.clip_pos[2]]

    	#Yeni fi değeri ön işlemeden geçirilir ve fourier alanına dönüştürülür.
    	self.fi = np.fft.fft2(pre_process(fi))

    	# Formül kullanılarak Ai ve Bi değerleri güncellenir.
    	self.Ai = self.lr * (self.G * np.conjugate(self.fi)) + (1 - self.lr) * self.Ai
    	self.Bi = self.lr * (self.fi * np.conjugate(self.fi)) + (1 - self.lr) * self.Bi
   	 
    	# Takip penceresi kare üzerine çizilir.
    	cv2.rectangle(current_frame, (self.pos[0], self.pos[1]), (self.pos[0]+self.pos[2], self.pos[1]+self.pos[3]), (255, 0, 0), 2)
    	return current_frame

```

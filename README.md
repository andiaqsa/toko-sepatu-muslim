1). Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2). Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3). Jelaskan fungsi git dalam pengembangan perangkat lunak!
4). Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
5). Mengapa model pada Django disebut sebagai ORM?

                        Jawab:
1). Langkah-langkah yang dilakukan:
1. Membuat direktori utama, saya menamakannya toko-sepatu-muslim
2. Mengaktifkan virtual environment melalui command prompt
3. Menjalankan perintah di command prompt untuk membuat aplikasi bernama main di dalam proyek e-commerce
4. Mendaftarkan aplikasi main dengan menambahkan 'main' ke variable INSTALLED_APPS di file setting.py
5. Membuat direktori bernama templates didalam aplikasi main, kemudian membuat dan mengisi file main.html
   yang berisi:
    name sebagai nama item dengan tipe CharField,
    price sebagai harga item dengan tipe IntegerField, dan
    description sebagai deskripsi item dengan tipe TextField.
6. Menghubungkan view dengan template dengan cara membuka file views.py di file aplikasi main
7. Kemudian menambahkan fungsi show_main dibawah impor, contoh:
    def show_main(request):
    context = {
        'Name' : 'Andi Aqsa',
        'Price': 'Rp300.000',
        'Description': 'sepatu ini dibuat menggunakan bahan yang bagus, serta produk original'
    }
    return render(request, "main.html", context)
8. Modifikasi template, ubah template main.html dengan mengubah name, price, dan 
   description menjadi struktur kode Django yang sesuai untuk menampilkan data. 
   Contoh:
   {{ Name }}, {{ Price }} dan {{ Description }}

9. Mengonfigurasi Routing URL Aplikasi main, dengan mengubah urls.py dengan kode berikut:
   from django.urls import path
   from main.views import show_main
   app_name = 'main'
   urlpatterns = [
    path('', show_main, name='show_main'),
   ]
10. Menambahkan rute URL dalam urls.py proyek untuk menghubungkannya ke tampilan main
11. Buka berkas urls.py di dalam direktori proyek toko-sepatu-muslim, 
    bukan yang ada di dalam direktori aplikasi main. 
12. Lalu menambahkan import, from django.urls import path, include
13. Menambahkan rute url untuk mengarahkan ke tampilan main di dalam variabel urlpatterns
   urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
    ]
14. Berkas urls.py ini bertanggung jawab untuk mengatur rute URL tingkat proyek
15. Menjalankan proyek Django dengan perintah python manage.py runserver
16. Kemudian buka link http://localhost:8000/ di web browser untuk melihat halaman yang sudah dibuat
17. Kemudian membuat proyek baru di pws
18. Pada settings.py di proyek Django yang sudah kamu buat tadi,
    tambahkan URL deployment PWS pada ALLOWED_HOSTS. ...
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "andi-aqsa-tokosepatumuslim.pbp.cs.ui.ac.id"]
19. Setelah mendapatkan Project Credentials dan Project Command, jalankan instruksi project command


2)...

3). Fungsi git dalam pengembangan perangkat lunak adalah:
    • Membantu mengorganisir folder project dengan optimal sesuai versinya. Dimana akan tersimpan 1 project yang disimpan dengan menggunakan database khusus dengan isi dokumen semua file versi proyek yang Anda miliki.  

    • Open Source, bisa dilakukan dengan gratis dan kompatibel untuk semua jenis sistem operasi.

    • Mudah berkolaborasi, akan memudahkan programmer untuk bisa bekerja sama dengan programmer yang lainnya untuk membuat atau mengembangkan sistem.

    • Backup, programmer bisa mendapatkan kemudahan untuk melakukan restore script program untuk kembali pada kondisi yang sebelumnya.

    • Platformnya fleksibel, sehingga bisa dipakai untuk mengerjakan beragam proyek bersama dengan tim yang Anda miliki.

4). Menurut saya, Framework django dijadikan permulaan dalam pembelajaran pengembangan perangkat lunak karena:
    • Django dilengkapi banyak fitur bawaan, sehingga bisa lebih         memudahkan bagi pemula dan dapat lebih menghemat waktu.
    • Django menggunakan pola Model-View-Template (MVT), sehingga dapat lebih mudah dipelajari tentang pembagian tanggung jawab di dalam aplikasi
    • Django mudah diiintegrasikan dengan teknologi lain, seperti penyimpanan file, API dan cloud.
    • Django memungkinkan pengembangan cepat karena alat dan fitur yang dibangun di dalamnya.

5). Disebut sebagai ORM (Object-Relational-Mapping) karena model di Django bertindak sebagai penghubung antara objek Python dan relasi database, sehingga memungkinkan pengembang bekerja dengan database menggunakan objek Python tanpa menulis query SQL secara langsung. 



                Tugas 5 
Andi Aqsa Mappatunru Marzuki
2306275046

1). Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Urutan prioritas pengambilan CSS Selector adalah berdasarkan specificity dan cascadenya, yaitu:
 • Inline Styles, yang ditulis pada HTML dengan atribut style= ""
 • ID Selector, seperti 
 #my-id {
    color: red;
 }
 • Class Selector,Attribute Selector, Pseudo-class
  contohnya;
  .my-class {
    color: blue;
  }

  [type="text"] {
      color: red;
  }

  :hover {
      color: yellow;
  }

• Element/Tag Selector
    div {
    color: yellow;
    }

2). Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Responsive design penting dalam pengembangan aplikasi web karena memungkinkan sebuah website untuk menyesuaikan tampilannya secara dinamis berdasarkan perangkat yang digunakan oleh pengguna, seperti desktop, tablet, atau ponsel.
contoh aplikasi yg sudah menerapkan responsive design: Youtube, Twiter
Aplikasi yang belum menggunakan: website pemerintah yang sudah lama


3). Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

• Padding adalah ruang antara konten elemen dan border elemen. Padding mengontrol jarak di dalam elemen itu sendiri, antara konten elemen (seperti teks atau gambar) dan tepi dalam elemen.

cara implementasi:
div {
    padding: 20px;  /* Menambahkan padding 20px ke semua sisi */
}

• Border adalah garis pembatas yang mengelilingi elemen HTML, antara padding dan margin. Border memisahkan konten dan padding elemen dari elemen lainnya di luar elemen tersebut.
cara implementasi:
div {
    border: 2px solid black;  /* Border hitam solid dengan ketebalan 2px */
}

• Margin adalah ruang di luar border elemen. Margin mengontrol jarak antara elemen satu dengan elemen lainnya di dalam halaman.
cara implementasi:
div {
    margin: 10px;  /* Memberikan jarak 10px pada semua sisi elemen */
}

4). Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Konsep Utama Flex box:
Flex box mengatur elemen di sepanjang satu sumbu, baik sumbu utama (row atau column) maupun sumbu silang (cross axis).
Cocok digunakan untuk tata letak satu dimensi: mengatur elemen dalam satu arah, baik secara horizontal maupun vertikal.
Fleksibel dan responsif terhadap perubahan ukuran layar atau kontainer.

Kegunaan Flex box:
Sangat cocok untuk layout sederhana: Seperti mengatur navbar, mengatur elemen dalam satu baris atau kolom, atau mengatur kotak di dalam kolom/baris tunggal.
Penggunaan populer: Header, footer, navigation bar, card layout, dan tata letak sederhana di mana elemen-elemen perlu diatur secara fleksibel.

Konsep Utama Grid Layout:
Grid menggunakan baris dan kolom, yang memungkinkan pembuatan tata letak dua dimensi.
Setiap elemen grid ditempatkan di cell tertentu yang dapat direntangkan di beberapa baris atau kolom.
Memungkinkan kontrol yang lebih presisi dibandingkan flexbox dalam tata letak kompleks.

Kegunaan Grid Layout:
Sangat cocok untuk layout kompleks: Seperti tata letak halaman dengan banyak kolom dan baris (misalnya, layout dashboard, galeri gambar, atau tata letak majalah).
Mudah mengatur elemen secara dua dimensi: Elemen dapat disusun dalam grid yang fleksibel dan responsif.

5). Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!



                TUGAS 6 
Andi Aqsa Mappatunru Marzuki
2306275046

1). Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!

penggunaan JavaScript dalam pengembangan aplikasi web tentunya memberikan banyak manfaat, diantaranya:

• Interaktivitas Dinamis
JavaScript memungkinkan pengembang untuk membuat halaman web yang interaktif dan responsif. Misalnya, elemen-elemen seperti tombol, formulir, dan menu navigasi dapat bereaksi terhadap tindakan pengguna (misalnya klik, hover, input). Contohnya:

- Validasi Formulir: Formulir dapat diperiksa langsung di sisi klien sebelum dikirim ke server, memberikan respons cepat jika ada kesalahan input.

- AJAX (Asynchronous JavaScript and XML): Menggunakan AJAX, JavaScript memungkinkan pengambilan data dari server tanpa perlu memuat ulang seluruh halaman. Ini meningkatkan kecepatan dan efisiensi interaksi pengguna dengan aplikasi.

• Pengalaman Pengguna yang lebih baik

JavaScript memungkinkan aplikasi web untuk memperbarui konten halaman secara dinamis tanpa harus memuat ulang seluruh halaman. Ini membuat aplikasi terasa lebih cepat dan responsif, sehingga meningkatkan pengalaman pengguna secara keseluruhan. Contoh:

Single Page Applications (SPA): JavaScript adalah dasar dari SPA seperti React dan Angular, di mana hanya konten yang berubah diperbarui di halaman, tanpa memuat ulang seluruh halaman.

• Pengembangan Cepat dan Mudah

JavaScript memiliki ekosistem yang kaya dengan pustaka dan framework yang memudahkan pengembangan aplikasi web. Misalnya, pustaka seperti jQuery, dan framework seperti React, Vue.js, dan Angular membantu mempercepat pengembangan fitur-fitur kompleks dengan kode yang lebih sedikit dan lebih mudah dikelola.

• Efisiensi Penggunaan Bandwidth

Karena JavaScript dijalankan di sisi klien (browser), beberapa tugas komputasi dapat dipindahkan dari server ke pengguna. Ini dapat mengurangi beban server dan penggunaan bandwidth karena hanya data yang relevan yang dikirim bolak balik antara klien dan server.

2). Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?


Fungsi dari penggunaan await ketika kita menggunakan fetch() dalam JavaScript adalah untuk membuat proses pengambilan data (fetching) bersifat asinkron dan menunggu hingga operasi fetch() selesai sebelum melanjutkan ke baris kode berikutnya. Dengan menggunakan await, kita dapat menulis kode asinkron yang tampak lebih mirip kode sinkron, lebih mudah dibaca dan dipahami.

Jika kita tidak menggunakan await ketika kita menggunakan fetch(), maka kode akan berjalan asinkron sepenuhnya dan fetch() akan mengembalikan promise segera tanpa perlu menunggu datanya selesai diambil. Akibatnya, kode dibawah fetch() akan dieksekusi sebelum data dari fetch() tersedia.


3). Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?

Kita perlu menggunakan decorator csrf_exempt pada view karena Decorator csrf_exempt membuat Django tidak perlu mengecek keberadaan csrf_token pada POST request yang dikirimkan ke fungsi ini, dalam beberapa kasus, berguna untuk menonaktifkan proteksi CSRF (Cross-Site Request Forgery) ketika pengiriman data dilakukan tanpa menyertakan token CSRF. Namun, ini bukan solusi yang direkomendasikan untuk keamanan jangka panjang.


4). Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

Pembersihan data input pengguna dilakukan di belakang (backend) juga, dan tidak hanya dilakukan di frontend saja karena:

• Keamanan yang Lebih Kuat

Frontend adalah tempat di mana pengguna berinteraksi langsung dengan aplikasi, dan kode JavaScript di frontend dapat dengan mudah dilihat, dimodifikasi, atau dilewati oleh pengguna berbahaya. Jika pembersihan data hanya dilakukan di frontend, penyerang bisa memodifikasi atau melewati validasi tersebut dengan menggunakan alat seperti browser developer tools atau mengirim request manual melalui alat seperti Postman atau cURL.

• Mencegah Serangan Keamanan

Serangan seperti Cross-Site Scripting (XSS), SQL Injection, atau Command Injection adalah contoh ancaman keamanan yang bisa terjadi jika data input tidak dibersihkan dengan benar. Pembersihan di backend memastikan bahwa data yang masuk ke dalam basis data atau sistem lainnya telah difilter dari karakter berbahaya atau elemen yang dapat menyebabkan eksekusi kode berbahaya.

Jika hanya mengandalkan pembersihan di frontend, serangan ini masih bisa dilakukan oleh penyerang yang dapat mengabaikan pembersihan frontend dan langsung berinteraksi dengan backend.

• Konsistensi dalam Validasi Data

Backend memastikan bahwa setiap input diproses secara konsisten, bahkan jika terdapat bug atau kekurangan dalam validasi frontend.

Ini memastikan bahwa logika pembersihan dan validasi selalu berlaku pada semua jenis input, baik dari browser, aplikasi mobile, maupun alat API lainnya.


5).  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Step by Step:

Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX.

 AJAX GET
 Ubahlah kode cards data product agar dapat mendukung AJAX GET.

	Untuk mendapatkan objek-objek produk dari endpoint /json, pertama-tama saya menghapus product_entries = Product.objects.filter(user=request.user) dan product_entries': product_entries, di views.py karena kedua baris tersebut sudah redundant (tidak digunakan lagi). Selanjutnya saya memfilter penampilan pada show_json dan show_xml dengan menambahkan data = Product.objects.filter(user=request.user) di baris paling atas fungsi show_json dan show_xml. 
	
	Kemudian, pada main.html, saya menginisialisasi sebuah id baru dengan nama product_cards, membuat fungsi baru didalam block script yang saya namakan getProductEntries(), dan menghapus block conditional di product_entries. 

Lakukan pengambilan data product menggunakan AJAX GET. Pastikan bahwa data
yang diambil hanyalah data milik pengguna yang logged-in.

Untuk memastikan data hanyalah milik pengguna, pada tugas sebelumnya sudah terdapat  @login_required(login_url='/login') yang memastikan kalau dia telah logged-in. Kemudian fungsi show_json yang sudah diubah akan mengembalikan data json milik pengguna yang login. AJAX GET request akan di handle oleh async function getProductEntries() di main.html. Product.objects.filter(user=request.user) dalam fungsi show_json memastikan bahwa setiap pengguna hanya dapat mengakses data produk mereka sendiri.

AJAX POST
Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk 
menambahkan product

Di dalam main.html, saya menambahkan sebuah tombol yang akan membuka modal ketika diklik.
Dengan menggunakan onclick="showModal();" built in javascript pada tombol akan memanggil showModal() yang dimana modal tersebut berisi form untuk menambahkan produk baru.
Berikut kode implementasinya:
html
<button
  data-modal-target="crudModal"
  data-modal-toggle="crudModal"
  class="btn bg-[#7289da] hover:bg-[#5a6bbd] text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105 mx-4"
  onclick="showModal();"
>
  Add New Product by AJAX
</button>


Buatlah fungsi view baru untuk menambahkan product baru ke dalam basis data.

Saya membuat fungsi view baru di views.py bernama add_product_ajax, namun sebelumnya saya mengimpor csrf_exempt dan require_POST karena csrf_exempt karena permintaan dilakukan via AJAX dan view hanya menerima permintaan POST. kedua import tersebut ditaruh diatas fungsi add_product_entry_ajax dengan @csrf_exempt dan @require_POST. Saya juga mengimport dan menngunakan strip_tags di dalam fungsi tersebut guna untuk mencegah serangan XSS.

Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.

Saya menambahkan path baru berupa path('create-product-ajax', add_product_ajax, name='add_product_ajax'), di urls.py. Tujuan saya membuat path ini agar request POST ditangani dan fungsi add_product_ajax akan dipanggil.
Berikut snippet implementasinya di kode saya:

python
urlpatterns = [
	# ... path lainnya
	path('create-product-ajax', add_product_ajax, name='add_product_ajax'),
]



Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.
Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar product terbaru tanpa reload halaman utama secara keseluruhan
1). Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2). Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3). Jelaskan fungsi git dalam pengembangan perangkat lunak!
4). Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
5). Mengapa model pada Django disebut sebagai ORM?

                        Jawab:
1). Langkah-langkah yang dilakukan:
1. Membuat direktori utama, saya menamakannya Toko-Sepatu_sunnah
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
11. Buka berkas urls.py di dalam direktori proyek e_commerce, 
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
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "andi-aqsa-ecommerce.pbp.cs.ui.ac.id"]
19. Setelah mendapatkan Project Credentials dan Project Command, jalankan instruksi project command


2).

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


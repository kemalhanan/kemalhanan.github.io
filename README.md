# Tugas 6

## 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

   1. Eksekusi Tugas:
   Synchronous Programming: Tugas-tugas dieksekusi secara berurutan, satu per satu. Setiap tugas harus menyelesaikan eksekusinya sebelum tugas berikutnya dapat dimulai. Dalam kata lain, eksekusi kode berjalan secara linier.
   Asynchronous Programming: Tugas-tugas tidak harus menunggu tugas sebelumnya selesai untuk dieksekusi. Sebaliknya, tugas-tugas dapat berjalan secara bersamaan, dan eksekusi dapat berlanjut tanpa harus menunggu tugas lain selesai. Hal ini memungkinkan pemrosesan yang lebih efisien, terutama ketika ada tugas yang memerlukan waktu lama untuk menyelesaikan eksekusinya.

   2. Blocking vs Non-blocking:
   Synchronous Programming: Karena tugas-tugas dieksekusi secara berurutan, tugas yang memerlukan waktu lama akan "memblokir" atau menghentikan eksekusi tugas berikutnya hingga tugas sebelumnya selesai. Hal ini disebut "blocking".
   Asynchronous Programming: Dalam paradigma ini, tugas yang memerlukan waktu lama tidak akan menghentikan eksekusi tugas lain. Sebaliknya, mereka akan berjalan secara bersamaan, memungkinkan tugas lain untuk terus berjalan tanpa harus menunggu. Ini disebut "non-blocking".

   3. Manajemen Waktu:
   Synchronous Programming: Kode dieksekusi dalam urutan yang ditentukan, sehingga waktu eksekusi keseluruhan ditentukan oleh jumlah waktu yang dibutuhkan untuk menyelesaikan setiap tugas secara berurutan.
   Asynchronous Programming: Karena tugas-tugas dapat berjalan secara bersamaan, waktu eksekusi keseluruhan seringkali lebih pendek daripada pendekatan synchronous, karena beberapa tugas dapat diselesaikan bersamaan.

## 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
   Paradigma event-driven programming adalah pendekatan pemrograman di mana aliran eksekusi kode ditentukan oleh peristiwa atau event, seperti interaksi pengguna, respons dari server, atau perubahan status sistem. Dalam paradigma ini, program dirancang untuk merespons berbagai event yang dapat terjadi, daripada mengikuti aliran eksekusi linier yang ditentukan. Penerapan pada tugas ini adalah penggunaan modal untuk menambah assignment

## 3. Jelaskan penerapan asynchronous programming pada AJAX.
   Asynchronous programming adalah teknik pengembangan web yang memungkinkan aplikasi web untuk bekerja secara tidak langsung (asynchronous) – memproses setiap permintaan yang datang ke server di sisi background. Salah satu penerapan asynchronous programming pada Javascript adalah AJAX (Asynchronous Javascript and XML), yang memungkinkan untuk mengambil konten dari server back-end secara tidak sinkron, tanpa perlu merefresh halaman. Dengan menggunakan AJAX, konten dapat diperbarui halaman web tanpa memuat ulang atau reload . Contoh penggunaan AJAX adalah fitur Google Autocomplete, sistem voting dan rating, chat room, dan notifikasi trending di Twitter. Untuk menggunakan AJAX, bisa dilakukan dengan menggunakan fungsi XMLHttpRequest (XHR) yang merupakan objek bawaan Javascript untuk melakukan permintaan data dan menangani tanggapan dari sebuah REST API.



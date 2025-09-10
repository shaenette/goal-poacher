Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat sebuah direktori baru dengan nama "goal-poacher" yang akan menjadi nama dari football-shop saya.
2. Mengubah Execution Policy yang ada pada komputer saya melalui akses sebagai administator pada PowerShell dengan menggunakan perintah "Set-ExecutionPolicy Unrestricted -Force". Hal ini saya lakukan karena setiap saya menyelesaikan suatu proyek saya selalu mengubah kembali policy-nya menjadi "Restricted".
3. Membuat virtual environment dengan menggunakan perintah "python -m venv env"
4. Mengaktifkan virtual environment dengan membuka terminal pada direktori "goal-poacher" dan menjalankan perintah "env\Scripts\activate"
5. Membuat berkas "requirements.txt" pada direktori "goal-poacher" kemudian mengisi file tersebut dengan dependencies yang diperlukan (saya mengambilnya melalui tutorial).
6. Meng-install semua dependencies dengan menjalankan perintah "pip install -r requirements.txt" pada Command Prompt
7. Karena saya mendapatkan notif bahwa ada versi "pip" yang baru rilis, saya menjalankan perintah "python.exe -m pip install --upgrade pip" pada Command Prompt
8. Untuk memastikan bahwa semua dependencies sudah terinstall dengan baik saya menjalankan ulang perintah "pip install -r requirements.txt" pada Command Prompt
9. Membuat proyek Django dengan nama "goal_poacher" dengan menjalankan perintah "django-admin startproject goal_poacher .".
10. Membuka VScode kemudian membuat file ".env" pada direktori utama.
11. Mengisi file ".env" dengan konfikurasi "PRODUCTION=False"
12. Membuat file ".env.prod" pada direktpro yang sama dan mengisinya dengan database yang diberikan oleh kampus dengan schema "tugas_individu" dan "PRODUCTION=True"
13. Memodifikasi file "settings.py" dengan menambahkan kode
"import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()"
setelah import path.
14. Menambahkan string "localhost", "127.0.0.1" pada list kosong "ALLOWED_HOSTS" yang ada di settings.py.
15. Menambahkan konfigurasi "PRODUCTION = os.getenv('PRODUCTION', 'False').lower() == 'true'" tepat di atas code DEBUG di settings.py.
16. Mengubah konfigurasi database yang ada di "settings.py" menggunakan konfigurasi yang sudah disediakan di tutorial 0.
17. Membuka Command Prompt (masih pada direktori utama), kemudian menjalankan perintah "python manage.py migrate" kemudian dilanjuti dengan perintah "python manage.py runserver"
18. Membuat repositori baru di github dengan nama yang sama dengan direktori utama saya yaitu "goal-poacher" dan mengatur visibilitasnya menjadi public
19. Pada terminal direktori utama, saya menjalankan perintah "git init" untuk menginisiasi direktori lokal saya sebagai repositori Git.
20. Menambahkan berkas ".gitignore" pada direktori utama dan mengisi berkas tersebut dengan teks yang sudah disediakan pada tutorial 0.
21. Menyalin link yang ada di bagian "Code" pada repository github saya kemudian menjalankan perintah " git remote add origin [link]" pada Command Prompt (masih di direktori yang sama).
22. Membuat branch utama bernama master dengan menjalankan perintah "git branch -M master" pada Command Prompt.
23. Melakukan perintah:
"""
git add .
git commit -m "Inisiasi Toko Footbal"
git push origin master
"""
pada command prompt di direktori utama (lokal)
24. Membuat akun proyek beru di PWS dengan project name "goalpoacher" kemudian menekan "Create New Project".
25. Menyimpan kredensial yang muncul pada laman PWS
26. Menge-klik proyek "goalpoacher" pada sidebar 
27. Menge_klik tab "Environs" kemudian mengisi "Raw Editor" dengan isi file ".env.prod" yang ada di direktori utama
28. Menambahkan url deployment web saya pada ALLOWED_HOSTS di "settings.py"
29. Commit updates ke github dengan menjalankan perintah:
"""
git add .
git commit -m "Buat Proyek Django"
git push origin master
"""
30. Menjalankan perintah:
"""
git remote add pws [url saya]
git branch -M master
git push pws master
"""
31. Membuat aplikasi bernama "main" dalam proyek "goal-poacher" dengan menjalankan perintah "python manage.py startapp main" pada Command Prompt di direktori utama.
32. Membuka berkas "settings.py" di direktori proyek dan menambahkan "main" pada variable INSTALLED_APPAS sebagai elemen paling akhir. Pada Django, kalau ada aplikasi yang mendefinisikan hal yang sama, maka yang ditulis lebih bawah akan menimpa konfigurasi yang di atas. Dan karena "main" merupakan aplikasi buatan kita sendiri, bukan bawaan Django.
33. Mengisi berkas models.py yang ada pada direktori aplikasi dengan kode:
"""
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    @property
    def is_out_of_stock(self):
        return self.stock <= 0

    def decrease_stock(self, amount=1):
        if self.stock >= amount:
            self.stock -= amount
            self.save()
            return True
        return False
"""
34. Melakukan migrasi model yang telah dibuat dengan menjalankan perintah: "python manage.py makemigrations"
35. Menjalankan perintah "python manage.py migrate" untuk menerapkan perubahan pada model yang telah dibuat ke database lokal
36. Menambahkan fungsi "show_main" pada berkas views.py yang ada pada direktori aplikasi dengan code:
"""
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def show_main(request):
    context = {
        "app_name": "Football Shop",
        "student_name": "Nazwa Zahra Sausan",
        "class_name": "PBP D",
    }
    return render(request, "main.html", context)
"""
37. Membuat direktori baru bernama "templates" pada direktori aplikasi "main", kemudian membuat berkas "main.html"
38. Mengisi berkas"main.html" dengan kode:
"""
<!DOCTYPE html>
<html>
<head>
    <title>{{ app_name }}</title>
</head>
<body>
    <h1>{{ app_name }}</h1>
    <p>Nama: {{ student_name }}</p>
    <p>Kelas: {{ class_name }}</p>
</body>
</html>
"""
yang merupakan template dari aplikasi saya (yang akan ditampilkan ke layar).
39. Membuat berkas "urls.py" di direktori "main" kemudian mengisinya dengan code:
"""
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
"""
40. Membuka berkas "urls.py" yang ada di direktori utama "goal-poacher" kemudian meng-import fungsi "include" dari "django.urls" dengan menambahkan ", include" pada code import yang sudah tersedia.
41. Menambahkan elemen "path('', include('main.urls'))," (tanpa tanda kutip), pada variable urlspatterns yang ada di berkas "urls.py"
42. Menjalankan proyek Django dengan perintah "python manage.py runserver."
43. Melihat proyek yang telah dibuat melalui fitur "View Project" yang ada di PWS
44. Membuat unit test dengan mengisinya dengan perintah yang ada pada berkas "tests.py" di direktori main
45. Menjalankan perintah "python manage.py test" untuk menjalankan test
46. Melakukan push ke repository github dengan perintah:
"""
git add .
git commit -m "Complete tugas_individu 2: Implementasi Model-View-Template (MVT) pada Django"
git push origin master
git push pws master
"""

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Link gambar: https://drive.google.com/file/d/1MdWbQ6ZtML1CuWFiSTj-EldUSX3xsHSB/view?usp=drivesdk
Penjelasan:
urls.py berperan sebagai "peta" yang memetakan request (berupa HTTP request) yang dimasukkan oleh user, kemudian mencocokkan url tersebut dengan pola url yang telah ditentukan.
Jika terdapat pola yang sesuai, maka fungsi view (yang terdapat pada views.py) yang sesuai akan dipanggil.
Fungsi view yang dipanggil tersebut akan mengambil data dari database menggunakan model yang ada di "models.py".
views.py  kemudian mengirim data ke template HTML dan mengisi template HTML dengan data yang ada.
Berkas HTML yang sudah jadi dikirim kembali ke browser pengguna (HTTP response), menampilkan halaman web yang di-request.

Jelaskan peran settings.py dalam proyek Django!
settings.py pada proyek Django berperan seperti "otak" dari proyek tersebut. File settings.py digunakan untuk menyimpan konfigurasi dan pengaturan untuk proyek Django yang kita buat, seperti konfigurasi basis data, pengaturan middleware, aplikasi yang diinstal, dan lain sebagainya. Dengan mengubah dan melengkapi berkas ini, developer dapat mengonfigurasi proyek Django.

Bagaimana cara kerja migrasi database di Django?
Migrasi database pada Django merupakan cara framework menghubunkan model dengan struktur tabel di database. Dengan menjalankan perintah "python manage.py makemigrations" di Command Prompt, Django akan secara otomatis membuat berkas migrasi berdasarkan perubahan (yang belum diaplikasikan ke database) yang dilakukan pada model kita. Kemudian, jika kita menjalankan perintah "python manage.py migrate", maka perubahan yang tercantum dalam berkas migrasi yang telah dibuat sebelumnya akan diaplikasikan ke database.

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sering dijadikan sebagai framework pertama dalam pembelajaran pengembangan perangkat lunak karena berbasis Python yang mudah dipahami, bersifat free dan open source, serta memiliki banyak fitur bawaan yang mendukung proses development. Selain itu, Django menggunakan arsitektur Model-View-Template (MVT) yang jelas dan mudah diikuti. 

Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Sudah cukup baik, para asdos standby dan siap untuk menjawab pertanyaan dan kendala dari mahasiswa.

References:
Fazry. (2024, April 12). Pengenalan Django: Membangun Aplikasi Web Pertama Anda. Rumah Coding. Retrieved from https://rumahcoding.co.id/pengenalan-django-membangun-aplikasi-web-pertama-anda/

Ryabtsev, A. (2025, March 20). Configuring Django Settings: Best Practices. Django Stars. Retrieved from https://djangostars.com/blog/configuring-django-settings-best-practices/

Smaniotto, B. (2023, November 16). Why Use Django Web Framework for App Development. Cheesecake Labs. Retrieved from https://cheesecakelabs-com.translate.goog/blog/django-framework-app-development/?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=tc

Supriyono, E. (2024, July 4). Bagaimana mengelola settings pada sebuah proyek. Kementerian Keuangan Republik Indonesia. 

VinDevs. (2024, October 9). How to write a Django data migration. How they work. Retrieved from https://vindevs-com.translate.goog/blog/how-to-write-a-django-data-migration-how-they-work-p76/?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=rq#:~:text=Migrasi%20data%20Django%20adalah%20jenis,dalam%20tabel%20basis%20data%20Anda.
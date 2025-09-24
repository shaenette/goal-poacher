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
    11. Mengisi file ".env" dengan konfigurasi "PRODUCTION=False"
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

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Karena dalam mengembangkan suatu platform ada saat ketika kita perlu mengirimkan data dari satu stack ke stack lainnya sehingga akhirnya data bisa diakses oleh user. Data delivery diperlukan untuk memastikan akurasi data, mendeteksi error, dan juga memvalidasi data


Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    Menurut saya, dari sisi keterbacaan data JSON lebih baik dari XML karena data pada JSON direpresentasikan dalam bentuk dictionary, sehingga setiap feilds dari datanya menjadi lebih cepat dibaca dan dipahami, berbeda dengan XML yang menggunakan end tag. JSON dapat merepresentasikan data yang sama dalam bentuk yang lebih ringan dan ringkas dibanding XML sehingga ukuran filenya lebih kecil dan transfer data menjadi lebih cepat.

Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    Method is_valid() digunakan untuk memastikan bahwa data yang dimasukkan pengguna sudah sesuai dengan ketentuan validasi field (misalnya panjang string, tipe data, dll) sebelum data disimpan ke database. Metode ini akan melempar True jika datanya valid dan False jika datanya tidak valid. Jadi, kita membutuhhkan method ini untuk memvalidasi data yang dimasukkan oleh user.

Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    Kita membutuhkan csrf_token saat membuat form di Django karena csrf_token berfungsi sebagai perlindungan terhadap serangan CSRF (Cross-Site Request Forgery). Token ini adalah sebuah token unik yang disisipkan ke dalam form yang harus dikirimkan kembali oleh browser saat form tersebut disubmit agar server dapat memverifikasi bahwa permintaan tersebut benar-benar berasal dari pengguna yang sah dan bukan dari ppenyerang.

    Jika csrf_token tidak ditambahkan pada form Django, maka aplikasi menjadi rentan terhadap serangan CSRF. Penyerang dapat memanfaatkan kelemahan ini dengan membuat pengguna yang sudah login pada suatu situs web melakukan tindakan yang tidak diinginkan secara diam-diam, seperti mengirim form secara otomatis tanpa sepengetahuan pengguna. 

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Membuat berkas baru pada direktori main dengan nama forms.py dengan membuat sebuah object bernama ProductForm
    2. Meng-import berkas forms ke views.py dan menambahkan beberapa fungsi yang digunakan untuk menghasilkan form yang dapat menambahkan data Product secara otomatis ketika data disubmit (add_product) dan fungsi show_product untuk mengambil object Product berdasarkan id, jika object tidak ditemukan maka akan mengembalikan 404.
    3. Menambahkan url baru yang menuju ke fungsi-fungsi yang telah ditambahkan pada urls.py yang ada di directory main
    4. Meng-update berkas main.html agar dapat menampilkan form dengan kode yang dapat dilihat pada ./main/templates/main.html
    5. Membuat berkas add_product.html pada main/templates/ sebagai template dari halaman input form dan detail product
    6. Membuat berkas product_detail.html sebagai halaman untuk menampilkan detail dari product yang ditambahkan
    7. Menambahkan CSRF_TRUSTED_ORIGINS = ["https://nazwa-zahra-goalpoacher.pbp.cs.ui.ac.id."] pada settings.py tepat setelah variable ALLOWED_HOSTS
    8. Meng-import HttpResponse dan serializers ke berkas.py untuk digunakan pada fungsi yang akan ditambahkan kemudian
    9. Menambahkan 2 fungsi baru yakni show_xml dan show_json yang menerima parameter request dan mengembalikan HttpResponse pada views.py. Fungsi ini berfungsi untuk mengembalikan data dalam bentuk XML/JSON
    10. Menambahkan 2 fungsi baru yakni show_xml_by_id dan show_json_id yang yang menerima parameter berupa request dan id product serta mengembalikan HttpResponse pada views.py. Fungsi ini berfungsi untuk mengembalikan data dalam bentuk XML/JSON berdasarkan id, pada fungsi ini juga saya tambahkan bock try except yang akan mengembalikan HttpResponse daengan status 404 jika data dengan id tertentu tidak ditemukan dalam database.
    11. Menege-push semua kode yang ditambahkan ke github dan pws melalui kode
    """
    perintah:
    """
    git add .
    git commit -m "Mesage"
    git push origin master
    git push pws master
    """

Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
    Sudah cukup baik, para asdos standby dan siap untuk menjawab pertanyaan dan kendala dari mahasiswa. Pada tutorial 2 juga ada penjelasan di awal sebelum memulai tutorial.

POSTMAN TEST
https://docs.google.com/document/d/1t7HU_7Mt8mieijadC7Ntr-5nCLGAABS3N0ieZnme2gg/edit?usp=drivesdk

=======TUGAS 4=======
Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
    AuthenticationForn adalah built-in class dari django yang dapat meng-handle login dari user dengan memvalidasi username dan password. Form inu akan secara otomatis menyediakan field untuk username dan password dan mengecek apakah username dan password yang dimasukkan sudah benar dan sesuai dengan data user yang ada di database.
    Kelebihan:
    1) Mudah digunakan (langsung tersedia tanpa perlu membuat form login dari awal)
    2) Terintegrasi dengan sistem autentikasi Django
    3) Validasinya otomatis dan aman (Django)
    Kekurangan:
    1) Kurang fleksibel jika ingin menambah field atau kustomisasi form login
    2) Hanya mendukung autentikasi standar (username & password)

Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
    Autentikasi adalah proses "memverifikasi" identitas pengguna, misalnya dengan login menggunakan username dan password. Tujuannya memastikan bahwa pengguna adalah siapa yang mereka klaim. Sedangkan, otorisasi adalah proses menentukan "hak akses" pengguna setelah mereka terautentikasi, misalnya apakah pengguna boleh mengakses halaman tertentu atau melakukan aksi tertentu.

Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
    Perbandingan Session dan Cookies
    Session:
        Kelebihan:
            - Data disimpan di server, sehingga lebih aman dan sulit dimodifikasi oleh pengguna.
            - Mampu menyimpan data dalam jumlah besar tanpa membebani browser.
            - Ideal untuk menyimpan data sensitif, seperti status login atau keranjang belanja (shopping cart).

        Kekurangan
            - Membutuhkan resource server tambahan untuk menyimpan data session.
            - Tidak bertahan ketika pengguna berganti perangkat atau browser.
            - Memerlukan mekanisme identifikasi, biasanya melalui session ID yang tersimpan di cookie.

    Cookies
        Kelebihan
            - Data disimpan di browser pengguna, sehingga tidak membebani server.
            - Dapat bertahan lama (persistent) sesuai tanggal kedaluwarsa yang ditentukan.
            - Cocok untuk menyimpan preferensi pengguna, pelacakan (tracking), atau data dengan ukuran kecil.

    Kekurangan
        - Kapasitas penyimpanan terbatas, biasanya sekitar 4KB per cookie.
        - Rentan dimanipulasi atau dicuri jika tidak dilindungi dengan enkripsi.
        - Tidak disarankan untuk menyimpan data sensitif.

Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
    Secara default, penggunaan cookies dalam pengembangan web tidak sepenuhnya aman karena ada beberapa risiko yang perlu diperhatikan. Misalnya, cookies bisa diekspos pada serangan cross-site scripting (XSS) disalahgunakan dalam cross-site request forgery (CSRF), atau diakses secara tidak sah jika tidak dikonfigurasi dengan benar. Untuk mengurangi risiko ini, ada praktik keamanan yang biasanya diterapkan, seperti memberi atribut Secure agar cookie hanya dikirim lewat HTTPS, HttpOnl supaya tidak bisa diakses lewat JavaScript, membatasi domain dan path cookie, serta mengenkripsi data yang sensitif. Selain itu, aturan privasi seperti GDPR mewajibkan persetujuan pengguna sebelum menyimpan cookie dan keterbukaan soal bagaimana cookie digunakan.

    Django menangatasi risiko potensial yang ada dengan menyediakan pengaturan bawaan yang cukup aman. Misalnya, cookie untuk sesi biasanya di-set dengan HttpOnly dan bisa dengan mudah dikonfigurasi jadi Secure. Django juga punya mekanisme bawaan untuk mencegah CSRF dengan token khusus yang disisipkan di setiap permintaan. Selain itu, developer bisa dengan mudah menyesuaikan konfigurasi cookie di Django agar lebih ketat sesuai kebutuhan aplikasi, sehingga risiko bisa ditekan dan standar privasi tetap terpenuhi.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1) Mengaktifkan virtual environment
    2) Mengimport UserCreationForm dan messages di views.py dengan menjalankan kode: 
    '''
    from django.contrib.auth.forms import UserCreationForm from django.contrib import messages
    '''
    3) Menambahkan fungsi "register" ke dalam viws.py, dengan kode:
    '''
    def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
    '''
    4) Membuat berkas register.html untuk meng-handle registrasi:
    {% extends 'base.html' %}

    {% block meta %}
    <title>Register</title>
    {% endblock meta %}

    {% block content %}

    <div>
    <h1>Register</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input type="submit" name="submit" value="Daftar" /></td>
        </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}
    </div>

    {% endblock content %}
    '''
    5) Mengimpor fungsi register yang baru dibuat di views.py ke urls.py yang ada di direktori main
    6) Menambahkan url path ke dalam variable urlpatterns
    7) Menambahkan impor berikut di views.py:
    '''
    from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
    from django.contrib.auth import authenticate, login
    '''
    8) Mneambahkan fungsi baru "login)user" ke dalam views.py dengan kode berikut:
    '''
    def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('main:show_main')

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
    '''
    9) Membuat berkas login.html di main/tempates, kemudian mengisinya dengan kode di bawah:
    '''
    {% extends 'base.html' %}

    {% block meta %}
    <title>Login</title>
    {% endblock meta %}

    {% block content %}
    <div class="login">
    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Login" /></td>
        </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %} Don't have an account yet?
    <a href="{% url 'main:register' %}">Register Now</a>
    </div>

    {% endblock content %}
    '''
    10) Mengimport fungsi yang baru dibuat "login_user" dan urlpathnya ke file urls.py yang ada di direktori main (mirip seperti langkah 5-6)
    11) Menambahkan fungsi logout dengan pertama mengimport logout dari "django.contrib.auth" ke berkas views.py dan menambahkan fungsi berikut:
    '''
    def logout_user(request):
        logout(request)
        return redirect('main:login')
    '''
    12) Menambahkan hyperlink tag untuk Button logout di berkas main.html
    13) Mengimport fungsi "logout" ke berkas urls.py dan menambahkan url oath baru yang diarahkan ke fungsi logout di variable urlpatterns
    14) Menambahkan import baru views.py di direktori main, yaitu :
    from django.contrib.auth.decorators import login_required
    15) Mengimplementasikan dekorator "@login_required(login_url='/login')" dengan meletakkannya di atas fungsi show_main dan show_news
    16) Menambahkan import baru di views.py untuk mengimplementasikan cookies:
    '''
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    '''
    17) Mengubah fungsi "login_user" menjadi:
    '''
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    '''
    18) Menambahkan key dan value:
    '''
    'last_login': request.COOKIES.get('last_login', 'Never')
    ''' ke dalam variable context yang ada di fungsi show_main pada views.py
    19) Mengubah fungsi "logout_user" menjadi:
    '''
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    '''
    20) Menambahkan kode yang tertulis di bawah ke berkasi main.html untuk menampilkan data waktu terakhir pengguna login:
    '''
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    '''
    21) Menjalankan proyek django di local host dan membuat user baru (untuk keperluan step selanjutnya)
    22) Mengimport: from django.contrib.auth.models import User ke dalam models.py
    23) Menambahkan kode: 
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    '''
    ke class Product
    24) Mengubah fungsi add_product yang ada di views.py menjadi:
    '''
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "add_product.html", context)
    '''
    25) Memodifikasi fungsi show_main menjadi:
    '''
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        "app_name": "Goal Poacher",
        "username": request.user.username,
        "student_name": "Nazwa Zahra Sausan",
        "class_name": "PBP D",
        "npm": "2406397750",
        'product_list' : product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, "main.html", context)
    '''
    26) Menambahkan kode:
    '''
    a href="?filter=all">
        <button type="button">All Products</button>
    </a>
    <a href="?filter=my">
        <button type="button">My Products</button>
    </a> 
    '''
    ke berkas main.html setelah kodesesi terakhir login
    27) Menampilkan author yang mencreate product dengan menambahkan porongankode berikut ke berkas product.detail.html:
    '''
    {% if news.user %}
    <p>Author: {{ news.user.username }}</p>
    {% else %}
        <p>Author: Anonymous</p>
    {% endif %}
    '''
    28) Melakukan add, commit, push ke github dan pws
    29) Menambahkan 2 username dan 3 product ke local host untuk keperluan penilaian.

References:
Fazry. (2024, April 12). Pengenalan Django: Membangun Aplikasi Web Pertama Anda. Rumah Coding. Retrieved from https://rumahcoding.co.id/pengenalan-django-membangun-aplikasi-web-pertama-anda/

Ryabtsev, A. (2025, March 20). Configuring Django Settings: Best Practices. Django Stars. Retrieved from https://djangostars.com/blog/configuring-django-settings-best-practices/

Smaniotto, B. (2023, November 16). Why Use Django Web Framework for App Development. Cheesecake Labs. Retrieved from https://cheesecakelabs-com.translate.goog/blog/django-framework-app-development/?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=tc

Supriyono, E. (2024, July 4). Bagaimana mengelola settings pada sebuah proyek. Kementerian Keuangan Republik Indonesia. 

VinDevs. (2024, October 9). How to write a Django data migration. How they work. Retrieved from https://vindevs-com.translate.goog/blog/how-to-write-a-django-data-migration-how-they-work-p76/?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=rq#:~:text=Migrasi%20data%20Django%20adalah%20jenis,dalam%20tabel%20basis%20data%20Anda.

Amazon Web Services. (n.d.). What is the difference between JSON and XML? AWS. Retrieved from https://aws.amazon.com/id/compare/the-difference-between-json-xml

Coding Studio. (2023, November 19). CSRF (Cross Site Request Forgery): Pengertian, Jenis dan Cara Mencegahnya. Coding Studio. https://codingstudio.id/blog/csrf-adalah

Kontorskyy, D., & Ristić, V. (2024, July 26). Django contact form: Tutorial with code snippets. Mailtrap. Retrieved from https://mailtrap.io/blog/django-contact-form/

Risky, A. S. (2024, July 30). Mempelajari Pentingnya CSRF Protection Pada Laravel Web Development. BuildWithAngga. Retrieved from https://buildwithangga.com/tips/mempelajari-pentingnya-csrf-protection-pada-laravel-web-development

Sean. (2024, October 23). What is Data Delivery and Why is it Important?. FanRuan. Retrieved from https://www.fanruan.com/en/glossary/big-data/data-delivery

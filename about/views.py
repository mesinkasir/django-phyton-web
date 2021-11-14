from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    SEO1 = ["Pembuatan website aplikasi android dan kasir point of sale POS APPS."]
    SEO2 = ["Modern website untuk toko shop restoran cafe rumah makan company profile dan sekolah plus android dan aplikasi."]
    gsite = [""]
    title = ["Pembuatan website aplikasi android dan kasir point of sale mu."]
    desc = ["Saat nya kini kembangkan technology mu bersama kami untuk masa depan yang terbaik, kebutuhan project develope dan deploy modern website dengan modern technology hingga aplikasi android plus aplikasi pembukuan kasir point of sale untuk toko shop dan restoran siap untuk kamu gunakan ."]
    himg = ["https://1.bp.blogspot.com/-UfbS7fzia0s/YY_T9KGzogI/AAAAAAAAR3M/f5fyHLwcM5IpeCEpImdvFkVaig_B9RL7gCLcBGAsYHQ/s1712/pembuatan%2Bwebsite%2Bterbaru%2Bmodern.png"]
    aimg = ["https://1.bp.blogspot.com/-YbzqygBEcxY/YY_VwwqTieI/AAAAAAAAR3U/z-d69ct02KwLTevk6ztSmUpSnzdr6sDZQCLcBGAsYHQ/s666/pembuatan%2Bandroid%2Bterbaru.png"]
    bimg = ["https://1.bp.blogspot.com/-YN5d4Sv9P8s/YY_awY9_ojI/AAAAAAAAR3o/ZjImPTro0gEEV0JPJvNqsaU8U8JbGCn-QCLcBGAsYHQ/s519/pembuatan%2Bwebsite.png"]
    cimg = ["https://1.bp.blogspot.com/-udm1kuJJ_YM/YY_akT1oZHI/AAAAAAAAR3c/k8EXsbU3J4oqNYOMDt_EhT8pH0HqwndSACLcBGAsYHQ/s626/aplikasi%2Bbisnis.jpg"]
    fotimg = ["https://1.bp.blogspot.com/-4qdfwtJupvQ/YY_akT-SY0I/AAAAAAAAR3k/tTvsBrwJvKAbeQP9Xzwiw056E1fIVoyLwCLcBGAsYHQ/s1200/website%2Bapplikasi.jpg"]
    hsec1 = ["Aplikasi Android."]
    sec1 = ["Kebutuhan untuk pembuatan aplikasi android guna upload ke google playstore memungkinkan untuk kemajuan bisnis dan usaha mu, dengan memiliki APK android bundle sendiri akan memudahkan untuk semakin dekat dengan pelanggan mu untuk memberikan informasi detail mengenai bisnis usaha dan lain nya. Develope dengan flutter dart native java kotlin memberikan kemudahan untuk upload google playstore dengan cepat."]
    uri1 = ["/services/pembuatanandroid"]
    hsec2 = ["Modern Website."]
    sec2 = ["Kembangkan pembuatan website informasi dan toko online shop mu bersama kami hasil yang terbaik dengan penggunaan berbagai technology yang bisa kamu pilih dalam develope dan deploy modern situs mu, dengan laravel, django , angular, react , gatsby , jekyll , modx, symfony , getaxcora cms dan lain sebagai nya plus dukungan penuh technology terbaru untuk website modern mu."]
    uri2 = ["/services/pembuatanwebsite"]
    hsec3 = ["Aplikasi Online."]
    sec3 = ["Dan sempurnakan kebutuhan untuk bekerja dengan mudah via aplikasi online , apapun bidang usaha mu , aplikasi online ini tersedia beberapa variant berdasarkan bidang bisnis industri dan edukasi, mulai dari aplikasi kasir point of sale pos toko ,restoran , invoice, akuntansi accounting, reservasi booking online, sekolah ERP dan banyak lagi lain nya yang dapat digunakan untuk mempercepat transaksi kasir, sebagai pembukuan detail digital mu plus monitoring kinerja via laporan laporan detail hadir di dalam nya."]
    uri3 = ["/services/pembuatanaplikasi"]
    hfoot = ["All In one Website Application."]
    cfoot = ["Atau sempurnakan dengan all in one website modern situs mu terintegrasi dengan aplikasi kasir toko invoice akuntansi sekolah hingga android apps dalam satu paket untuk siap majukan bisnis usaha mu, bersama kami saat nya era digital dimulai."]
    wa = ["https://wa.me/6285646104747"]
    call = ["tel:+6285331361404"]
    mail = ["mailto:axcora@gmail.com"]
    return render(request, "about/index.html" , {"SEO1": SEO1,"SEO2": SEO2,"gsite": gsite,"title": title,"himg": himg,"desc": desc,"aimg": aimg,"bimg": bimg,"cimg": cimg,"fotimg": fotimg,"hsec1": hsec1,"hsec2": hsec2,"hsec3": hsec3, "hfoot": hfoot,"cfoot": cfoot,"sec1": sec1,"sec2": sec2,"sec3": sec3,"uri1": uri1,"uri2": uri2,"uri3": uri3,"wa": wa,"call": call,"mail": mail})
  



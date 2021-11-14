from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    SEO1 = ["Axcora Technology - pembuatan website modern dan aplikasi android"]
    SEO2 = ["solusi pembuatan aplikasi kasir toko restoran dan website terintegrasi plus android apps axcora technology"]
    title = ["Phyton Django Web Apps"]
    gsite = [""]
    uri = ["about"]
    desc = ["Mudahkan segalanya bersama phyton django untuk develope modern website mu."]
    img = ["https://1.bp.blogspot.com/-7O4lZT7kOdA/YY_Pf2DKTPI/AAAAAAAAR3E/_MbtNJ7BygUmq-8Ps_w6ve6R57xCcatOQCLcBGAsYHQ/s400/pembuatan%2Bwebsite%2Bdjanggo%2Bphyton1.png"]
    return render(request, "home/index.html",{"title": title,"uri": uri, "desc": desc, "img": img,"SEO1": SEO1,"SEO2": SEO2,"gsite": gsite,})



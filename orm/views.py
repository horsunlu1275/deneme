from django.shortcuts import render
from .models import Personel

# Create your views here.
def orm(request):
    alert=""
    if request.method == 'POST':
        if "save" in request.POST:
            name = request.POST.get('p_name')
            surname = request.POST.get('p_surname')
            rutbe = request.POST.get('p_rutbe')
            age = request.POST.get('age')

            personel = Personel.objects.create(
            name=name,
            surname=surname,
            rutbe=rutbe,
            age=age
            
        )
            alert = "işlem başarılı"
                
            return  render(request, 'orm/homepage.html', {"alert":alert})
        
        if "select" in request.POST:
            name = request.POST.get("personal_name","")
            print(name)
            personeller = Personel.objects.filter(name__icontains=name)
            for personel in personeller:
                ad = personel.name
                soyad = personel.surname
                rutbe = personel.rutbe
                yas = personel.age
            return render(request,'orm/homepage.html',{"personeller":personeller,"ad":ad,"soyad":soyad,"rutbe":rutbe,"yas":yas})
            
    return render(request, 'orm/homepage.html', {"alert":alert})
    
    
    
from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'Name' : 'Andi Aqsa',
        'Price': 'Rp300.000',
        'Description': 'Sepatu ini dibuat menggunakan bahan yang bagus, serta produk original'
    }

    return render(request, "main.html", context)
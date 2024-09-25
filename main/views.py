from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Andi Aqsa',
        'price': 'Rp300.000',
        'description': 'Sepatu ini dibuat menggunakan bahan yang bagus, serta produk original',
        'stock' : '15',
    }

    return render(request, "main.html", context)
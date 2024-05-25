from django.shortcuts import render, HttpResponse

# Create your views here.

def tambah(request, num1, num2):
    context = {
        'title': 'Kalkulator Tambah',
        'result': f"{num1} + {num2} = {num1+num2}",
    }
    return render(request, 'kalkulator/index.html', context)
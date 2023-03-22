from django.shortcuts import render

def instrument_function(request):
    return render(request, 'app/instrument_function.html', {})

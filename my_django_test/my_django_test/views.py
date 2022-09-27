from django.shortcuts import render


def my_custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)

def home_page(request):
    return render(request, 'base.html')
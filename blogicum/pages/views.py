from django.shortcuts import render


def about(request):
    # Логика обработки запроса
    template = 'about.html'
    return render(request, template)


def rules(request):
    # Логика обработки запроса
    template = 'rules.html'
    return render(request, template)

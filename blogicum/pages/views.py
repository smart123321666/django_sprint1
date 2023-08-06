from django.shortcuts import render


def about(request):
    # Логика обработки запроса
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    # Логика обработки запроса
    template = 'pages/rules.html'
    return render(request, template)

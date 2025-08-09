from django.http import HttpResponse

def home(request):
    return HttpResponse('Olá cliente, bem-vindo ao meu site!')

from django.http import HttpResponse


def home(request):
    content = '<a href="/auth/login">login</a>' \
              '<br><a href="/your_name/cards">verify</a>' \
              '<br><a href="/auth/logout">logout</a>' \
              '<br><a href="/your_name/cards">verify</a>'
    return HttpResponse(content)

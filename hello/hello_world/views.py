from django.http import HttpResponse


def hello(request, user_name):
    return HttpResponse("Hello,!{}" .format(user_name))
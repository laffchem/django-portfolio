from django.shortcuts import render


# Create your views here.
def web_proj(request):
    return render(request, "webprojects/web.html")

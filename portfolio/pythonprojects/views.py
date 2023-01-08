from django.shortcuts import render


# Create your views here.
def py_proj(request):
    return render(request, "pythonprojects/python.html")


def py_jokes(request):
    return render(request, "pythonprojects/dad_jokes.html")

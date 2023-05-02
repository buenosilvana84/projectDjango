from django.shortcuts import render

# Create your views here.
def vista1(request):
    mensaje = "mi primera vista"
    return render(request, 'vista1.html',{'mensaje': mensaje})

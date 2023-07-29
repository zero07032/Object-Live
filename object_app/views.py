from django.shortcuts import render, redirect
from .models import blog
from django.forms import ValidationError
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    #pb = blog.objects.get(pk=6)
    #pb.title = "oke"
    context = {"blogs": blog.objects.all()}
    return render(request, "home.html", context)


def AddBlog(request):
    title = request.POST.get("title")
    image = request.FILES["img"] if "img" in request.FILES else None
    blog1 = blog.objects.create(title=title, img=image)
    blog1.save()
    return redirect("/")


def BlogApdateView(request, pk):
    blog1 = blog.objects.get(pk=pk)
    context = {"blog1": blog1}
    return render(request, "update_form.html", context)


def UpdateBlog(request, pk):
    blog1 = blog.objects.get(pk=pk)
    title = request.POST.get("title")
    image = request.FILES["img"] if "img" in request.FILES else blog1.img
    blog1.title = title
    blog1.img = image
    blog1.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

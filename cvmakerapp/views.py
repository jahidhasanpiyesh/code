from django.shortcuts import render
from .models import profile
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io


# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name" , "")
        phone = request.POST.get("phone" , "")
        email = request.POST.get("email" , "")
        school = request.POST.get("school" , "")
        collage = request.POST.get("collage" , "")
        university = request.POST.get("university" , "")
        degree = request.POST.get("degree" , "")
        skill = request.POST.get("skill" , "")
        about_you = request.POST.get("about_you" , "")
        previews_work = request.POST.get("previews_work" , "")

        data = profile(name=name , phone=phone , email=email , school=school , collage=collage ,
                       university=university , degree=degree , skill=skill , about_you=about_you ,
                       previews_work=previews_work)
        data.save()

    return render(request , "index.html")


def cv(request , id):
    CV = profile.objects.get(id=id)
    template = loader.get_template("cv.html")
    html = template.render({'CV': CV})
    option = {
        'page-size': 'Letter' ,
        'encoding': 'UTF-8' ,
    }
    pdf = pdfkit.from_string(html , False , option)
    response = HttpResponse(pdf , content_type="application/pdf")
    response['Content-Disposition'] = 'attachment'
    return response
    return render(request , "cv.html" , {'CV': CV})

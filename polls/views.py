from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from .forms import ContactForm
from .models import Pagedata
from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

def contact(request):
    form_class = ContactForm
    return render(request, 'contact.html', {
        'form': form_class,
    })
def boottmp(request):
    p=Pagedata
    template=get_template('boottemp.html')
    tabledb=p.objects.all()
   # pagecontext={'TEXT': p.objects.get(title='My data').info,'TITLE':p.objects.get(pk=1).title,'dt':p.objects.all()}
    
   # output=template.render(pagecontext)
    return render(request,'boottemp.html',{'TEXT': p.objects.get(title='My data').info,'TITLE':p.objects.get(pk=1).title,'dt':p.objects.all()})


def index(request):
    return HttpResponse("MY FIRST APP index page")
def test(request):
    myname="Lolly Boy"
    msg="<html><body> <b>greetings %s, weclome to my view<body></b></html>" % myname
    return HttpResponse(msg)
def temtest(request):
    template= get_template('boottemp.html')
    myms={'mycon':'POOOOOOOOOOOOOOOOP klllk real','my_bod':'NAAAAAAAAAAAAAN'}
    # var=Context({'mycon':'******WELCOME******',
    #             'my_bod':'The BODY '})
    var2=Context(myms)
    output=template.render(var2)
    return HttpResponse(output)



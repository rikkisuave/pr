from django.shortcuts import render


# Create your views here.
# add to the top
from .forms import ContactForm

# add to your views
def contact(request):
    form_class = ContactForm()
    if request.method=='POST':
        form_class = ContactForm(request.POST)
        ent=form_class.save(commit=False)
        ent.save()
    
    
        
    return render(request, 'contact.html', {
        'form': form_class,
    })

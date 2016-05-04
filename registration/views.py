from django.shortcuts import render,redirect
from .models import Guest
from .models import GuestPassport
from .forms import GuestForm
from .forms import PassportForm

def Base(request):
    return render(request, 'registration/base.html', {})

def Guestregistration(request):
    if request.method == 'POST':
    	form = GuestForm(request.POST)
    	if form.is_valid():
            post = form.save(commit=False)
            #post.requirement = Guest.objects.latest('id')
            post.save()
            return redirect('Base')
    else:
    	form = GuestForm()
        return render(request,'registration/Guestregistration.html',{'form':form})


def Passportupload(request):
    if request.method == 'POST':
    	form = PassportForm(request.POST,request.FILES)
    	if form.is_valid():
            post = form.save(commit=False)
            
            post.save()
            return render(request, 'registration/base.html', {})
            
    else:
    	form = PassportForm()
        return render(request,'registration/Passportupload.html',{'form':form}) 

# def Passportupload(request):
#     if request.method == 'POST':
#         form = PassportForm(request.POST, request.FILES)
#         if form.is_valid():
#             m = ExampleModel.objects.get(pk=course_id)
#             m.model_pic = form.cleaned_data['image']
#             m.save()
#             return HttpResponse('image upload success')
#     # return HttpResponseForbidden('allowed only via POST')    







  
# Create your views here.

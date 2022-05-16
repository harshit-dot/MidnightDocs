from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# import pyautogui
from django.contrib.auth.models import  User
from django.core.files.storage import FileSystemStorage
from django.contrib import messages #import messages

#
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('/')
        else:
            messages.error(request, 'Username or Password Wrong')

            return redirect('/')
def main(request):
    from .models import blogpost
    bala=blogpost.objects.all()
    return render(request, 'app1/index.html', {'bala': bala})
def createblog(request,names):
    if request.method=='POST':
        print(names)

        catagoy=request.POST['catagory']
        name=request.POST['name']
        gender=request.POST['gender']
        mobile_number=request.POST['mobile-number']
        mobile_number=request.POST['mobile-number']
        email=request.POST['email']
        age=request.POST['age']

        if catagoy=='' or name=='' or gender=='' or mobile_number=='' or email=='' or age=='' :
            messages.error(request,'Enter All The Fields')

            # pyautogui.alert('enter all the fields')
            bar = get_user_model().objects.get(username=names)
            return render(request, 'app1/createblog.html', {'bar': bar})
        from .models import appointment
        blog=appointment(catagory=catagoy, name=names, gender=gender, mobile_number=mobile_number, age=age, email=email)
        blog.save()
        send_mail(
            'we have just get your message regarding your doctor appointment (MidnightDocs)',
            'we will get back to you soon with all the details regarding your appointment query, till explore MidnightDocs website....',
            'khannaharshit064@gmail.com',
            [email],
            fail_silently=False,
        )
        messages.success(request, 'Congrats! you appointment has been successfully booked, you will get further notification on your mobile number and email address')

        return redirect('/')
    else:
        bar=get_user_model().objects.get(username=names)
        return render(request, 'app1/createblog.html' , {'bar':bar})
def about(request):
    return render(request, 'app1/about.html')
def contact(request):
    if request.method=='POST':
        email=request.POST['email']
        regarding=request.POST['catagory']
        text=request.POST['textarea']
        if email=='' or regarding=='' or text=='':
            messages.error(request, 'Enter All The Fields')

            # pyautogui.alert('Enter All The Fields')
            return render(request, 'app1/contact.html')
        send_mail(
            'we have just get your query (MidnightDocs)',
            'we get your query, we will reply it as soon as possible till explore MidnightDocs website....',
            'khannaharshit064@gmail.com',
            [email],
            fail_silently=False,
        )
        from .models import contact
        con=contact(email=email, regarding=regarding, text=text)
        con.save()
        messages.success(request, "We have received your message")

        # pyautogui.confirm(' send')
        return redirect('contact')
    else:
        return render(request, 'app1/contact.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']

        password=request.POST['password']

        password1=request.POST['password1']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        if username=='' or password=='' or password1=='' or first_name=='' or last_name=='' or email=='':
            # pyautogui.alert('Enter All The Fields')
            messages.error(request,'Enter All The Fields')
            return redirect('/')


        if password1!=password:
            messages.error(request,'Password Not Matched')

            # pyautogui.alert(request, 'password not matched')
            return redirect('/')

        send_mail(
            'Wow you have just signed up in MidnightDocs',
            'congratulations your account is now setup. you can login through the main website and can take appointments.....',
            'khannaharshit064@gmail.com',
            [email],
            fail_silently=False,
        )
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name=first_name
        myuser.last_name=last_name
        myuser.save()
        messages.success(request, 'User Created')
        return redirect('/')





def logout(request):
    auth_logout(request)
    return redirect('/')
def forgot(request):
    if request.method=='POST':
        email=request.POST['email']
        username=request.POST['username']
        # password=request.POST['password']
        # password1=request.POST['password1']
        # if password1!=password:
        #     pyautogui.alert('password did not matched')
        #     return redirect('/')
        if email=='' or username=='':
            messages.error(request,'Enter All The Fields')
            return redirect('forgot')
        bog=User.objects.get(username=username, email=email)
        if bog is None:
            messages.error(request,'Username or Password Wrong')

            return redirect('/')


        harsh='this is the link, click it http://midnightdocs.herokuapp.com/forgotpass/'+str(bog.id)
        print(harsh)
        print(bog.password)
        send_mail(
            'click the link to change your password MidnightDocs',
            harsh,
            'khannaharshit064@gmail.com',
            [email],
            fail_silently=False,
        )
        messages.success(request, 'Mail has been sent to your email address.')
        # pyautogui.confirm('mail has been sent to your email')
        return render(request, 'app1/forgot.html')

    else:
        return render(request, 'app1/forgot.html')
def search(request):
    searchtex=request.POST['search']

    print(searchtex)
    searchtext=searchtex.lower()
    print(searchtext)
    if len(searchtext)==0:
        messages.error(request, 'Enter Something')
        # pyautogui.alert('enter something!')
        return redirect('/')
    from .models import blogpost
    blog=blogpost.objects.filter(catagory=searchtext)
    if len(blog)==0:
        messages.error(request,' Not Found Anything ')
        # pyautogui.alert('not found anything')
        return redirect('/')
    else:
        return render(request,'app1/index.html', {'blog':blog})

def blogpost(request, id):
    from .models import blogpost
    blog=blogpost.objects.filter(ids=id)
    return render(request,'app1/blopost.html', {'blog':blog})
def forgotpass(request, id):
    bog = get_user_model().objects.get(id=int(id))
    return render(request, 'app1/forgetpass.html', {'bog': bog})
def changepassword(request,id):
    if request.method=='POST':
        password=request.POST['password']
        password1=request.POST['password1']
        if password!=password1:
            messages.error(request,'Password Not Matched')
            bog = get_user_model().objects.get(id=int(id))
            return render(request, 'app1/forgetpass.html', {'bog': bog})
        bog = get_user_model().objects.get(id=int(id))
        bog.set_password(password)
        bog.save()
        messages.success(request,'Password Saved')
        return render(request, 'app1/forgot.html')
def myprofile(request, name):
    bog=get_user_model().objects.get(username=name)
    print(name)
    from .models import image
    from .models import appointment
    har=appointment.objects.filter(name=name)
    print(har)

    kar=len(har)
    return render(request,'app1/myprofile.html', {'bog': bog , 'har': har, 'kar':kar})
def deletepost(request,id):
    from .models import appointment
    blog=appointment.objects.get(ids=id)
    name=blog.name
    print(name)
    bog=get_user_model().objects.get(username=name)
    blog.delete()
    har = appointment.objects.filter(name=name)
    print(har)
    kar = len(har)


    return render(request,'app1/myprofile.html',{'bog':bog,'har':har, 'kar':kar})

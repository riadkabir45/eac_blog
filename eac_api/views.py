from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import login,authenticate
from .models import Student, Post
from datetime import datetime as dt
import copy

# Create your views here.

def home(req):
    if req.method == "POST":
        pdata = req.POST
        uname = pdata["username"]
        upass = pdata["password"]
        redata = {"username": uname}
        user = authenticate(username=uname,password=upass)
        print(user)
        if user is not None:
            login(req,user)
            return redirect(users)
        else:
            redata['msgf'] = "Invalid credintials"
        return render(req,"index.html",redata)
    return render(req,"index.html")

def signup(req):
    date = dt.now().year
    now = dt.now().strftime('%Y-%m-%d')
    if req.method == 'POST':
        pdata = req.POST
        usname=pdata['username']
        if Student.objects.filter(username=usname).exists():
            udata = {key: value for key, value in pdata.items()}
            udata['msgf'] = "Username already taken"
            return render(req,"signup.html",udata)        
        uname=pdata['name']
        upass=pdata['password']
        cpass=pdata['cpassword']
        umail=pdata['email']
        udate=pdata['date']
        ubatch=pdata['batch']
        uins=pdata['instution']
        usub=pdata['subject']
        ubio=pdata['bio']
        img=req.FILES.get("img")
        if ubatch == "":
            ubatch = 0
        if upass == cpass:
            conc = Student.objects.create_user(username=usname,password=upass,name=uname,date=udate,batch=ubatch,instution=uins,subject=usub,bio=ubio,image=img)
            conc.save()
        else:
            udata = {key: value for key, value in pdata.items()}
            udata['msgf'] = "Both password did not match"
            return render(req,"signup.html",udata)        
        return redirect(home)
    return render(req,"signup.html",{'year':date,'date':now})

@login_required(login_url='home')
def img(req,student_id):
    try:
        student = Student.objects.get(username=student_id)
        image_data = student.image.read()
        content_type = 'image/jpeg'
        response = HttpResponse(image_data, content_type=content_type)
        response['Content-Disposition'] = f'attachment; filename="{student.image.name}"'
        return response
    except Student.DoesNotExist:
        return HttpResponse('Student not found', status=404)

@login_required(login_url='home')
def users(req):
    return render(req,"users.html",{'users': Student.objects.all()})

@login_required(login_url='home')
def profile(req,user_id=None):
    if user_id is not None:
        user = Student.objects.get(id=user_id)
        return render(req,"profile.html",{'user': user})
    return render(req,"profile.html",{'user': req.user})

@login_required(login_url='home')
def post(req):
    if req.method == 'POST':
        pdata = req.POST
        utext=pdata['ptext']
        npost = Post(student=req.user,text=utext)
        npost.save()
    posts = list(Post.objects.all())
    posts.reverse()
    return render(req,"post.html",{'users': posts})


def logout(req):
    req.session.flush()
    return redirect(home)
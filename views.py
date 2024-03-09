
# from os import uname
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from practice.forms import *
from practice.models import *
from tkinter import *
from tkinter import messagebox
from datetime import date


# Create your views here.




def index(request):
    if 'student' in request.session.keys():
        return redirect('home1')
    else:
        return render(request,'index.html')

def save(request):
    if 'username' in request.session.keys():
        s1=user(uname=request.POST['nm'],uemail=request.POST['em'],upass=request.POST['pswd'],uroll=request.POST['rm'])
        s1.save()
        return render(request,'home1.html',{'s1':s1})
    else:
        return redirect('/practice/signup')

    # s1=user(uname=request.POST['nm'],uemail=request.POST['em'],upass=request.POST['pswd'])
    # s1.save()
    # return render(request,'home1.html',{'s1':s1})

def check(request):
    try:
        if 'student' in request.session.keys():
            std = request.session['student']
            s1=user.objects.get(uemail=std)
            return render(request,'home1.html',{'s1':s1})
        else :
            s1=user.objects.get(uemail=request.POST['em'])
            if(s1.upass==request.POST['pswd']):
                request.session['student']=request.POST['em']
                return render(request,'home1.html',{'s1':s1})
            else:
                root1=Tk()
                root1.withdraw()
                root1.attributes('-topmost',True)
                messagebox.showerror('incorrect password','The entered password does not match with the email')
                return redirect('/practice/index')
                # return HttpResponse('<h1>incorrect password</h>')
    except Exception as e: 
        root=Tk()
        root.withdraw()
        root.attributes('-topmost',True)
        messagebox.showerror('invalid','this email is not registered with us')
        return redirect('/practice/index')
        # return HttpResponse('Unable to locate the address')


def signup(request):
    request.session['username']='param'
    return render(request,'signup.html')



def home1(req):
    if 'student' in req.session.keys():
        return render(req,'home1.html')
    else:
        return redirect('index')
    





def attendance(request):
    if 'student' in request.session.keys():
        n=request.GET['srr']
        s1=user.objects.get(uname=n)
        m=s1.jm.keys()
        p=s1.jp.keys()
        c=s1.jc.keys()
        el=s1.jel.keys()
        ex=s1.jex.keys()
        mv=s1.jm.values()
        pv=s1.jp.values()
        cv=s1.jc.values()
        elv=s1.jel.values()
        exv=s1.jex.values()
        return render(request,'attendance.html',{'m':m,'p':p,'c':c,'el':el,'ex':ex,'mv':mv,'pv':pv,'cv':cv,'elv':elv,'exv':exv})
    else :
        return redirect("./index")

def teacher(request):
    if 'email' in request.session.keys():
        s1=user.objects.all().values()
        return render(request,'teacher.html',{'s':s1})
    else:
        return redirect("./tlogin")


def deleteS(request):
    roll=request.GET['sr']
    s1=user.objects.filter(uroll=roll)
    s1.delete()
    return redirect('/practice/teacher')

def updateS(request):
    roll=request.GET['sr1']
    s1=user.objects.get(uroll=roll)
    return render(request,'updateS.html',{'s':s1})

def updateSR(request):
    n=request.GET['sr1']
    s1=user.objects.get(uname=n)
    return render(request,'updateSR.html',{'s':s1})


def upsave(request):
    # if request.method == 'POST':
       roll = request.POST.get('r')
       s1=user.objects.get(uroll=roll)
       s1.uname=request.POST.get('n')
       s1.uemail=request.POST.get('e')
       s1.umob=request.POST.get('m')
       s1.ubranch=request.POST.get('b')
       s1.upaid=request.POST.get('p')
       s1.ufine=request.POST.get('f')
       s1.save()
       print(request.POST.get('m'))
       return redirect('/practice/teacher')

def upsaveSR(request):
    if request.method == 'POST':
       n = request.POST.get('n')
       s1=user.objects.get(uname=n)
       s1.um=request.POST.get('m')
       s1.uphy=request.POST.get('p')
       s1.uchem=request.POST.get('c')
       s1.uelec=request.POST.get('el')
       s1.uelex=request.POST.get('ex')
       s1.um2=request.POST.get('m2')
       s1.uphy2=request.POST.get('p2')
       s1.uchem2=request.POST.get('c2')
       s1.uelec2=request.POST.get('el2')
       s1.uelex2=request.POST.get('ex2')
       s1.am=request.POST.get('ma')
       s1.aphy=request.POST.get('pa')
       s1.achem=request.POST.get('ca')
       s1.aelec=request.POST.get('ela')
       s1.aelex=request.POST.get('exa')
       s1.save()
       return redirect('/practice/teacher')

def formmm(request):
    obj=DB()
    return render(request,'database.html',{'obj':obj})

def insert(request):
    s1=user(uroll=request.POST['roll'],uname=request.POST['name'],uemail=request.POST['email'],umob=request.POST['contact'])
    s1.save()
    return redirect("/practice/teacher")
    

def assign(req):
    if 'student' in req.session.keys():
        return render (req,'assignment.html') 
    else :
        return redirect("./index")

def profile(request):
    return render(request,'profile.html')

def ajax2(req):
    v=req.GET['val']
    s1=user.objects.get(uname=v)
    return render(req,'ajax.html',{'s1':s1})

def result(request):
    if 'student' in request.session.keys():
        n=request.GET['srr']
        return render(request,'result.html',{'n':n})
    else :
        return redirect("./index")

def ajax2res(req):
    v=req.GET['val']
    v1=req.GET['val1']
    s1=user.objects.get(uname=v1)
    if (v=="Test 1"):
        return render(req,'ajax2res.html',{'v':v,'s1':s1})
    else:
        return render(req,'ajax2res2.html',{'v':v,'s1':s1})

def tlogin(req):
    if 'email' in req.session.keys():
        s1=teacherr.objects.get(temail = req.session['email'])
        return redirect('/practice/teacher?s1=s1')
    else :        
        return render(req,'tlogin.html')

def tcheck(request):
    try:
        s1=teacherr.objects.get(temail=request.POST['em'])
        if(s1.tpass==request.POST['pswd']):
            request.session['email'] = request.POST['em']
            return redirect('/practice/teacher?s1=s1')
        else:
            root=Tk()
            root.withdraw()
            root.attributes('-topmost',True)
            messagebox.showerror('incorrect password','The entered password does not match with the email')
            return redirect('/practice/tlogin')
    except Exception as e: 
        root=Tk()
        root.withdraw()
        root.attributes('-topmost',True)
        messagebox.showerror('invalid','this email is not registered with us')
        return redirect('/practice/tlogin')

def fees(req):
    if 'student' in req.session.keys():
        n=req.GET['srr']
        s1=user.objects.get(uname=n)
        s1.upending=107325-s1.upaid
        s1.save()
        return render(req,'fees.html',{'s1':s1})
    else :
        return redirect("./index")

def tsave(req):
    obj=savee()
    return render(req,'tsave.html',{'obj':obj})

def ss(req):
    s1=teacherr(temail=req.POST['email'],tpass=req.POST['password'])
    s1.save()
    return HttpResponse('done')

def upattend(req):
    if 'email' in req.session.keys():
        s1=user.objects.all().values()
        today=date.today().strftime('%Y-%m-%d')
        return render(req,'upattend.html',{'s':s1,'today':today})
    else:
        return redirect("./tlogin")
 
def attendsave(req):
    s1=user.objects.all()
    n=req.POST["1"]
    for record in s1:
        r=str(record.uroll)
        attend=req.POST[r]
        if attend=='p':
            record.uattendance="present"
            d=req.POST["date"]
            if n=="submit1":
                record.jm[d]="present"
                print(record.jm[d])
                print(d)
            elif n=="submit2":
                record.jp[d]="present"
            elif n=="submit3":
                record.jc[d]="present"
            elif n=="submit4":
                record.jel[d]="present"
            elif n=="submit5":
                record.jex[d]="present"
        else:
            record.uattendance="absent"
            d=req.POST["date"]
            if n=="submit1":
                record.jm[d]="absent"
            elif n=="submit2":
                record.jp[d]="absent"
            elif n=="submit3":
                record.jc[d]="absent"
            elif n=="submit4":
                record.jel[d]="absent"
            elif n=="submit5":
                record.jex[d]="absent"
        record.save()
    return redirect('/practice/teacher')



def logout(req):
    if 'student' in req.session.keys():
        del req.session['student']
        return redirect('./index')
    return redirect('./index')

def tlogout(req):
    if 'email' in req.session.keys():
        del req.session['email']
        return redirect('./tlogin')
    return redirect('./tlogin')


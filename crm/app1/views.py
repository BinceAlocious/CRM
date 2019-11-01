from django.shortcuts import render,get_object_or_404
from app1.forms import RegCourse,RegBatch,RegUser,NewUser
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from app1.models import Course,Batch,Register,User,HrUser,ApprovedTable,Trainer,Payment
from django.views.generic import CreateView,TemplateView,ListView
from dsp.models import SessionReport
from timetable.models import ToApproveTB
# Create your views here.
def index(request):
    return render(request,"app1/index.html")

def reg(request):
    obj=RegCourse()
    cr=Course.objects.all()
    dict={"reg":obj,"cr":cr}
    if request.method=='POST':
        frm=RegCourse(request.POST)
        if frm.is_valid():
            frm.save(commit=True)
    return render(request,"app1/addcourse.html",dict)
def edit(request,pk):
    obj=get_object_or_404(Course,pk=pk)
    frm=RegCourse(instance=obj)
    dict={"frm":frm}
    if(request.method=='POST'):
        fm=RegCourse(request.POST)
        if fm.is_valid():
            up=fm.cleaned_data["Course_Name"]
            obj.Course_Name=up
            obj.save()
            return reg(request)
    return render(request,"app1/edit.html",dict)

def delete(request,pk):
    obj=get_object_or_404(Course,pk=pk)
    dict={"obj":obj}
    if(request.method=='POST'):
        obj.delete()
        return reg(request)
    return render(request,"app1/delete.html",dict)
def batchreg(request):
    obj=RegBatch()
    ba=Batch.objects.all()
    dict={"obj":obj,"ba":ba}
    if request.method=='POST':
        rec=RegBatch(request.POST)
        if rec.is_valid():
            rec.save(commit=True)
    return render(request,"app1/addbatch.html",dict)
def editb(request,pk):
    obj=get_object_or_404(Batch, pk=pk)
    frm=RegBatch(instance=obj)
    dict={"frm": frm}
    if (request.method == 'POST'):
        fm=RegBatch(request.POST)
        if fm.is_valid():
            bc=fm.cleaned_data["Batch_Code"]
            sc=fm.cleaned_data["Select_Course"]
            d=fm.cleaned_data["Date"]
            fe=fm.cleaned_data["Fees"]
            obj.Batch_Code=bc
            obj.Select_Course=sc
            obj.Date=d
            obj.Fees=fe
            obj.save()
            return batchreg(request)
    return render(request,"app1/editb.html",dict)

def deleteb(request,pk):
    obj=get_object_or_404(Batch,pk=pk)
    dict={"obj":obj}
    if (request.method == 'POST'):
        obj.delete()
        return batchreg(request)
    return render(request,"app1/deleteb.html",dict)
def get_batch(request):
    course=request.GET.get('Select_Course')
    batch = Batch.objects.filter(Select_Course_id=course)
    return render(request,'app1/getdrop.html', {'batch': batch})
def newuser(request):
    obj=NewUser()
    dict1={"nusr":obj}
    if request.method=='POST':
        mydit=dict(request.POST)
        print(mydit)
        print(mydit["Name"][0])
        co=Course.objects.get(pk=mydit["Select_Course"][0])
        ba=Batch.objects.get(pk=mydit["Select_Batch"][0])
        pa=Payment.objects.get(pk=mydit["Payment"][0])
        em=mydit["Email"][0]
        vm=mydit["Verify_Email"][0]
        if(em==vm):
            nus=Register(Name=mydit["Name"][0],Qualification=mydit["Qualification"][0],Address=mydit["Address"][0],Phone_No=mydit["Phone_No"][0],Email=mydit["Email"][0],Verify_Email=mydit["Verify_Email"][0],Password=mydit["Password"][0],Select_Course=co,Select_Batch=ba,Payment=pa)
            nus.save()
        else:
            raise ValidationError("Error Emails Do not Match")
    return render(request,"app1/register.html",dict1)
def admin(request):
    return render(request,"app1/admin.html")
class RegisterHR(CreateView):
    model = HrUser
    fields = '__all__'
    template_name = 'app1/registerhr.html'
    success_url = reverse_lazy('app1:admin')
def hr(request):
    form = RegUser()
    dict = {'form': form}
    us =HrUser.objects.all()
    if request.method == 'POST':
        frm = RegUser(request.POST)
        if frm.is_valid():
            em = frm.cleaned_data['User_Email']
            pa = frm.cleaned_data['Password']
            for i in us:
                if (i.Email == em and i.Password == pa):
                    dict = {'stu': i}
                    return render(request, "app1/hr.html", dict)
    return render(request,"app1/hr.html",dict)
def vcourse(request):
    obj=Course.objects.all()
    dict={"obj":obj}
    return render(request,"app1/courses.html",dict)
def vbatch(request,pk):
    co=Course.objects.get(Course_Name=pk)
    obj=Batch.objects.filter(Select_Course=co)
    dict={"rec":obj}
    return render(request,"app1/batches.html",dict)
def vstudent(request,pk):
    ba=Batch.objects.get(Batch_Code=pk)
    obj=Register.objects.filter(Select_Batch=ba)
    dict={"rec":obj}
    return render(request,"app1/students.html",dict)
def studetails(request,pk):
    obj=Register.objects.get(Name=pk)
    dict = {"rec": obj}
    return render(request, "app1/userpg.html", dict)
def allstu(request):
    obj=Register.objects.all()
    dict = {"rec": obj}
    return render(request, "app1/students.html", dict)
def search(request):
    if request.method=='GET':
        pk=request.GET.get('q')
        result=Register.objects.filter(Q(Name__icontains=pk) |Q(Qualification__icontains=pk) |Q(Email__icontains=pk) |Q(Address__icontains=pk))
        if result.exists():
            dict={"records":result}
            return render(request,"app1/searchpg.html",dict)
        else:
            result=Batch.objects.filter(Q(Batch_Code__icontains=pk) |Q(Date__icontains=pk))
            if result.exists():
                dict={"rec":result}
                return render(request,"app1/batches.html",dict)
            else:
                result=Course.objects.filter(Q(Course_Name__icontains=pk))
                if result.exists():
                    dict={"obj":result}
                    return render(request,"app1/courses.html",dict)
                else:
                    return index(request)
    return render(request,"app1/base.html")
class Homepg(TemplateView):
    template_name = 'registration/home.html'
def Stupg(request):
    form=RegUser()
    dict={'form':form}
    us=Register.objects.all()
    if request.method=='POST':
        frm=RegUser(request.POST)
        if frm.is_valid():
            em=frm.cleaned_data['User_Email']
            pa=frm.cleaned_data['Password']
            for i in us:
                if(i.Email==em and i.Password==pa):
                    dict={'stu':i}
                    return render(request,"app1/studentpg.html",dict)
    return render(request,"app1/studentpg.html",dict)
class ViewTimeTable(ListView):
    model = ToApproveTB
    context_object_name = 'records'
    template_name = 'app1/timetable.html'
def aptimetable(request):
    tb=ToApproveTB.objects.all()
    ob = ApprovedTable.objects.all()
    ob.delete()
    for i in tb:
        obj=ApprovedTable(Select_Batch=i.Select_Batch,Start_Time=i.Start_Time,End_Time=i.End_Time,Class_Room=i.Class_Room,Date=i.Date)
        obj.save()
    return admin(request)
class VTimeTable(ListView):
    model = ApprovedTable
    context_object_name = 'records'
    template_name = 'app1/viewtimetable.html'
class AddTrainer(CreateView):
    model = Trainer
    fields = '__all__'
    template_name = 'app1/addtrainer.html'
    success_url = reverse_lazy('app1:admin')
class Addpayment(CreateView):
    model = Payment
    fields = '__all__'
    template_name = 'app1/payment.html'
    success_url = reverse_lazy('app1:hr')
class ViewTrainer(ListView):
    model = Trainer
    context_object_name = 'records'
    template_name = 'app1/viewtrainer.html'
def TrainerPg(request):
    form = RegUser()
    dict = {'form': form}
    us =Trainer.objects.all()
    if request.method == 'POST':
        frm = RegUser(request.POST)
        if frm.is_valid():
            em = frm.cleaned_data['User_Email']
            pa = frm.cleaned_data['Password']
            for i in us:
                if (i.Email == em and i.Password == pa):
                    dict = {'stu': i}
                    return render(request, "app1/trainer.html", dict)
    return render(request,"app1/trainer.html",dict)
def vdailysession(request,pk):
    obj=Trainer.objects.get(pk=pk)
    dsp=SessionReport.objects.filter(Trainer_Name=obj)
    print(dsp)
    dict={"records":dsp}
    return render(request,"app1/dailysessionreports.html",dict)
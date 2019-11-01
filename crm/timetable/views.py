from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView
# Create your views here.
from timetable.models import Batch,ClassRoom,TimeTable,ToApproveTB
from timetable.forms import TableForm
from app1.models import Trainer
from django.contrib import messages
from django.contrib.messages import get_messages
lst=[]
ro={}
re={}
class Homepg(TemplateView):
    template_name = 'base.html'
def get_room(request):
    global ro
    global re
    st=request.GET.get('Start_Time')
    en=request.GET.get('End_Time')
    print("st",st,"end",en)
    cls=ClassRoom.objects.all()
    if st not in ro or en not in re:
        for i,j in zip(ro,re):
            if((st>i and st<j) or (en>i and en<j)):
                print("------------------------error---------------------------")
                messages.warning(request, 'Error:Time Added Conflicts with Existing Schedule')
        else:
            cls = ClassRoom.objects.all()
            return render(request, 'timetable/getdrop.html', {'cls': cls})
    else:
        if(ro[st]==re[en]):
            for k in range(0,len(ro[st])):
                cls=cls.exclude(Class_Name=ro[st][k])
            return render(request, 'timetable/getdrop.html', {'cls': cls})
    return render(request,'timetable/getdrop.html', {'cls':cls})
def get_form(request):
    global lst
    frm = TableForm(lst)
    dit = {"form": frm}
    return render(request, "timetable/index.html", dit)
def CreateTable(request):
    frm=TableForm(None)
    global lst
    global ro
    global re
    dit={"form":frm}
    if request.method=='POST':
        storage = get_messages(request)
        mydit=dict(request.POST)
        if(not storage):
            bc=Batch.objects.get(pk=mydit["Select_Batch"][0])
            ts=mydit['Start_Time'][0]
            en=mydit['End_Time'][0]
            cls=ClassRoom.objects.get(pk=mydit['Class_Room'][0])
            fm=TimeTable(Select_Batch=bc,Start_Time=ts,End_Time=en,Class_Room=cls)
            fm.save()
            if ts not in ro:
                ro.update({ts:[cls]})
            else:
                cl=ro[ts]
                cl.append(cls)
                ro[ts]=cl
            if en not in re:
                re.update({en:[cls]})
            else:
                cl=re[en]
                cl.append(cls)
                re[en]=cl
            print("ro",ro,"re",re)
            if(bc not in lst):
                lst.append(bc)
                return get_form(request)
        return get_form(request)
    return render(request,"timetable/index.html",dit)
class ViewTimeTable(ListView):
    model = TimeTable
    context_object_name = 'records'
    template_name = 'timetable/timetable.html'
def toapprovetimetable(request):
    tb=TimeTable.objects.all()
    ob = ToApproveTB.objects.all()
    ob.delete()
    for i in tb:
        obj=ToApproveTB(Select_Batch=i.Select_Batch,Start_Time=i.Start_Time,End_Time=i.End_Time,Class_Room=i.Class_Room,Date=i.Date)
        obj.save()
    return render(request,"timetable/timetable.html",{"records":tb})

def endsession(request):
    TimeTable.objects.all().delete()
    global ro
    global lst
    global re
    lst=[]
    ro={}
    re={}
    return render(request,'app1/index.html')
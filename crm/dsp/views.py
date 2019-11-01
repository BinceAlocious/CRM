from django.shortcuts import render
from django.urls import reverse_lazy
from dsp.models import SessionReport
from app1.models import Register
from dsp.forms import SessionForm
from django.views.generic import CreateView,TemplateView,DetailView
def DailyReport(request,pk):
    rec=SessionReport.objects.filter(Student_Name=pk)
    nm=Register.objects.get(Name=pk)
    form=SessionForm(initial={'Student_Name':nm.Name})
    dict={'form':form,'record':rec}
    if(request.method=='POST'):
        frm=SessionForm(request.POST)
        if frm.is_valid():
            frm.save(commit=True)
            return render(request,"dsp/report.html",dict)
    return render(request,"dsp/report.html",dict)

class Detail(DetailView):
    model = SessionReport
    fields='__all__'
    context_object_name = 'rec'
    template_name = 'dsp/details.html'
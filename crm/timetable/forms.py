from django.forms import ModelForm
from timetable.models import TimeTable,ClassRoom
from app1.models import Batch

class TableForm(ModelForm):
    class Meta:
        model= TimeTable
        exclude= ('Date',)
    def __init__(self,batchcode, *args, **kwargs):
        super(TableForm,self).__init__(*args, **kwargs)
        if(batchcode):
            obj = Batch.objects.all()
            for i in batchcode:
                obj=obj.exclude(Batch_Code=i)
            self.fields['Select_Batch'].queryset =obj
        self.fields['Class_Room'].queryset =ClassRoom.objects.none()

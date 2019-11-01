from django.contrib import admin
from app1.models import Course,Batch,User,Register,HrUser,ApprovedTable,Payment,Trainer
# Register your models here.
admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(User)
admin.site.register(Register)
admin.site.register(HrUser)
admin.site.register(ApprovedTable)
admin.site.register(Trainer)
admin.site.register(Payment)


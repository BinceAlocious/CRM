from django.urls import path
from app1 import views
app_name='app1'
urlpatterns = [
    path("",views.index,name='index'),
    path("home",views.Homepg.as_view(),name='home'),
    path("addcourse",views.reg,name='course'),
    path("edit/<int:pk>",views.edit,name='edit'),
    path("delete/<int:pk>",views.delete,name='delete'),
    path("editb/<int:pk>",views.editb,name='editb'),
    path("deleteb/<int:pk>",views.deleteb,name='deleteb'),
    path("addbatch",views.batchreg,name='batch'),
    path("register",views.newuser,name='newusr'),
    path("adm", views.admin, name='admin'),
    path("hr", views.hr, name='hr'),
    path("vcourse",views.vcourse,name='vcourse'),
    path("vbatch/<str:pk>",views.vbatch,name='vbatch'),
    path("vstu/<str:pk>", views.vstudent, name='vstu'),
    path("details/<str:pk>", views.studetails, name='details'),
    path("allstu", views.allstu, name='allstu'),
    path('ajax/getdrop',views.get_batch,name='getdrop'),
    path("search",views.search,name='search'),
    path("studentpg", views.Stupg, name='stupg'),
    path("registerhr",views.RegisterHR.as_view(),name='regHR'),
    path("approvetmtable",views.ViewTimeTable.as_view(),name='verifytm'),
    path("verifiedtables",views.aptimetable,name='aptb'),
    path("studentViewTb",views.VTimeTable.as_view(),name='stutb'),
    path("addtrainer",views.AddTrainer.as_view(),name='addtra'),
    path("addpayment",views.Addpayment.as_view(),name='addpay'),
    path("viewtrainer", views.ViewTrainer.as_view(), name='viewtra'),
    path("trainerpg",views.TrainerPg,name='trapg'),
    path("viewdailysessionreport/<int:pk>", views.vdailysession, name='vdsp'),

]

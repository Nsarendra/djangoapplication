from django.urls import path
from admissions.views import addAdmission
from admissions.views import admissionReport
from admissions.views import addVendor
from admissions.views import deleteStudent
from admissions.views import updateStudent
from admissions.views import FirstClassBasedView






urlpatterns = [

    path('newadm/', addAdmission ),
    path('admreport/', admissionReport ),
    path('newvendor/', addVendor ),
    path('delete/', deleteStudent ),
    path('update/', updateStudent ),
    path('firstcbv/', FirstClassBasedView.as_view()),



]

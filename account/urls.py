from django.urls import path
from account.views import doctorSignup, paitentSignup, doctorSignin, paitentSignin, dashboard, home, logout

app_name = "account"

urlpatterns = [
    path('', home, name='home'),
    path('doctor_signup/', doctorSignup, name='doctor_signup'),
    path('paitent_signup/', paitentSignup, name='paitent_signup'),
    path('doctor_signin/', doctorSignin, name='doctor_signin'),
    path('paitent_signin/', paitentSignin, name='paitent_signin'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout, name='logout'),
]

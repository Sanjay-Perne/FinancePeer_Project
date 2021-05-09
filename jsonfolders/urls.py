from django.conf.urls import include,url
from . import views

urlpatterns = [

    #signup
    url('signup', views.signup, name="signup"),

    #signin
    url('signin', views.signin, name="signin"),

    #signout
    url('signout', views.signout, name="signout"),

    #jsonfolders
    url(r'^$', views.index, name="index"),

    #data
    url('data', views.parseData, name="parsedata"),

]

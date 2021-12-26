from . import views
# from .views import *
from django.urls import path
urlpatterns=[
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.login,name="login"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("logout/",views.logout,name="logout"),
    path("profile/",views.profile,name="profile"),
    path("blogadv/",views.blogadv,name="blogadv"),
    path("newsletter/",views.newsletter,name="newsletter"),
    path("editprofile/",views.editprofile,name="editprofile"),
    path("changepassword/",views.changepassword,name="changepassword"),
    path("resendpass/",views.resendpass,name="resendpass"),
    path("crudblog/",views.crudblog,name="crudblog"),
    path("crudadv/",views.crudadv,name="crudadv"),
    path("createadv/",views.createadv,name="createadv"),
    path("deleteadv/",views.deleteadv,name="deleteadv"),
    path("createblog/",views.createblog,name="createblog"),
    path("deleteblog/",views.deleteblog,name="deleteblog"),
    path("rentpg/",views.rentpg,name="rentpg"),
    path("listpg/",views.listpg,name="listpg"),
    path("crudpg/",views.crudpg,name="crudpg"),
    path("addpg/",views.addpg,name="addpg"),
    path("delpg/",views.delpg,name="delpg"),
    path("uppg/",views.uppg,name="uppg"),
    path("search/",views.search,name="search"),
    path("advsearch/",views.advsearch,name="advsearch"),
]
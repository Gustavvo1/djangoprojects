from django.urls import path

from . import views 


urlpatterns = [
    path('',views.index , name="index"),
    path('index.html',views.index , name="index"),
    path('portfolio.html',views.portfolio , name="portfolio"),
    path('blog.html',views.blog , name="blog"),
    path('blog-single.html',views.detail , name="detail"),
    path('about.html',views.about , name="about"),
    path('donate.html',views.donate , name="donate"),
    path('takeaction.html',views.takeaction , name="takeaction"),
    ]

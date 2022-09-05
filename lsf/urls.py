from django.contrib import admin
from django.conf import settings
from django.urls import path
from App1 import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="home"),
    path('request/Famous/posts',views.jono,name="jono"),
    path('request/contact',views.contactus,name="contact"),
    path('book/review',views.book,name="bookreview"),
    path('samprotik', views.samprotik, name="samprotik"),
    path('samajik/andolon',views.samazik,name="samazik"),
    path('songbad/',views.dailysongbad, name="songbad"),
    path('etihash',views.etihash,name="etihash"),
    path('Ainibebostha',views.crime,name="crime"),
    path('Policitcs',views.rajniti,name="rajniti"),
    path('inverviews',views.interviews,name="interview"),
    path('Life',views.jiboni,name="jiboni"),
    path('islam',views.islam,name="islam"),
    path('bibidh',views.bibidh,name="bibidh"),
    path('blog', views.blogs,name="blog"),
    path('request/catagory',views.category,name="catagory"),
    path('(<slug>[\w-]+)/',views.single,name="single"),
    path('breakingnews/(<slug>[\w-]+)/',views.BrakingNews,name="bournews"),
    path('book/(<slug>[\w-]+)/',views.breview,name="sin"),
    path('socity/Reform(<slug>[\w-]+)/',views.samaziksingle,name="samaz"),
    path('history/all/updates(<slug>[\w-]+)/',views.historysingle,name="newhisto"),
    path('news/(<slug>[\w-]+)/', views.songbadsingle,name="allnews"),
    path('law/updates(<slug>[\w-]+)/', views.newlaw, name="newlaws"),
    path('pilitics/updates(<slug>[\w-]+)/', views.politicssingle, name="politics"),
    path('interviews/updates(<slug>[\w-]+)/', views.interviewsingle, name="myinter"),
    path('biographi/pesonalities/updates(<slug>[\w-]+)/', views.singlejiboni, name="myjibon"),
    path('Life/style&islam/(<slug>[\w-]+)/',views.singleislamic,name="myislam"),
    path('bibidh/post/updates(<slug>[\w-]+)/', views.singlebibidh, name="mybibidh"),
    path('blog/post/updates(<slug>[\w-]+)/', views.singleblog, name="myblog"),
    path('recent/world-s/updates(<slug>[\w-]+)/', views.singlesamprotik, name="myworld"),
    path('search',views.search,name="search"),

]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
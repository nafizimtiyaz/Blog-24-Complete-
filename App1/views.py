from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .models import artical,bookreview,somajsongsker,songbad,itihash,law,politics,interview,Personality,Islamic,Bibidh,blog,Recentworld,BrakingNews,ElectedPost
from django.core.paginator import Paginator
from django.db.models import Q

def Home(request):
    my =artical.objects.all().order_by('slug')[:7]
    me=bookreview.objects.all().order_by('slug')[:7]
    somaj=somajsongsker.objects.all().order_by('slug')[:7]
    mynews = songbad.objects.all().order_by('slug')[:7]
    myhisto = itihash.objects.all().order_by('slug')[:7]
    melaw  = law.objects.all().order_by('slug')[:7]
    mypoli= politics.objects.all().order_by('slug')[:7]
    allinter=interview.objects.all().order_by('slug')[:7]
    myper=Personality.objects.all().order_by('slug')[:7]
    ourislam=Islamic.objects.all().order_by('slug')[:7]
    ourbi=Bibidh.objects.all().order_by('slug')[:7]
    ourblog=blog.objects.all().order_by('slug')[:7]
    myrecent=Recentworld.objects.all().order_by('slug')[:7]
    bnews=BrakingNews.objects.all().order_by('slug')[:7]
    myelected=ElectedPost.objects.all().order_by('slug')[:13]


    recent01 = artical.objects.all().order_by('slug')[:1]
    recent02 = bookreview.objects.all().order_by('slug')[:1]
    recent03 = somajsongsker.objects.all().order_by('slug')[:1]
    recent04 = songbad.objects.all().order_by('slug')[:1]
    recent05 = itihash.objects.all().order_by('slug')[:1]
    recent06 = law.objects.all().order_by('slug')[:1]
    recent07 = politics.objects.all().order_by('slug')[:1]
    recent08 = interview.objects.all().order_by('slug')[:1]
    recent09 = Personality.objects.all().order_by('slug')[:1]
    recent10 = Islamic.objects.all().order_by('slug')[:1]
    recent11 = Bibidh.objects.all().order_by('slug')[:1]
    recent12 = blog.objects.all().order_by('slug')[:1]
    recent13 = Recentworld.objects.all().order_by('slug')[:1]



    famous01 = artical.objects.all().order_by('views')[:1]
    famous02 = bookreview.objects.all().order_by('views')[:1]
    famous03 = somajsongsker.objects.all().order_by('views')[:1]
    famous04 = songbad.objects.all().order_by('views')[:1]
    famous05 = itihash.objects.all().order_by('views')[:1]
    famous06 = law.objects.all().order_by('views')[:1]
    famous07 = politics.objects.all().order_by('views')[:1]
    famous08 = interview.objects.all().order_by('views')[:1]
    famous09 = Personality.objects.all().order_by('views')[:1]
    famous10 = Islamic.objects.all().order_by('views')[:1]
    famous11 = Bibidh.objects.all().order_by('views')[:1]
    famous12 = blog.objects.all().order_by('views')[:1]
    famous13 = Recentworld.objects.all().order_by('views')[:1]




    return render(request,"index.html",{'my':my,'me':me,'somaj':somaj,'mynews':mynews,'myhisto':myhisto,
    'melaw':melaw,'mypoli':mypoli,'allinter':allinter,'myper':myper,'ourislam':ourislam,'ourbi':ourbi,
    'ourblog':ourblog,'myrecent':myrecent,'bnews':bnews,'myelected':myelected,'recent01':recent01,'recent02':recent02,'recent03':recent03,'recent04':recent04,'recent05':recent05,'recent06':recent06,'recent07':recent07,'recent08':recent08,'recent09':recent09,'recent10':recent10,'recent11':recent11,'recent12':recent12,'recent13':recent13,'famous01':famous01,'famous02':famous02,'famous03':famous03,'famous04':famous04,'famous05':famous05,'famous06':famous06,'famous07':famous07,'famous08':famous08,'famous09':famous09,'famous10':famous10,'famous11':famous11,'famous12':famous12,'famous13':famous13})

def search(request):
    a1=artical.objects.all()
    search = request.GET.get('q')
    if search:
        a1 = a1.filter(
            Q(title__icontains=search)
        )
    b1=bookreview.objects.all()
    search = request.GET.get('q')
    if search:
        b1 = b1.filter(
            Q(title__icontains=search)
        )
    c1=somajsongsker.objects.all()
    search = request.GET.get('q')
    if search:
        c1 = c1.filter(
            Q(title__icontains=search)
        )
    d1=songbad.objects.all()
    search = request.GET.get('q')
    if search:
        d1 = d1.filter(
            Q(title__icontains=search)
        )
    e1=itihash.objects.all()
    search = request.GET.get('q')
    if search:
        e1 = e1.filter(
            Q(title__icontains=search)
        )
    f1=law.objects.all()
    search = request.GET.get('q')
    if search:
        f1 = f1.filter(
            Q(title__icontains=search)
        )
    g1=politics.objects.all()
    search = request.GET.get('q')
    if search:
        g1 = g1.filter(
            Q(title__icontains=search)
        )
    h1=interview.objects.all()
    search = request.GET.get('q')
    if search:
        h1 = h1.filter(
            Q(title__icontains=search)
        )
    i1=Personality.objects.all()
    search = request.GET.get('q')
    if search:
        i1 = i1.filter(
            Q(title__icontains=search)
        )
    j1=Islamic.objects.all()
    search = request.GET.get('q')
    if search:
        j1 = j1.filter(
            Q(title__icontains=search)
        )
    k1=Bibidh.objects.all()
    search = request.GET.get('q')
    if search:
        k1 = k1.filter(
            Q(title__icontains=search)
        )
    l1=blog.objects.all()
    search = request.GET.get('q')
    if search:
        l1 = l1.filter(
            Q(title__icontains=search)
        )
    m1=Recentworld.objects.all()
    search = request.GET.get('q')
    if search:
        m1 = m1.filter(
            Q(title__icontains=search)
        )
    return render(request,"search.html",{'a1':a1,'b1':b1,'c1':c1,'d1':d1,'e1':e1,'f1':f1,'g1':g1,'h1':h1,'i1':i1,'j1':j1,'k1':k1,'l1':l1,'m1':m1})

def contactus(request):

    return render(request,"contact.html")
def category(request):
    post = artical.objects.all()
    search = request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search)
        )
    paginator = Paginator(post,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,"category.html",{'post':page_obj})
def book(request):
    post = bookreview.objects.all()
    search = request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search)
        )
    paginator = Paginator(post, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"book_review.html",{'post': page_obj})

def samazik(request):
    post = somajsongsker.objects.all()
    search = request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search)
        )
    paginator = Paginator(post, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"samazik.html",{'post': page_obj})

def dailysongbad(request):
    post = songbad.objects.all()
    search = request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search)
        )
    paginator = Paginator(post, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"songbad.html",{'post': page_obj})

def etihash(request):
    post = itihash.objects.all()
    search = request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search)
        )
    paginator = Paginator(post, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"etihash.html",{'post': page_obj})


def crime(request):
    post = law.objects.all()
    search = request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search)
        )
    paginator = Paginator(post, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"crim.html",{'post': page_obj})


def rajniti(request):
    post = politics.objects.all()
    search = request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search)
        )
    paginator = Paginator(post, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"rajniti.html",{'post': page_obj})

def interviews(request):
    post = interview.objects.all()
    search = request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search)
        )
    paginator = Paginator(post, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"interview.html",{'post': page_obj})

def jiboni(request):
    post = Personality.objects.all()
    search = request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search)
        )
    paginator = Paginator(post, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "jiboni.html",{'post': page_obj})

def islam(request):
    post = Islamic.objects.all()
    search = request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search)
        )
    paginator = Paginator(post, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "Islam cinta.html",{'post': page_obj})

def bibidh(request):
    post = Bibidh.objects.all()
    search = request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search)
        )
    paginator = Paginator(post, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "bibidh.html",{'post': page_obj})

def samprotik(request):
    post = Recentworld.objects.all()
    search = request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search)
        )
    paginator = Paginator(post, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "samptikbissho.html",{'post': page_obj})

def blogs(request):
    post = blog.objects.all()
    search = request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search)
        )
    paginator = Paginator(post, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "blog.html",{'post': page_obj})

def jono(request):
    return render(request,"jono.html")

def single(request,slug):
    obj = artical.objects.get(slug=slug)
    obj.views = obj.views + 1
    obj.save()
    return render(request,"single-post.html",{'obj': obj})

def breview(request,slug):
    book = bookreview.objects.get(slug=slug)
    book.views = book.views + 1
    book.save()
    return render(request, "single-book.html", {'book': book})

def samaziksingle(request,slug):
    socity = somajsongsker.objects.get(slug=slug)
    socity.views = socity.views + 1
    socity.save()
    return render(request, "single-samazik.html", {'socity': socity})

def songbadsingle(request,slug):
    daily = songbad.objects.get(slug=slug)
    daily.views = daily.views + 1
    daily.save()
    return render(request, "single-news.html", {'daily':daily})
def historysingle(request,slug):
    histo = itihash.objects.get(slug=slug)
    histo.views = histo.views + 1
    histo.save()
    return render(request, "single-history.html", {'histo':histo})
def newlaw(request,slug):
    crim = law.objects.get(slug=slug)
    crim.views = crim.views + 1
    crim.save()
    return render(request, "single-law.html", {'crim':crim})

def politicssingle(request,slug):
    poli = politics.objects.get(slug=slug)
    poli.views = poli.views + 1
    poli.save()
    return render(request, "single-poli.html", {'poli':poli})
def interviewsingle(request,slug):
    inter = interview.objects.get(slug=slug)
    inter.views = inter.views + 1
    inter.save()
    return render(request, "single-int.html", {'inter': inter})
def singlejiboni(request,slug):
    jibon = Personality.objects.get(slug=slug)
    jibon.views = jibon.views + 1
    jibon.save()
    return render(request, "single-jiboni.html", {'jibon': jibon})
def singleislamic(request,slug):
    islamic = Islamic.objects.get(slug=slug)
    islamic.views = islamic.views + 1
    islamic.save()
    return render(request, "single-islamic.html", {'islamic': islamic})
def singlebibidh(request,slug):
    bibi = Bibidh.objects.get(slug=slug)
    bibi.views = bibi.views + 1
    bibi.save()
    return render(request, "single-bibidh.html", {'bibi': bibi})
def singleblog(request,slug):
    bl = blog.objects.get(slug=slug)
    bl.views = bl.views + 1
    bl.save()
    return render(request, "single-blog.html", {'bl': bl})
def singlesamprotik(request,slug):
    recent = Recentworld.objects.get(slug=slug)
    recent.views = recent.views + 1
    recent.save()
    return render(request, "single-recent.html", {'recent': recent})

from django.shortcuts import render, HttpResponse
from blog.models import Blog, Contact
import math

# Create your views here.

def home(request):
    #return HttpResponse("This is home ")
    return render(request, 'index.html')

def blog(request):
    no_of_posts = 7
    # if request.GET['pageno']
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
        print(page)
        '''
        1 : 0 - 3
        2 : 3 - 6
        3 : 6 - 9
        
                
        1 : 0 - 0 + no_of_posts
        2 : no_of_posts to no_of_posts+ no_of_posts
        3 : no_of_posts+ no_of_posts to no_of_posts+ no_of_posts+ no_of_posts
        
        (page_no-1)*no_of_posts to page_no*no_of_posts
        
                '''
        
        
        
    blogs = Blog.objects.all()
    length = len(blogs)
    blogs =  blogs[(page-1)*no_of_posts: page*no_of_posts]
    
    #return HttpResponse("This is blog ")
    if page>1:
        prev = page -1 
    else:
        prev = None
   # 3.67 = 4
   # 4.56 = 5 (math funcation ) 
    if page<math.ceil(length/no_of_posts):
        nxt = page + 1   
    else:
        nxt = None    
    context = {'blogs': blogs, 'prev': prev, 'nxt': nxt}
    return render(request, 'bloghome.html', context)


def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog': blog}
    
    #return HttpResponse(f"you are viewing {slug}")
    return render(request, 'blogpost.html', context)


def search(request):
   # return HttpResponse("contact.html")
    return render(request, 'search.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
       # print(name, email, phone, desc)
        instance = Contact(name=name, email=email, phone=phone, desc=desc)
        instance.save()
    return render(request, 'contact.html')
      #  print("the data has been written to be db ")
   


#def contact(request):
   # return HttpResponse("contact.html")
   


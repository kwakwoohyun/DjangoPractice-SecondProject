from django.shortcuts import render
from .models import Blog
# Create your views here.
def home(request):
    blogs = Blog.objects #모델로 부터 불러온 객체 : queryset 쿼리셋  # 쿼리셋 메소드 : 쿼리셋을 사용하게 하는것 
    return render(request, 'home.html', {'blogs' : blogs})

    #  쿼리셋과 메소드 형식
    #  모델.쿼리셋(objects).메소드 

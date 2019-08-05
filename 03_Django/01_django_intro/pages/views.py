from django.shortcuts import render
from datetime import datetime
import random

#1. 기본 로직
def index(request):
    return render(request, 'index.html')

def introduce(request):
    return render(request, 'introduce.html')

#2. Template Variable(템플릿 변수)
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'dinner.html', context)

def image(request):
    return render(request, 'image.html')

#3. Variable Routing(동적 라우팅)
def hello(request, name):
    # names = ['justin', 'john', 'jason', 'juan', 'zzulu']
    # name = random.choice(names)
    context = {'name': name}
    return render(request, 'hello.html', context)

#4. 실습
#4-1. 동적 라우팅을 활용해서 (name과 age를 인자로 받아) 자기소개 페이지
def introduce2(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'introduce2.html', context)

#4-2. 두 개의 숫자를 인자로 받아(num1, num2) 곱셈 결과를 출력
def times(request, num1, num2):
    num3 = num1 * num2
    context = {
        'num3': num3,
        'num2': num2,
        'num1': num1,
    }
    return render(request, 'times.html', context)

#4-3. 반지름(r)을 인자로 받아 원의 넓이(area)를 구하시오.
def area(request, r):
    area = 3.14 * (r**2)
    context = {
        'area': area, 
        'r': r,
    }

    return render(request, 'area.html', context)

#5. DTL(Django Template Language)
def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)

#13_workshop
def info(request):
    return render(request, 'info.html')

#13_homework
def student(request, name):
    d = {'박길동': 28, '김길동': 27, '홍길동': 26}
    age = d[name]

    context = {
        'name': name,
        'age' : age
    }
    return render(request, 'student.html', context)
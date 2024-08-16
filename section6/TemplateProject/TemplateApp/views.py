from django.shortcuts import render

# Create your views here.
def index(request):
    val = 'matsumoto'
    return render(request, 'index.html', context={'value': val })

def home(request, first_name):
    my_name = f'{first_name}'
    favolit_fruts = ['apple', 'grape', 'lemon']
    my_info = {'name': 'matsumoto',
               'age': 28,
               }
    return render(request, 'home.html', context={
        'my_name': my_name,
        'favolit_fruits': favolit_fruts,
        'my_info': my_info 
    })

def sample1(request):
    return render(request, 'sample1.html')

def sample2(request):
    return render(request, 'sample2.html')

def sample(request):
    name = 'matsumoto'
    height = 175.5
    weight = 72
    bmi = weight / (height/100)**2
    page_url = 'ホームページ : https://www.google.com'
    favorite_fruits = [
        'Apple', 'Grape', 'Lemon'
    ]
    msg = """
    hello 
    my name is 
    ichiro
    """
    msg2 = 123456789
    return render(request, 'sample.html', context={
        'name': name,
        'bmi': bmi,
        'page_url': page_url,
        'fruits': favorite_fruits,
        'msg1': msg,
        'msg2': msg2
    })
    
class Country:
    
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital
    
def sample3(request):
    country = Country('Japan', 100000000, 'Tokyo')
    return render(request, 'sample3.html', context={
        'country': country
    })
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html',{'name':'Alireza Konarizadeh','age':'23','gender':'Man',
                                        'languages':'English and Persian',
                                        'degree': 'Student',
                                        'email': 'awp.828.cr7@gmail.com',
                                        'city':'Bandar Abbas, Hormozgan, Iran',
                                        'freelance':'Available'})
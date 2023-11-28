from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

n = 7
c = 0
while(n):
    if(n>5):
        c = c+ n-1
        n = n-1
    else:
        break
print(n)
print(c)

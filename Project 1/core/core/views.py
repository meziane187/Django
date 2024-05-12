from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render 

def hello_world(request):
    return HttpResponse("""
<h1 style="background-color: aquamarine; color: brown;border:4px solid black;margin: 15px;text-align: center;width: 300px;">hello world from django</h1>""")

@csrf_exempt
def addxy(request):
    if request.method=='POST' :
        x=int(request.POST.get('firstvalue'))
        y=int(request.POST.get('secondvalue'))
        result=x+y
        return HttpResponse(""" result:  """+ str(result))
    else :
        return HttpResponse(""" 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="addxy" method="POST">
        <p>
            <label for="firstvalue">enter first number</label>
        <input type="text" name="firstvalue">
        
        </p>
        <p>
            <label for="secondvalue">enter second number</label>
            <input type="text" name="secondvalue">
        </p>
        <button type="submit"> envoyer</button>    
    </form>

</body>
</html>""")
    
from .forms import InputForm
def add(request):
    form=InputForm()
    if request.method=='POST' :
        form=InputForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            x=cd['x']
            y=cd['y']
            output=x+y  
    return render(request,'pages/addition.html',{'form':form ,'output':output})


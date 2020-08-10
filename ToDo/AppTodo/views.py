from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import TodoItems  #current file hence . used 
# Create your views here.
import base64
def frontView(request):
    return render(request,'rootPage.html') 


def todoView(request):
    res=TodoItems.objects.all()
    return render(request,'index.html',{'all_items':res} )  

def addTodo(request):
    #create a new todo
    #save 
    #redirect the browser
    c=request.POST['content']
    new_item=TodoItems(content=c)
    new_item.save()
    return HttpResponseRedirect('/AppTodo/')

def deleteTodo(request,todo_id):
        to_delete=TodoItems.objects.get(id=todo_id)
        to_delete.delete()
        return HttpResponseRedirect('/AppTodo/')
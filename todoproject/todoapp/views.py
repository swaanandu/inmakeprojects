from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView, DeleteView
from todoapp.form import todoform
from todoapp.models import Todo


# Create your views here.
def add(request):
    x=Todo.objects.all()
    if request.method == 'POST':
        x = request.POST.get('task','')
        y = request.POST.get('priority','')
        l = request.POST.get('date', '')
        z=Todo(task=x,priority=y,datefield=l)
        z.save();
        return redirect('/')
    return render(request,"home.html",{'result':x})
def delete(request,del_id):

    if request.method=='POST':
        y = Todo.objects.get(id=del_id)
        y.delete()
        return redirect('/')

    return render(request,"delete.html")
def update(request,up_id):
    a=Todo.objects.get(id=up_id)
    b=todoform(request.POST or None,instance=a)
    if b.is_valid():
        b.save();
        return redirect('/')
    return render(request,"update.html",{'obj1':a,'obj2':b})
class listview(ListView):
    model = Todo
    template_name='home.html'
    context_object_name = 'result'
class detailview(DetailView):
    model=Todo
    template_name='detail.html'
    context_object_name = 'task'
class updateview(UpdateView):
    model= Todo
    template_name = 'edit.html'
    context_object_name = 'y'
    fields = ('task','priority','datefield')
    def get_success_url(self):
        return reverse_lazy('todoapp:cbvdetail',kwargs={'pk':self.object.id})


class deleteview(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:listview')

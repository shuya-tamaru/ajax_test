from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import CommentCreateForm
from .models import Comment
import json
from django.shortcuts import resolve_url
from django.http import JsonResponse


def photo_add_view(request):
    form = CommentCreateForm(request.POST or None)
    data = {}
    if request.is_ajax():
        if form.is_valid():
            form.save()
            data['title']= form.cleaned_data.get('title')
            data['status']= 'ok'
            return JsonResponse(data)
    context = {
        'form': form,
    }
    return render(request, 'building/main.html', context)

def hello_world_view(request):
    print(1)
    return JsonResponse({'text':'hello'})

class IndexView(generic.ListView):
    model = Comment
    template_name = 'building/building_list.html'

class AddView(generic.CreateView):
    model = Comment
    template_name = 'building/building_form.html'
    form_class = CommentCreateForm
    success_url = reverse_lazy('building:index')

    # def form_valid(self, form):
    #     print(self.request.POST.get('モデルのフィールド名'))
    #     return super().form_valid(form)

    # def form_valid(self,form):
    #     data = self.object
    #     context = {
    #         'id': data.id,
    #         'title': data.title,
    #         'text': data.text,
    #         # 'year': self.object.date.year,
    #         # 'month': self.object.date.month,
    #         # 'date': self.object.date.,
    #         'cordinate': data.cordinate,
    #     } 
    #     return self.render_to_responce(context)


    # def get_success_url(self):
    #     context = {
    #         'id': self.object.pk,
    #         'title': self.object.title,
    #         'text': self.object.text,
    #         # 'year': self.object.date.year,
    #         # 'month': self.object.date.month,
    #         # 'date': self.object.date.,
    #         'cordinate': self.object.cordinate,
    #     }
        
        # json_data = json.dumps(context)
        # print(json_data)
        # return self.render_to_responce(json_data)
        # return resolve_url('building:index')

# def add(request):
#     form = CommentCreateForm(request.POST or None)

#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         data = {
#             'flg': "true"
#         }
#         context = {

#         return render(request, 'building/building_form.html',context, {'data_json': json.dumps(data)})
#         # return redirect('building:add')

#     context = {
#         'form':CommentCreateForm()
#     }
#     return render(request, 'building/building_form.html', context)

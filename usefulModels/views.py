from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.generic.base import View
from .forms import PostForm


# Create your views here.
class AddPost(View):
    def get(self, request):
        i = PostForm
        return render(
            request, 
            'readPageSite.html',{
            'i': i}
            )
    def post(self, request):
        i = PostForm(request.POST)
        i.save()
        return HttpResponse ('ok')
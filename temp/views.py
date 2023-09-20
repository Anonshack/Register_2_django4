from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  TemplateView,
                                  CreateView,
                                  DeleteView,
                                  DetailView
                                  )
from .models import Person
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render


# Create your views here.
class HomePageView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    def get(self, request):
        context = {}
        clay = Person.objects.all()
        context['temp'] = clay
        return render(request, 'home.html', {'temp': clay})

    def test_func(self):
        return self.request.user.is_authenticated
        # def test_func(self):
    #     return self.request.user.is_staff


# class InfoPageView(TemplateView):
#     def get(self, request):
#         themes = request.GET.get('person')
#         if themes is None:
#             themes = 1
#         context = {}
#         context['data'] = Person.objects.filter(id=themes)
#         return render(request, 'info.html', context)


class NewsPostView(CreateView):
    template_name = 'new_post.html'
    model = Person
    fields = ['name', 'last_name', 'age', 'birthday'];


class BlogDetailView(DetailView):
    model = Person
    template_name = 'post_detail.html'


class BlogDeleteView(DeleteView):
    model = Person
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


    # def delete_post(self, post_id=None):
    #     post_to_delete = Person.objects.get(id=post_id)
    #     post_to_delete.delete()
    #     return HttpResponseRedirect('home')


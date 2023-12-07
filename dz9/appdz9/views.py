from django.shortcuts import render

from appdz9.models import User


def index_view(request):
    context = {'user_list': User.objects.all()}
    return render(request, 'index.html', context)


def user_detail_view(request, id):
    user = User.objects.get(pk=id)
    context = {'name': user,
               'surname': user,
               'age': user,
               'gender': user,
               }
    return render(request, 'user_detail.html', context=context)
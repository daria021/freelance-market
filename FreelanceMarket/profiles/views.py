from django.shortcuts import render
from .models import Executor, Client


def executor_profile(request, executor_id: int):
    executor: Executor = Executor.objects.get(id=executor_id)
    context = {'executor': executor}
    return render(request, 'executor_profile.html', context=context)


def client_profile(request, client_id: int):
    client: Client = Client.objects.get(id=client_id)
    context = {'client': client}
    return render(request, 'client_profile.html', context=context)

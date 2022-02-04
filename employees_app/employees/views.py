from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse(f'{request.method}: This is home')


def department_details(request, id):
    return HttpResponse(f'This is department {id}')


def list_departments(request):
    return HttpResponse('This is a list of departments')

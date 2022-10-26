from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogAuthor
from django.db.models import Min

def get_employee(requeat):
    queryset = BlogAuthor.objects.filter(first_name__in=['Qosim', 'Umar'], last_name='shamsiyev')
    print("\n", queryset.query)
    str_data = ""

    for i in queryset:
        str_data += f"<li>{i}</li>"
    return HttpResponse(f"<ul>{str_data}</ul>")
    
 
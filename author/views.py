# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from author.forms import AuthorForm

@csrf_protect
def add(request):
    author_form = AuthorForm()
    return render_to_response(
        'author/add.html', 
        {'author_form': author_form.as_table()}, 
        context_instance=RequestContext(request)
    )


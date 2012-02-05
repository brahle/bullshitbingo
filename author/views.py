# Create your views here.

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from author.forms import AuthorForm
from author.models import Author

@csrf_protect
def add(request):
    message = ''
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author = Author(name=author_form.cleaned_data['name'],
                            nickname=author_form.cleaned_data['nickname'],
                            gender=author_form.cleaned_data['gender'])
            author.save()
            return HttpResponseRedirect('/view/author/{}/'.format(author.id))
    else:
        author_form = AuthorForm()
    return render_to_response(
        'author/add.html', 
        {'form': author_form, 'message': message}, 
        context_instance=RequestContext(request)
    )

def listAll(request):
    authors = Author.objects.all()
    return render_to_response(
        'author/list.html',
        {'authors': authors},
        context_instance=RequestContext(request)
    )
    
def view(request, ID):
    try:
        author = Author.objects.get(id=ID)
    except ObjectDoesNotExist:
        return render_to_response(
            'author/dne.html',
            {'author_id': ID},
            context_instance=RequestContext(request)
        )
    return render_to_response(
        'author/view.html',
        {'author': author},
        context_instance=RequestContext(request)
    )
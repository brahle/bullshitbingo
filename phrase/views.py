# Create your views here.

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from phrase.forms import PhraseForm
from phrase.models import Phrase

@csrf_protect
def add(request):
    message = ''
    if request.method == 'POST':
        phrase_form = PhraseForm(request.POST)
        if phrase_form.is_valid():
            phrase = phrase_form.save()
            return HttpResponseRedirect('/view/phrase/{}/'.format(phrase.id))
    else:
        phrase_form = PhraseForm()
    return render_to_response(
        'phrase/add.html', 
        {'form': phrase_form, 'message': message}, 
        context_instance=RequestContext(request)
    )

def listAll(request):
    phrases = Phrase.objects.all()
    return render_to_response(
        'phrase/list.html',
        {'phrases': phrases},
        context_instance=RequestContext(request)
    )
    
def view(request, ID):
    try:
        phrase = Phrase.objects.get(id=ID)
    except ObjectDoesNotExist:
        return render_to_response(
            'phrase/dne.html',
            {'phrase_id': ID},
            context_instance=RequestContext(request)
        )
    return render_to_response(
        'phrase/view.html',
        {'phrase': phrase},
        context_instance=RequestContext(request)
    )
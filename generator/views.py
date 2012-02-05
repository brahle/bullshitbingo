# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from phrase.models import Phrase

def generate(request, x=3, y=3):
    x = int(x)
    y = int(y)
    quotesQS = Phrase.objects.all()
    if quotesQS.count() < x * y:
        return render_to_response(
            'simple_view.html',
            {'failed': True, 'count': x*y - quotesQS.count()},
            context_instance=RequestContext(request)
        )
    else:
        def split(A, m):
            ret = []
            for i in range(0, len(A), m):
                ret.append(A[i:i+m])
            return ret
        quotes = split(quotesQS.order_by('?')[:x*y], y)
    return render_to_response(
        'simple_view.html', 
        {'quotes': quotes}, 
        context_instance=RequestContext(request)
    )
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context_processors import csrf
from django.conf import settings
from .models import UrlDetail
import random, string, json


def home(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('home.html', c)


def short_link(request):
    url = request.POST.get("url", '')
    if not (url == ''):
        if not url.startswith('http'):
            url = "http://" + url
        short_url_id = get_short_code()
        data = UrlDetail(http_main_url=url, short_url_id=short_url_id)
        data.save()
 
        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" + short_url_id
        return HttpResponse(json.dumps(response_data),  content_type="application/json")
    return HttpResponse(json.dumps({"error": "An error occured while performing"}),
                                     content_type="application/json")


def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase

    while True:
        short_url_id = ''.join(random.choice(char) for x in range(length))
        try:
            temp = UrlDetail.objects.get(pk=short_url_id)
        except:
            return short_url_id


def original_link_redirect(request, short_url_id):
    url = get_object_or_404(UrlDetail, pk=short_url_id)
    url.count += 1
    url.save()
    return HttpResponseRedirect(url.http_main_url)


def all_link(request):
    res = UrlDetail.objects.all()
    base_url = settings.SITE_URL
    context = {
        'res': res,
        'base_url': base_url
    }
    return render(request, 'all_link.html', context)


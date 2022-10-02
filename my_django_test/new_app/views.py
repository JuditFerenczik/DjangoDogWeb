from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


articles = {
    'sports': 'Sport page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
    }

my_var = {
    'first_name': "Judit",
    'last_name': "FereNCzik",
    'test_list': [1, 2, 6],
    'test_dir': {'inside_key': 'inside_value'}
}


def index(request):
    return HttpResponse("Hello this is a view inside a view")


def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        result = "No page was found!"
        #return HttpResponseNotFound(result)
        raise Http404("404 generic error")


def num_page_view(request, num_page):
    try:
        topic_list = list(articles.keys())
        topic = topic_list[num_page]
        webpage = reverse('topic_page', args=[topic])
        return HttpResponseRedirect(webpage)
    except:
        raise Http404("405 generic error")


def sample_view(request):
    return render(request, 'new_app/templates/example.html', context=my_var)


def variable_view(request):
    return render(request, 'new_app/templates/variable.html')

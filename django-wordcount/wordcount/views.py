from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

def result(req):
    text = req.GET['fulltext']
    words = text.split()
    wdict = {}
    for word in words:
        wdict[word] = wdict[word] + 1 if word in wdict else 1
    return render(req, 'result.html', { 'full': text, 'total': len(words), 'wdict': wdict.items() })
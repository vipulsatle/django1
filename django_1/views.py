from django.http import HttpResponse

#def hello(request):
#	text = """<h1>welcome to my app !</h1>"""
#	return HttpResponse(text)


def index(request):
	return HttpResponse("<title> Menu </title><head>Menu</head><br><a href='https://google.com'>1. Google</a><br><a href='/'>2.Back</a><br>")
def main(request):
	return HttpResponse("<p> Welcome to Django Website<p><br><a href=/menu>Menu</a>")
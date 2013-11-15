from django.http import HttpResponse
from django.template import RequestContext
from django.template import loader

def index(request):
	context = RequestContext(request)
	t = loader.get_template('/home/alpha/test3/theme/templates/index.html')
	return HttpResponse(t.render(context))

def service(request):
	context = RequestContext(request)
	t = loader.get_template('/home/alpha/test3/theme/templates/service.html')
	return HttpResponse(t.render(context))

def aboutus(request):
	context = RequestContext(request)
	t = loader.get_template('/home/alpha/test3/theme/templates/aboutus.html')
	return HttpResponse(t.render(context))

def blog(request):
	context = RequestContext(request)
	t = loader.get_template('/home/alpha/test3/theme/templates/blog.html')
	return HttpResponse(t.render(context))

def blogsingle(request):
	context = RequestContext(request)
	t = loader.get_template('/home/alpha/test3/theme/templates/blog-single.html')
	return HttpResponse(t.render(context))

def careers(request):
	context = RequestContext(request)
	t = loader.get_template('/home/alpha/test3/theme/templates/careers.html')
	return HttpResponse(t.render(context))

def comingsoon(request):
	context = RequestContext(request)
	t = loader.get_template('/home/alpha/test3/theme/templates/comingsoon.html')
	return HttpResponse(t.render(context))

def contact(request):
	context = RequestContext(request)
	t = loader.get_template('/home/alpha/test3/theme/templates/contact.html')
	return HttpResponse(t.render(context))

def error(request):
	context = RequestContext(request)
	t = loader.get_template('/home/alpha/test3/theme/templates/error.html')
	return HttpResponse(t.render(context))

def faq(request):
	context = RequestContext(request)
	t = loader.get_template('/home/alpha/test3/theme/templates/faq.html')
	return HttpResponse(t.render(context))

def features(request):
	context = RequestContext(request)
	t = loader.get_template('/home/alpha/test3/theme/templates/features.html')
	return HttpResponse(t.render(context))

def gallery(request):
	context = RequestContext(request)
	t = loader.get_template('/home/alpha/test3/theme/templates/gallery.html')
	return HttpResponse(t.render(context))

def login(request):
	context = RequestContext(request)
	t = loader.get_template('/home/alpha/test3/theme/templates/login.html')
	return HttpResponse(t.render(context))

def portfolio(request):
	context = RequestContext(request)
	t = loader.get_template('/home/alpha/test3/theme/templates/portfolio.html')
	return HttpResponse(t.render(context))

def pricing(request):
	context = RequestContext(request)
	t = loader.get_template('/home/alpha/test3/theme/templates/pricing.html')
	return HttpResponse(t.render(context))

def products(request):
	context = RequestContext(request)
	t = loader.get_template('/home/alpha/test3/theme/templates/products.html')
	return HttpResponse(t.render(context))

def support(request):
	context = RequestContext(request)
	t = loader.get_template('/home/alpha/test3/theme/templates/support.html')
	return HttpResponse(t.render(context))

def testimonials(request):
	context = RequestContext(request)
	t = loader.get_template('/home/alpha/test3/theme/templates/testimonials.html')
	return HttpResponse(t.render(context))


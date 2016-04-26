from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from acorta.models import Urls_List
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def new_url(request) :

	resp = ""

	if request.method == "GET" :
		resp += "<form method='post'>"
		resp += 	"<input name='url' type='text'>"
		resp +=		"<br>"
		resp += 	"<input type='submit' value='Send'>"
		resp +="</form"

	if request.method == "POST" :

		url = request.POST["url"]
		if url.find("http") != 0 :
			url = "http://" + url 

		aux = 0
		try :
			aux = Urls_List.objects.get(url=url).id
		except :
			Urls_List(url=url).save()
			aux = Urls_List.objects.get(url=url).id

		resp += "<p> Yout url <b>" + url + "</b> has been shortened as : "
		resp += 	"<a href='/" + str(aux) + "'>" 
		resp += 		str(aux) 
		resp += 	"</a>"
		resp += "</p>"

	resp += cat_shortened_urls()
	return HttpResponse(resp)

def url(request, shortened):

	try :
		resp = Urls_List.objects.get(id=shortened).url
		return HttpResponseRedirect(resp)
	except :
		resp = "Url Not Found"
		return HttpResponse(resp)


def cat_shortened_urls():

	ret = "<br>"
	all_entries = Urls_List.objects.all()
	for entry in all_entries :
		ret += "<p> " + entry.url + "</b> : "
		ret +=		"<a href='/" + str(entry.id) + "'>" 
		ret += 			str(entry.id) 
		ret += 		"</a>"
		ret += "</p>"

	return ret

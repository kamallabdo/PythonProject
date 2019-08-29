from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from blog.forms import UserRegisterForm
# Create your views here.
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from django.views.generic import View

from Rapide.utils import render_to_pdf #created in step 4


from blog.models import Fichier 

def home(request):

	return render(request,'blog/home.html')


def profile(request):
	
	fichier =Fichier.objects.all()
	context = {

	'fichier' : fichier,
	}  

	return render(request, 'blog/profile.html',context)


def search(request):
	query=request.GET.get("query")
	if not query:
		fich = Fichier.objects.all()
	else:
		fich = Fichier.objects.filter(title__icontains=query)
	
	
	context = {
	"fich":fich,
	}
	return render(request,"blog/search.html",context)
	
	
	pass












class Pdf(View):
	
	def get(self, request,fich_id,*args, **kwargs):
		
		fich = 	get_object_or_404(Fichier,pk=fich_id)
		
		if fich.id== 1:
	
			pdf = render_to_pdf('blog/invoice.html')
	
		elif fich.id==3:
	
			pdf = render_to_pdf("blog/logout.html")

		return HttpResponse(pdf,content_type='application/pdf')
	



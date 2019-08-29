from django.urls import path,include

from blog import views

from blog.views import Pdf

from django.conf.urls import url

urlpatterns = [
	path(" ",views.profile,name="blog-profile"),
   
    url(r'^print/(?P<fich_id>[0-9]+)/$',Pdf.as_view(),name="pdf"),

    path('search/',views.search,name="search"),
]


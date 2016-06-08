#from django.http import HttpResponse
from django.http import Http404
#from django.template import loader
#shortcut of above 
from django.shortcuts import render, get_object_or_404
from models import Album, Songs

def index(request):
	all_albums= Album.objects.all()	
	context= {'all_albums': all_albums }
	return render(request, "music/index.html", context)
	#it covers Httprespose too.
	


def details(request, album_id):
	album= Album.objects.get(pk=album_id)
	'''try:
		album= Album.objects.get(pk=album_id)
	except Album.DoesNotExist:
		raise Http404("Album Does Not Exist")'''
	# We can directly do
	album= get_object_or_404(Album, pk=album_id)

	return render(request, "music/detail.html", {'album':album})


def favorite(request, album_id ):
	album= Album.objects.get(pk=album_id)
	try:
		selected_song= album.songs_set.get(pk=request.POST['song'])
	except(KeyError , Songs,DoesNotExist):
		return 	render(request, "music/detail.html", {'album':album, 'error_message':"You Did Not Selected A Valid Song"})
	else:
		selected_song.is_favorite = True
		selected_song.save()
		return 	render(request, "music/detail.html", {'album':album})



# from django.http import Http404
# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

# Create your views here.
def index(request):
    # Conect to the database to recover all albums
    all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')
    # context = {'all_albums': all_albums,}
    # html = ''
    # for album in all_albums:
    #     url = '/music/' + str(album.id) + '/'
    #     html += '<H2><a href="' + url + '">' + album.album_title + '</a></h2><br>'
    #
    #
    # # Detail a title on the music website page
    # # return HttpResponse("<h1>This will be a list of all Albums in DataBase</h1>")
    # return HttpResponse(html)
    # return HttpResponse(template.render(context, request))
    # return render(request, 'music/index.html', context)
    return render(request, 'music/index.html', {'all_albums': all_albums,})

def detail(request, album_id):
    # return HttpResponse("<h2>Details for Album Id : " + str(album_id) + "</h2>")
    # try:
    #     album = Album.objects.get(id=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album does not Exist...")
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'music/detail.html',  {'album': album, })

def favorite(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    try:
        # Here we query the database for that song that was selected
        # Tries to get the Id of the selected song, if not then the except pop in
        sel_song = album.song_set.get(id=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        # Here in this error situation, re-direct user to the detail template, with an error msg
        # Note: error msg is in a dictionary
        return render(request, 'music/detail.html',  {
            'album': album,
            'error_msg': "You did Not select a valid song!!"
        })
    else:
        # Update the database, field : is_favorite and save!!
        sel_song.is_favorite = True
        sel_song.save()
        # Go back to the detail template
        return render(request, 'music/detail.html',  {'album': album})
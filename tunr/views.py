from django.shortcuts import render, redirect

from .models import Artist, Song

from .forms import ArtistForm, SongForm

from django.contrib.auth.decorators import login_required

from django.shortcuts import render


@login_required
def home(request):
    return render(request, 'core/home.html')

# Create your views here.
def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'tunr/artist_list.html', {'artists': artists})


def artist_detail(request):
    artist = Artist.objects.get(id=pk)
    return render(request, 'tunr/artist_detail.html', {'artist': artist})


def artist_detail(request, pk):
    artist = Artist.objects.get(id=pk)
    return render(request, 'tunr/artist_detail.html', {'artist': artist})


@login_required
def artist_create(request):
    #check if request is a post request
    if request.method == 'POST':
    # if it instantiate a form with the Artistform model
        form = ArtistForm(request.POST)
    #check that form data is valid
        if form.is_valid():
    #if the form data is valid and save the form
            artist = form.save()
    #and redirect the user to the artist_detail
            return redirect('artist_detail', pk=artist.pk)
    else:
    # if it's not a post form request
    #render an empty artist form for the user to fill out
        form = ArtistForm()
    return render(request, 'tunr/artist_form.html', {'form': form})


@login_required
def artist_edit(request, pk):
    artist = Artist.objects.get(pk=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'tunr/artist_form.html', {'form': form})


@login_required
def artist_delete(request, pk):
    Artist.objects.get(id=pk).delete()
    return redirect('artist_list')


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'tunr/song_list.html', {'songs': songs})


def song_detail(request, pk):
    song = Song.objects.get(id=pk)
    return render(request, 'tunr/song_detail.html', {'song': song})


@login_required
def song_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save()
            return redirect('song_detail', pk=song.pk)
    else:
        form = SongForm()
    return render(request, 'tunr/song_form.html', {'form': form})


@login_required
def song_edit(request, pk):
    song = Song.objects.get(pk=pk)
    if request.method == "POST":
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            song = form.save()
            return redirect('song_detail', pk=song.pk)
    else:
        form = SongForm(instance=song)
    return render(request, 'tunr/song_form.html', {'form': form})


@login_required
def song_delete(request, pk):
    Song.objects.get(id=pk).delete()
    return redirect('song_list')

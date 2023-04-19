from logging import getLogger
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.http import HttpResponseRedirect

from app_player.models import Song, Part
from app_player.forms import SongForm, PartForm
from app_player.additon import get_length

LOGGER = getLogger()


def index(request):
    return render(request, template_name='index.html')


class PlayerView(ListView):
    template_name = 'songs.html'
    model = Song

    def get_queryset(self):
        return Song.objects.filter(user=self.request.user)


class SongCreateView(CreateView):
    model = Song
    template_name = 'form_add.html'
    form_class = SongForm
    success_url = reverse_lazy('songs_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class SongUpdateView(UpdateView):
    template_name = 'form.html'
    model = Song
    form_class = SongForm
    success_url = reverse_lazy('songs_list')


class SongDeleteView(DeleteView):
    template_name = 'delete_song_confirmation.html'
    model = Song
    success_url = reverse_lazy('songs_list')


class LooperUpdateView(UpdateView):
    template_name = 'looper_update.html'
    model = Part
    form_class = PartForm


def looper(request, pk):
    urlval = Song.objects.get(id=pk).song_url
    parts = Part.objects.filter(song_id=pk).values('start_p', 'stop_p', 'id')
    length = get_length(urlval)

    part_id = request.POST.get('id_value')

    if request.POST.get('id_value'):
        start_video = request.POST.get('start_value')
        stop_video = request.POST.get('stop_value')
        part_to_save = Part.objects.get(id=part_id)
        part_to_save.start_p = start_video
        part_to_save.stop_p = stop_video
        part_to_save.save()

    else:
        start_video = 0
        stop_video = length

    context = {'song_url': urlval, 'start_video': start_video, 'stop_video': stop_video, 'parts': parts,
               'lenght': length}
    return render(request, template_name='looper.html', context=context)

def save_video(request, video_url):

    band = 'BAND'
    song_title = 'TITLE'


    new_song = Song(user=request.user , band=band, song_title=song_title, song_url=video_url, description='')
    new_song.save()


    length = get_length(video_url)

    context = {'song_url': video_url, 'start_video': 0, 'stop_video': length,
               'lenght': length}
    return  render(request, template_name='looper.html', context=context)


def looper_basic(request, video_url):
    length_sec = get_length(video_url)

    if request.POST.get('start_value'):
        start_video = request.POST.get('start_value')
        stop_video = request.POST.get('stop_value')
        if start_video >= stop_video:
            stop_video = length_sec
    else:
        start_video = 0
        stop_video = length_sec

    context = {'video_url': video_url, 'length': length_sec, 'start_video': start_video, 'stop_video': stop_video}
    return render(request, template_name='looper_basic.html', context=context)


def add_part(request, song_url):
    song_id = Song.objects.get(song_url=song_url).id

    stop = get_length(song_url)
    new_loop = Part(start_p=0, stop_p=stop, song_id=song_id)
    new_loop.save()

    # return render(request, template_name='looper.html', context={id:id})
    return HttpResponseRedirect(reverse('looper', args=(song_id,)))


def delete_part(request, id):
    song_id = Part.objects.get(id=id).song_id
    Part.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('looper', args=(song_id,)))

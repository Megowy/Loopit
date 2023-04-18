from django.forms import CharField, IntegerField, ModelForm, Form
from app_player.models import Song, Part

from django import forms


class SongForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for visible in self.visible_fields():
        #     visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Song
        fields = ['band', 'song_title', 'song_url', 'description']

        # exclude = ('song_url',)



class PartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = Part
        fields = '__all__'



class LooperBasic(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    video_url = CharField(max_length=11)
    title = CharField(max_length=100)
    description = CharField(max_length=200)


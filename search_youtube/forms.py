from django.forms import Form, CharField


class SearchResult(Form):
    video_thumbnail = CharField(max_length=100)
    title = CharField(max_length=100)
    description = CharField(max_length=200)


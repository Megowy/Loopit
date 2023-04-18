import requests
import re




def get_length(urlval):
    API_KEY = 'AIzaSyByG2wn7WwPrea9_RMYeRejfVKi8yBf5xs'
    url_dit = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id={urlval}&key={API_KEY}"
    response = requests.get(url_dit)
    data = response.json()
    length = data['items'][0]['contentDetails']['duration']

    return yt_time(length)

def yt_time(duration):
    """
    Converts YouTube duration (ISO 8061)
    into Seconds

    see http://en.wikipedia.org/wiki/ISO_8601#Durations
    """
    ISO_8601 = re.compile(
        'P'   # designates a period
        '(?:(?P<years>\d+)Y)?'   # years
        '(?:(?P<months>\d+)M)?'  # months
        '(?:(?P<weeks>\d+)W)?'   # weeks
        '(?:(?P<days>\d+)D)?'    # days
        '(?:T' # time part must begin with a T
        '(?:(?P<hours>\d+)H)?'   # hours
        '(?:(?P<minutes>\d+)M)?' # minutes
        '(?:(?P<seconds>\d+)S)?' # seconds
        ')?')   # end of time part
    # Convert regex matches into a short list of time units
    units = list(ISO_8601.match(duration).groups()[-3:])
    # Put list in ascending order & remove 'None' types
    units = list(reversed([int(x) if x != None else 0 for x in units]))
    # Do the maths
    return sum([x*60**units.index(x) for x in units])



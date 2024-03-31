from django.shortcuts import render
from pytube import *
from django.contrib import messages

def youtube(request):
    if request.method == 'POST':
        link = request.POST['link']
        if link:
            try:
                video = YouTube(link)
                stream = video.streams.get_lowest_resolution()
                stream.download()
                messages.success(request, "Video successfully downloaded")
                return render(request, 'youtube.html', {})
            except Exception as e:
                messages.error(request, f"An error ooccured: {str(e)}")
                return render(request, 'youtube.html', {})
    return render(request, 'youtube.html', {})
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os


def uploadpc(request):
    return render(request, 'uploadpc.html')

@csrf_exempt
def upload_server(request):
    if request.method == 'POST' and request.FILES.get('video'):
        video_file = request.FILES['video']
        file_path = os.path.join(settings.MEDIA_ROOT, video_file.name)

        with open(file_path, 'wb+') as destination:
            for chunk in video_file.chunks():
                destination.write(chunk)

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'failed', 'error': 'No video file uploaded'})

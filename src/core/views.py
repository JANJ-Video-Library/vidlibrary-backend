from django.http import JsonResponse
from django.shortcuts import render

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class VideoView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'link': 'https://janj.webex.com/janj/lsr.php?RCID=3e449732b66c4854abd390828d145f43',
            'title' : 'JA  Merck Speaker Series Spotlighting Career Lessons from Merck Finance Leaders',
            'category' : 'Executive Speaker Series'
        }
        return Response(data)


'''
# no longer needed because using rest_framework
def video(request):
    data = {
        'link': 'https://janj.webex.com/janj/lsr.php?RCID=3e449732b66c4854abd390828d145f43',
        'title' : 'JA  Merck Speaker Series Spotlighting Career Lessons from Merck Finance Leaders',
        'category' : 'Executive Speaker Series'
    }
    return JsonResponse(data)
'''


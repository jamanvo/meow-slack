from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import json


# Create your views here.
class catbot(APIView):
  def post(self, request):
    # slack message 형태
    response = {
      'response_type': 'in_channel',
      'text': 'Meow Bot!',
      'attachments': [
        {
          'text': 'meow',
          "image_url": "http://my-website.com/path/to/image.jpg"
        }
      ]
    }

    return Response(response, status=status.HTTP_200_OK)


# 앱 설치시 Oauth 인증 API
class auth(APIView):
  def get(self, request):
    code = request.query_params['code']

    # TODO: 슬랙 앱 생성시 수정
    data = {
      'client_id': '',
      'client_secret': 'a',
      'code': code
    }

    # TODO: 예외 처리
    r = requests.post('https://slack.com/api/oauth.access', data)
    response = json.loads(r.text)

    # 이건 어따쓰는거지?
    # access_token = response['access_token']

    # TODO: template 필요, 일단 임의로 파일명 넣어둠
    if response['ok']:
      return render(request, 'auth_success.html')
    else:
      return render(request, 'auth_fail.html')
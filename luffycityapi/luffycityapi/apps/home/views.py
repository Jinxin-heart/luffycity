from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_redis import get_redis_connection
import logging
logger = logging.getLogger('django')

class HomeAPIView(APIView):
    def get(self, request):
        logger.error('error message')
        logger.info('info message')

        # print("hello")
        # brother = ['jinx', 'jin', 'jinxin']
        redis = get_redis_connection('sms_code')
        brother = redis.lrange('jinx', 0, -1)
        return Response(brother, status.HTTP_200_OK)
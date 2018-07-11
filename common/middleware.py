# --coding:utf-8

import time

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render

from common import rds
from common.keys import BLOCK_KEY



class BlockMiddleware(MiddlewareMixin):

    def process_request(self, request):

        if request.path.startswith(settings.STATIC_URL) or request.path == '/post/top10/':
            return
        if rds.get(BLOCK_KEY % request.session.session_key):
            print('你已被加入黑名单')
            return render(request, 'blockers.html')


        now = time.time()
        time0, time1 = request.session.get('request_time',[0, 0])

        request.session['request_time'] = [time1, now]
        request.session.save()

        if now - time0 < 1:
            print('你访问太频繁了')
            key = BLOCK_KEY % request.session.session_key
            rds.setex(key, 1, 60)
        print ('一切正常')
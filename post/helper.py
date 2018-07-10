# --coding:utf-8

from django.core.cache import cache

from post.models import Post


from common import keys
from common import rds



def page_cache(timeout):
    def wrapper1(view_func):
        def wrapper2(request):
            if request.method == 'GET':
                key = keys.PAGE_CACHE_KEY % (request.session.session_key, request.get_full_path())
                response = cache.get(key)
                if response is None:
                    response = view_func(request)
                    cache.set(key,response,timeout)
            else:
                response = view_func(request)
            return response
        return wrapper2
    return wrapper1


def read_count(view_read_func):
    def wrapper(request):
        response = view_read_func(request)
        if response.status_code == 200:
            post_id  = int(request.GET.get('post_id'))
            rds.zincrby(keys.READ_COUNTER, post_id)
        return response

    return wrapper


def get_top_n(num):
    ori_data = rds.zrevrange(keys.READ_COUNTER,0,num-1,withscores=True)

    rank_data = [[int(post_id),int(count)] for post_id,count in ori_data]

    post_id_list = [post_id for post_id, _ in rank_data]
    posts = Post.objects.in_bulk(post_id_list)
    for item in rank_data:
        post_id = item[0]
        item[0] = posts[post_id]

    return rank_data
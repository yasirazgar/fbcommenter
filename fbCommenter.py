# Comment on posts
import requests
import json

TOKEN = 'EAACEdEose0cBAFAUYH4Qog6qAucCTuQMkZCFXGzcFiQMkQ570dG1ZAZCosWtNKIjImnHtrc1udwuona92bU0jyGdIJL1wI2NydQ2D8iqfRKID2A307srTA9oURokIDB7ZAlQLDkAEdKNZCsxsY1V3oJvGs0DmooJYZAj6lb9IrvtBzd9Tuv5QO'

def get_post_ids():
    query = ''

    get_posts_params = {'access_token': TOKEN, 'fields': 'feed.order(reverse_chronological).limit(20)'}
    get_posts_url = 'https://graph.facebook.com/v2.8/me'
    get_posts_response = requests.get(get_posts_url, params = get_posts_params)

    posts = json.loads(get_posts_response.text)["feed"]["data"]
    post_ids = []

    for post in posts:
        post_ids.append(post["id"])

    return post_ids

def comment_on_posts(post_ids):
    for post_id in post_ids:
        get_poster_url = 'https://graph.facebook.com/v2.8/{}'.format(post_id)
        get_poster_params = {'access_token': TOKEN, 'fields': 'from'}
        get_poster_response = requests.get(get_poster_url, params = get_poster_params)

        poster_name = json.loads(get_poster_response.text)["from"]["name"]
        message = 'Thanks {} :)'.format(poster_name)

        comment_url = 'https://graph.facebook.com/{}/comments'.format(post_id)
        comment_params = {'access_token': TOKEN, 'message': message}
        comment_response = requests.post(comment_url, params = comment_params)

        print " Comment for post_id {} is {}".format(post_id, comment_response.status_code)

if __name__ == '__main__':
    comment_on_posts(get_post_ids())

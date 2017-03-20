# Comment on posts
# gem install requests
require "requests/sugar"


TOKEN = ''

def get_post_ids
    query = ''

    get_posts_params = {:access_token => TOKEN, :fields => 'feed.order(reverse_chronological).limit(20)'}
    get_posts_url = 'https://graph.facebook.com/v2.8/me'
    get_posts_response = Requests.get(get_posts_url, :params => get_posts_params)

    posts = get_posts_response.json["feed"]["data"]
    post_ids = []

    posts.each do |post|
        post_ids << post["id"]
    end

    return post_ids
end

def comment_on_posts(post_ids)
    post_ids.each_with_index do |post_id, index|
        break if index == 50
        get_poster_url = "https://graph.facebook.com/v2.8/#{post_id}"
        get_poster_params = {:access_token => TOKEN, :fields => 'from'}
        get_poster_response = Requests.get(get_poster_url, :params => get_poster_params)

        poster_name = get_poster_response.body["from"]["name"]
        message = "Thanks #{poster_name} :)"

        comment_url = "https://graph.facebook.com/#{post_id}/comments"
        comment_params = {:access_token => TOKEN, :message => message}
        comment_response = Requests.post(comment_url, :params => comment_params)

        puts " Comment for post_id #{post_id} is {comment_response.status_code}"
    end
end


comment_on_posts(get_post_ids)

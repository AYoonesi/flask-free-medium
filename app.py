'''
    This bullshit frees medium articles for free!
'''

twitter_shit = {
    'api_key': 'Consumer Keys / API Key',
    'api_key_secret': 'Consumer Keys / API Secret',
    'acc_token': 'Authentication Tokens / Access Token',
    'acc_token_secret': 'Authentication Tokens / Access Secret',
}

from flask import *
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')

@app.route('/freer', methods=['GET'])
def free_this_article():
    try:
        wanted_url = request.args.to_dict()['wanted']
    except:
        return redirect('/', code=302)
    
    if (is_url(wanted_url) and is_medium(wanted_url)):
        res = freer_user.create_tweet(text=f'{hashlib.md5((str(random.randint(0, 9999)) + str(random.randint(9999, 99999999))).encode()).hexdigest()} \n {wanted_url}')
        return render_template('article.html', url=res.data['text'].rsplit(' ')[-1])
    else:
        return render_template('error.html')

@app.route('/direct_freer', methods=['GET'])
def free_this_article_direct():
    try:
        wanted_url = request.args.to_dict()['wanted']
    except:
        return redirect('/', code=302)
    
    if (is_url(wanted_url) and is_medium(wanted_url)):
        res = freer_user.create_tweet(text=f'{hashlib.md5((str(random.randint(0, 9999)) + str(random.randint(9999, 99999999))).encode()).hexdigest()} \n {wanted_url}')
        return redirect(res.data['text'].rsplit(' ')[-1], code=302)
    else:
        return 'What the fuck?'

@app.route('/wp_freer', methods=['GET'])
def free_this_article_wp():
    try:
        wanted_url = request.args.to_dict()['wanted']
    except:
        return 'what da fuck?'
    
    if (is_url(wanted_url) and is_medium(wanted_url)):
        res = freer_user.create_tweet(text=f'{hashlib.md5((str(random.randint(0, 9999)) + str(random.randint(9999, 99999999))).encode()).hexdigest()} \n {wanted_url}')
        return res.data['text'].rsplit(' ')[-1]
    else:
        return 'What the fuck?'



def is_medium(url):
    if (url[0:8] != 'https://' and url[0:7] != 'http://'):
        url = 'https://' + url
    try:
        url_html = requests.get(url).text
    except:
        return False
    target = 'M588.67 296.36c0 163.67-131.78 296.35-294.33 296.35S0 460 0 296.36 131.78 0 294.34 0s294.33 132.69 294.33 296.36M911.56 296.36c0 154.06-65.89 279-147.17 279s-147.17-124.94-147.17-279 65.88-279 147.16-279 147.17 124.9 147.17 279M1043.63 296.36c0 138-23.17 249.94-51.76 249.94s-51.75-111.91-51.75-249.94 23.17-249.94 51.75-249.94 51.76 111.9 51.76 249.94'
    if (url_html.find(target) >= 0 ):
        return True
    else:
        return False

def refine_url(url: str):
    print('before of refinery (inside function): ', url)
    url = urllib.parse.unquote(url)
    print('after refinery: ', url)
    return url

def is_url(url: str):
    if (validators.url(url)):
        return True
    elif (url[0:8] != 'https://' or url[0:7] != 'http://'):
        url = 'https://' + url
        return validators.url(url)

if __name__ == '__main__':
    import tweepy, random, hashlib, validators, urllib.parse, requests
    freer_user = tweepy.Client(consumer_key=twitter_shit['api_key'], consumer_secret=twitter_shit['api_key_secret'], access_token=twitter_shit['acc_token'], access_token_secret=twitter_shit['acc_token_secret'])
    # app.run(port=8000)
    app.run(port=5001, debug=True)
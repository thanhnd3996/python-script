from flask import render_template, request
from counting import counting
import time
import redis


@counting.route('/')
@counting.route('/index')
def count_user_agent():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    today = time.strftime("%d/%m/%Y")
    user_agent = request.headers['User-Agent']
    r.pfadd(today, user_agent)
    count = str(r.pfcount(today))
    return render_template("index.html",
                           count=count,
                           user_agent=str(user_agent))

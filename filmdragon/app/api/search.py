#coding:utf-8
from flask import jsonify, request, Response
from . import api
from app import db
from app.models import User, Story, Storyc
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy.sql import func
import json

@api.route('/search/', methods = ['POST'])
def search():
    if request.method == 'POST':
        keyword = request.get_json().get('keyword')
        storys = Story.query.all()
        findlist = []
        b = 0 #判断有无
        for s in storys:
            keywords = s.keywords.split(" ")
            for k in keywords:
                if keyword == k:
                    b = 1
                    title = s.title
                    username = User.query.filter_by(id=s.user_id).first().username
                    storyid = s.id
                    floors = s.floors
                    time = s.time
                    sc = Storyc.query.filter_by(storyckeyword=k).first()
                    storyc = sc.storyc
                    likenum = sc.likenum
                    findlist.append({'username':username,
                                    'title':title,
                                    'storyid':storyid,
                                    'storyc':storyc,
                                    'floors':floors,
                                    'likenum':likenum,
                                    'time':time
                                    })
        return jsonify ({"findlist":findlist}),200

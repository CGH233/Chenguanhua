#coding:utf-8
from flask import jsonify, request, Response
from . import api
from app import db
from app.models import User, Story, Storyc
from flask_login import login_user, logout_user, current_user, login_required
import json

@api.route('/user/<int:uid>/', methods = ['GET'])
def me(uid):
    if request.method == 'GET':
        token = request.headers['token']
        user = User.query.filter_by(id=uid).first()
        if user.confirm(token):
            usa = user.usa
            usb = user.usb
            userlikenum = user.userlikenum
            return jsonify({"usa":usa,
                            "usb":usb,
                            "userlikenum":userlikenum
                            }),200

@api.route('/user/<int:uid>/join/', methods = ['GET'])
def join(uid):
    if request.method == 'GET':
        token = request.headers['token']
        user = User.query.filter_by(id=uid).first()
        storyclist = []
        if user.confirm(token):
            s = Storyc.query.all()
            for a in s:
                if a.user_id == uid:
                    perstoryctext = a.storyc
                    perstoryckeyword = a.storyckeyword
                    likenum = a.likenum
                    storyclist.append({"storyc":perstoryctext,
                    "storyckeyword":perstoryckeyword,
                    "storyid":a.story_id,
                    "likenum":likenum
                    })
            return jsonify({"join":storyclist
                            }),200    

@api.route('/user/<int:uid>/write/', methods = ['GET'])
def begin(uid):
    if request.method == 'GET':
        token = request.headers['token']
        user = User.query.filter_by(id=uid).first()
        storylist = []
        if user.confirm(token):
            story = []
            s = Story.query.all()
            for a in s:
                if a.user_id == uid:
                    perstoryid = a.id
                    perstorytitle = a.title
                    storylist.append({"storyid":perstoryid,
                    "title":perstorytitle,
                    "likenum":a.likenum
                    })
            return jsonify({"start":storylist
                            }),200

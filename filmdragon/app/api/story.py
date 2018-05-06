#coding:utf-8
from flask import jsonify, request, Response
from . import api
from app import db
from app.models import User, Story, Storyc
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy.sql import func
import random
import json
import redis
import time

r = redis.Redis(host='localhost',port=6379,db=0)

@api.route('/story/<int:storyid>/', methods = ['GET'])
def readstory(storyid):
    if request.method == 'GET':
        storys = Story.query.all()
        storycs = Storyc.query.all()
        sid = []
        storyclist = []
        for x in storys:
            sid.append(x.id)
            if x.id == storyid:
                uid = x.user_id
                user = User.query.filter_by(id=uid).first()
                title = x.title
                floors = x.floors
                time = x.time
                storylikenum = x.likenum
                username = user.username
                scl = []          
                for sc in storycs:
                    if sc.story_id == storyid:
                        scl.append(sc.id)
                scl.sort()
                for z in scl:
                    storyc1 = Storyc.query.filter_by(id=z).first()
                    usernamec = User.query.filter_by(id=storyc1.user_id).first().username
                    storyctext = storyc1.storyc
                    storyctime = storyc1.time
                    storycid = storyc1.id
                    storyclikenum = storyc1.likenum
                    storyckeyword = storyc1.storyckeyword
                    storyclist.append({"storycid":storycid,
                                    "storyctext":storyctext,
                                    "usernamec":usernamec,
                                    "likenumc":storyc1.likenum,
                                    "time":storyctime,
                                    "storyckeyword":storyckeyword})
                return jsonify({"title":title,
                                "likenum":storylikenum,
                                "floors":floors,
                                "time":time,
                                "username":username,
                                "storyclist":storyclist}),200
        if (storyid in sid) == False:
                return jsonify({
                        "message":"wrong"
                    }),400

@api.route('/story/<int:storyid>/<int:storycid>/like/', methods = ['GET'])
def like(storyid, storycid):
    if request.method == 'GET':        
        token = request.headers['token']
        users = User.query.all()
        for user in users:
            if user.confirm(token):
                i = 0
                for x in range(r.llen(storycid)):
                    if user.id == int(r.lindex(storycid,x)):
                        i = 1
                if (i == 0):
                    r.lpush(storycid,user.id)
                    story = Story.query.filter_by(id=storyid).first()
                    storyc = Storyc.query.filter_by(id=storycid).first()
                    user = User.query.filter_by(id = story.user_id).first()
                    storylikenum = int(story.likenum) + 1
                    storyclikenum = int(storyc.likenum) + 1
                    userlikenum = int(user.userlikenum) + 1
                    story.likenum = storylikenum
                    storyc.likenum = storyclikenum
                    user.userlikenum = userlikenum
                    db.session.add(story)
                    db.session.add(storyc)
                    db.session.commit()
                    return jsonify({
                        "likenum":storyc.likenum    
                    }),200
                else:
                    return jsonify({
                        "likenum":"-1"
                        })



@api.route('/story/hotest/', methods = ['GET'])
def hotest():
    if request.method == 'GET':
        story1 = Story.query.all()
        story = []
        s = []
        for a in story1:
            s.append(a.likenum)
        s.sort()
        for a in range(8):
            n = s[-(a + 1)]
            sn = Story.query.filter_by(likenum=n).first()
            title = sn.title
            floors = sn.floors
            time = sn.time
            sc = Storyc.query.filter_by().first()
            username = User.query.filter_by(id=sn.user_id).first().username
            story.append({'username':username,
                           'title':title,
                           'storyid':sn.id,
                           'storyc':sc.storyc,
                           'floors':floors,
                           'likenum':n,
                           'time':time,
                           'keyword':sn.keywords})
        
        return jsonify({
            "hotest":story
            }),200 


@api.route('/story/lastest/', methods = ['POST'])
def lastest():
    if request.method == 'POST':
        story1 = Story.query.all()
        address = request.get_json().get('address'); 
        story = []
        s = []
        storynum = 0 #故事数
        for a in story1:
            s.append(a.id)
            storynum += 1
        s.sort()
        if (storynum >= 8 * address):
            l = 8 #返回数
        else:
            l = storynum - 8 * (int(address) - 1)
        for a in range(l):
            n = s[-(a + 1 + 8 * (int(address) - 1))]
            sn = Story.query.filter_by(id=n).first()
            title = sn.title
            floors = sn.floors
            sc = Storyc.query.filter_by(story_id=sn.id).first()
            likenum = sc.likenum
            time = sn.time
            username = User.query.filter_by(id=sn.user_id).first().username
            story.append({'username':username,
                           'title':title,
                           'storyid':sn.id,
                           'storyc':sc.storyc,
                           'floors':floors,
                           'likenum':likenum,
                           'time':time,
                           'keyword':sn.keywords})
        return jsonify({
            "lastest":story
            }),200 
	
@api.route('/story/write/', methods = ['POST'])
def write():
    if request.method == 'POST':
        token = request.headers['token']
        uid = request.get_json().get('uid')
        user = User.query.filter_by(id=uid).first()
        if user.confirm(token):
            user.usb = int(user.usb) + 1
            title = request.get_json().get('title')
            storyckeyword = request.get_json().get('storyckeyword')
            storyc = request.get_json().get('storyc')
            storykeyword = storyckeyword
            localtime = time.strftime('%Y-%m-%d %a %H:%M:%S',time.localtime(time.time()))
            story = Story(title = title, 
                          likenum = 0,
                          floors = 1,
                          time = localtime,
                          keywords = storykeyword, 
                          user_id = uid)
            db.session.add(story)
            db.session.commit()
            storyc = Storyc(storyc = storyc,
                        likenum = 0,
                        storyckeyword = storyckeyword,
                        time = localtime,
                        story_id = story.id,
                        user_id = uid)
            db.session.add(storyc)
            db.session.commit()
            return jsonify({
                "storyid":story.id,
                "time":localtime
            }),200
        else:
            return jsonify({}),403


@api.route('/story/<int:storyid>/continue/', methods = ['POST'])
def continue1(storyid):
    if request.method == 'POST':
        token = request.headers['token']
        uid = request.get_json().get('uid')
        user = User.query.filter_by(id=uid).first()
        if user.confirm(token):
            user.usa = user.usa + 1
            storyc = request.get_json().get('storyc')
            storyckeyword = request.get_json().get('storyckeyword')
            story = Story.query.filter_by(id=storyid).first()
            storykeyword = story.keywords + ' ' + storyckeyword
            story.floors += 1
            localtime = time.strftime('%Y-%m-%d %a %H:%M:%S',time.localtime(time.time()))
            storyc1 = Storyc(storyc=storyc,
                             likenum = 0,
                             storyckeyword = storyckeyword,
                             time = localtime,
                             story_id=storyid,
                             user_id=uid)
            story.keywords = storykeyword
            #user.usa += 1
            #user.userwords += len(storyc)
            db.session.add(storyc1,story)
            db.session.commit()
            return jsonify({
                    "storycid":storyc1.id,
                    "time":localtime
                })

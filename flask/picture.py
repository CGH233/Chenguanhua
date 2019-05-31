#coding:GBK
from flask import Flask, render_template

app = Flask(__name__)

local_list = ['东北', '华北', '华东', '华南', '西北', '西南']
html_list = ['2019年东北地区AQI影响指标雷达图.html', '2019年华北地区AQI影响指标雷达图.html', '2019年华东地区AQI影响指标雷达图.html', '2019年华南地区AQI影响指标雷达图.html', '2019年西北地区AQI影响指标雷达图.html', '2019年西南地区AQI影响指标雷达图.html']

@app.route('/<local>')
def picture(local):
    index = local_list.index(local)
    return render_template(html_list[index])


if __name__ == '__main__':
    app.run()

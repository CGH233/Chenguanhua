#coding:GBK
from flask import Flask, render_template

app = Flask(__name__)

local_list = ['����', '����', '����', '����', '����', '����']
html_list = ['2019�궫������AQIӰ��ָ���״�ͼ.html', '2019�껪������AQIӰ��ָ���״�ͼ.html', '2019�껪������AQIӰ��ָ���״�ͼ.html', '2019�껪�ϵ���AQIӰ��ָ���״�ͼ.html', '2019����������AQIӰ��ָ���״�ͼ.html', '2019�����ϵ���AQIӰ��ָ���״�ͼ.html']

@app.route('/<local>')
def picture(local):
    index = local_list.index(local)
    return render_template(html_list[index])


if __name__ == '__main__':
    app.run()

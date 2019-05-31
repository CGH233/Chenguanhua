#coding:GBK
from flask import Flask, render_template

app = Flask(__name__)

local_list = ['dongbei', 'huabei', 'huadong', 'huanan', 'xibei', 'xinan']
html_list = ['1.html', '2.html', '3.html', '4.html', '5.html', '6.html']

@app.route('/<local>')
def picture(local):
    index = local_list.index(local)
    return render_template(html_list[index])


if __name__ == '__main__':
    app.run()

'''
Author: HaoTian Qi
Date: 2021-04-14 10:58:57
Description: 
LastEditTime: 2021-04-14 11:00:22
LastEditors: HaoTian Qi
FilePath: \flask-demo\flask-demo.py
'''

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


def main():
    app.run('0.0.0.0', 80, debug=True)


if __name__ == '__main__':
    main()

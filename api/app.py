from flask import Flask, jsonify, render_template,request
from chatResponse import *
import time

app = Flask(__name__)

@app.route('/')
def index():
    return 'welcome to chatbot api'

@app.route('/api/chatbot',methods=['GET'])
def chatbot_response():
	if request.method == 'GET':
            query=request.args.get('query')
            reply=get_chatbot_response(user_input=query)
            data={'reply':reply}
            return jsonify(data)


@app.route('/api/time', methods=['GET'])
def get_data():
    curr_time=time.strftime("%H:%M:%S" ,time.localtime())
    data={'time':curr_time}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, send_from_directory, redirect
from pygame import mixer
import os

#from playsound import playsound

app = Flask(__name__)
mixer.init()
mixer.music.load("static/music/bensound-creativeminds.mp3")

@app.route('/',methods=['GET', 'POST'])
def index():

# Write your code here

@app.route('/listen')
def music():
# Write your code here

@app.route('/abc.png')
def anv():
# Write your code here
                               
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
  
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000,debug=True, threaded=True)

    
    
  
    
    
    

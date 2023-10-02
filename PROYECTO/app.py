from flask import Flask
import os


template_dir=os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir=os.path.join(template_dir,'src','templates')

app=Flask(__name__,template_folder=template_dir)

app.route('/')
def home():

    return render_template('Nombre del index')

if __name__=='__main__':
    app,run(debug=True,port=3306)
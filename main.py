from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from extract import extract_text_pdf
from chat import converse_with_ai



app = Flask(__name__)
app.config['SECRET_KEY'] = 'omagad'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")




# @app.route('/', methods = ('GET', 'POST'))
# @app.route('/home', methods = ('GET', 'POST'))
# def home():
#     form = UploadFileForm()
#     if form.validate_on_submit():
#         file = form.file.data
#         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
#         return "File has been uploaded!"
#     return render_template('home.html', form = form)


@app.route('/', methods = ('GET', 'POST'))
@app.route('/home', methods = ('GET', 'POST'))
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        extracted_text = extract_text_pdf(file_path)

        conversation_history = session.get('conversation_history', [])

        user_message = extracted_text

        conversation_history.append({"role": "user", "content": user_message})

        ai_response = converse_with_ai(conversation_history)

        conversation_history.append({"role": "assistant", "content": ai_response})

        session['conversation_history'] = conversation_history 
        
        return render_template('result.html', ai_reponse=ai_response)
    
    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_DOCUMENT_EXTENSIONS = {'doc', 'xls', 'pdf', 'ppt', 'txt', 'pptx', 'docx', 'xlsx'}
ALLOWED_MEDIA_EXTENSIONS = {'mp3', 'mp4'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']

        if file and allowed_file(file.filename, ALLOWED_DOCUMENT_EXTENSIONS):
            category = 'document'
            dropdown_options = ALLOWED_DOCUMENT_EXTENSIONS
        elif file and allowed_file(file.filename, ALLOWED_MEDIA_EXTENSIONS):
            category = 'media'
            dropdown_options = ALLOWED_MEDIA_EXTENSIONS
        else:
            return render_template('index.html', error='Invalid file format')

        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        return render_template('index.html', category=category, current_extension=file.filename.rsplit('.', 1)[1], dropdown_options=dropdown_options)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


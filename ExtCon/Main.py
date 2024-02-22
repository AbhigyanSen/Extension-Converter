from flask import Flask, render_template, request, flash, send_file
from werkzeug.utils import secure_filename
import os
import PyPDF2
from docx import Document
from fpdf import FPDF

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_DOCUMENT_EXTENSIONS = {'doc', 'xls', 'pdf', 'ppt', 'txt', 'pptx', 'docx', 'xlsx'}
ALLOWED_MEDIA_EXTENSIONS = {'mp3', 'mp4'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def replace_problematic_characters(text):
    problematic_chars = ['\u2019', '\u2013']
    for char in problematic_chars:
        text = text.replace(char, '?')
    return text

def pdf_to_txt(input_path, output_dir):
    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    output_path = os.path.join(output_dir, os.path.splitext(os.path.basename(input_path))[0] + '.txt')
    with open(output_path, 'w') as txt_file:
        txt_file.write(text)

def pdf_to_docx(input_path, output_dir):
    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        doc = Document()
        for page_num in range(len(reader.pages)):
            text = reader.pages[page_num].extract_text()
            doc.add_paragraph(text)
    output_path = os.path.join(output_dir, os.path.splitext(os.path.basename(input_path))[0] + '.docx')
    doc.save(output_path)

def txt_to_pdf(input_path, output_dir):
    with open(input_path, 'r', encoding='utf-8') as file:
        text = file.read()

    text = replace_problematic_characters(text)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(200, 10, txt=text)

    output_path = os.path.join(output_dir, os.path.splitext(os.path.basename(input_path))[0] + '.pdf')
    pdf.output(output_path)

# Add functions for txt_to_docx, docx_to_pdf, docx_to_txt

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    print(request.files)

    if request.method == 'POST':
        file = request.files['file']

        if file and allowed_file(file.filename, ALLOWED_DOCUMENT_EXTENSIONS):
            category = 'document'
            dropdown_options = ALLOWED_DOCUMENT_EXTENSIONS
        elif file and allowed_file(file.filename, ALLOWED_MEDIA_EXTENSIONS):
            category = 'media'
            dropdown_options = ALLOWED_MEDIA_EXTENSIONS
        else:
            flash('Invalid file format', 'error')
            return render_template('index.html')

        filename = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(filename)

        selected_extension = request.form.get('other_extensions')

        if selected_extension == 'pdf' and category == 'document':
            pdf_to_txt(filename, app.config['UPLOAD_FOLDER'])
        elif selected_extension == 'docx' and category == 'document':
            pdf_to_docx(filename, app.config['UPLOAD_FOLDER'])
        elif selected_extension == 'txt' and category == 'document':
            txt_to_pdf(filename, app.config['UPLOAD_FOLDER'])
        # Add similar conditions for other conversion types

        # Provide the converted file name for download
        converted_filename = os.path.splitext(os.path.basename(filename))[0] + f'.{selected_extension}'
        conversion_success_message = "Conversion Successful"

        return render_template('index.html', category=category, current_extension=file.filename.rsplit('.', 1)[1],
                               dropdown_options=dropdown_options, conversion_success_message=conversion_success_message,
                               converted_filename=converted_filename)

    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
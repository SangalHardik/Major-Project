from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename
from main_flowchart import draw_flowchart
import logging
from datetime import datetime
import shutil

app = Flask(__name__, template_folder="template")
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'cpp', 'h', 'hpp'}
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1MB file size limit
app.config['STATIC_FOLDER'] = 'static'

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ensure directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['STATIC_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('front.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        logger.warning("No file part in upload request")
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        logger.warning("No selected file in upload request")
        return jsonify({'error': 'No selected file'}), 400
    
    if not allowed_file(file.filename):
        logger.warning(f"Invalid file type attempted: {file.filename}")
        return jsonify({'error': 'Invalid file type. Only .cpp, .h, .hpp files are allowed.'}), 400
    
    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        logger.info(f"File uploaded successfully: {filename}")
        return jsonify({
            'success': True,
            'filename': filename,
            'content': content
        })
    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        return jsonify({'error': f'Error processing file: {str(e)}'}), 500

@app.route('/convert', methods=['POST'])
def convert_to_flowchart():
    start_time = datetime.now()
    data = request.get_json()
    if not data or 'code' not in data:
        logger.warning("No code provided in conversion request")
        return jsonify({'error': 'No code provided'}), 400
    
    code = data['code']
    if not code.strip():
        logger.warning("Empty code provided in conversion request")
        return jsonify({'error': 'Empty code provided'}), 400
    
    try:
        # Generate unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"flowchart_{timestamp}.png"
        output_path = os.path.join(app.config['STATIC_FOLDER'], output_filename)
        
        # Call the original flowchart function
        error_message = draw_flowchart(code)
        
        if error_message:
            logger.error(f"Flowchart generation failed: {error_message}")
            return jsonify({
                'success': False,
                'error': str(error_message)
            }), 400
        
        # Check for the actual generated file (flowchart.gv.png instead of flowchart.png)
        actual_output = "flowchart.gv.png"
        if os.path.exists(actual_output):
            # If flowchart.gv.png exists, use it
            source_file = actual_output
        elif os.path.exists("flowchart.png"):
            # Fallback to original filename in case it changes in the future
            source_file = "flowchart.png"
        else:
            # Neither file exists
            error_msg = "Flowchart generation succeeded but output file not found"
            logger.error(error_msg)
            return jsonify({
                'success': False,
                'error': error_msg
            }), 500
        
        # Move the file to static folder
        shutil.move(source_file, output_path)
        
        processing_time = (datetime.now() - start_time).total_seconds()
        logger.info(f"Flowchart generated successfully in {processing_time:.2f} seconds")
        
        return jsonify({
            'success': True,
            'image_url': f'/static/{output_filename}',
            'processing_time': processing_time
        })
    except Exception as e:
        logger.error(f"Error generating flowchart: {str(e)}")
        # Clean up if something went wrong
        for possible_file in ["flowchart.png", "flowchart.gv.png"]:
            if os.path.exists(possible_file):
                os.remove(possible_file)
        return jsonify({
            'success': False,
            'error': f'Error generating flowchart: {str(e)}'
        }), 500

@app.route('/static/<path:filename>')
def serve_static(filename):
    try:
        return send_from_directory(app.config['STATIC_FOLDER'], filename)
    except FileNotFoundError:
        logger.error(f"Static file not found: {filename}")
        return jsonify({'error': 'File not found'}), 404

@app.errorhandler(413)
def request_entity_too_large(error):
    logger.warning("File upload too large")
    return jsonify({'error': 'File size exceeds 1MB limit'}), 413

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
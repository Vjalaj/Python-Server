import os
import socket
import argparse
from flask import Flask, request, render_template, send_from_directory, redirect, url_for

app = Flask(__name__)

# Ensure the content directory exists
CONTENT_FOLDER = 'content'
os.makedirs(CONTENT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    # List all files in the content directory
    files = os.listdir(CONTENT_FOLDER)
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    # Save the file to the content folder
    file.save(os.path.join(CONTENT_FOLDER, file.filename))
    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(CONTENT_FOLDER, filename, as_attachment=True)

@app.route('/content/<filename>')
def serve_content(filename):
    # Serve files for preview without forcing download
    return send_from_directory(CONTENT_FOLDER, filename, as_attachment=False)

def get_ip_address():
    # Get the local IP address of the machine
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't need to be reachable
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def create_templates():
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    # Create index.html template
    with open('templates/index.html', 'w') as f:
        f.write('''
<!DOCTYPE html>
<html>
<head>
    <title>File Server</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            color: #333;
        }
        .upload-form {
            margin: 20px 0;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        .file-list {
            margin-top: 20px;
        }
        .file-item {
            padding: 10px;
            border-bottom: 1px solid #eee;
        }
        .file-item:hover {
            background-color: #f5f5f5;
        }
        .file-link {
            text-decoration: none;
            color: #0066cc;
        }
        .file-link:hover {
            text-decoration: underline;
        }
        .no-files {
            color: #666;
            font-style: italic;
        }
    </style>
</head>
<body>
    <h1>File Server</h1>
    
    <div class="upload-form">
        <h2>Upload File</h2>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file" required>
            <button type="submit">Upload</button>
        </form>
    </div>
    
    <div class="file-list">
        <h2>Available Files</h2>
        {% if files %}
            <ul>
            {% for file in files %}
                <div class="file-item">
                    <a class="file-link" href="/download/{{ file }}">{{ file }}</a>
                </div>
            {% endfor %}
            </ul>
        {% else %}
            <p class="no-files">No files available for download.</p>
        {% endif %}
    </div>
</body>
</html>
''')

if __name__ == '__main__':
    # Create the templates
    create_templates()
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='File Server')
    parser.add_argument('--port', type=int, default=5000, help='Port to run the server on')
    args = parser.parse_args()
    
    # Get the IP address
    ip_address = get_ip_address()
    
    print(f"\nServer running at http://{ip_address}:{args.port}")
    print(f"You can also access it at http://localhost:{args.port}")
    print("Press Ctrl+C to stop the server\n")
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=args.port, debug=True, threaded=True)
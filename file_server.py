import os
import socket
import argparse
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, send_from_directory, redirect, url_for, flash, jsonify, Response
import json

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for flash messages

# Configuration
CONTENT_FOLDER = 'content'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024 * 1024  # 16GB max file size
ALLOWED_EXTENSIONS = {
    'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx',
    'mp4', 'mp3', 'wav', 'avi', 'mkv', 'zip', 'rar', '7z',
    'exe', 'msi', 'iso', 'csv', 'xlsx', 'pptx', 'py', 'js'
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_file_size(filepath):
    return round(os.path.getsize(filepath) / (1024 * 1024), 2)  # Size in MB

# Ensure the content directory exists
os.makedirs(CONTENT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    files = []
    for filename in os.listdir(CONTENT_FOLDER):
        filepath = os.path.join(CONTENT_FOLDER, filename)
        size_mb = get_file_size(filepath)
        files.append({'name': filename, 'size': size_mb})
    return render_template('index.html', files=files, allowed_extensions=ALLOWED_EXTENSIONS)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file selected', 'error')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No file selected', 'error')
        return redirect(request.url)
    
    if not allowed_file(file.filename):
        flash('File type not allowed', 'error')
        return redirect(url_for('index'))
    
    try:
        filename = secure_filename(file.filename)
        file.save(os.path.join(CONTENT_FOLDER, filename))
        flash('File uploaded successfully', 'success')
    except Exception as e:
        flash(f'Error uploading file: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/delete/<filename>')
def delete_file(filename):
    try:
        file_path = os.path.join(CONTENT_FOLDER, secure_filename(filename))
        if os.path.exists(file_path):
            os.remove(file_path)
            flash('File deleted successfully', 'success')
        else:
            flash('File not found', 'error')
    except Exception as e:
        flash(f'Error deleting file: {str(e)}', 'error')
    return redirect(url_for('index'))

@app.route('/progress/<task_id>')
def get_progress(task_id):
    progress = session.get(f'progress_{task_id}', 0)
    return jsonify({'progress': progress})

@app.route('/download/<filename>')
def download_file(filename):
    def generate():
        file_path = os.path.join(CONTENT_FOLDER, filename)
        file_size = os.path.getsize(file_path)
        
        with open(file_path, 'rb') as f:
            bytes_sent = 0
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break
                bytes_sent += len(chunk)
                progress = int((bytes_sent / file_size) * 100)
                yield chunk
    
    return Response(
        generate(),
        mimetype='application/octet-stream',
        headers={'Content-Disposition': f'attachment; filename={filename}'}
    )

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
    os.makedirs('templates', exist_ok=True)
    
    with open('templates/index.html', 'w') as f:
        f.write('''
<!DOCTYPE html>
<html data-theme="light">
<head>
    <title>File Server</title>
    <style>
        :root[data-theme="light"] {
            --bg-color: #ffffff;
            --text-color: #333333;
            --card-bg: #f9f9f9;
            --border-color: #ddd;
            --hover-bg: #f5f5f5;
            --link-color: #0066cc;
            --delete-color: #dc3545;
        }
        
        :root[data-theme="dark"] {
            --bg-color: #1a1a1a;
            --text-color: #ffffff;
            --card-bg: #2d2d2d;
            --border-color: #404040;
            --hover-bg: #353535;
            --link-color: #66b3ff;
            --delete-color: #ff4d4d;
        }

        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: var(--bg-color);
            color: var(--text-color);
            transition: all 0.3s ease;
        }

        .theme-toggle {
            background: none;
            border: none;
            padding: 10px;
            cursor: pointer;
        }

        .theme-toggle svg {
            width: 24px;
            height: 24px;
            fill: var(--text-color);
        }

        .logo {
            width: 50px;
            height: 50px;
            margin-right: 10px;
            vertical-align: middle;
        }

        .upload-form {
            margin: 20px 0;
            padding: 20px;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            background-color: var(--card-bg);
        }

        .progress-bar {
            width: 100%;
            height: 20px;
            background-color: var(--border-color);
            border-radius: 10px;
            margin: 10px 0;
            overflow: hidden;
            display: none;
        }

        .progress {
            width: 0%;
            height: 100%;
            background-color: var(--link-color);
            transition: width 0.3s ease;
        }

        .file-item {
            padding: 15px;
            margin: 10px 0;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            background-color: var(--card-bg);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .file-link {
            text-decoration: none;
            color: var(--link-color);
        }

        .delete-btn {
            color: var(--delete-color);
            padding: 5px 10px;
            border: 1px solid var(--delete-color);
            border-radius: 4px;
            text-decoration: none;
        }

        button {
            padding: 8px 16px;
            background-color: var(--link-color);
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        /* Rest of your existing styles with var() */
    </style>
</head>
<body>
    <svg style="display: none;">
        <!-- Server Logo -->
        <symbol id="server-logo" viewBox="0 0 24 24">
            <path d="M4 1h16c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2zm0 2v4h16V3H4zm0 8v4h16v-4H4zm0 8v4h16v-4H4z"/>
            <circle cx="8" cy="5" r="1"/>
            <circle cx="8" cy="13" r="1"/>
            <circle cx="8" cy="21" r="1"/>
        </symbol>
        <!-- Sun icon -->
        <symbol id="sun-icon" viewBox="0 0 24 24">
            <circle cx="12" cy="12" r="5"/>
            <path d="M12 1v2m0 18v2M4.22 4.22l1.42 1.42m12.72 12.72 1.42 1.42M1 12h2m18 0h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/>
        </symbol>
        <!-- Moon icon -->
        <symbol id="moon-icon" viewBox="0 0 24 24">
            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
        </symbol>
    </svg>

    <div style="display: flex; align-items: center;">
        <svg class="logo"><use href="#server-logo"/></svg>
        <h1>File Server</h1>
        <button class="theme-toggle" onclick="toggleTheme()">
            <svg><use href="#sun-icon" class="sun-icon"/></svg>
            <svg style="display: none;"><use href="#moon-icon" class="moon-icon"/></svg>
        </button>
    </div>

    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <div class="flash-messages">
            {% for category, message in messages %}
                <div class="flash-message {{ category }}">{{ message }}</div>
            {% endfor %}
            </div>
        {% endif %}
    {% endwith %}
    
    <div class="upload-form">
        <h2>Upload File</h2>
        <form id="uploadForm" action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file" required>
            <button type="submit">Upload</button>
            <div class="progress-bar" id="uploadProgress">
                <div class="progress"></div>
            </div>
        </form>
        <p><small>Allowed files: {{ ', '.join(allowed_extensions) }}</small></p>
        <p><small>Maximum file size: 16GB</small></p>
    </div>
    
    <div class="file-list">
        <h2>Available Files</h2>
        {% if files %}
            {% for file in files %}
                <div class="file-item">
                    <div>
                        <a class="file-link" href="/download/{{ file.name }}" 
                           onclick="showDownloadProgress(event, '{{ file.name }}')">{{ file.name }}</a>
                        <span class="file-size">{{ file.size }} MB</span>
                    </div>
                    <a class="delete-btn" href="/delete/{{ file.name }}" 
                       onclick="return confirm('Are you sure?')">Delete</a>
                    <div class="progress-bar" id="download-{{ file.name }}">
                        <div class="progress"></div>
                    </div>
                </div>
            {% endfor %}
        {% else %}
            <p class="no-files">No files available for download.</p>
        {% endif %}
    </div>

    <script>
        function updateProgress(progressBar, url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    const progress = progressBar.querySelector('.progress');
                    progress.style.width = data.progress + '%';
                    if (data.progress < 100) {
                        setTimeout(() => updateProgress(progressBar, url), 500);
                    }
                });
        }

        // Upload handling with real progress
        document.getElementById('uploadForm').onsubmit = function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const progressBar = document.getElementById('uploadProgress');
            progressBar.style.display = 'block';
            
            const xhr = new XMLHttpRequest();
            xhr.open('POST', '/upload', true);
            
            xhr.upload.onprogress = function(e) {
                if (e.lengthComputable) {
                    const progress = (e.loaded / e.total) * 100;
                    progressBar.querySelector('.progress').style.width = progress + '%';
                }
            };
            
            xhr.onload = function() {
                window.location.reload();
            };
            
            xhr.send(formData);
        };

        // Theme toggle with icon swap
        function toggleTheme() {
            const html = document.documentElement;
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            
            const sunIcon = document.querySelector('.sun-icon').parentElement;
            const moonIcon = document.querySelector('.moon-icon').parentElement;
            if (newTheme === 'dark') {
                sunIcon.style.display = 'none';
                moonIcon.style.display = 'block';
            } else {
                sunIcon.style.display = 'block';
                moonIcon.style.display = 'none';
            }
        }

        // Set initial theme and icon
        const savedTheme = localStorage.getItem('theme') || 'light';
        document.documentElement.setAttribute('data-theme', savedTheme);
        const sunIcon = document.querySelector('.sun-icon').parentElement;
        const moonIcon = document.querySelector('.moon-icon').parentElement;
        if (savedTheme === 'dark') {
            sunIcon.style.display = 'none';
            moonIcon.style.display = 'block';
        }
    </script>
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
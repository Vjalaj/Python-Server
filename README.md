# File Server

A simple and elegant file server built with Flask that allows you to easily share files within your local network. This server provides a modern web interface with light and dark mode support for uploading and downloading files.

## Features

- 🎯 Simple and intuitive web interface
- 🌓 Light and dark mode support
- 📤 Easy file upload functionality
- 📥 Quick file downloads
- 🖼️ File preview support
- 📱 Responsive design for all devices
- 🔄 Real-time file list updates
- 🌐 Access from any device in local network

## Prerequisites

- Python 3.6 or higher
- Flask

## Installation

1. Clone this repository or download the files
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the server:
```bash
python file_server.py
```

2. By default, the server will run on port 5000. You can specify a different port using the `--port` argument:
```bash
python file_server.py --port 8080
```

3. Access the server:
   - Local access: `http://localhost:5000`
   - Network access: `http://<your-ip-address>:5000`

## Project Structure

```
Python-Server/
│
├── file_server.py      # Main server application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
│
├── static/
│   └── css/
│       └── style.css  # Stylesheet for the web interface
│
├── templates/
│   └── index.html     # Main page template
│
└── content/           # Directory for uploaded files
```

## Contributing

Feel free to open issues and submit pull requests to improve the project.

## License

This project is open source and available under the MIT License.

Created by Jalaj

---

**Note:** This file server is designed for local network use. Make sure to implement proper security measures if you plan to expose it to the internet.
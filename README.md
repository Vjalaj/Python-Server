<div align="center">

# 🗂️ Flask File Server
### *The Ultimate Local Network File Sharing Solution*

*Transform your device into a powerful file sharing hub with this beautifully crafted Flask server*

[![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20|%20macOS%20|%20Linux-lightgrey?style=for-the-badge)](https://github.com)
[![Stars](https://img.shields.io/github/stars/Vjalaj/Python-Server?style=for-the-badge&logo=github)](https://github.com/Vjalaj/Python-Server/stargazers)

> 💡 **Why struggle with USB drives and cloud storage when you can instantly share files across all your devices?**
> 
> This isn't just another file server – it's your personal file sharing ecosystem with a stunning interface that works flawlessly on every device!

🎯 [**Get Started in 2 Minutes**](#-quick-start) • ✨ [**See What's Possible**](#-features) • � [**Mobile Ready**](#accessing-the-server) • 🛡️ [**Security First**](#️-security-features)

</div>

---

## ✨ Features

### 🎨 **Modern Interface**
- � **Dark/Light Mode** - Seamless theme switching
- 📱 **Responsive Design** - Perfect on desktop, tablet, and mobile
- 🎯 **Intuitive UI** - Clean and user-friendly interface
- 🖼️ **File Previews** - Quick preview support for various file types

### 🚀 **Powerful Functionality**
- 📤 **Drag & Drop Upload** - Easy file uploading with progress indicators
- 📥 **Instant Downloads** - Quick file access and sharing
- � **Real-time Updates** - Live file list synchronization
- 🌐 **Network Access** - Share files across your local network
- � **Secure Uploads** - File validation and size limits
- 📊 **File Management** - View file sizes, types, and upload dates

### 🛠️ **Technical Features**
- ⚡ **High Performance** - Built with Flask for speed and reliability
- 🔧 **Configurable** - Customizable port, upload limits, and file types
- 📦 **Lightweight** - Minimal dependencies and resource usage
- 🛡️ **Security** - Secure filename handling and upload validation

## 🚀 Quick Start - **Be Running in 2 Minutes!**

> 💡 **Pro Tip**: Have Python installed? You're already 90% there!

### Prerequisites ✅
- 🐍 **Python 3.6+** (Check with `python --version`)
- 📦 **pip** (Comes with Python - you're good to go!)

### 🎯 **The Fastest Setup Ever**

**Step 1: Get the code**
```bash
git clone https://github.com/Vjalaj/Python-Server.git
cd Python-Server
```

**Step 2: Set up environment** *(recommended but optional)*
```bash
python -m venv venv

# Windows users:
venv\Scripts\activate

# macOS/Linux users:
source venv/bin/activate
```

**Step 3: Install & Launch**
```bash
pip install -r requirements.txt
python file_server.py
```

**🎉 Boom! Your server is live!** Open `http://localhost:5000` and start sharing files like a pro!

## � Usage - **It's This Easy!**

### 🎯 **Starting Your File Empire**

**For beginners:**
```bash
python file_server.py
# ✨ That's it! Your server is running on port 5000
```

**For power users:**
```bash
python file_server.py --port 8080
# 🚀 Custom port? No problem!
```

**For network ninjas:**
```bash
python file_server.py --port 3000 --host 0.0.0.0
# 🌐 Maximum network accessibility
```

### 🗺️ **Access Your Server Anywhere**

| 🎯 **Access Method** | 🔗 **URL** | 📝 **Perfect For** |
|---------------------|------------|-------------------|
| 🏠 **Same Computer** | `http://localhost:5000` | Testing and personal use |
| 🌐 **Network Devices** | `http://<your-ip>:5000` | Sharing across devices |
| 📱 **Mobile Quick Access** | Bookmark the URL | Instant mobile file access |

> 💡 **Pro Tip**: To find your IP address, run `ipconfig` (Windows) or `ifconfig` (macOS/Linux)

### 🎬 **The File Sharing Experience**

#### 📤 **Uploading Files** *(So satisfying!)*
1. 🌐 Open your browser to the server URL
2. 🎯 Click **"Choose Files"** or simply **drag & drop** 
3. ⚡ Watch files upload instantly to the `content/` folder
4. 🎉 See them appear in your file list immediately!

#### 📥 **Downloading Files** *(One-click magic!)*
1. 👀 Browse the beautiful file list interface
2. 🖱️ Click any filename
3. 💫 File downloads to your device automatically
4. ✅ Done! No complicated steps, no confusion

## 📁 Project Structure

```
📦 Python-Server/
├── 🐍 file_server.py          # Main Flask application
├── 📋 requirements.txt        # Python dependencies
├── 📖 README.md              # Project documentation
│
├── 📁 templates/             # HTML templates
│   ├── 🌐 index.html        # Main web interface
│   └── 🎨 style.css         # Responsive stylesheet
│
├── 📁 content/               # File storage directory
│   └── 📄 file.txt          # Example uploaded file
│
└── 📁 venv/                  # Virtual environment (auto-generated)
```

## ⚙️ Configuration

### Environment Variables
```bash
export FLASK_ENV=development          # Development mode
export FLASK_DEBUG=1                  # Enable debug mode
export MAX_CONTENT_LENGTH=16GB        # Maximum file size
```

### Supported File Types
```python
ALLOWED_EXTENSIONS = {
    # Documents
    'txt', 'pdf', 'doc', 'docx', 'csv', 'xlsx', 'pptx',
    
    # Images
    'png', 'jpg', 'jpeg', 'gif', 'svg', 'webp',
    
    # Media
    'mp4', 'mp3', 'wav', 'avi', 'mkv',
    
    # Archives
    'zip', 'rar', '7z', 'tar', 'gz',
    
    # Code
    'py', 'js', 'html', 'css', 'json', 'xml'
}
```

## 🛡️ Security Features

- ✅ **Secure Filename Handling** - Prevents path traversal attacks
- ✅ **File Type Validation** - Only allowed file extensions
- ✅ **Size Limitations** - Configurable maximum file size (16GB default)
- ✅ **Input Sanitization** - All user inputs are properly sanitized
- ⚠️ **Local Network Only** - Designed for trusted local network use

## 🚨 Important Security Notes

> **⚠️ WARNING**: This server is designed for local network use only. Do not expose it directly to the internet without implementing additional security measures such as:
> - Authentication and authorization
> - HTTPS/SSL encryption  
> - Rate limiting
> - Input validation
> - Access logs and monitoring

## 📱 Screenshots

*Screenshots will be added here to showcase the beautiful interface*

## 🔧 Troubleshooting - **We've Got You Covered!**

### 🆘 **Common Issues** *(And their instant fixes)*

<details>
<summary><strong>🐛 Import Error with Werkzeug</strong></summary>

```bash
ImportError: cannot import name 'url_quote' from 'werkzeug.urls'
```
**💡 Quick Fix:**
```bash
pip install flask==2.3.3 werkzeug==2.3.7
```
*This updates to compatible versions that work perfectly together!*
</details>

<details>
<summary><strong>🔒 Permission Denied Error</strong></summary>

```bash
PermissionError: [Errno 13] Permission denied
```
**💡 Solutions:**
- Check if the `content/` folder has write permissions
- Try running as administrator (Windows) or with `sudo` (macOS/Linux)
- Make sure no antivirus is blocking the application
</details>

<details>
<summary><strong>🚫 Port Already in Use</strong></summary>

```bash
OSError: [Errno 48] Address already in use
```
**💡 Easy Fix:**
```bash
python file_server.py --port 8080
# Or try 3000, 4000, 8000 - any available port!
```
</details>

<details>
<summary><strong>🌐 Can't Access from Other Devices</strong></summary>

**💡 Troubleshooting Steps:**
1. Check if devices are on the same network
2. Verify firewall settings aren't blocking the port
3. Try running with: `python file_server.py --host 0.0.0.0`
4. Use your actual IP address, not localhost
</details>

### 🆘 **Still Need Help?**
- 💬 [Open an issue](https://github.com/Vjalaj/Python-Server/issues) - we respond fast!
- 📧 Contact the developer
- 🌟 Check existing issues for solutions

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🐛 Reporting Bugs
1. Check existing issues first
2. Create a detailed bug report
3. Include steps to reproduce
4. Add screenshots if applicable

### 💡 Suggesting Features
1. Open a feature request issue
2. Describe the feature in detail
3. Explain the use case
4. Consider implementation details

### 🔧 Code Contributions
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Jalaj

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## 👨‍💻 Author

**Jalaj**
- 💼 Developer & Creator
- 🌟 Passionate about building useful tools

---

<div align="center">

## 🌟 **Love This Project?**

### **Show Your Support!**

⭐ **Star this repository** if it made your life easier!  
🍴 **Fork it** to create your own awesome version!  
🐛 **Report issues** to help us improve!  
💡 **Suggest features** - we love good ideas!

---

### 🎉 **Join the Community**

[![GitHub followers](https://img.shields.io/github/followers/Vjalaj?style=social)](https://github.com/Vjalaj)
[![GitHub issues](https://img.shields.io/github/issues/Vjalaj/Python-Server)](https://github.com/Vjalaj/Python-Server/issues)
[![GitHub forks](https://img.shields.io/github/forks/Vjalaj/Python-Server?style=social)](https://github.com/Vjalaj/Python-Server/network)

**Built with ❤️ by [Jalaj](https://github.com/Vjalaj)**  
*Passionate developer creating tools that make life easier*

---

### 🚀 **Ready to Share Files Like a Pro?**

**[⬆️ Back to Quick Start](#-quick-start---be-running-in-2-minutes) | [🎯 See All Features](#-features-that-will-blow-your-mind) | [🛡️ Security Info](#️-security-features)**

*Happy file sharing! May your transfers be swift and your storage be endless! �✨*

</div>
#LAN CLOUD STORAGE
#CLOUD STORAGE

# Flask Cloud Storage

A simple personal cloud storage system built with Flask.

## Features

- Login system with credentials stored in `users.json`
- Upload and download files
- User session management
- Easy to self-host via LAN

## Run the server

```bash
pip install flask
python app.py
```

## Access from LAN

- Open in browser: `http://<your-ip>:5000` (e.g. http://192.168.31.160:5000)
- Make sure your PC and phone are connected to the same Wi-Fi.

## File Structure

- `app.py`: Main application
- `uploads/`: Folder to store uploaded files
- `templates/`: HTML pages

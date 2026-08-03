# GoDaddy Shared/Cloud Hosting Deployment Guide

## Architecture
GoDaddy uses **Passenger WSGI** to run Python apps, not Gunicorn. Passenger is an app server that automatically detects and runs WSGI applications.

## What Changed
This app has been updated for GoDaddy Passenger deployment:

### 1. **passenger_wsgi.py** (new file)
   - Entry point for Passenger WSGI server
   - Imports Flask app and exposes as `application`
   - Passenger automatically loads this file

### 2. **Disabled Debug Mode** (app.py)
   - Changed `debug=True` to `debug=False`
   - Changed host to `127.0.0.1` (Passenger manages the public interface)
   - Removed development mode security risks

### 3. **Updated requirements.txt**
   - Removed Gunicorn (not needed for Passenger)
   - Kept Flask and Werkzeug

## Deployment Steps

### 1. Push to GoDaddy
```bash
# Commit and push your changes
git add .
git commit -m "Configure for GoDaddy Passenger deployment"
git push origin main
```

### 2. GoDaddy Control Panel Setup
1. Go to **Hosting → Python**
2. Select **WSGI Application**
3. Set:
   - **Application Path**: `/home/your_username/python/render_app`
   - **Application Startup File**: `passenger_wsgi.py`
   - **Entry Point**: `application` (this is the variable name)

### 3. Install Dependencies
Via SSH or GoDaddy terminal:
```bash
cd ~/python/render_app
pip install -r requirements.txt
```

### 4. Restart Python App
In GoDaddy control panel: **Hosting → Python → Restart**

## File Structure (as GoDaddy expects)
```
~/python/render_app/
├── app.py
├── passenger_wsgi.py      ← Entry point for Passenger
├── requirements.txt
├── render.yaml            ← Can be ignored
└── godaddy-deployment.md
```

## Testing Locally
```bash
# Test that WSGI app loads correctly
python -c "from passenger_wsgi import application; print('✓ App loads successfully')"

# Or run Flask dev server
python app.py
```

## Troubleshooting

| Error | Solution |
|-------|----------|
| `SyntaxError in passenger_wsgi.py` | Verify `passenger_wsgi.py` has correct syntax (check colon position) |
| `ModuleNotFoundError: No module named 'flask'` | Run `pip install -r requirements.txt` in SSH |
| `Timeout errors` | Check if app starts with: `python -c "from passenger_wsgi import application"` |
| `Permission denied` | Run: `chmod 755 ~/python/render_app` and subdirs |

## Performance Notes
- Passenger automatically manages processes (similar to Gunicorn)
- No need to configure workers manually
- Static files should be served separately if present

## Important Files
- **passenger_wsgi.py** — Must exist and export `application` variable
- **requirements.txt** — Installed via GoDaddy Python manager
- **app.py** — Your Flask application logic

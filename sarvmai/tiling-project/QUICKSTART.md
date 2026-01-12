# 🚀 Quick Start Guide

## Option 1: Automated Setup (Recommended for Windows)

### Using Batch File (cmd.exe)
```powershell
# Navigate to project folder
cd c:\Users\saide\OneDrive\Desktop\sarvmai\tiling-project

# Run setup
setup.bat
```

The script will:
- ✅ Create a Python virtual environment
- ✅ Install all dependencies
- ✅ Start the backend API (http://localhost:5000)
- ✅ Open the frontend in your browser

---

## Option 2: Using PowerShell

```powershell
# Navigate to project folder
cd c:\Users\saide\OneDrive\Desktop\sarvmai\tiling-project

# Run setup (may need to enable script execution first)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\setup.ps1
```

---

## Option 3: Manual Setup

### Step 1: Backend Setup
```powershell
cd backend

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\Activate

# Install dependencies
pip install -r requirements.txt

# Start the API
python app.py
```

The API will run at: **http://localhost:5000**

### Step 2: Frontend Setup (in a new terminal/PowerShell window)
```powershell
cd frontend

# Option A: Open directly
start index.html

# Option B: Use Python HTTP server
python -m http.server 8000
# Then open: http://localhost:8000
```

---

## 🧪 Testing the Application

1. **Open the UI** in your browser
2. **Enter room dimensions:**
   - Length: 6
   - Width: 4

3. **Enter tile specifications:**
   - Tile A: Size 1, Cost 2
   - Tile B: Size 2, Cost 3
   - Tile C: Size 3, Cost 6

4. **Click "Calculate Solution"**

5. **Expected Output:**
   ```
   Tiles of size A: 0
   Tiles of size B: 12
   Tiles of size C: 0
   Total Cost: $36.00
   ```

---

## 📝 Troubleshooting

### Python not found
```powershell
# Check if Python is in PATH
python --version

# If not, either:
# 1. Install from https://www.python.org (check "Add Python to PATH")
# 2. Or use full path: C:\Users\YourName\AppData\Local\Programs\Python\Python310\python.exe
```

### Port 5000 already in use
```powershell
# Find what's using port 5000
netstat -ano | findstr :5000

# Kill the process (replace PID with the number found)
taskkill /PID <PID> /F

# Or change port in app.py line: app.run(debug=True, port=5001)
```

### CORS errors
- Make sure backend is running on port 5000
- Make sure frontend is opening from same machine
- Check browser console for errors (F12)

### Dependencies installation fails
```powershell
# Upgrade pip first
python -m pip install --upgrade pip

# Then retry
pip install -r requirements.txt
```

---

## 🎯 Project Files

```
tiling-project/
├── backend/
│   ├── app.py                 # Flask API - Main calculations
│   ├── requirements.txt       # Python packages
│   └── venv/                  # Virtual environment (created on setup)
│
├── frontend/
│   └── index.html             # Complete web UI (HTML + CSS + JS)
│
├── setup.bat                  # Windows batch setup script
├── setup.ps1                  # PowerShell setup script
├── QUICKSTART.md              # This file
└── README.md                  # Full documentation
```

---

## 📚 Next Steps

- Customize tile sizes and costs for your needs
- Modify the algorithm in `backend/app.py` if needed
- Add more features to the UI in `frontend/index.html`
- Extend the API with additional endpoints

---

## 🆘 Need Help?

1. Check the README.md for full documentation
2. Review code comments in app.py
3. Open browser developer tools (F12) to see API responses
4. Check backend terminal for error messages

**Happy Tiling! 🧩**

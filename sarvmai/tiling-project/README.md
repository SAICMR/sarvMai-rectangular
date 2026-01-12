# 🧩 Non-Optimal Tiling for Cost-Inefficient Flooring

A full-stack web application that calculates the maximum cost tiling solution for rectangular rooms using three types of square tiles.

## 📋 Overview

This project solves the non-optimal flooring tiling problem where the goal is to **maximize total cost** (not minimize) by strategically choosing which tile types to use for covering a room.

### Problem Statement
Given:
- Room dimensions: L × W meters
- Three tile types with different sizes and costs
- Constraint: Tiles cannot be cut; if they exceed room boundaries, they're wasted

Goal: Find a tiling solution that **maximizes total cost**

## 📁 Project Structure

```
tiling-project/
├── backend/
│   ├── app.py              # Flask API server
│   └── requirements.txt    # Python dependencies
├── frontend/
│   └── index.html          # Web UI (HTML/CSS/JS)
└── README.md              # This file
```

## 🚀 Getting Started

### Backend Setup

1. **Navigate to backend directory:**
   ```powershell
   cd backend
   ```

2. **Create a Python virtual environment (optional but recommended):**
   ```powershell
   python -m venv venv
   venv\Scripts\Activate
   ```

3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Run the API server:**
   ```powershell
   python app.py
   ```
   
   The server will start at `http://localhost:5000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```powershell
   cd frontend
   ```

2. **Open in browser:**
   - Simply open `index.html` in any modern web browser
   - Or use a local server:
     ```powershell
     python -m http.server 8000
     ```
     Then visit `http://localhost:8000`

## 📊 API Endpoints

### POST /calculate

Calculates the maximum-cost tiling solution.

**Request:**
```json
{
  "length": 6,
  "width": 4,
  "tiles": [
    {"size": 1, "cost": 2},
    {"size": 2, "cost": 3},
    {"size": 3, "cost": 6}
  ]
}
```

**Response:**
```json
{
  "status": "success",
  "room": {
    "length": 6,
    "width": 4,
    "area": 24
  },
  "tiles_used": [
    {
      "size": 1,
      "cost_per_tile": 2,
      "count": 0,
      "total_cost": 0
    },
    {
      "size": 2,
      "cost_per_tile": 3,
      "count": 12,
      "total_cost": 36
    },
    {
      "size": 3,
      "cost_per_tile": 6,
      "count": 0,
      "total_cost": 0
    }
  ],
  "total_cost": 36,
  "visualization": "ASCII art grid representation"
}
```

## 🧮 Sample Usage

### Input:
```
Room: 6m × 4m
Tile A: 1×1, cost $2
Tile B: 2×2, cost $3
Tile C: 3×3, cost $6
```

### Expected Output:
```
Tiles of size A: 0
Tiles of size B: 12
Tiles of size C: 0
Total Cost: $36
```

## 🎨 Features

✅ **Web-based UI** - Clean, responsive interface
✅ **Real-time Calculation** - Get results instantly
✅ **ASCII Visualization** - See your tiling layout
✅ **Multiple Tile Support** - Handle 3 different tile types
✅ **Cost Tracking** - Detailed breakdown of costs per tile type
✅ **CORS Enabled** - Frontend-backend communication
✅ **Error Handling** - Validate inputs and display errors

## 🔧 How It Works

1. **Input Validation**: Checks room dimensions and tile specifications
2. **Solution Generation**: Tries different combinations of tiles
3. **Layout Simulation**: Places tiles using a greedy algorithm
4. **Cost Calculation**: Computes total cost for each valid solution
5. **Optimization**: Returns the solution with maximum total cost
6. **Visualization**: Generates ASCII art representation

## 📦 Requirements

- **Python 3.7+**
- **Flask 2.3.2**
- **flask-cors 4.0.0**
- **Modern web browser** (Chrome, Firefox, Safari, Edge)

## 🖥️ Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 💡 Algorithm Details

The calculator uses a greedy placement algorithm:

1. **Sort tiles** by size (largest first)
2. **Iterate through room** grid from (0,0) to (L,W)
3. **Try to place largest available tile** at each position
4. **Fall back to smaller tiles** if larger ones don't fit
5. **Validate** complete room coverage
6. **Calculate total cost** and rank solutions

## 🎯 Future Enhancements

- [ ] Voice input support (SarvM.AI integration)
- [ ] Multi-language support
- [ ] Advanced visualization with colors
- [ ] Save/load configurations
- [ ] Cost optimization mode
- [ ] Batch processing
- [ ] Database integration

## 📝 License

Open source - feel free to use and modify!

## 👨‍💻 Support

For issues or questions, check the code comments or test with the sample input first.

---

**Made with ❤️ for SarvM.AI**

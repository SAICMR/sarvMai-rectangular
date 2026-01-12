# 📝 Configuration & API Examples

## 🔧 Backend Configuration

### Flask Configuration (app.py)

**Change Server Port:**
```python
# Line 175 in app.py
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change 5000 to any port
```

**Disable Debug Mode (Production):**
```python
if __name__ == '__main__':
    app.run(debug=False, port=5000)
```

**Enable CORS for Specific Domains:**
```python
from flask_cors import CORS

CORS(app, resources={
    r"/calculate": {"origins": ["http://localhost:3000", "https://yourdomain.com"]}
})
```

---

## 🔌 API Endpoints Reference

### GET /
**Health check and endpoint info**

Response:
```json
{
  "status": "Tiling Calculator API Running",
  "endpoints": {
    "/calculate": "POST - Calculate optimal tiling",
    "/health": "GET - Health check"
  }
}
```

---

### GET /health
**Check if API is running**

Response:
```json
{
  "status": "healthy"
}
```

---

### POST /calculate
**Calculate the maximum-cost tiling solution**

Request Headers:
```
Content-Type: application/json
```

Request Body:
```json
{
  "length": 6,
  "width": 4,
  "tiles": [
    {
      "size": 1,
      "cost": 2
    },
    {
      "size": 2,
      "cost": 3
    },
    {
      "size": 3,
      "cost": 6
    }
  ]
}
```

Response (Success):
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
  "visualization": "ASCII grid visualization"
}
```

Response (Error):
```json
{
  "status": "error",
  "message": "Error description here"
}
```

---

## 💻 cURL Examples

### Test API Health
```bash
curl http://localhost:5000/health
```

### Calculate Tiling (Example 1: Small Room)
```bash
curl -X POST http://localhost:5000/calculate \
  -H "Content-Type: application/json" \
  -d '{
    "length": 6,
    "width": 4,
    "tiles": [
      {"size": 1, "cost": 2},
      {"size": 2, "cost": 3},
      {"size": 3, "cost": 6}
    ]
  }'
```

### Calculate Tiling (Example 2: Large Room)
```bash
curl -X POST http://localhost:5000/calculate \
  -H "Content-Type: application/json" \
  -d '{
    "length": 10,
    "width": 8,
    "tiles": [
      {"size": 1, "cost": 1},
      {"size": 2, "cost": 3.5},
      {"size": 5, "cost": 15}
    ]
  }'
```

---

## 🧪 Python Examples

### Using requests library
```python
import requests
import json

API_URL = "http://localhost:5000/calculate"

payload = {
    "length": 6,
    "width": 4,
    "tiles": [
        {"size": 1, "cost": 2},
        {"size": 2, "cost": 3},
        {"size": 3, "cost": 6}
    ]
}

response = requests.post(API_URL, json=payload)
result = response.json()

print(f"Total Cost: ${result['total_cost']}")
print(f"Visualization:\n{result['visualization']}")
```

### Direct Python calculation (without API)
```python
from backend.app import TilingCalculator

# Create calculator
calc = TilingCalculator(
    length=6,
    width=4,
    tiles=[(1, 2), (2, 3), (3, 6)]  # (size, cost) tuples
)

# Generate solutions
result = calc.generate_solutions()

# Access results
print(f"Best solution: {result['best_solution']}")
print(f"Best cost: {result['best_cost']}")
print(f"Visualization:\n{calc.get_ascii_visualization(result['best_layout'])}")
```

---

## 🌐 JavaScript Fetch Examples

### Basic Fetch
```javascript
const payload = {
  length: 6,
  width: 4,
  tiles: [
    { size: 1, cost: 2 },
    { size: 2, cost: 3 },
    { size: 3, cost: 6 }
  ]
};

fetch('http://localhost:5000/calculate', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(payload)
})
.then(response => response.json())
.then(data => {
  console.log('Total Cost:', data.total_cost);
  console.log('Visualization:', data.visualization);
})
.catch(error => console.error('Error:', error));
```

### Async/Await Example
```javascript
async function calculateTiling(length, width, tiles) {
  try {
    const response = await fetch('http://localhost:5000/calculate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ length, width, tiles })
    });
    
    const data = await response.json();
    
    if (data.status === 'success') {
      return data;
    } else {
      throw new Error(data.message);
    }
  } catch (error) {
    console.error('Calculation failed:', error);
  }
}

// Usage
const result = await calculateTiling(6, 4, [
  { size: 1, cost: 2 },
  { size: 2, cost: 3 },
  { size: 3, cost: 6 }
]);
```

---

## 📋 Test Cases

### Test Case 1: Simple Perfect Fit
```json
{
  "length": 4,
  "width": 4,
  "tiles": [
    {"size": 2, "cost": 10}
  ]
}
```
Expected: 4 tiles, cost = $40

### Test Case 2: Mixed Tiles
```json
{
  "length": 10,
  "width": 10,
  "tiles": [
    {"size": 1, "cost": 1},
    {"size": 2, "cost": 3},
    {"size": 5, "cost": 20}
  ]
}
```
Expected: Multiple solutions, max cost depends on combination

### Test Case 3: Large Room
```json
{
  "length": 100,
  "width": 100,
  "tiles": [
    {"size": 10, "cost": 100},
    {"size": 25, "cost": 500},
    {"size": 50, "cost": 1500}
  ]
}
```
Expected: Solution using largest most expensive tiles

### Test Case 4: Decimal Values
```json
{
  "length": 5.5,
  "width": 3.5,
  "tiles": [
    {"size": 1.5, "cost": 2.5},
    {"size": 2.5, "cost": 5.0}
  ]
}
```
Expected: Handles floating point dimensions

---

## ⚙️ Environment Variables

Create a `.env` file in the backend folder (optional):

```env
FLASK_ENV=development
FLASK_DEBUG=1
FLASK_PORT=5000
CORS_ORIGINS=http://localhost:3000,http://localhost:8000
```

Then load in app.py:
```python
import os
from dotenv import load_dotenv

load_dotenv()

port = int(os.getenv('FLASK_PORT', 5000))
app.run(debug=True, port=port)
```

---

## 🔐 Security Considerations

### Input Validation
```python
# Already implemented in app.py
- Check all values are positive numbers
- Check values are reasonable (< 10000)
- Sanitize input strings
```

### Production Deployment
```python
# Disable debug mode
app.run(debug=False)

# Set CORS restrictions
CORS(app, resources={
    r"/calculate": {"origins": ["https://yourdomain.com"]}
})

# Add rate limiting
from flask_limiter import Limiter
limiter = Limiter(app)

@app.route('/calculate', methods=['POST'])
@limiter.limit("10 per minute")
def calculate():
    ...
```

---

## 📊 Response Examples

### Example 1: Successful Calculation
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
  "visualization": "222222222222\n222222222222\n222222222222\n222222222222"
}
```

### Example 2: Error Response
```json
{
  "status": "error",
  "message": "Please fill in all dimensions"
}
```

---

**For more help, check README.md or QUICKSTART.md** 📚

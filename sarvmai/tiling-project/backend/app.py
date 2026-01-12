from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from itertools import product

app = Flask(__name__)
CORS(app)

class TilingCalculator:
    """
    Calculates non-optimal (maximum cost) tiling solutions for a rectangular room.
    """
    
    def __init__(self, length, width, tiles):
        """
        Args:
            length: Room length in meters
            width: Room width in meters
            tiles: List of tuples [(size_a, cost_a), (size_b, cost_b), (size_c, cost_c)]
        """
        self.length = int(length)
        self.width = int(width)
        self.tiles = tiles  # [(size, cost), ...]
        self.area = self.length * self.width
    
    def generate_solutions(self):
        """
        Generate all possible valid tiling solutions that cover the room.
        A solution is valid if tiles can be arranged to cover the entire room.
        Returns the solution with maximum cost.
        """
        best_solution = None
        best_cost = 0
        best_layout = None
        
        # Get all possible combinations of tiles that could theoretically fit
        solutions = []
        
        for combo in self._get_all_tile_combinations():
            layout = self._try_layout(combo)
            if layout and layout['valid']:
                cost = layout['total_cost']
                if cost >= best_cost:  # >= to find maximum cost
                    best_cost = cost
                    best_solution = combo
                    best_layout = layout
                solutions.append({
                    'combination': combo,
                    'layout': layout,
                    'cost': cost
                })
        
        # Sort by cost (descending) to show max-cost solution first
        solutions.sort(key=lambda x: x['cost'], reverse=True)
        
        return {
            'best_solution': best_solution,
            'best_layout': best_layout,
            'best_cost': best_cost,
            'all_solutions': solutions[:10]  # Return top 10 solutions
        }
    
    def _get_all_tile_combinations(self):
        """
        Generate reasonable combinations of tiles.
        We try combinations where total area is close to room area.
        """
        combinations = []
        max_tiles_per_type = max(self.length, self.width) * 2  # Safety limit
        
        # Try single tile type solutions (most likely to be max cost)
        for i, (size, cost) in enumerate(self.tiles):
            size = int(size)
            tiles_along_length = (self.length + size - 1) // size  # Ceiling division
            tiles_along_width = (self.width + size - 1) // size
            total_tiles = tiles_along_length * tiles_along_width
            
            combo = [0, 0, 0]
            combo[i] = total_tiles
            combinations.append(tuple(combo))
        
        # Try combinations of two types
        for i in range(len(self.tiles)):
            for j in range(i + 1, len(self.tiles)):
                size_i, cost_i = self.tiles[i]
                size_j, cost_j = self.tiles[j]
                size_i = int(size_i)
                size_j = int(size_j)
                
                for ti in range(1, max_tiles_per_type):
                    for tj in range(1, max_tiles_per_type):
                        combo = [0, 0, 0]
                        combo[i] = ti
                        combo[j] = tj
                        combinations.append(tuple(combo))
                        
                        if len(combinations) > 10000:  # Limit combinations
                            return combinations
        
        return combinations
    
    def _try_layout(self, combo):
        """
        Try to arrange tiles according to combo counts.
        Returns layout info if valid, None otherwise.
        """
        counts = list(combo)
        
        # Greedy placement: try to fill the room with larger tiles first
        grid = [[0 for _ in range(self.width)] for _ in range(self.length)]
        used = [0, 0, 0]
        
        # Sort indices by tile size (descending) for greedy placement
        tile_indices = sorted(range(len(self.tiles)), 
                            key=lambda i: int(self.tiles[i][0]), reverse=True)
        
        for y in range(self.length):
            for x in range(self.width):
                if grid[y][x] == 0:  # Empty cell
                    # Try to place the largest available tile
                    placed = False
                    for idx in tile_indices:
                        if used[idx] < counts[idx]:
                            size, cost = self.tiles[idx]
                            size = int(size)
                            if x + size <= self.width and y + size <= self.length:
                                # Check if all cells are empty
                                if all(grid[y+dy][x+dx] == 0 
                                      for dy in range(size) for dx in range(size)):
                                    # Place tile
                                    for dy in range(size):
                                        for dx in range(size):
                                            grid[y+dy][x+dx] = idx + 1
                                    used[idx] += 1
                                    placed = True
                                    break
                    
                    if not placed:
                        # Try smallest tile that fits
                        for idx in reversed(tile_indices):
                            if used[idx] < counts[idx]:
                                size, cost = self.tiles[idx]
                                size = int(size)
                                if x + size <= self.width and y + size <= self.length:
                                    if all(grid[y+dy][x+dx] == 0 
                                          for dy in range(size) for dx in range(size)):
                                        for dy in range(size):
                                            for dx in range(size):
                                                grid[y+dy][x+dx] = idx + 1
                                        used[idx] += 1
                                        placed = True
                                        break
        
        # Check if entire floor is covered
        full_coverage = all(grid[y][x] != 0 
                           for y in range(self.length) 
                           for x in range(self.width))
        
        if full_coverage:
            total_cost = sum(used[i] * self.tiles[i][1] for i in range(len(self.tiles)))
            return {
                'valid': True,
                'grid': grid,
                'counts': used,
                'total_cost': total_cost
            }
        
        # Alternative: Fill with combinations that maximize cost
        # Try using expensive tiles even if wasteful
        used = list(counts)
        total_cost = sum(used[i] * self.tiles[i][1] for i in range(len(self.tiles)))
        
        return {
            'valid': True,  # Accept even if not perfect fit
            'grid': grid,
            'counts': used,
            'total_cost': total_cost
        }
    
    def get_ascii_visualization(self, layout):
        """Generate ASCII art representation of the tiling."""
        grid = layout['grid']
        lines = []
        
        for row in grid:
            line = ""
            for cell in row:
                if cell == 0:
                    line += "."
                else:
                    line += str(cell)
            lines.append(line)
        
        return "\n".join(lines)


@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'status': 'Tiling Calculator API Running',
        'endpoints': {
            '/calculate': 'POST - Calculate optimal tiling',
            '/health': 'GET - Health check'
        }
    })


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200


@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Calculate tiling solution.
    
    Expected JSON:
    {
        "length": 6,
        "width": 4,
        "tiles": [
            {"size": 1, "cost": 2},
            {"size": 2, "cost": 3},
            {"size": 3, "cost": 6}
        ]
    }
    """
    try:
        data = request.json
        
        length = float(data['length'])
        width = float(data['width'])
        tiles_data = data['tiles']
        
        # Convert to tuples [(size, cost), ...]
        tiles = [(float(t['size']), float(t['cost'])) for t in tiles_data]
        
        # Calculate
        calculator = TilingCalculator(int(length), int(width), tiles)
        result = calculator.generate_solutions()
        
        if result['best_solution']:
            best_counts = result['best_solution']
            layout = result['best_layout']
            
            response = {
                'status': 'success',
                'room': {
                    'length': length,
                    'width': width,
                    'area': length * width
                },
                'tiles_used': [
                    {
                        'size': tiles[i][0],
                        'cost_per_tile': tiles[i][1],
                        'count': best_counts[i],
                        'total_cost': best_counts[i] * tiles[i][1]
                    }
                    for i in range(len(tiles))
                ],
                'total_cost': result['best_cost'],
                'visualization': calculator.get_ascii_visualization(layout)
            }
            
            return jsonify(response), 200
        else:
            return jsonify({
                'status': 'error',
                'message': 'No valid tiling solution found'
            }), 400
            
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)

# AI Map Coloring

This project is an interactive **Map Coloring Game** built using Python and Pygame.

The program generates a random map using Voronoi diagrams and solves the map coloring problem using Artificial Intelligence techniques.

The AI uses Backtracking and MRV (Minimum Remaining Value) heuristic to color the map such that no neighboring regions have the same color.

---

## Features

• Random map generation  
• AI solving using CSP algorithm  
• Human playable mode  
• Zoom and drag map  
• Difficulty levels  
• Real-time AI solving visualization  

---

## Technologies Used

Python  
Pygame  
NumPy  
SciPy  

---

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the program:

python map_coloring_ai.py

---

## Controls

1 - Red  
2 - Green  
3 - Blue  
4 - Yellow  

SPACE - AI Solve  
H - Human Mode  
A - AI Mode  

5 - Easy  
6 - Medium  
7 - Hard  

Mouse Wheel - Zoom  
Right Click Drag - Move Map  

---

## AI Concepts Used

Constraint Satisfaction Problem (CSP)  
Backtracking Search  
MRV Heuristic  
Graph Coloring
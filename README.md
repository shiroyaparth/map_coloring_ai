
# 🎨 AI Map Coloring using Pygame

An interactive Python project that demonstrates **Artificial Intelligence concepts** using a **Map Coloring problem**.
The system generates random maps and solves them using an AI algorithm based on **Backtracking + MRV (Minimum Remaining Values) heuristic**.

---

## 🚀 Project Overview

This project simulates the classic **Map Coloring Problem**, where:

* A map is divided into multiple regions
* Each region must be colored
* **No two adjacent regions can have the same color**

The project supports:

* 🤖 AI-based automatic solving
* 🧑 Human interactive coloring
* 🔍 Zoom & drag map navigation
* 🎯 Difficulty levels

---

## 🧠 AI Concepts Used

* **Backtracking Algorithm**
* **MRV Heuristic (Minimum Remaining Values)**
* Constraint Satisfaction Problem (CSP)
* Graph-based neighbor relationships

---

## 🗺️ How It Works

1. Random points are generated
2. A **Voronoi diagram** is created (map regions)
3. Neighbor relationships are calculated
4. AI assigns colors while satisfying constraints:

   * No neighboring regions share the same color

---

## 🎮 Features

* 🎨 4-color map coloring (Red, Green, Blue, Yellow)
* 🤖 AI Solver with step visualization
* 🧑 Manual play mode
* 🔍 Zoom in/out using mouse wheel
* 🖱️ Drag map using right click
* ⚙️ Difficulty levels:

  * Easy
  * Medium
  * Hard
* ⏱️ Time tracking (AI vs Human)
* 📊 Step counter for AI

---

## 🎹 Controls

| Key              | Action               |
| ---------------- | -------------------- |
| 1-4              | Select color         |
| SPACE            | Run AI Solver        |
| H                | Switch to Human Mode |
| A                | Switch to AI Mode    |
| R                | Reset current map    |
| N                | Generate new map     |
| 5                | Easy difficulty      |
| 6                | Medium difficulty    |
| 7                | Hard difficulty      |
| Mouse Wheel      | Zoom                 |
| Right Click Drag | Move map             |

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

### Required Libraries:

* pygame
* numpy
* scipy

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧪 Example Workflow

1. Start the program
2. Choose:

   * Human mode → manually color regions
   * AI mode → press SPACE to auto solve
3. Watch how AI fills the map step-by-step
4. Compare AI time vs your time 😄

---

## 📁 Project Structure

```
AI-Map-Coloring/
│
├── main.py
├── requirements.txt
├── README.md
```

---

## 💡 Future Improvements

* Forward Checking algorithm
* Arc Consistency (AC-3)
* Better UI/animations
* Save & load maps
* More color options

---

## 🎯 Learning Outcome

This project helps in understanding:

* Constraint Satisfaction Problems (CSP)
* Heuristic optimization techniques
* Real-world application of AI
* Visualization of algorithms

---

## 🙌 Conclusion

This project is a great combination of:

* 🎮 Interactive UI (Pygame)
* 🧠 AI Algorithms
* 📊 Problem-solving logic

Perfect for **students, mini-projects, and portfolio showcase** 🚀

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub and share it!

---

# 🌊 Hydrofoil Flow Visualizer

An interactive physics application to simulate and visualize **2D potential flow over a hydrofoil**. This project dynamically demonstrates fundamental aerodynamics and fluid mechanics concepts like **streamlines, stagnation points, lift generation via circulation, and conformal mapping**.

---

## 🚀 Features

* 🌊 **Real-time streamline animation** of fluid flow via a high-performance interactive particle system.
* ✈️ **Joukowski Transformation**: Analytically maps classical cylinder flows into a true asymmetrical hydrofoil wing geometry.
* 🔄 Adjustable **Circulation (Γ)** to simulate pressure differentials and aerodynamic vertical lift.
* 🎯 Automatic mathematical tracking of shifting **Stagnation Points**.
* 🖱️ **Kinematic Drag Interaction**: Click and drag the hydrofoil in real-time, instantly shifting apparent wind vectors while perfectly preserving solid-boundary irrotational flow restrictions.
* 🎛️ Complete UI parameter controls (Velocity, Angle of attack, Scale, Stream density, Resolution).
* 🌓 Sleek, responsive UI with **Dark / Light theme** toggling.

---

## 🧠 Concepts Covered

* Potential Flow Theory & Irrotational Physics
* Superposition Principle (Uniform Flow + Doublet + Vortex)
* Conformal Mapping (Joukowski Equation)
* Circulation and the Kutta-Joukowski Lift Theorem
* Apparent Wind & Frame-of-Reference Physics Transformations

---

## ⚙️ Tech Stack

* **High-Speed Web Simulator**: Pure HTML5, CSS3, Vanilla JavaScript Canvas (No backend required)
* **Mathematical Reference Script**: Python (NumPy, Matplotlib)

---

## 🎮 User Inputs

Users can precisely control the simulation parameters:

* 🌊 Free Stream Velocity (`U∞`)
* 🔄 Circulation (`Γ`)
* 📐 Hydrofoil Scale/Radius (`R`)
* 🌀 Flow Direction Angle (`α`)
* 🧵 Streamline Density & Grid Resolution
* 🎯 Stagnation Points & Themes (Toggles)

---

## 🛠️ Installation & Setup

### Web Visualizer (Recommended)
Because the simulator is built entirely on the client, no server is required:
1. Clone the repository
2. Simply double-click on `hydrofoil_visualization.html` to open it natively in any modern web browser!

### Python Simulator (Optional)
If you wish to view the static matplotlib reference script:
1. Ensure Python 3 is installed.
2. Install dependencies:
```bash
pip install numpy matplotlib
```
3. Run the application:
```bash
python anti_gravity_hydrofoil.py
```

---

## 📂 Project Structure

```
hydrofoil-flow-visualizer/
│── anti_gravity_hydrofoil.py       # Python mathematical flow visualization logic
│── hydrofoil_visualization.html    # Full interactive web simulation (Frontend, JS Physics, & UI)
│── README.md
```

---

## 🎯 Objective

This project aims to provide an **interactive and highly visual understanding of advanced fluid flow behaviors** around aerospace bodies. It helps students, engineers, and learners grasp key aerodynamics principles like lift, stagnation shifting, and circulation without requiring a fluid dynamics lab.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request for new physics integrations or features.

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

**Rupam Halder**

---

⭐ *If you found this project useful, consider giving it a star!*

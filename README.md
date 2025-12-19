# Numerical Integration Methods in Python

**Numerical Integration Methods** is a Python project that demonstrates how to approximate definite integrals using the **Rectangular Method** and **Trapezoidal Method**. These methods are foundational in numerical analysis and are widely used in scientific computing, engineering, and data analysis.

---

## 📌 Table of Contents
- [Introduction](#introduction)
- [Methods](#methods)
  - [Rectangular Method](#rectangular-method)
   - [Trapezoidal Method](#trapezoidal-method)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

---

## 📊 Introduction
Numerical integration is a technique used to approximate the value of a definite integral when an analytical solution is difficult or impossible to obtain. This project provides Python implementations of two popular numerical integration methods:

1. **Rectangular Method**: Uses rectangles to approximate the area under a curve.
2. **Trapezoidal Method**: Uses trapezoids to approximate the area under a curve.

These methods are particularly useful for integrating complex functions or data sets where traditional calculus techniques are not feasible.

---

## 🔧 Methods

---

### Rectangular Method
The Rectangular Method approximates the integral by dividing the area under the curve into rectangles and summing their areas.

- **Formula**:
  \[
  \int_{a}^{b} f(x) \,dx \approx \Delta x \sum_{i=1}^{n} f(x_i^*)
  \]
  where \( x_i^* \) is the midpoint of each subinterval.

- **Use Case**: Simple and easy to implement, but generally less accurate compared to other methods like the Trapezoidal or Simpson's Rule.

---

### Trapezoidal Method
The Trapezoidal Method approximates the integral by dividing the area under the curve into trapezoids and summing their areas. This method is more accurate than the Rectangular Method because it accounts for the slope of the function between points.

- **Formula**:
  \[
  \int_{a}^{b} f(x) \,dx \approx \frac{\Delta x}{2} \left[ f(x_0) + 2 \sum_{i=1}^{n-1} f(x_i) + f(x_n) \right]
  \]
  where:
  - \( \Delta x \) is the width of each subinterval.
  - \( f(x_0) \) and \( f(x_n) \) are the function values at the endpoints of the interval.
  - \( f(x_i) \) are the function values at intermediate points.

- **Steps**:
  1. Divide the interval \([a, b]\) into \( n \) equal subintervals.
  2. Calculate the width of each subinterval, \( \Delta x = \frac{b-a}{n} \).
  3. Evaluate the function at each endpoint and intermediate point.
  4. Apply the Trapezoidal Rule formula to approximate the integral.

- **Use Case**: The Trapezoidal Method is more accurate than the Rectangular Method, especially for smooth functions. It is widely used in scientific computing and engineering applications.

---

## 🛠 Installation
To run this project, you need Python 3.x and the NumPy library. You can install NumPy, Pandas, Matplotlib and scikit-learn using pip:

```bash
pip install numpy
pip install pandas
pip install matplotlib
pip install Scikit-Learn
```

## 🚀 Usage

1. Clone this repository or download the script.
2. Run the script in a Python environment.
3. Enter the number of points (`n`) when prompted.

```python
# Example usage
n = int(input("Enter total number of points: "))
rectangular_method(n)
trapezoidal_method(n)
```

## ⚙ How It Works

Rectangular Method

1. Divides the interval ([0, \pi]) into (n) equal subintervals.
2. Calculates the midpoint of each subinterval.
3. Computes the area of each rectangle using the function value at the midpoint.
4. Sums the areas of all rectangles to approximate the integral.
5. Trapezoidal Method

Trapezoidal Method

1. Divides the interval ([0, \pi]) into (n) equal subintervals.
2. Uses the function values at the endpoints of each subinterval.
3. Computes the area of each trapezoid.
4. Sums the areas of all trapezoids to approximate the integral.

## 📈 Results

The accuracy of the approximation improves with a higher number of points (n).
The interval for integration is fixed from (0) to (\pi) in both methods.

## 🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

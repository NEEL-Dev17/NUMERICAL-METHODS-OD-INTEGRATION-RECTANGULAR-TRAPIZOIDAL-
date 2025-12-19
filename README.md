# Numerical Integration Methods

This repository contains Python implementations of two numerical integration methods:
1. **Rectangular Method** for integrating `x * sin(sin(x))`
2. **Trapezoidal Method** for integrating `3x² + 2x`

---

## Table of Contents
- [Introduction](#introduction)
- [Methods](#methods)
  - [Rectangular Method](#rectangular-method)
  - [Trapezoidal Method](#trapezoidal-method)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [How It Works](#how-it-works)
- [Example](#example)

---

## Introduction
Numerical integration is a method to approximate the value of a definite integral. This repository provides simple Python implementations of the Rectangular and Trapezoidal methods for numerical integration.

---

## Methods

### Rectangular Method
- Approximates the integral by summing the areas of rectangles under the curve.
- Uses midpoints of subintervals to calculate the height of each rectangle.

### Trapezoidal Method
- Approximates the integral by summing the areas of trapezoids under the curve.
- Uses the average of the function values at the endpoints of each subinterval.

---

## Usage
1. Clone this repository or download the script.
2. Run the script in a Python environment.
3. Enter the number of points when prompted.

---

## Dependencies
- Python 3.x
- NumPy

You can install NumPy using pip:
```bash
pip install numpy
```

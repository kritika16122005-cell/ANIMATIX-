# manim-genai-assignment

AI-Generated Manim Animations using Google Gemini API.

## Project Overview
Used Gemini API to generate Manim animation code for:
1. Pythagorean Theorem visualisation
2. Fourier Series Square Wave Decomposition

## Files
- `pythagoras.py` - Manim scene for Pythagorean Theorem
- `fourier_series.py` - Manim scene for Fourier Series
- `PythagoreanTheorem.mp4` - Rendered video
- `FourierSeries.mp4` - Rendered video

## How to Run
Install dependencies:
pip install manim

Run scenes:
manim -pql pythagoras.py PythagoreanTheorem
manim -pql fourier_series.py FourierSeries

## Critical Analysis
### Pythagorean Theorem - 5 Shortcomings
1. Hardcoded vertex coordinates - not scalable to other triangles
2. Square on side a extends in wrong direction for some configurations
3. Side labels use temporary Line object - fragile positioning
4. Missing wait() calls - animation feels rushed
5. Area labels may overlap triangle for small squares

 ## Assignment 2 - Task 2: Project Feedback & Ideas

1. **Interactive Parameter Control** - Allow users to input custom triangle sides (a, b) and watch the animation update in real time.
2. **3D Visualisation** - Extend the Fourier series into 3D using Manim's ThreeDScene to show frequency domain representation.
3. **Step-by-step Proof Overlay** - Add text overlays explaining each step of the proof as the animation plays.
4. **Comparison Mode** - Show LLM-generated code vs fixed code side by side to highlight improvements.
5. **More Theorems** - Extend the project to visualise other theorems like Euler's Identity or Taylor Series.
### Fourier Series - 5 Shortcomings
1. Y-axis range ignores Gibbs phenomenon overshoot (~9%)
2. Higher harmonics too small to see - no amplitude scaling
3. Legend parent group never added to scene - layout bug
4. Transform targets wrong object using self.mobjects[-1]
5. No target square wave shown - convergence not visible

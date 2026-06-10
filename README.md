# AI-Powered Productivity Tracker 🚀

A real-time behavioral analytics tool that uses Computer Vision and Machine Learning to track focus, detect drowsiness, and generate detailed productivity reports.

## 🧠 Project Overview
This project transforms a standard webcam feed into a productivity engine. By analyzing 478 3D facial landmarks, the system distinguishes between deep work and various distractions (looking down, head turned, drowsiness) to help users optimize their "flow state."

## 🛠️ Tech Stack
- **Languages:** Python
- **Computer Vision:** MediaPipe (Face Mesh), OpenCV
- **Machine Learning:** Scikit-learn (Random Forest), XGBoost
- **Data:** NumPy, Pandas, JSON

## ✨ Key Features
- **478 3D Landmark Extraction:** High-fidelity tracking of facial biomechanics.
- **Geometric Normalization:** Uses zero-centering and scale invariance to ensure accuracy regardless of camera distance or lighting.
- **70% Confidence Gate:** Logic layer that prevents "flickering" by requiring high model certainty before changing states.
- **Automated Analytics:** Generates session-based JSON reports calculating a final Productivity Score.

## 📊 Productivity Logic
The system calculates your efficiency using the following formula:

$$Productivity\ Score = \left( \frac{Time\ Spent\ Focused}{Total\ Session\ Time} \right) \times 100$$

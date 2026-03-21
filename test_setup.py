import cv2 as cv
import mediapipe as mp

print("--- Version Check ---")
print(f"OpenCV: {cv.__version__}")
print(f"MediaPipe: {mp.__version__}")

# Test the Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
print("\nSuccess! The libraries are finally talking to each other.")
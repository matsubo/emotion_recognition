import cv2
import face_recognition
from deepface import DeepFace
import numpy as np

def process_video(video_path):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    
    # Get video properties
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    
    emotions = []
    
    for frame_number in range(frame_count):
        # Read a frame from the video
        success, frame = video.read()
        if not success:
            break
        
        # Convert the image from BGR color (which OpenCV uses) to RGB color
        rgb_frame = frame[:, :, ::-1]
        
        # Find all the faces in the frame
        face_locations = face_recognition.face_locations(rgb_frame)
        
        for face_location in face_locations:
            # Extract the face ROI
            top, right, bottom, left = face_location
            face_image = frame[top:bottom, left:right]
            
            # Perform emotion recognition
            try:
                result = DeepFace.analyze(face_image, actions=['emotion'], enforce_detection=False)
                dominant_emotion = result[0]['dominant_emotion']
                emotions.append(dominant_emotion)
            except Exception as e:
                print(f"Error in emotion detection: {str(e)}")
        
        # Process every 5th frame to reduce computation (adjust as needed)
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_number + 5)
    
    video.release()
    
    # Analyze emotions
    if emotions:
        emotion_counts = {emotion: emotions.count(emotion) for emotion in set(emotions)}
        dominant_video_emotion = max(emotion_counts, key=emotion_counts.get)
        print(f"Dominant emotion in the video: {dominant_video_emotion}")
        print(f"Emotion distribution: {emotion_counts}")
    else:
        print("No emotions detected in the video.")

# Usage
video_path = 'trim.mp4'
process_video(video_path)
import cv2
import face_recognition
from deepface import DeepFace
import json
import os
import sys

def process_video(video_path):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    
    # Get video properties
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    
    emotions_data = []
    
    for frame_number in range(0, frame_count, 5):  # Process every 5th frame
        # Set the frame position
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        
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
                
                # Calculate the time in seconds
                time_in_seconds = frame_number / fps
                
                # Append the emotion data
                emotions_data.append({
                    "time": time_in_seconds,
                    "emotion": dominant_emotion
                })
            except Exception as e:
                print(f"Error in emotion detection at frame {frame_number}: {str(e)}")
    
    video.release()
    
    # Save emotions data to JSON file
    # Print emotions data to standard output
    print(json.dumps(emotions_data, ensure_ascii=False, indent=4))

# Usage
if len(sys.argv) < 2:
    print("Please provide the video file path as an argument.")
    sys.exit(1)

video_path = sys.argv[1]
process_video(video_path)

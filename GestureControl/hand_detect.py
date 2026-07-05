import cv2
import mediapipe as mp
import math
from volume_control import VolumeController
from brightness_control import BrightnessController

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# -----------------------------
# Load Model
# -----------------------------
base_options = python.BaseOptions(
    model_asset_path="models/hand_landmarker.task"
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=2
)

detector = vision.HandLandmarker.create_from_options(options)
# Create Volume Controller
volume_controller = VolumeController()
brightness_controller = BrightnessController()
mode = "volume"

print("✅ Hand Landmarker created successfully!")

# -----------------------------
# Camera
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not found!")
    exit()

# Hand Connections
connections = [
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (5,9),(9,10),(10,11),(11,12),
    (9,13),(13,14),(14,15),(15,16),
    (13,17),(17,18),(18,19),(19,20),
    (0,17)
]

tips=[4,8,12,16,20]

while True:

    success, frame = cap.read()

    if not success:
        break

    frame=cv2.flip(frame,1)

    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    mp_image=mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    result=detector.detect(mp_image)

    h,w,_=frame.shape

    if result.hand_landmarks:

        for hand in result.hand_landmarks:

            # Draw all landmarks
            for point in hand:

                x=int(point.x*w)
                y=int(point.y*h)

                cv2.circle(frame,(x,y),5,(0,255,0),-1)

            # Draw Skeleton
            for start,end in connections:

                x1=int(hand[start].x*w)
                y1=int(hand[start].y*h)

                x2=int(hand[end].x*w)
                y2=int(hand[end].y*h)

                cv2.line(frame,(x1,y1),(x2,y2),(255,0,0),2)

            # Fingertips
            for tip in tips:

                x=int(hand[tip].x*w)
                y=int(hand[tip].y*h)

                cv2.circle(frame,(x,y),10,(0,0,255),-1)

            # --------------------------
            # Thumb & Index Distance
            # --------------------------

            thumb_x=int(hand[4].x*w)
            thumb_y=int(hand[4].y*h)

            index_x=int(hand[8].x*w)
            index_y=int(hand[8].y*h)

            cv2.line(
                frame,
                (thumb_x,thumb_y),
                (index_x,index_y),
                (0,255,255),
                3
            )

            distance=math.hypot(
                index_x-thumb_x,
                index_y-thumb_y
            )
            if mode == "volume":
                percentage = volume_controller.set_volume(distance)
            else:
                percentage = brightness_controller.set_brightness(distance)
                
            cv2.putText(
                frame,
                f"Distance : {int(distance)}",
                (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,255),
                2
            )
            cv2.putText(
                frame,
                f"{mode.title()} : {percentage}%",
                (20,80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2
            )
            cv2.putText(
                frame,
                "Press V = Volume | B = Brightness",
                (20,120),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255,255,255),
                2
            )
            cv2.putText(
                frame,
                f"Mode : {mode.upper()}",
                (20,160),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255,255,0),
                2
            )
            

    cv2.imshow("AI Hand Detection",frame)

    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('v'):
        mode = "volume"

    elif key == ord('b'):
        mode = "brightness"

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

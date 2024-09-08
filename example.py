import cv2
from viewer import AndroidViewer

# This will deploy and run server on android device connected to USB
android = AndroidViewer(adb_path='/opt/homebrew/bin/adb')

while True:
    frames = android.get_next_frames()
    if frames is None:
        continue
    
    for frame in frames:
        cv2.imshow('game', frame)
        cv2.waitKey(1)
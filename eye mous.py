import cv2
import mediapipe as mp
import pyautogui
cam=cv2.VideoCapture(0)
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)
screen_w,screen_h=pyautogui.size()
while True:
    _ , frame=cam.read()
    frame=cv2.flip(frame,1)
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=face_mesh.process(rgb_frame)
    Landmark_points = output.multi_face_landmarks
    frame_h,frame_w,_ = frame.shape
    if Landmark_points:
        Landmarks = Landmark_points[0].landmark
        for id,Landmark in enumerate(Landmarks[474:478]):
            x= int(Landmark.x * frame_w)
            y= int(Landmark.y * frame_h)
            cv2.circle(frame,(x,y),3,(30,255,30))
            if id==1:
                screen_x = screen_w/frame_w*x
                screen_y = screen_h/frame_h*y
                pyautogui.moveTo(screen_x,screen_y)
        left=[Landmarks[145],Landmarks[159]]
        for Landmark in left:
            x= int(Landmark.x * frame_w)
            y= int(Landmark.y * frame_h)
            cv2.circle(frame,(x,y),3,(30,255,235))
        if(left[0].y-left[1].y)<0.020:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('Eye Controled Mouse',frame)
    cv2.waitKey(1)



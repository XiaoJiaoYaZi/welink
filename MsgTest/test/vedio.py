import cv2


video_capture = cv2.VideoCapture(0)

while True:
    ret ,frame = video_capture.read()

    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)

    rgb_small_frame = small_frame[:,:,::-1]

    cv2.imshow('monitor',frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()


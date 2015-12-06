import numpy as np
import cv2
cap = cv2.VideoCapture('sample.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold=300,
                                          detectShadows=False)
kernel = np.ones((2, 2), np.uint8)
key = True
print cv2.__version__
ret, frame = cap.read()
while ret:
    # capture dimensions of the video
    dimensions = frame.shape
    fgmask = fgbg.apply(frame)
    cv2.line(frame, ((dimensions[1]/2), (dimensions[0]-450)),
                    ((dimensions[1]/2), dimensions[0]-30),
                    (0, 255, 0), 3, cv2.LINE_8, 0)
    erosion = cv2.erode(fgmask, kernel, iterations=2)
    opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel, iterations=1)
    erosion = cv2.erode(opening, kernel, iterations=1)
    dilation = cv2.dilate(erosion, kernel, iterations=45)
    img, cont, hier = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)
    if len(cont) > 0:
        for quad in cont:
            x, y, w, h = cv2.boundingRect(quad)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.circle(frame, (((w/2)+x), ((h/2)+y)), 3, (0, 255, 0))
    cv2.imshow('frame', fgmask)
    cv2.imshow('original', frame)
    if key:
        print frame.shape
        key = False
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    ret, frame = cap.read()
cap.release()
cv2.destroyAllWindows()

import cv2 as cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
startDist = None
scale = 0
cx, cy = 500, 500
img1 = cv2.imread("cat.png")
img1 = cv2.resize(img1, (250, 250))

while True:
    succ, img = cap.read()
    if not succ:
        break
    hands, img = detector.findHands(img)
    
    if len(hands) == 2:
        if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]
            if startDist is None:
                x1, y1 = lmList1[8][0], lmList1[8][1]
                x2, y2 = lmList2[8][0], lmList2[8][1]
                length, info, img = detector.findDistance((x1, y1), (x2, y2), img)
                startDist = length
            x1, y1 = lmList1[8][0], lmList1[8][1]
            x2, y2 = lmList2[8][0], lmList2[8][1]
            length, info, img = detector.findDistance((x1, y1), (x2, y2), img)
            scale = int(length - startDist) // 2
            cx, cy = info[4:]
    else:
        startDist = None

    h1, w1, _ = img1.shape
    newH, newW = max(2, ((h1 + scale) // 2) * 2), max(2, ((w1 + scale) // 2) * 2)
    resized_img1 = cv2.resize(img1, (newW, newH))

    y1 = max(0, cy - newH // 2)
    y2 = min(img.shape[0], cy + newH // 2)
    x1 = max(0, cx - newW // 2)
    x2 = min(img.shape[1], cx + newW // 2)

    resized_img1 = resized_img1[:y2 - y1, :x2 - x1]

    
    img[y1:y2, x1:x2] = resized_img1
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

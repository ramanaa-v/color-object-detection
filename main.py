import cv2

from PIL import Image

from util import get_limits

target_color = [0, 255, 0] # green in BGR colorspace
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_Limit, upper_Limit = get_limits(color=target_color)

    mask = cv2.inRange(hsvImage, lower_Limit, upper_Limit)

    mask_ = Image.fromarray(mask)

    bounding_box = mask_.getbbox()

    if bounding_box is not None:
        x1, y1, x2, y2 = bounding_box

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)

    print(bounding_box)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
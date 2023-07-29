import cv2
import numpy as np

def detect_red():
    # Access camera
    cam = cv2.VideoCapture(0)

    while True:
        # Read frame
        ret, frame = cam.read()

        # Convert frame from BGR to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Detect redness
        # Make lower mask
        lower_lim = np.array([0,50,50])
        upper_lim = np.array([10,255,255])
        mask1 = cv2.inRange(hsv, lower_lim, upper_lim)

        # make upper mask
        lower_lim = np.array([170,50,50])
        upper_lim = np.array([180,255,255])
        mask2 = cv2.inRange(hsv, upper_lim, lower_lim)

        # combine red masks and apply
        red_mask = mask1+mask2
        mask_apply = cv2.bitwise_and(frame, frame, mask=red_mask)

        # Display original frame and frame with red mask applied (only red detected)
        cv2.imshow("Original", frame)
        cv2.imshow("Only Redness Displayed", mask_apply)

        # Exit when 1 pressed
        if cv2.waitKey(1) & 0xFF == ord("1"):
            break

    # close camera and OpenCV windows
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_red()
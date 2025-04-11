#-----morphological edge detection
import cv2
import numpy as np

def morphological_edge_detection(frame, kernel_size=(3, 3)):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Create a structuring element (kernel)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)

    # Apply dilation and erosion
    dilated = cv2.dilate(gray, kernel, iterations=1)
    eroded = cv2.erode(gray, kernel, iterations=1)

    # Compute the morphological gradient
    gradient = cv2.absdiff(dilated, eroded)

    # Normalize the gradient to [0, 255] for display
    gradient = cv2.normalize(gradient, None, 0, 255, cv2.NORM_MINMAX)

    return gradient

def main():
    # Open the camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to access camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture frame.")
            break

        # Apply morphological edge detection
        edges = morphological_edge_detection(frame)

        # Display the result
        cv2.imshow("Morphological Edge Detection", edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

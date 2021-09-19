import cv2
import numpy as np


class MotionDetector:

    def transform_to_binary(self, frame):
        # Blur frame
        blur = cv2.GaussianBlur(frame, (11, 11), 0)
        # Transform to binary
        _, binary = cv2.threshold(blur, 15, 255, cv2.THRESH_BINARY)

        return binary

    def clean_frame(self, frame):
        # Init frame and kernel
        transformations_frame = frame
        circle_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

        # Morphological Transformations
        transformations_frame = cv2.morphologyEx(transformations_frame, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
        transformations_frame = cv2.morphologyEx(transformations_frame, cv2.MORPH_CLOSE, circle_kernel)
        transformations_frame = cv2.dilate(transformations_frame, circle_kernel, iterations=3)

        return transformations_frame

    def get_frame_diff(self, current_frame, previous_frame):
        # Convert to gray scale
        current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
        previous_frame_gray = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)
        # Get bitwise difference between frames
        frame_diff = cv2.absdiff(current_frame_gray, previous_frame_gray)

        return frame_diff

    def get_object_boxes(self, frame):
        # Find contours in binary frame
        contours, _ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Reset motion boxes
        boxes = []

        # Run over all contours and save as boxes
        for contour in contours:
            rect = (cv2.minAreaRect(contour))
            boxes.append(np.int0(cv2.boxPoints(rect)))

        return boxes

    def find_motion_rects(self, current_frame, previous_frame, result_frame):
        # Get frame difference
        frame_diff = self.get_frame_diff(current_frame, previous_frame)

        # Make differance frame to binary
        binary_frame = self.transform_to_binary(frame_diff)

        # Use morphological transformations to clean noise
        clean_binary_frame = self.clean_frame(binary_frame)

        # Get bounding boxes 
        boxes = self.get_object_boxes(clean_binary_frame)

        return boxes

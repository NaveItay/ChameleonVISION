import cv2
import numpy as np
from .helper import *
import time
# import keyboard

WEIGHT_OF_SCREEN = 1274
HEIGHT_OF_SCREEN = 720
threshold_jump = 10


class FieldDetection:

    #   *** Dynamic field thresholds ***    #
    img_flag = True

    # img thresholds field
    img_path = '/home/chameleonvision/Desktop/FinalProject/ChameleonVISION/assets/threshhold_field.jpeg'
    field_img = cv2.imread(img_path)
    img = np.zeros((1274, 720, 3), dtype=np.uint8)
    field_img = cv2.resize(field_img, (int(field_img.shape[1] / 2), int(field_img.shape[0] / 2)),
                           interpolation=cv2.INTER_AREA)
    img[0:360, 0:655] = field_img

    circles = []
    x_click = 0
    y_click = 0
    mode = None

    # Left line
    LL = int(WEIGHT_OF_SCREEN * 0.1)  # left threshold of left line
    RL = int(WEIGHT_OF_SCREEN * 0.3)  # right threshold of left line

    # Net Line
    LN = int(WEIGHT_OF_SCREEN * 0.35)  # left threshold of net
    RN = int(WEIGHT_OF_SCREEN * 0.65)  # right threshold of net

    # Right line
    LR = int(WEIGHT_OF_SCREEN * 0.8)  # left threshold of right line
    RR = int(WEIGHT_OF_SCREEN * 0.95)  # right threshold of right line

    # Up line
    UT = int(HEIGHT_OF_SCREEN * 0.1)  # up threshold of top line
    DT = int(HEIGHT_OF_SCREEN * 0.35)  # down threshold of top line

    # Bottom Line
    UB = int(HEIGHT_OF_SCREEN * 0.7)  # up threshold of Bottom line
    DB = int(HEIGHT_OF_SCREEN * 0.95)  # down threshold of Bottom line

    UpLine = None
    LeftLine = None
    DownLine = None
    RightLine = None
    NetLine = None
    field_center = None

    LeftUp = None
    LeftDown = None
    RightUp = None
    RightDown = None

    field_contour = None
    Gamma_Min = 51

    def init_frame(self, frame):
        current_frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Threshold
        res, binary = cv2.threshold(current_frame_gray, self.Gamma_Min, 255, cv2.THRESH_BINARY)
        # Canny algorithm
        edges = cv2.Canny(binary, 1, 255)
        return edges

    def detect_lines(self, edges):

        # get the lines of te field
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 7, np.array([]), 200, 100)

        if lines is not None:
            slopeLines = self.SlopeCalc(lines)
            self.NetLine = self.LinesFilter(slopeLines, self.LN, self.RN, 0, 2, None)
            self.UpLine = self.LinesFilter(slopeLines, self.UT, self.DT, 1, 3, False)
            self.LeftLine = self.LinesFilter(slopeLines, self.LL, self.RL, 0, 2, True)
            self.DownLine = self.LinesFilter(slopeLines, self.UB, self.DB, 1, 3, False)
            self.RightLine = self.LinesFilter(slopeLines, self.LR, self.RR, 0, 2, True)

            # print(f'NTL = {self.NTL}')
            # print(f'NTR = {self.NTR}')

    def detect_field(self, frame):
        edges = self.init_frame(frame)
        self.detect_lines(edges)
        try:

            if self.UpLine is not None and self.LeftLine is not None:
                # Left up corner
                self.LeftUp = self.line_intersection(self.UpLine, self.LeftLine)

            if self.DownLine is not None and self.LeftLine is not None:
                # Left down corner
                self.LeftDown = self.line_intersection(self.DownLine, self.LeftLine)

            if self.DownLine is not None and self.RightLine is not None:
                # Right down corner
                self.RightDown = self.line_intersection(self.DownLine, self.RightLine)

            if self.UpLine is not None and self.RightLine is not None:
                # Right up corner
                self.RightUp = self.line_intersection(self.UpLine, self.RightLine)

            if self.NetLine:
                self.field_center = (self.NetLine[0] + self.NetLine[2]) // 2

            if self.LeftUp is not None and self.LeftDown is not None and self.RightDown and self.RightUp is not None:
                self.field_contour = self.get_field_contour(self.LeftUp, self.LeftDown, self.RightDown, self.RightUp)

            return self.LeftUp, self.LeftDown, self.RightDown, \
                   self.RightUp, self.NetLine, self.field_center, self.field_contour

        except NameError:
            print("FieldDetection.detect_field: error occurred")

    def det(self, a, b):
        return a[0] * b[1] - a[1] * b[0]

    def line_intersection(self, line1, line2):

        x1, y1, x2, y2 = line1
        a1, b1, a2, b2 = line2

        xdiff = (x1 - x2, a1 - a2)
        ydiff = (y1 - y2, b1 - b2)

        try:
            div = self.det(xdiff, ydiff)
            if div == 0:
                print("lines do not intersect")
                # raise Exception('lines do not intersect')
            else:
                d = (self.det((x1, y1), (x2, y2)), self.det((a1, b1), (a2, b2)))
                x = self.det(d, xdiff) / div
                y = self.det(d, ydiff) / div
                return int(x), int(y)
        except NameError:
            print("lines do not intersect")

    def SlopeCalc(self, lines):
        Angle_Sum = np.array([(180 / np.pi) * np.arctan2(lines[:, :, 3] - lines[:, :, 1],
                                                         lines[:, :, 2] - lines[:, :, 0])])
        Angle_Sum = Angle_Sum.reshape(Angle_Sum.shape[1], Angle_Sum.shape[0], Angle_Sum.shape[2])
        slopeLines = np.append(lines, Angle_Sum, axis=2)
        return slopeLines

    def LinesFilter(self, slopeLines, threshold1, threshold2, x, y, isVertical):

        if isVertical:
            slopeLines = slopeLines[slopeLines[..., 4] > 70]  # slope

        elif isVertical is None:
            slopeLines = slopeLines[slopeLines[..., 4] > 50]  # slope

        else:
            slopeLines = slopeLines[slopeLines[..., 4] < 5]  # slope

        if slopeLines is not None:
            slopeLines = slopeLines[slopeLines[..., x] > threshold1]  # x1
        if slopeLines is not None:
            slopeLines = slopeLines[slopeLines[..., x] < threshold2]  # x1
        if slopeLines is not None:
            slopeLines = slopeLines[slopeLines[..., y] > threshold1]  # x2
        if slopeLines is not None:
            slopeLines = slopeLines[slopeLines[..., y] < threshold2]  # x2

        if len(slopeLines) >= 1:
            X1 = np.mean(slopeLines[..., 0])  # x1
            X2 = np.mean(slopeLines[..., 2])  # y1
            Y1 = np.mean(slopeLines[..., 1])  # x2
            Y2 = np.mean(slopeLines[..., 3])  # y2
            avgLine = int(X1), int(Y1), int(X2), int(Y2)
            return avgLine

    def draw_field(self, frame):
        # Polygon corner points coordinates
        if self.LeftUp is None or self.LeftDown is None or self.RightDown is None or self.RightUp is None:
            return frame

        FieldContour = np.array([self.LeftUp, self.LeftDown, self.RightDown, self.RightUp])
        FieldContour.reshape((-1, 1, 2))
        overlay = frame.copy()
        cv2.drawContours(overlay, [FieldContour], 0, (255, 0, 255), -1)
        cv2.addWeighted(overlay, 0.2, frame, 1, 0, frame)
        return frame

    def draw_field_lines(self, frame):
        if self.NetLine is not None:
            cv2.line(frame, (self.NetLine[0], self.NetLine[1]), (self.NetLine[2], self.NetLine[3]),
                     (0, 255, 0), 8, cv2.LINE_AA)

        if self.UpLine is not None:
            cv2.line(frame, (self.UpLine[0], self.UpLine[1]), (self.UpLine[2], self.UpLine[3]),
                     (0, 128, 255), 8, cv2.LINE_AA)

        if self.LeftLine is not None:
            cv2.line(frame, (self.LeftLine[0], self.LeftLine[1]), (self.LeftLine[2], self.LeftLine[3]),
                     (0, 255, 255), 8, cv2.LINE_AA)

        if self.DownLine is not None:
            cv2.line(frame, (self.DownLine[0], self.DownLine[1]), (self.DownLine[2], self.DownLine[3]),
                     (255, 255, 0), 8, cv2.LINE_AA)

        if self.RightLine is not None:
            cv2.line(frame, (self.RightLine[0], self.RightLine[1]), (self.RightLine[2], self.RightLine[3]),
                     (255, 128, 128), 8, cv2.LINE_AA)

    def get_field_contour(self, LeftUp, LeftDown, RightDown, RightUp):
        FieldContour = np.array([self.LeftUp, self.LeftDown, self.RightDown, self.RightUp])
        FieldContour.reshape((-1, 1, 2))
        return FieldContour

    # ***********************
    # Calibration screen
    # ***********************

    def calibration(self, frame):

        # Current frame
        frame_copy = frame.copy()
        current_frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Threshold frame
        res, binary = cv2.threshold(current_frame_gray, self.Gamma_Min, 255, cv2.THRESH_BINARY)

        # Edges frame
        edges = cv2.Canny(binary, 1, 255)

        # draw lines
        self.draw_field_lines(frame_copy)

        field = self.draw_field(frame)

        imgStack = stackImages(0.5, ([field, frame_copy], [binary, edges]))
        cv2.putText(imgStack, f'-> Gamma = {self.Gamma_Min}', (320, 700),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

        return imgStack

    # ***********************
    # Field thresholds screen
    # ***********************

    def dynamic_field_thresholds(self, result_frame):

        # Draw field
        result_frame = self.draw_field(result_frame)

        copy = result_frame.copy()

        # config thresholds
        copy[360:720, 0:655] = self.field_img
        result_frame = cv2.addWeighted(result_frame, 0.5, copy, 0.5, 0)

        # mouse_click event
        cv2.namedWindow("# Field thresholds calibration screen")
        cv2.setMouseCallback("# Field thresholds calibration screen", self.printCoordinate)
        print(self.mode)

        point = self.x_click, self.y_click

        # Draw click
        cv2.circle(result_frame, point, 9, (0, 0, 0), 2)
        if 38 < self.x_click < 53 and 390 < self.y_click < 402:
            # Draw click
            cv2.circle(result_frame, point, 9, (0, 0, 255), 2)
            self.mode = "LL"

        elif 189 < self.x_click < 207 and 388 < self.y_click < 403:
            # Draw click
            cv2.circle(result_frame, point, 9, (0, 0, 255), 2)
            self.mode = "RL"

        elif 283 < self.x_click < 300 and 391 < self.y_click < 404:
            # Draw click
            cv2.circle(result_frame, point, 9, (255, 0, 0), 2)
            self.mode = "LN"

        elif 395 < self.x_click < 415 and 388 < self.y_click < 407:
            # Draw click
            cv2.circle(result_frame, point, 9, (255, 0, 0), 2)
            self.mode = "RN"

        elif 482 < self.x_click < 498 and 390 < self.y_click < 407:
            # Draw click
            cv2.circle(result_frame, point, 9, (0, 0, 255), 2)
            self.mode = "LR"

        elif 626 < self.x_click < 644 and 392 < self.y_click < 405:
            # Draw click
            cv2.circle(result_frame, point, 9, (0, 0, 255), 2)
            self.mode = "RR"

        elif 589 < self.x_click < 610 and 415 < self.y_click < 433:
            # Draw click
            cv2.circle(result_frame, point, 9, (0, 255, 0), 2)
            self.mode = "UT"

        elif 592 < self.x_click < 610 and 490 < self.y_click < 503:
            # Draw click
            cv2.circle(result_frame, point, 9, (0, 255, 0), 2)
            self.mode = "DT"

        elif 589 < self.x_click < 610 and 599 < self.y_click < 611:
            # Draw click
            cv2.circle(result_frame, point, 9, (0, 255, 0), 2)
            self.mode = "UB"

        elif 589 < self.x_click < 610 and 668 < self.y_click < 685:
            # Draw click
            cv2.circle(result_frame, point, 9, (0, 255, 0), 2)
            # font = cv2.FONT_HERSHEY_PLAIN
            # cv2.putText(result_frame, f'({point})',
            #             (self.x_click + 10, self.y_click - 10), font, 3, (0, 0, 0))
            self.mode = "DB"

        else:
            self.mode = None

        # give me threshold line
        f_point, s_point, threshold_name, line_color = self.give_me_line()

        # Draw threshold line
        if f_point is not None:
            result_frame = cv2.line(result_frame, f_point, s_point, line_color, 2)
        else:
            cv2.putText(result_frame, f'Please, select the threshold line.',
                        (10, HEIGHT_OF_SCREEN // 2), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 5)

        cv2.imshow("# Field thresholds calibration screen", result_frame)

        return result_frame

    def printCoordinate(self, event, x, y, flags, params):
        try:
            if event == cv2.EVENT_LBUTTONDOWN:
                self.x_click, self.y_click = int(x), int(y)

        except NameError:
            print("Field dynamic thresholds error")

    def reset_click(self):
        self.x_click, self.y_click = 0, 0

    def give_me_line(self):

        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

        if self.mode == "LL":

            # if keyboard.is_pressed('left'):
            #     print("left")
            #
            # elif keyboard.is_pressed('right'):
            #     print("left")

            f_point = (self.LL, 0)
            s_point = (self.LL, HEIGHT_OF_SCREEN)
            threshold_name = "LL"
            return f_point, s_point, threshold_name, colors[2]

        elif self.mode == "RL":
            f_point = (self.RL, 0)
            s_point = (self.RL, HEIGHT_OF_SCREEN)
            threshold_name = "RL"
            return f_point, s_point, threshold_name, colors[2]

        elif self.mode == "LN":
            f_point = (self.LN, 0)
            s_point = (self.LN, HEIGHT_OF_SCREEN)
            threshold_name = "LN"
            return f_point, s_point, threshold_name, colors[0]

        elif self.mode == "RN":
            f_point = (self.RN, 0)
            s_point = (self.RN, HEIGHT_OF_SCREEN)
            threshold_name = "RN"
            return f_point, s_point, threshold_name, colors[0]

        elif self.mode == "LR":
            f_point = (self.LR, 0)
            s_point = (self.LR, HEIGHT_OF_SCREEN)
            threshold_name = "LR"
            return f_point, s_point, threshold_name, colors[2]

        elif self.mode == "RR":
            f_point = (self.RR, 0)
            s_point = (self.RR, HEIGHT_OF_SCREEN)
            threshold_name = "RR"
            return f_point, s_point, threshold_name, colors[2]

        elif self.mode == "UT":
            f_point = (0, self.UT)
            s_point = (WEIGHT_OF_SCREEN, self.UT)
            threshold_name = "UT"
            return f_point, s_point, threshold_name, colors[1]

        elif self.mode == "DT":
            f_point = (0, self.DT)
            s_point = (WEIGHT_OF_SCREEN, self.DT)
            threshold_name = "DT"
            return f_point, s_point, threshold_name, colors[1]

        elif self.mode == "UB":
            f_point = (0, self.UB)
            s_point = (WEIGHT_OF_SCREEN, self.UB)
            threshold_name = "UB"
            return f_point, s_point, threshold_name, colors[1]

        elif self.mode == "DB":
            f_point = (0, self.DB)
            s_point = (WEIGHT_OF_SCREEN, self.DB)
            threshold_name = "DB"
            return f_point, s_point, threshold_name, colors[1]

        elif self.mode is None:
            return None, None, None, (0, 0, 0)





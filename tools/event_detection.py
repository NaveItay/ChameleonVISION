import cv2
import numpy as np
from .helper import *


class EventDetection:
    # Switching flags for calculate slopes
    ball_position_flag = False
    ball_slope_flag = False

    # Ball coordinates
    current_ball = None
    prev_ball = None

    # Ball slopes
    current_slop = None
    prev_slop = None

    # Calc different slope
    slope_difference = None

    last_player_touch = None
    current_player_touch = None

    ball_center = None
    field_contour = None

    counter_draw_slope_diff = 90

    # Variable to check if the ball is inside a player's BOX
    ball_inside_player = False

    # Draw slope diff event variables
    slopeDiff = None
    ball_point_event = None

    def check_ball_event(self, result_frame, classes, detection_boxes, field_contour, ball_box, field_center):

        # Field
        if len(field_contour) != 0:
            self.field_contour = field_contour

        if self.field_contour is None:
            return result_frame, None, None

        # Ball
        if len(ball_box) != 0:
            self.ball_center = get_box_center(ball_box)
        else:
            # Draw slope difference event for 3.6s
            self.counter_draw_slope_diff += 1
            self.draw_slope_diff(result_frame, self.slope_difference, self.current_ball)
            return result_frame, None, None

        # Players
        if len(detection_boxes) != 0:
            player_index = [index for index, object_class in enumerate(classes) if object_class == 0]
            playersBoxes = detection_boxes[player_index]
        else:
            return result_frame, None, None

        self.current_player_touch = None

        for playerBox in playersBoxes:

            x, y, w, h = playerBox

            playerLeftUp = (x, y)
            playerLeftDown = (x, y + h)
            playerRightDown = (x + w, y + h)
            playerRightUp = (x + w, y)

            playerContour = np.array([playerLeftUp, playerLeftDown, playerRightDown, playerRightUp])
            playerContour.reshape((-1, 1, 2))
            ballInOut_playerBox = int(cv2.pointPolygonTest(playerContour, self.ball_center, True))

            # Check if ball inside the boundingBoxes of the players
            if ballInOut_playerBox >= 0:
                self.last_player_touch = (x, y, w, h)
                self.current_player_touch = self.last_player_touch
                self.ball_inside_player = True

                self.current_ball = None
                self.prev_ball = None

                self.current_slop = None
                self.prev_slop = None
                self.prev_ball = None

                # Draw slope difference event for 3.6s
                self.counter_draw_slope_diff += 1
                self.draw_slope_diff(result_frame, self.slope_difference, self.current_ball)

                return result_frame, None, None
            else:
                self.ball_inside_player = False

        # Draw slope difference event for 3.6s
        self.counter_draw_slope_diff += 1
        self.draw_slope_diff(result_frame, self.slope_difference, self.current_ball)

        # If ball was found
        if len(ball_box) != 0:

            # inverse position flag
            self.ball_position_flag = not self.ball_position_flag

            if self.ball_position_flag:
                self.current_ball = self.ball_center
            else:
                self.prev_ball = self.ball_center

            if self.current_ball is None or self.prev_ball is None:
                return result_frame, None, None

            # inverse slope flag
            self.ball_slope_flag = not self.ball_slope_flag

            if self.ball_slope_flag:
                self.current_slop = self.claculate_slope(self.prev_ball, self.current_ball)
            else:
                self.prev_slop = self.claculate_slope(self.current_ball, self.prev_ball)

        # Check if ball slope was found before
        if self.current_slop is None or self.prev_slop is None:
            return result_frame, None, None

        # Check change direction and if the ball is inside a player's BOX
        self.slope_difference = abs(abs(self.current_slop) - abs(self.prev_slop))

        if self.slope_difference > 90:
            # Draw slope difference event for 3.6s
            self.counter_draw_slope_diff = 0
            self.draw_slope_diff(result_frame, self.slope_difference, self.current_ball)

            BallInOut = int(cv2.pointPolygonTest(field_contour, self.current_ball, True))

            if BallInOut >= 0:
                # Ball In
                team = self.check_event_side(field_center, True)
                return result_frame, False, team
            else:
                # Ball Out
                team = self.check_event_side(field_center, False)
                return result_frame, True, team
        # No ball event
        return result_frame, None, None

    def draw_slope_diff(self, result_frame, slope_difference, current_ball):
        if self.counter_draw_slope_diff == 0:
            self.slopeDiff = slope_difference
            self.ball_point_event = current_ball

        # if self.ball_point_event and self.slopeDiff and self.counter_draw_slope_diff < 200:
        #     cv2.putText(result_frame, f'{self.slopeDiff} -> slope difference',
        #                 (self.ball[0] + 20, self.ball[1] + 20),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        #     cv2.circle(result_frame, self.ball_point_event, 5, (0, 0, 0), -1)

    def claculate_slope(self, pointA, pointB):
        slope_line = (pointA[0], pointA[1], pointB[0], pointB[1])
        slope = (180 / np.pi) * np.arctan2(slope_line[3] - slope_line[1], slope_line[2] - slope_line[0])
        return slope

    def check_event_side(self, field_center, is_ball_in):
        ball_side = self.get_object_side(self.current_ball, field_center)
        last_player_side = self.get_object_side(self.last_player_touch, field_center)

        if ball_side == last_player_side:
            return int(not ball_side)
        else:
            if is_ball_in:
                return last_player_side
            else:
                return ball_side

    def get_object_side(self, obj_point, field_center):

        if field_center and obj_point and obj_point[0] < field_center:
            return 0
        else:
            return 1

    def draw_event(self, frame, field_center):

        if self.current_ball and self.prev_ball:
            cv2.line(frame, (self.current_ball[0], self.current_ball[1]),
                     (self.prev_ball[0], self.prev_ball[1]),
                     (0, 255, 0), 4, cv2.LINE_AA)
        if self.current_slop and self.prev_slop:
            cv2.putText(frame, f' slope difference = {self.slope_difference}',
                        (self.current_ball[0], self.current_ball[1]),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

        if self.current_player_touch:
            x, y, w, h = self.current_player_touch
            playerLeftUp = (x, y)
            playerRightDown = (x + w, y + h)
            cv2.rectangle(frame, playerLeftUp, playerRightDown, (0, 255, 253), 2)

        if self.current_ball and self.last_player_touch:
            ball_side = self.get_object_side(self.current_ball, field_center)
            last_player_side = self.get_object_side(self.last_player_touch, field_center)

            cv2.putText(frame, f'ball_side = {self.int_to_side(ball_side)}', (640, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

            cv2.putText(frame, f'last_player_side = {self.int_to_side(last_player_side)}', (640, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

            # Draw slope diff event
            if self.ball_point_event and self.slopeDiff and self.counter_draw_slope_diff < 200:
                cv2.putText(frame, f'{self.slopeDiff} -> slope difference',
                            (self.ball_point_event[0] + 20, self.ball_point_event[1] + 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                cv2.circle(frame, self.ball_point_event, 5, (0, 0, 0), -1)

        return frame

    def int_to_side(self, _int):
        if _int == 0:
            return "Left"
        else:
            return "Right"

    def is_in_serve_position(self, left, rigth):

        if not self.last_player_touch or left is None or rigth is None:
            return False

        x, y, w, h = self.last_player_touch
        playerLeftUp = (x, y)
        playerLeftDown = (x, y + h)
        playerRightDown = (x + w, y + h)
        playerRightUp = (x + w, y)

        playerContour = np.array([playerLeftUp, playerLeftDown, playerRightDown, playerRightUp])
        playerContour.reshape((-1, 1, 2))
        ballInOut_playerBox = int(cv2.pointPolygonTest(playerContour, self.current_ball, True))

        if ballInOut_playerBox >= 0 and (x < left or x > rigth):
            return True
        else:
            return False

    def check_net_touch(self, frame, NetLine):

        if NetLine is None:
            return

        net_slop = abs(self.claculate_slope((NetLine[0], NetLine[1]), (NetLine[2], NetLine[3])))
        if net_slop > 80:
            cv2.line(frame, (NetLine[0], NetLine[1]), (NetLine[2], NetLine[3]),
                     (0, 255, 0), 8, cv2.LINE_AA)
        elif net_slop > 75:
            cv2.line(frame, (NetLine[0], NetLine[1]), (NetLine[2], NetLine[3]),
                     (0, 0, 255), 8, cv2.LINE_AA)

    def reset_data(self):
        self.current_ball = None
        self.prev_ball = None
        self.current_slop = None
        self.prev_slop = None
        self.found_last_frame = False
        self.last_player_touch = None
        self.current_player_touch = None

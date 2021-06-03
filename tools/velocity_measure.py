import math
import cv2


class VelocityMeasure:
    fps = 25
    current_ball = None
    prev_ball = None
    ball_flag = True

    def get_velocity(self, ball_box, field_contour):
        # Calculate how much pixels in 16 meters
        # field_pixels_length = 1600cm
        field_pixels_length = max(field_contour[:, 0]) - min(field_contour[:, 0])

        pixel_to_cm = field_pixels_length / 1600
        distance = self.distance(ball_box)
        if distance is not None:
            distance_cm = distance * pixel_to_cm

            # distance / time = velocity
            velocity_cm_sec = distance_cm / (2 / self.fps)
            return velocity_cm_sec
        else:
            return None

    def distance(self, ball_box):

        if self.ball_flag:
            self.current_ball = ball_box
            self.ball_flag = not self.ball_flag
        else:
            self.prev_ball = ball_box
            self.ball_flag = not self.ball_flag

        if self.current_ball and self.prev_ball:
            x1, y1, _, _, _ = self.current_ball
            x2, y2, _, _, _ = self.prev_ball
            distance = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
            return distance
        else:
            return None

    def draw_velocity(self, result_frame, ball_velocity_cm_sec):

        if self.current_ball and ball_velocity_cm_sec is not None:
            x, y, _, _, _ = self.current_ball
            cv2.putText(result_frame, f'V: {round(ball_velocity_cm_sec, 2)} cm/s', (x+25, y+25),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

        return result_frame

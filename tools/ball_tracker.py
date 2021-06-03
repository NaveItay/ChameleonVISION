import math
import cv2


class BallTracker:

    ball_inside_field = []
    ball_outside_field = []
    balls_trackerInside = []
    balls_trackerOutside = []

    def __init__(self):
        # Store the center positions of the objects
        self.center_points = {}
        # Keep the count of the IDs
        # each time a new object id detected, the count will increase by one
        self.id_count = 1

    def get_center(self, box):
        x, y, w, h = box
        cx = (x + x + w) // 2
        cy = (y + y + h) // 2
        return cx, cy

    def track_inside_field(self, classes, detection_boxes, field_contour):

        # Ball
        ball_index = [index for index, object_class in enumerate(classes) if object_class == 1]
        ball_boxes = detection_boxes[ball_index]

        self.ball_inside_field = []
        self.ball_outside_field = []

        self.balls_trackerInside = []
        self.balls_trackerOutside = []

        # balls exists?
        if len(ball_boxes) != 0:
            for ballBox in ball_boxes:

                x, y = self.get_center(ballBox)
                ball_center = (x, y)

                ball_check_insideField = int(cv2.pointPolygonTest(field_contour, ball_center, True))
                if ball_check_insideField >= 0:
                    self.ball_inside_field.append(ballBox)
                else:
                    self.ball_outside_field.append(ballBox)

            if len(self.ball_inside_field) >= 1:
                self.balls_trackerInside = self.tracker(self.ball_inside_field)
                # If there is more than one ball, take the ball as tracked.
                if len(self.balls_trackerInside) > 1:
                    # self.balls_trackerInside[4] = 0
                    return self.balls_trackerInside[0]
                elif len(self.balls_trackerInside) == 1:
                    self.balls_trackerInside[0][4] = 0
                    return self.balls_trackerInside[0]
            # If there is no ball in the field, you will be allowed to take a ball from outside.
            else:
                self.balls_trackerOutside = self.tracker(self.ball_outside_field)
                # If there is more than one ball, take the ball as tracked.
                if len(self.balls_trackerOutside) > 1:
                    # self.balls_trackerOutside[4] = 1
                    return self.balls_trackerOutside[0]
                elif len(self.balls_trackerOutside) == 1:
                    self.balls_trackerOutside[0][4] = 1
                    return self.balls_trackerOutside[0]
        else:
            return []

    def tracker(self, objects_rect):
        # Objects boxes and ids
        objects_bbs_ids = []

        # Get center point of new object\
        for rect in objects_rect:
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            # Find out if that object was detected already
            same_object_detected = False
            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                if dist < 25:
                    self.center_points[id] = (cx, cy)

                    objects_bbs_ids.append([x, y, w, h, id])
                    same_object_detected = True
                    break

            # New object is detected we assign the ID to that object
            if same_object_detected is False:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.id_count])
                self.id_count += 1

        # Clean the dictionary by center points to remove IDS not used anymore
        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center

        # Update dictionary with IDs not used removed
        self.center_points = new_center_points.copy()

        # return index players missing
        # objects_bbs_ids = self.give_me_back(objects_bbs_ids)

        return objects_bbs_ids

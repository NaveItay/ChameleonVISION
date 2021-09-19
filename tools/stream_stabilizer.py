# import required libraries
# from vidgear.gears.stabilizer import Stabilizer
#
#
# class StreamStabilizer:
#
#     stab = Stabilizer()
#
#
#     def stbilizer_frame(self, frame):
#
#         # send current frame to stabilizer for processing
#         stabilized_frame = self.stab.stabilize(frame)
#
#         # wait for stabilizer which still be initializing
#         if stabilized_frame is None:
#             return frame
#         else :
#             return stabilized_frame
#
#
#
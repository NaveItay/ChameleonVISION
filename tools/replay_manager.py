import cv2
import numpy as np

from .helper import *
from PyQt5.QtCore import pyqtSignal, QThread, QObject


class ReplayManager(QThread):
    current_frame = 0
    replay_start_frame = 0
    replay_end_frame = 0
    replay_flag = False
    replay_view = None
    cap = None
    replay_slider = None
    sliderChanging = False

    def start_replay(self, cap, replay_view, replay_slider):
        self.replay_end_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        self.replay_start_frame = self.replay_end_frame - 200
        self.replay_slider = replay_slider
        self.init_replay_bar()
        self.replay_view = replay_view
        self.cap = cap
        self.replay_flag = True
        self.start()

    def run(self):

        self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.replay_start_frame)

        while self.replay_flag:

            if self.sliderChanging:
                continue

            ret, current_frame = self.cap.read()

            if ret and int(self.replay_slider.value()) < self.replay_end_frame:
                self.replay_slider.setValue(int(self.replay_slider.value()) + 1)
                try:
                    self.cap.set(cv2.CAP_PROP_POS_FRAMES, int(self.replay_slider.value()))
                    qt_img = convert_cv_qt(current_frame, self.replay_view.size())
                    self.replay_view.setPixmap(qt_img)
                except:
                    continue

            else:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.replay_start_frame)
                self.replay_slider.setValue(self.replay_start_frame)

    def init_replay_bar(self):
        self.replay_slider.setMinimum(self.replay_start_frame)
        self.replay_slider.setMaximum(self.replay_end_frame)

    def replay_slider_pressed(self):
        self.sliderChanging = True
        print('replay_slider_pressed')

    def replay_slider_released(self):
        self.sliderChanging = False
        print('replay_slider_released')

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self.replay_flag = False

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QRect, QTimer
import time
from datetime import datetime

from tools.helper import *
from tools.detection_manager import Detector
from screens.ui.UI_Game import EventElement, UI_Game
from tools.statistics import Statistics
import cv2


class Game(QWidget, UI_Game):
    detector = None
    timer = None
    start_time = None
    lastAlertTime = None
    current_alert_team = None
    current_alert_time = None
    current_alert_name = None
    is_alert_allowed = True

    alerts = 0
    true_alert = 0

    # init Statistics export method
    Stat = Statistics()

    def __init__(self, parent=None):
        super(Game, self).__init__(parent)
        self.setupUi(self)
        self.hide_none_start_items()
        # create the video capture thread
        self.detector = Detector()
        # start the thread
        self.detector.start()
        self.init_gamma_bar()
        self.start_timer()
        self.connect_signals()

    def hide_none_start_items(self):
        self.alert.hide()
        self.gamma_slider.hide()
        self.replay_slider.hide()
        self.replay_view.hide()

    def init_gamma_bar(self):
        self.gamma_slider.setMinimum(0)
        self.gamma_slider.setMaximum(255)

    def start_timer(self):
        self.start_time = datetime.now()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

    def connect_signals(self):
        self.detector.change_pixmap_signal.connect(self.update_image_slot)
        self.detector.ball_event_signal.connect(self.update_alert_slot)
        self.detector.in_serve_position.connect(self.allow_alerts)
        self.play_btn.clicked.connect(self.on_play_btn_click)
        self.stop_btn.clicked.connect(self.on_stop_btn_click)

        # Right side buttons
        self.game_btn.clicked.connect(self.on_game_btn_click)
        self.thresholds_btn.clicked.connect(self.on_thresholds_btn_click)
        self.debug_btn.clicked.connect(self.on_debug_btn_click)
        self.calibration_btn.clicked.connect(self.on_calibration_btn_click)

        self.switch_btn.clicked.connect(self.on_switch_btn_click)
        try:
            self.replay_slider.sliderReleased.connect(self.detector.replayManager.replay_slider_released)
        except NameError:
            print("replay problem")
        self.replay_slider.sliderPressed.connect(self.detector.replayManager.replay_slider_pressed)
        self.gamma_slider.valueChanged.connect(self.gamma_value_changed)
        self.alert_true_btn.clicked.connect(self.on_true_alert_btn_click)
        self.alert_false_btn.clicked.connect(self.on_false_alert_btn_click)
        self.alert_replay_btn.clicked.connect(self.on_replay_btn_click)

    # SLOTS

    def update_image_slot(self, cv_img):
        ## Updates the image_label with a new opencv image
        qt_img = convert_cv_qt(cv_img, self.game_view.size())
        self.game_view.setPixmap(qt_img)

    def update_alert_slot(self, isOut=None, team=None, netTouch=None):

        currentAlertTime = time.time()

        if self.lastAlertTime is not None:
            if self.lastAlertTime + 5 < currentAlertTime:
                self.lastAlertTime = None
                self.alert.hide()
            else:
                return

        if not self.is_alert_allowed: return

        team_color = "rgb(50, 50, 200)"
        if team == 1:
            team_color = "rgb(200, 50, 50)"
        self.alert_team_color.setStyleSheet(f"background-color:{team_color};\n"
                                            "border-style:outset;\n"
                                            "border-radius:10px;\n"
                                            "color: rgb(250, 255, 255);\n"
                                            "font: 14pt;")
        if isOut == True:
            self.lastAlertTime = time.time()
            self.alert_event_name.setText("Ball-Out")
            self.current_alert_team = team
            self.current_alert_time = self.game_time.text()
            self.alert.show()

        elif isOut == False:
            self.lastAlertTime = time.time()
            self.alert_event_name.setText("Ball-In")
            self.current_alert_team = team
            self.current_alert_time = self.game_time.text()
            self.alert.show()

    def on_game_btn_click(self):

        try:
            cv2.destroyWindow('# Field thresholds calibration screen')
        except:
            pass

        self.detector.debug_flag = False
        self.detector.calibration_flag = False
        self.detector.fieldThresholds_flag = False
        self.gamma_slider.hide()

    def on_debug_btn_click(self):

        try:
            cv2.destroyWindow('# Field thresholds calibration screen')
        except:
            pass

        self.detector.debug_flag = True
        self.detector.calibration_flag = False
        self.detector.fieldThresholds_flag = False
        self.gamma_slider.hide()

    def on_calibration_btn_click(self):

        try:
            cv2.destroyWindow('# Field thresholds calibration screen')
        except:
            pass

        self.detector.calibration_flag = True
        self.detector.debug_flag = False
        self.detector.fieldThresholds_flag = False
        self.gamma_slider.setValue(self.detector.field_detector.Gamma_Min)
        self.gamma_slider.show()

    def on_thresholds_btn_click(self):
        self.detector.fieldThresholds_flag = True
        self.detector.debug_flag = False
        self.detector.calibration_flag = False
        self.gamma_slider.hide()

    def on_play_btn_click(self):
        self.detector.play_flag = True
        self.timer.start(1000)

    def on_stop_btn_click(self):
        self.detector.play_flag = False
        self.timer.stop()

    def update_time(self):
        delta_time = datetime.now() - self.start_time
        game_time = time.gmtime(delta_time.total_seconds())
        game_time = time.strftime('%H:%M:%S', game_time)
        self.game_time.setText(game_time)
        self.update_alert_slot()

    def gamma_value_changed(self, value):
        self.detector.field_detector.Gamma_Min = int(value)

    def on_true_alert_btn_click(self):

        # update statistics
        self.alerts += 1
        self.true_alert += 1
        self.Stat.save(self.true_alert, self.alerts)
        # self.saveStat(self, name, teamA, teamB, Location, Date, Weather,
        #          TeamA_Accuracy_BallIn, TeamB_Accuracy_BallIn,
        #          TeamA_Accuracy_BallOut, TeamB_Accuracy_BallOut)

        # self.is_alert_allowed = False
        self.update_score()
        self.update_event_logs()
        self.alert.hide()
        self.detector.replayManager.stop()
        self.detector.replayManager.quit()
        self.detector.replayManager.wait()
        self.detector.replay_flag = False
        self.timer.start(1000)
        self.replay_slider.hide()
        self.replay_view.hide()

    def on_false_alert_btn_click(self):

        # update statistics
        self.alerts += 1
        self.Stat.save(self.true_alert, self.alerts)
        # self.saveStat(self, name, teamA, teamB, Location, Date, Weather,
        #          TeamA_Accuracy_BallIn, TeamB_Accuracy_BallIn,
        #          TeamA_Accuracy_BallOut, TeamB_Accuracy_BallOut)

        self.lastAlertTime = None
        self.alert.hide()
        self.detector.replayManager.stop()
        self.detector.replayManager.quit()
        self.detector.replayManager.wait()
        self.detector.replay_flag = False
        self.timer.start(1000)
        self.replay_slider.hide()
        self.replay_view.hide()

    def update_score(self):
        if self.current_alert_team == 1:
            self.red_points.setText(str(int(self.red_points.text()) + 1))
        else:
            self.blue_points.setText(str(int(self.blue_points.text()) + 1))

    def update_event_logs(self):
        event_element = EventElement(self.verticalLayoutWidget, self.current_alert_team, self.alert_event_name.text(),
                                     self.current_alert_time)
        self.events_holder.addWidget(event_element)

    def allow_alerts(self):
        self.is_alert_allowed = True

    def on_switch_btn_click(self):

        blue_name_p = QRect(self.blue_name.x(), self.blue_name.y(), self.blue_name.width(), self.blue_name.height())
        red_points_p = QRect(self.red_points.x(), self.red_points.y(), self.red_points.width(),
                             self.red_points.height())
        red_name_p = QRect(self.red_name.x(), self.red_name.y(), self.red_name.width(), self.red_name.height())
        blue_points_p = QRect(self.blue_points.x(), self.blue_points.y(), self.blue_points.width(),
                              self.blue_points.height())

        self.blue_name.setGeometry(red_name_p)
        self.red_name.setGeometry(blue_name_p)
        self.blue_points.setGeometry(red_points_p)
        self.red_points.setGeometry(blue_points_p)

        self.detector.o_detection.switch_sides()
        self.detector.switch_flag = not self.detector.switch_flag

    def on_replay_btn_click(self):
        self.timer.stop()
        self.replay_view.show()
        self.replay_slider.show()
        self.alert.show()
        self.detector.replay_flag = True
        self.detector.replayManager.start_replay(self.detector.cap, self.replay_view, self.replay_slider)

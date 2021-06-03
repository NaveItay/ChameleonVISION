# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GameScreen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UI_Game(object):
    def setupUi(self, Game):
        Game.setObjectName("Game")
        Game.resize(1920, 1080)
        Game.setMinimumSize(QtCore.QSize(1920, 1080))
        Game.setMaximumSize(QtCore.QSize(1920, 1080))
        Game.setStyleSheet("background-color: rgb(50, 50, 50);")
        # Game.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.game_view = QtWidgets.QLabel(Game)
        self.game_view.setGeometry(QtCore.QRect(490, 200, 1280, 720))
        self.game_view.setStyleSheet("background-color: rgb(250, 250, 250);\n"
                                     "border-style:outset;\n"
                                     "border-radius:10px;\n"
                                     "color: rgb(10, 10, 10);\n"
                                     "font: 14pt;")
        self.game_view.setAlignment(QtCore.Qt.AlignCenter)
        self.game_view.setObjectName("game_view")

        self.replay_view = QtWidgets.QLabel(Game)
        self.replay_view.setGeometry(QtCore.QRect(490, 200, 1280, 720))
        self.replay_view.setStyleSheet("background-color: rgb(250, 250, 250);\n"
                                       "border-style:outset;\n"
                                       "border-radius:10px;\n"
                                       "color: rgb(10, 10, 10);\n"
                                       "font: 14pt;")
        self.replay_view.setAlignment(QtCore.Qt.AlignCenter)
        self.replay_view.setObjectName("replay_view")

        self.logo = QtWidgets.QLabel(Game)
        self.logo.setGeometry(QtCore.QRect(40, 30, 301, 71))
        self.logo.setStyleSheet("background-color: rgb(20, 20, 20);\n"
                                "border-style:outset;\n"
                                "border-radius:10px;\n"
                                "color: rgb(250, 255, 255);\n"
                                "font: 14pt;")
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.blue_points = QtWidgets.QLineEdit(Game)
        self.blue_points.setGeometry(QtCore.QRect(1000, 30, 71, 71))
        self.blue_points.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-style:outset;\n"
                                       "border-radius:10px;\n"
                                       "color: rgb(10, 10, 10);\n"
                                       "font: 14pt;")
        self.blue_points.setAlignment(QtCore.Qt.AlignCenter)
        self.blue_points.setObjectName("blue_points")
        self.red_points = QtWidgets.QLineEdit(Game)
        self.red_points.setGeometry(QtCore.QRect(1190, 30, 71, 71))
        self.red_points.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "color: rgb(10, 10, 10);\n"
                                      "font: 14pt;")
        self.red_points.setAlignment(QtCore.Qt.AlignCenter)
        self.red_points.setObjectName("red_points")
        self.blue_name = QtWidgets.QLineEdit(Game)
        self.blue_name.setGeometry(QtCore.QRect(610, 30, 361, 71))
        self.blue_name.setStyleSheet("background-color: rgb(50, 50, 200);\n"
                                     "border-style:outset;\n"
                                     "border-radius:10px;\n"
                                     "color: rgb(250, 255, 255);\n"
                                     "font: 14pt;")
        self.blue_name.setAlignment(QtCore.Qt.AlignCenter)
        self.blue_name.setObjectName("blue_name")
        self.red_name = QtWidgets.QLineEdit(Game)
        self.red_name.setGeometry(QtCore.QRect(1290, 30, 361, 71))
        self.red_name.setStyleSheet("background-color: rgb(200, 50, 50);\n"
                                    "border-style:outset;\n"
                                    "border-radius:10px;\n"
                                    "color: rgb(250, 255, 255);\n"
                                    "font: 14pt;")
        self.red_name.setAlignment(QtCore.Qt.AlignCenter)
        self.red_name.setObjectName("red_name")
        self.events_background = QtWidgets.QLabel(Game)
        self.events_background.setGeometry(QtCore.QRect(20, 130, 331, 941))
        self.events_background.setStyleSheet("background-color: rgb(10, 10, 10);\n"
                                             "border-style:outset;\n"
                                             "border-radius:10px;\n"
                                             "color: rgb(250, 255, 255);\n"
                                             "font: 14pt;")
        self.events_background.setText("")
        self.events_background.setAlignment(QtCore.Qt.AlignCenter)
        self.events_background.setObjectName("events_background")
        self.top_bar = QtWidgets.QLabel(Game)
        self.top_bar.setGeometry(QtCore.QRect(20, 10, 1881, 111))
        self.top_bar.setStyleSheet("background-color: rgb(10, 10, 10);\n"
                                   "border-style:outset;\n"
                                   "border-radius:10px;\n"
                                   "color: rgb(250, 255, 255);\n"
                                   "font: 14pt;")
        self.top_bar.setText("")
        self.top_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.top_bar.setObjectName("top_bar")
        self.play_background = QtWidgets.QLabel(Game)
        self.play_background.setGeometry(QtCore.QRect(980, 950, 301, 101))
        self.play_background.setStyleSheet("background-color: rgb(20, 20, 20);\n"
                                           "border-style:outset;\n"
                                           "border-radius:40px;\n"
                                           "color: rgb(10, 10, 10);\n"
                                           "font: 14pt;")
        self.play_background.setText("")
        self.play_background.setAlignment(QtCore.Qt.AlignCenter)
        self.play_background.setObjectName("play_background")
        self.game_time = QtWidgets.QLabel(Game)
        self.game_time.setGeometry(QtCore.QRect(1170, 940, 91, 41))
        self.game_time.setStyleSheet("background-color: rgb(20, 20, 20);\n"
                                     "border-style:outset;\n"
                                     "border-radius:10px;\n"
                                     "color: rgb(250, 255, 255);\n"
                                     "font: 11pt;")
        self.game_time.setAlignment(QtCore.Qt.AlignCenter)
        self.game_time.setObjectName("game_time")

        # debug button
        self.debug_btn = QtWidgets.QPushButton(Game)
        self.debug_btn.setGeometry(QtCore.QRect(1810, 210, 51, 51))
        self.debug_btn.setStyleSheet("background-color: rgb(252, 233, 79);\n"
                                     "border-style:outset;\n"
                                     "border-radius:15px;\n"
                                     "color: rgb(10, 10, 10);\n"
                                     "font: 10pt;")
        self.debug_btn.setObjectName("debug_btn")

        self.switch_btn = QtWidgets.QPushButton(Game)
        self.switch_btn.setGeometry(QtCore.QRect(1105, 40, 51, 51))
        self.switch_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:15px;\n"
                                      "color: rgb(10, 10, 10);\n"
                                      "font: 10pt;")
        self.switch_btn.setObjectName("switch_btn")

        self.gamma_slider = QtWidgets.QSlider(Game)
        self.gamma_slider.setGeometry(QtCore.QRect(930, 220, 401, 51))
        self.gamma_slider.setStyleSheet("background-color: rgba(20, 20, 20, 90);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "color: rgb(10, 10, 10);\n"
                                        "font: 14pt;")
        self.gamma_slider.setOrientation(QtCore.Qt.Horizontal)
        self.gamma_slider.setObjectName("gamma_slider")

        self.replay_slider = QtWidgets.QSlider(Game)
        self.replay_slider.setGeometry(QtCore.QRect(930, 220, 401, 51))
        self.replay_slider.setStyleSheet("background-color: rgba(20, 20, 20, 90);\n"
                                         "border-style:outset;\n"
                                         "border-radius:10px;\n"
                                         "color: rgb(10, 10, 10);\n"
                                         "font: 14pt;")
        self.replay_slider.setOrientation(QtCore.Qt.Horizontal)
        self.replay_slider.setObjectName("replay_slider")

        self.play_btn = QtWidgets.QPushButton(Game)
        self.play_btn.setGeometry(QtCore.QRect(1020, 930, 61, 61))
        self.play_btn.setStyleSheet("background-color: rgb(50, 200, 50);\n"
                                    "border-style:outset;\n"
                                    "border-radius:20px;\n"
                                    "color: rgb(250, 255, 255);\n"
                                    "font: 14pt;")
        self.play_btn.setObjectName("play_btn")
        self.stop_btn = QtWidgets.QPushButton(Game)
        self.stop_btn.setGeometry(QtCore.QRect(1100, 930, 61, 61))
        self.stop_btn.setStyleSheet("background-color: rgb(150, 150, 150);\n"
                                    "border-style:outset;\n"
                                    "border-radius:20px;\n"
                                    "color: rgb(250, 255, 255);\n"
                                    "font: 14pt;")
        self.stop_btn.setObjectName("stop_btn")

        self.verticalLayoutWidget = QtWidgets.QScrollArea(Game)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(39, 150, 291, 900))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setStyleSheet("background-color: rgba(20, 20, 20, 0);")

        self.verticalLayoutWidget.setWidgetResizable(1)
        self.content = QtWidgets.QWidget()
        self.verticalLayoutWidget.setWidget(self.content)

        self.events_holder = QtWidgets.QVBoxLayout(self.content)
        self.events_holder.setAlignment(QtCore.Qt.AlignTop)
        self.events_holder.setContentsMargins(0, 2, 0, 2)
        self.events_holder.setObjectName("events_holder")

        # game button
        self.game_btn = QtWidgets.QPushButton(Game)
        self.game_btn.setGeometry(QtCore.QRect(1810, 420, 51, 51))
        self.game_btn.setStyleSheet("background-color: rgb(150, 120, 200);\n"
                                    "border-style:outset;\n"
                                    "border-radius:15px;\n"
                                    "color: rgb(10, 10, 10);\n"
                                    "font: 10pt;")
        self.game_btn.setObjectName("game_btn")

        # field thresholds calibration button
        self.thresholds_btn = QtWidgets.QPushButton(Game)
        self.thresholds_btn.setGeometry(QtCore.QRect(1810, 350, 51, 51))
        self.thresholds_btn.setStyleSheet("background-color: rgb(150, 0, 20);\n"
                                          "border-style:outset;\n"
                                          "border-radius:15px;\n"
                                          "color: rgb(10, 10, 10);\n"
                                          "font: 10pt;")
        self.thresholds_btn.setObjectName("thresholds_btn")

        # calibration button
        self.calibration_btn = QtWidgets.QPushButton(Game)
        self.calibration_btn.setGeometry(QtCore.QRect(1810, 280, 51, 51))
        self.calibration_btn.setStyleSheet("background-color: rgb(252, 175, 62);\n"
                                           # "border-style:outset;\n"
                                           "border-radius:15px;\n"
                                           "color: rgb(10, 10, 10);\n"
                                           "font: 10pt;")
        self.calibration_btn.setObjectName("calibration_btn")

        self.alert = QtWidgets.QFrame(Game)
        self.alert.setGeometry(QtCore.QRect(930, 850, 401, 51))
        self.alert.setStyleSheet("background-color: rgba(238, 238, 236,0);")
        self.alert.setObjectName("alert")
        self.alert_false_btn = QtWidgets.QPushButton(self.alert)
        self.alert_false_btn.setGeometry(QtCore.QRect(350, 10, 31, 31))
        self.alert_false_btn.setStyleSheet("background-color: rgb(200, 50, 50);\n"
                                           "border-style:outset;\n"
                                           "border-radius:10px;\n"
                                           "color: rgb(250, 255, 255);\n"
                                           "font: 14pt;")
        self.alert_false_btn.setObjectName("alert_false_btn")
        self.aleret_background = QtWidgets.QLabel(self.alert)
        self.aleret_background.setGeometry(QtCore.QRect(0, 0, 401, 51))
        self.aleret_background.setStyleSheet("background-color: rgba(20, 20, 20, 90);\n"
                                             "border-style:outset;\n"
                                             "border-radius:10px;\n"
                                             "color: rgb(10, 10, 10);\n"
                                             "font: 14pt;")
        self.aleret_background.setText("")
        self.aleret_background.setAlignment(QtCore.Qt.AlignCenter)
        self.aleret_background.setObjectName("aleret_background")
        self.alert_true_btn = QtWidgets.QPushButton(self.alert)
        self.alert_true_btn.setGeometry(QtCore.QRect(310, 10, 31, 31))
        self.alert_true_btn.setStyleSheet("background-color: rgb(50, 200, 50);\n"
                                          "border-style:outset;\n"
                                          "border-radius:10px;\n"
                                          "color: rgb(250, 255, 255);\n"
                                          "font: 14pt;")
        self.alert_true_btn.setObjectName("alert_true_btn")
        self.alert_event_name = QtWidgets.QLabel(self.alert)
        self.alert_event_name.setGeometry(QtCore.QRect(70, 0, 111, 51))
        self.alert_event_name.setStyleSheet("background-color: rgba(20, 20, 20,0);\n"
                                            "border-style:outset;\n"
                                            "border-radius:10px;\n"
                                            "color: rgb(250, 255, 255);\n"
                                            "font: 15pt;")
        self.alert_event_name.setAlignment(QtCore.Qt.AlignCenter)
        self.alert_event_name.setObjectName("alert_event_name")
        self.alert_replay_btn = QtWidgets.QPushButton(self.alert)
        self.alert_replay_btn.setGeometry(QtCore.QRect(200, 10, 101, 31))
        self.alert_replay_btn.setStyleSheet("background-color: rgb(100, 100, 100);\n"
                                            "border-style:outset;\n"
                                            "border-radius:10px;\n"
                                            "color: rgb(250, 255, 255);\n"
                                            "font: 14pt;")
        self.alert_replay_btn.setObjectName("alert_replay_btn")
        self.alert_team_color = QtWidgets.QLabel(self.alert)
        self.alert_team_color.setGeometry(QtCore.QRect(20, 10, 31, 31))
        self.alert_team_color.setStyleSheet("background-color: rgb(50, 50, 200);\n"
                                            "border-style:outset;\n"
                                            "border-radius:10px;\n"
                                            "color: rgb(250, 255, 255);\n"
                                            "font: 14pt;")
        self.alert_team_color.setText("")
        self.alert_team_color.setAlignment(QtCore.Qt.AlignCenter)
        self.alert_team_color.setObjectName("alert_team_color")
        self.aleret_background.raise_()
        self.alert_false_btn.raise_()
        self.alert_true_btn.raise_()
        self.alert_event_name.raise_()
        self.alert_replay_btn.raise_()
        self.alert_team_color.raise_()
        self.statistics_holder = QtWidgets.QFrame(Game)
        self.statistics_holder.setGeometry(QtCore.QRect(360, 130, 1531, 941))
        self.statistics_holder.setStyleSheet("background-color: rgb(10, 10, 10);\n"
                                             "border-style:outset;\n"
                                             "border-radius:10px;\n"
                                             "color: rgb(250, 255, 255);\n"
                                             "font: 14pt;")
        self.statistics_holder.setObjectName("statistics_holder")
        self.statistics_holder.raise_()
        self.events_background.raise_()
        self.top_bar.raise_()
        self.game_view.raise_()
        self.replay_view.raise_()
        self.logo.raise_()
        self.blue_points.raise_()
        self.red_points.raise_()
        self.blue_name.raise_()
        self.red_name.raise_()
        self.play_background.raise_()
        self.game_time.raise_()
        self.debug_btn.raise_()
        self.switch_btn.raise_()
        self.gamma_slider.raise_()
        self.replay_slider.raise_()
        self.play_btn.raise_()
        self.stop_btn.raise_()
        self.verticalLayoutWidget.raise_()
        self.game_btn.raise_()
        self.thresholds_btn.raise_()
        self.calibration_btn.raise_()
        self.alert.raise_()

        self.retranslateUi(Game)
        QtCore.QMetaObject.connectSlotsByName(Game)

    def retranslateUi(self, Game):
        _translate = QtCore.QCoreApplication.translate
        Game.setWindowTitle(_translate("Game", "Game"))
        self.game_view.setText(_translate("MainWindow", "Game View"))
        self.replay_view.setText(_translate("MainWindow", "Replay View"))
        self.logo.setText(_translate("MainWindow", "ChameleonVISION"))
        self.blue_points.setText(_translate("MainWindow", "0"))
        self.red_points.setText(_translate("MainWindow", "0"))
        self.blue_name.setText(_translate("MainWindow", "Team Blue"))
        self.red_name.setText(_translate("MainWindow", "Team Red"))
        self.game_time.setText(_translate("MainWindow", "00:00:00"))
        self.debug_btn.setText(_translate("MainWindow", "Debug"))
        self.switch_btn.setText(_translate("MainWindow", "←\n→"))
        self.play_btn.setText(_translate("MainWindow", "Play"))
        self.stop_btn.setText(_translate("MainWindow", "| |"))
        self.game_btn.setText(_translate("MainWindow", "Game"))
        self.thresholds_btn.setText(_translate("MainWindow", "Field"))
        self.calibration_btn.setText(_translate("MainWindow", "Calibrate"))
        self.alert_false_btn.setText(_translate("MainWindow", "X"))
        self.alert_true_btn.setText(_translate("MainWindow", "V"))
        self.alert_event_name.setText(_translate("MainWindow", "Ball-In"))
        self.alert_replay_btn.setText(_translate("MainWindow", "Replay"))


class EventElement(QtWidgets.QGroupBox):

    def __init__(self, parent, team, event_name, time):
        super(EventElement, self).__init__(parent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(289, 61))
        self.setMaximumSize(QtCore.QSize(289, 61))
        self.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.setObjectName("event_element")
        self.event_background_5 = QtWidgets.QLabel(self)
        self.event_background_5.setGeometry(QtCore.QRect(0, 0, 291, 61))
        self.event_background_5.setStyleSheet("background-color: rgb(20, 20, 20);\n"
                                              "border-style:outset;\n"
                                              "border-radius:10px;\n"
                                              "color: rgb(250, 255, 255);\n"
                                              "font: 14pt;")
        self.event_background_5.setText("")
        self.event_background_5.setAlignment(QtCore.Qt.AlignCenter)
        self.event_background_5.setObjectName("event_background_5")

        team_color = "rgb(50, 50, 200)"
        if team == 1:
            team_color = "rgb(200, 50, 50)"

        self.event_team_color_5 = QtWidgets.QLabel(self)
        self.event_team_color_5.setGeometry(QtCore.QRect(20, 20, 21, 21))
        self.event_team_color_5.setStyleSheet(f"background-color:{team_color};\n"
                                              "border-style:outset;\n"
                                              "border-radius:10px;\n"
                                              "color: rgb(250, 255, 255);\n"
                                              "font: 14pt;")
        self.event_team_color_5.setText("")
        self.event_team_color_5.setAlignment(QtCore.Qt.AlignCenter)
        self.event_team_color_5.setObjectName("event_team_color_5")
        self.event_name_5 = QtWidgets.QLabel(self)
        self.event_name_5.setGeometry(QtCore.QRect(70, 20, 71, 21))
        self.event_name_5.setStyleSheet("background-color: rgb(20, 20, 20);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "color: rgb(250, 255, 255);\n"
                                        "font: 10pt;")
        self.event_name_5.setAlignment(QtCore.Qt.AlignCenter)
        self.event_name_5.setObjectName("event_name_5")
        self.event_name_5.setText(event_name)
        self.event_time_5 = QtWidgets.QLabel(self)
        self.event_time_5.setGeometry(QtCore.QRect(180, 20, 71, 21))
        self.event_time_5.setStyleSheet("background-color: rgb(20, 20, 20);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "color: rgb(250, 255, 255);\n"
                                        "font: 10pt;")
        self.event_time_5.setAlignment(QtCore.Qt.AlignCenter)
        self.event_time_5.setObjectName("event_time_5")
        self.event_time_5.setText(time)

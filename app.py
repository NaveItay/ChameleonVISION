from PyQt5 import QtWidgets
import sys

import screens.login_screen as login_window
import screens.new_user_screen as new_user_window
import screens.game_screen as game_window


class GUIController:

    def __init__(self):
        pass

    def show_login_window(self):
        self.login = login_window.Login()
        self.login.switch_window.connect(self.show_newuser_window)
        self.login.switch_window1.connect(self.show_game_window)
        self.login.show()

        # self.game = game_window.Game()
        # self.login.close()
        # self.game.show()

    def show_game_window(self):
        self.game = game_window.Game()
        self.login.close()
        self.game.show()

    def show_newuser_window(self):
        self.newuser = new_user_window.Newuser()
        self.newuser.switch_window.connect(self.back_to_login)
        self.login.close()
        self.newuser.show()
        
    def back_to_login(self):
        self.newuser.close()
        self.show_login_window()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = GUIController()
    controller.show_login_window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

from PyQt6.QtWidgets import QMainWindow, QPushButton, QListWidget, QVBoxLayout, QLineEdit, \
    QWidget, QToolTip, QLabel, QFrame, QMessageBox, QCheckBox
from PyQt6.QtGui import QFont, QAction, QIcon
from PyQt6.QtCore import Qt, QEvent
from getfiledict import getmaclist
from donatewindow import DonateWindow, HelpWindow
from gethotkey import get_hotkey
from runmac import Run_all


### Main
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.main_window = QWidget()

        self.main()

    def selectionChanged(self):
        try:
            global selected_item
            global selected_row_item_main
            global selected_current_item_main
            selected_item = self.macrolist.currentItem().text()
            selected_row_item_main = self.macrolist.currentRow()
            selected_current_item_main = self.macrolist.currentItem()
            return selected_item, return_selected_item2()
        except:
            pass

    def return_selected_item(self):
        return selected_item

    def main(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        self.resize(320, 484)
        ######## Label #########
        macro_label = QLabel("Macro List", self)
        macro_label.setGeometry(10, 30, 141, 21)
        macro_label.setLineWidth(2)
        macro_label.setMidLineWidth(1)
        macro_label.setFrameShape(QFrame.Shape.Box)
        macro_label.setTextFormat(Qt.TextFormat.AutoText)
        macro_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        macro_label.setIndent(40)
        ######### End Label #########
        global turbo_mode
        self.turbo_mode = QCheckBox("Turbo", self.main_window)
        self.turbo_mode.adjustSize()
        self.turbo_mode.setGeometry(250, 420, 75, 23)
        self.turbo_mode.stateChanged.connect(self.switchturbo)
        self.turbo_mode.setChecked(False)
        turbo_mode = self.turbo_mode

        ## BUTTONS ##
        self.createbtn = QPushButton('Create', self.main_window)
        self.createbtn.resize(self.createbtn.sizeHint())
        self.createbtn.setGeometry(240, 70, 75, 23)
        self.createbtn.clicked.connect(self.show_add_item_main_window)

        self.editbtn = QPushButton('Edit', self.main_window)
        self.editbtn.resize(self.editbtn.sizeHint())
        self.editbtn.setGeometry(240, 100, 75, 23)
        self.editbtn.clicked.connect(self.show_edit_window)

        global runbtn
        self.runbtn = QPushButton('Run', self.main_window)
        self.runbtn.resize(self.runbtn.sizeHint())
        self.runbtn.setGeometry(240, 240, 75, 23)
        self.runbtn.clicked.connect(self.run_mac)
        runbtn = self.runbtn

        global stopbtn
        self.stopbtn = QPushButton('Stop', self.main_window)
        self.stopbtn.resize(self.stopbtn.sizeHint())
        self.stopbtn.setGeometry(240, 240, 75, 23)
        self.stopbtn.clicked.connect(self.stop_the_mac)
        self.stopbtn.hide()
        stopbtn = self.stopbtn

        self.deletebtn = QPushButton('Delete', self.main_window)
        self.deletebtn.setToolTip('This is a <b>QPushButton</b> widget')
        self.deletebtn.resize(self.deletebtn.sizeHint())
        self.deletebtn.setGeometry(240, 130, 75, 23)
        self.deletebtn.clicked.connect(self.delete_main_widget)

        self.save_item_btn = QPushButton('Save', self.main_window)
        self.save_item_btn.resize(self.save_item_btn.sizeHint())
        self.save_item_btn.setGeometry(240, 10, 75, 23)
        self.save_item_btn.clicked.connect(self.save_main_widget)

        ############## End BTN #############
        global script_name
        global macrolist_main
        try:
            script_name = getmaclist()
        except:
            pass
        self.macrolist = QListWidget(self.main_window)
        self.macrolist.setGeometry(10, 41, 141, 401)
        try:
            self.macrolist.addItems(script_name.keys())
        except:
            pass
        self.macrolist.itemSelectionChanged.connect(self.selectionChanged)

        macrolist_main = self.macrolist
        self.the_menu()
        self.setWindowTitle('SkyMacro')
        self.setWindowIcon(QIcon('thelogo.png'))
        self.setCentralWidget(self.main_window)

    def the_menu(self):
        menu = self.menuBar()

        button_action = QAction("Exit", self)
        button_action.setStatusTip("Exit")
        button_action.triggered.connect(self.onMyToolBarButtonClick)

        file_menu = menu.addMenu("File")
        file_menu.addAction(button_action)

        ## Help Area ##
        help_btn = QAction("Help", self)
        help_btn.triggered.connect(self.show_help_window)

        ## Donate Area ##
        donate_btn = QAction("Donate", self)
        donate_btn.setStatusTip("If you like it consider donating")
        donate_btn.triggered.connect(self.show_donate_window)

        ## Add Btn ##
        file_menu.addAction(button_action)
        menu.addAction(help_btn)
        menu.addAction(donate_btn)

        ## Donate Window
        self.donate_window = None
        self.help_window = None

    def switchturbo(self):
        if turbo_mode.isChecked():
            pressed_loop = True
        if not turbo_mode.isChecked():
            pressed_loop = False

    class AddItemMainWindow(QWidget):
        def __init__(self):
            super().__init__()
            global main_line_to_add
            layout = QVBoxLayout()
            self.line_add = QLineEdit(f"Name must be Unique")
            self.ok_add_item_btn = QPushButton('Ok')
            self.close_edit_item_btn = QPushButton('Cancel')
            self.ok_add_item_btn.clicked.connect(MainWindow.create_btn_func)
            layout.addWidget(self.line_add)
            layout.addWidget(self.ok_add_item_btn)
            self.setLayout(layout)
            self.setWindowTitle('Create')
            self.resize(260, 122)

            main_line_to_add = self.line_add

    def show_add_item_main_window(self, checked):
        global show_add_item_main_window
        self.add_item_window = MainWindow.AddItemMainWindow()
        self.add_item_window.show()
        show_add_item_main_window = self.add_item_window

    def show_donate_window(self, checked):
        if self.donate_window is None:
            self.donate_window = DonateWindow()
        self.donate_window.show()

    def show_help_window(self, checked):
        if self.help_window is None:
            self.help_window = HelpWindow()
        self.help_window.show()

    def show_edit_window(self):
        try:
            if selected_item:
                self.edit_window = EditWindow()
                self.edit_window.show()
                self.close()
                return selected_item
        except:
            pass

    def create_btn_func(self):
        macrolist_main.addItem(main_line_to_add.text())
        script_name[main_line_to_add.text()] = ["bindedkey=77"]

    def delete_main_widget(self):
        try:
            del script_name[selected_item]
            selected_current_item_main = None
            macrolist_main.takeItem(selected_row_item_main)
        except:
            pass

    def run_mac(self):
        if turbo_mode.isChecked():
            pressed_loop = True
        if not turbo_mode.isChecked():
            pressed_loop = False
        run_all = Run_all()
        run_all.run_mac(pressed_loop)
        runbtn.hide()
        stopbtn.show()

    def stop_the_mac(self):
        run_all = Run_all()
        run_all.stop_mac()
        stopbtn.hide()
        runbtn.show()

    def onMyToolBarButtonClick(self, s):
        self.close()

    def save_main_widget(self):
        with open("macro_file.txt", "w") as fi:
            for k, v in script_name.items():
                if k:
                    fi.write(str(f"[{k}]" + "\n"))
                if v:
                    for item in v:
                        if item.startswith("bindedkey="):
                            fi.write(item + "\n")
                        if item.replace('.', '', 1).isdigit():
                            fi.write(f"d={item}" + "\n")
                        if not item.startswith("bindedkey=") and not item.replace('.', '', 1).isdigit():
                            fi.write("e={" + f"{item}" + "}" + "\n")
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Saved!")
            dlg.setText("Macro Saved!")
            button = dlg.exec()

            if button == QMessageBox.StandardButton.Ok:
                print("OK!")


###### End Main #########


###### Edit Part ###########
def return_selected_item2():
    return selected_item


class EditWindow(QMainWindow):
    def __init__(self):
        super(EditWindow, self).__init__()

        self.edit_window = QWidget()
        self.edit_widget()

    def selection_edit_Changed(self):
        try:
            global selected_text_item
            global selected_row_item
            global selected_current_item
            selected_text_item = self.editlist.currentItem().text()
            selected_row_item = self.editlist.currentRow()
            selected_current_item = self.editlist.currentItem()
            return selected_text_item, selected_row_item
        except:
            pass

    def edit_widget(self):
        global q_list_widget
        QToolTip.setFont(QFont('SansSerif', 10))
        self.resize(320, 484)
        ######## Label #########
        macro_label = QLabel("Input List", self)
        macro_label.setGeometry(10, 30, 141, 21)
        macro_label.setLineWidth(2)
        macro_label.setMidLineWidth(1)
        macro_label.setFrameShape(QFrame.Shape.Box)
        macro_label.setTextFormat(Qt.TextFormat.AutoText)
        macro_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        macro_label.setIndent(40)

        bind_label = QLabel("Hotkey Code", self)
        bind_label.setGeometry(242, 40, 75, 23)
        ######### End Label #########

        ######## Btns ##########
        self.edit_item_btn = QPushButton('Edit Event', self.edit_window)
        self.edit_item_btn.setToolTip('This is a <b>QPushButton</b> widget')
        self.edit_item_btn.resize(self.edit_item_btn.sizeHint())
        self.edit_item_btn.setGeometry(240, 100, 75, 23)
        self.edit_item_btn.clicked.connect(self.show_edit_item_window)

        self.save_item_btn = QPushButton('Save', self.edit_window)
        self.save_item_btn.resize(self.save_item_btn.sizeHint())
        self.save_item_btn.setGeometry(240, 130, 75, 23)
        self.save_item_btn.clicked.connect(self.save_edit_widget)

        self.add_item_btn = QPushButton('Add Event', self.edit_window)
        self.add_item_btn.resize(self.add_item_btn.sizeHint())
        self.add_item_btn.setGeometry(240, 70, 75, 23)
        self.add_item_btn.clicked.connect(self.show_add_item_window)

        self.delete_item_btn = QPushButton('Delete Event', self.edit_window)
        self.delete_item_btn.resize(self.delete_item_btn.sizeHint())
        self.delete_item_btn.setGeometry(240, 160, 75, 23)
        self.delete_item_btn.clicked.connect(self.delete_edit_widget)

        self.back_item_btn = QPushButton('Back', self.edit_window)
        self.back_item_btn.resize(self.back_item_btn.sizeHint())
        self.back_item_btn.setGeometry(240, 240, 75, 23)
        self.back_item_btn.clicked.connect(self.show_main_window)
        global bind_item_btns
        try:
            self.bind_item_btn = QPushButton(script_name[selected_item][0][10:], self.edit_window)
        except:
            self.bind_item_btn = QPushButton('Unbinded', self.edit_window)
        self.bind_item_btn.resize(self.bind_item_btn.sizeHint())
        self.bind_item_btn.setGeometry(240, 40, 75, 23)
        self.bind_item_btn.clicked.connect(self.bind_hotkey)
        bind_item_btns = self.bind_item_btn

        ########################
        self.editlist = QListWidget(self.edit_window)
        self.editlist.setGeometry(10, 41, 141, 401)
        try:
            self.editlist.addItems(script_name[selected_item][1:])
        except:
            pass
        self.editlist.itemSelectionChanged.connect(self.selection_edit_Changed)

        MainWindow.the_menu(self)
        self.setWindowTitle('SkyMacro')
        self.setWindowIcon(QIcon('thelogo.png'))
        self.setCentralWidget(self.edit_window)

        q_list_widget = self.editlist

    def show_donate_window(self, checked):
        if self.donate_window is None:
            self.donate_window = DonateWindow()
        self.donate_window.show()

    def onMyToolBarButtonClick(self, s):
        self.close()

    def show_main_window(self, checked):
        self.close()
        self.main_window = MainWindow()
        self.main_window.show()

    def bind_hotkey(self):
        try:
            inputs = get_hotkey()
            script_name[selected_item][0] = f"bindedkey={inputs[1]}"
            bind_item_btns.setText(str(inputs[0]))
        except:
            pass

    def show_help_window(self, checked):
        if self.help_window is None:
            self.help_window = HelpWindow()
        self.help_window.show()

    ########## Save Edit #######
    def save_edit_widget(self):
        with open("macro_file.txt", "w") as fi:
            for k, v in script_name.items():
                if k:
                    fi.write(str(f"[{k}]" + "\n"))
                if v:
                    for item in v:
                        if item.startswith("bindedkey="):
                            fi.write(item + "\n")
                        if item.replace('.', '', 1).isdigit():
                            fi.write(f"d={item}" + "\n")
                        if not item.startswith("bindedkey=") and not item.replace('.', '', 1).isdigit():
                            fi.write("e={" + f"{item}" + "}" + "\n")
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Saved!")
            dlg.setText("Macro Saved!")
            button = dlg.exec()

            if button == QMessageBox.StandardButton.Ok:
                print("OK!")

    ##############################
    def delete_edit_widget(self):
        try:
            q_list_widget.takeItem(selected_row_item)
            selected_current_item = None
            update_value = []
            keybind = [script_name[selected_item][0]]
            for i in range(q_list_widget.count()):
                item = q_list_widget.item(i)
                update_value.append(item.text())
            script_name[selected_item] = keybind + update_value
            show_edit_item_window.close()
            print(script_name)
        except:
            pass

    class EditItemWindow(QWidget):
        def __init__(self):
            super().__init__()
            global line_to_edit
            layout = QVBoxLayout()
            self.line_edit = QLineEdit(
                f"{selected_text_item}")
            self.ok_edit_item_btn = QPushButton('Ok')
            self.close_edit_item_btn = QPushButton('Cancel')
            self.ok_edit_item_btn.clicked.connect(EditWindow.EditItemWindow.ok_edit_item_window)

            layout.addWidget(self.line_edit)
            layout.addWidget(self.ok_edit_item_btn)
            self.setLayout(layout)
            self.setWindowTitle(f'{selected_text_item}')
            self.resize(260, 122)
            self.line_edit.installEventFilter(self)
            line_to_edit = self.line_edit

        def ok_edit_item_window(self):
            selected_edit_item.setText(line_to_edit.text())
            update_value = []
            keybind = [script_name[selected_item][0]]
            for i in range(q_list_widget.count()):
                item = q_list_widget.item(i)
                update_value.append(item.text())
            script_name[selected_item] = keybind + update_value
            show_edit_item_window.close()
            print(script_name)

        def eventFilter(self, obj, event):
            if obj == self.line_edit and event.type() == QEvent.Type.KeyPress and event.key() == Qt.Key.Key_Return:
                selected_edit_item.setText(line_to_edit.text())
                update_value = []
                keybind = [script_name[selected_item][0]]
                for i in range(q_list_widget.count()):
                    item = q_list_widget.item(i)
                    update_value.append(item.text())
                script_name[selected_item] = keybind + update_value
                show_edit_item_window.close()
                print(script_name)
            return super().eventFilter(obj, event)

    def show_edit_item_window(self, checked):
        try:
            global selected_edit_item
            global selected_text_item
            global selected_row_item
            global show_edit_item_window
            selected_edit_item = self.editlist.currentItem()
            selected_text_item = self.editlist.currentItem().text()
            selected_row_item = self.editlist.currentRow()
            self.edit_item_window = EditWindow.EditItemWindow()
            self.edit_item_window.show()
            show_edit_item_window = self.edit_item_window
            return selected_text_item, selected_row_item
        except:
            pass

    ############# Add item part #############
    class AddItemWindow(QWidget):
        def __init__(self):
            super().__init__()
            global line_to_add
            layout = QVBoxLayout()
            self.line_add = QLineEdit(
                f"")
            self.ok_add_item_btn = QPushButton('Ok')
            self.close_edit_item_btn = QPushButton('Cancel')
            self.ok_add_item_btn.clicked.connect(EditWindow.AddItemWindow.ok_add_item_window)
            layout.addWidget(self.line_add)
            layout.addWidget(self.ok_add_item_btn)
            self.setLayout(layout)
            self.setWindowTitle('Add Event')
            self.resize(260, 122)
            self.line_add.installEventFilter(self)

            line_to_add = self.line_add

        def ok_add_item_window(self):
            q_list_widget.addItem(line_to_add.text())
            update_value = []
            keybind = [script_name[selected_item][0]]
            print(keybind)
            for i in range(q_list_widget.count()):
                item = q_list_widget.item(i)
                update_value.append(item.text())
            script_name[selected_item] = keybind + update_value
            show_add_item_window.close()

        def eventFilter(self, obj, event):
            if obj == self.line_add and event.type() == QEvent.Type.KeyPress and event.key() == Qt.Key.Key_Return:
                q_list_widget.addItem(line_to_add.text())
                update_value = []
                keybind = [script_name[selected_item][0]]
                print(keybind)
                for i in range(q_list_widget.count()):
                    item = q_list_widget.item(i)
                    update_value.append(item.text())
                script_name[selected_item] = keybind + update_value
                show_add_item_window.close()
            return super().eventFilter(obj, event)

    def show_add_item_window(self, checked):
        global show_add_item_window
        self.add_item_window = EditWindow.AddItemWindow()
        self.add_item_window.show()
        show_add_item_window = self.add_item_window

##### End Edit #######

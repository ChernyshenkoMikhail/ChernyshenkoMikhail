import PyQt5

#Далее нужно создать окно для расширения. Для этого примените следующий код
app = PyQt5.QtWidgets.QApplication(sys.argv)
window = PyQt5.QtWidgets.QMainWindow()
window.setWindowTitle('My Extension')
window.show()
sys.exit(app.exec_())

#Также можно добавить дополнительные параметры, такие как иконка и размер окна, используя следующий код
window.setWindowIcon(QtGui.QIcon('icon.png'))
window.resize(500, 300)

#Далее нужно создать несколько элементов управления для окна расширения
button = QtWidgets.QPushButton('My Button', window)
button.clicked.connect(my_function)
window.setCentralWidget(button)

#добавить поддержку для браузеров
view = QtWebEngineWidgets.QWebEngineView()
view.setUrl(QtCore.QUrl('https://www.example.com'))
window.setCentralWidget(view)

#также можно добавить несколько других параметров, например, обратный вызов для загрузки страницы, используя другую функцию
view.loadFinished.connect(my_function)
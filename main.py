import sys
import io
import folium  # pip install folium
from folium import plugins
from folium.plugins import MiniMap
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine

"""
Folium in PyQt5
"""


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Folium Map')
        self.showMaximized()

        layout = QVBoxLayout()
        self.setLayout(layout)

        coordinate = (39.99999021143304400, 34.50000978856695600)
        m = folium.Map(
            tiles='openstreetmap',
            zoom_start=13,
            location=coordinate,control_scale=True, prefer_canvas=True
        )

        folium.Marker(coordinate, popup='IKA',icon=folium.Icon(icon="arrow-down")).add_to(m) #harita üzerinde mark eklemek için kullanılır.

        folium.Circle(
            radius=5000,
            location=coordinate,
            color='crimson',
            fill=False, ).add_to(m)#harita üzerinde yuvarlak çizmek için kullanılır.

        folium.CircleMarker(location=coordinate, radius=100, fill_color='red').add_to(m) #dinamik bi circle çizer

        minimap = plugins.MiniMap(position="topleft",width=250, height=250)
        m.add_child(minimap)






        # save map data to data object
        # data = io.BytesIO()
        # m.save(data, close_file=False)
        #
        # webView = QWebEngineView()
        # webView.setHtml(data.getvalue().decode())
        # layout.addWidget(webView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Kapatılıyor...')
import os


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

        m = folium.Map([37, 0], zoom_start=1, tiles="stamentoner")
        merc = os.path.join("", "un")

        # if not os.path.isfile(merc):
        #     print(f"Could not find {merc}")
        # else:
        #     img = folium.raster_layers.ImageOverlay(
        #         name="Mercator projection SW",
        #         image=merc,
        #         bounds=[[-82, -180], [82, 180]],
        #         opacity=0.6,
        #         interactive=True,
        #         cross_origin=False,
        #         zindex=1,
        #     )
        #
        #     folium.Popup("I am an image").add_to(img)
        #
        #     img.add_to(m)
        #
        #     m = folium.Map([37, 0], zoom_start=1, tiles="stamentoner")

        folium.raster_layers.ImageOverlay(
            image=merc,
            name="I am a jpeg",
            bounds=[[-82, -180], [82, 180]],
            opacity=1,
            interactive=False,
            cross_origin=False,
            zindex=1,
            alt="Wikipedia File:Mercator projection SW.jpg",
        ).add_to(m)

        folium.LayerControl().add_to(m)

        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


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
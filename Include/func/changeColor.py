# This Python file uses the following encoding: utf-8
from PySide6.QtGui import QPixmap, QPainter, QIcon, QColor


def changeSVGColor(svg_filepath, color='darkCyan'):
    img = QPixmap(svg_filepath)
    qp = QPainter(img)
    qp.setCompositionMode(QPainter.CompositionMode_SourceIn)
    qp.fillRect(img.rect(), QColor(color))
    qp.end()
    return QIcon(img)
# if __name__ == "__main__":
#     pass

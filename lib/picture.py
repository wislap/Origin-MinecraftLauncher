from PySide6.QtGui import QPixmap,Qt,QPainter,QPainterPath

def Face_Ico_Processing(pixmapa_file,Face_ico_Size):
    pixmap = QPixmap(Face_ico_Size,Face_ico_Size)
    pixmap.fill(Qt.transparent)
    painter = QPainter(pixmap)
    #painter.begin(selff)  # 要将绘制过程用begin(self)和end()包起来
    painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)  # 一个是平滑，一个是缩放保持比例
    path = QPainterPath()
    path.addEllipse(0, 0, Face_ico_Size, Face_ico_Size)  # 绘制椭圆
    painter.setClipPath(path)
    painter.drawPixmap(0, 0, Face_ico_Size, Face_ico_Size, pixmapa_file)
    #painter.end()
    return pixmap


#!/usr/bin/env python
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtNetwork import *
from datetime import datetime

def fmtime(x):
  h,s = divmod(x,3600)
  m,s = divmod(s,60)
  return f"{h:02d}:{m:02d}:{s:02d}"

def clamp(x,a,b):
  return max(min(x,b),a)

class Countdown(QWidget):
  def handleUdp(self):
    self.app.quit()

  def __init__(self,t0):
    """Countdown(t0)
    t0 is integer timestamp of finishing time
    """
    super().__init__()
    self.app = QApplication.instance()

    # so we can kill via sending UDP to 2000
    self.udpSocket = QUdpSocket()
    self.udpSocket.readyRead.connect(self.handleUdp)
    try:
      if not self.udpSocket.bind(QHostAddress.Any,2000):
        raise Exception("Address bind failed")
    except Exception:
      print(f"Failed to bind UDP port 2000")
      exit(1)
      self.app.quit()

    m = 100
    self.t0 = t0
    scr = QGuiApplication.primaryScreen()
    geom = scr.geometry()
    sh = geom.height()
    sw = geom.width()

    x = m
    y = m
    w = sw-2*m
    h = sh-2*m
    self.w = w
    self.h = h

    # size and position – possibly necessary to recompute, resize and move depending on hud contents
    self.resize(w,h)
    self.move(x,y)
    #self.resize(600,600)

    # attributes for display
    self.fontname = "Optima"
    self.fontsize = 200
    self.font = QFont(self.fontname,self.fontsize)
    self.color = QColor(100,255,100)
    self.ocolor = Qt.black
    self.pen = QPen(self.ocolor,16)

    self.content = "Countdown"

    # window attributes
    self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    self.setAttribute(Qt.WA_TranslucentBackground)
    self.n = 60

    self.timer = QTimer(self)
    self.timer.setInterval(1000)
    self.timer.timeout.connect(self.ping)

    self.ping()

  def go(self):
    self.show()
    self.timer.start()

  def ping(self):
    try:
      t = int(datetime.now().timestamp())
      dt = self.t0 - t
      if dt < 0:
        self.app.quit()
      self.content = fmtime(dt)
      self.update()
    except KeyboardInterrupt:
      print("Keyboard Interrupt")
      self.app.quit()

  def paintEvent(self,event):
    with QPainter(self) as p:
      text = self.content
      metrics = QFontMetrics(self.font)
      tw = metrics.horizontalAdvance(text)
      x = (self.w-tw)/2
      h = metrics.height()
      sh = self.h
      dh = (sh-h)/2
      y = dh+h

      path = QPainterPath()
      path.addText(x,y,self.font,str(text))

      # draw twice so that the black outline is _behind_ the fill
      p.setPen(self.pen)
      p.drawPath(path)
      p.setBrush(self.color)
      p.setPen(Qt.NoPen)
      p.drawPath(path)

  def mousePressEvent(self,e):
    if e.button() == Qt.RightButton:
      print("Right click")
      self.app.quit()
    super().mousePressEvent(e)

  def finish(self):
    app.quit()

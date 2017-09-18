# -*- coding: utf-8 -*-
"""
中文世界用百度毫无头绪，Google 之后，发现在How to create PDF files in Python 中第二名的答案提到ReportLab很好用，那位网友亦贴出一段代码，我试过之后确实成功地将图片变成了PDF但只有一页。翻了ReportLab的使用手册将近两个小时，最后在搜索中找到结果，showPage就是停止当前页的指令，然后再次写入，就创造出第二页、第三页了。

注给不熟悉编程的人：

我写的这几行代码中，

E:\\Q 是需要替换的，换成你电脑里的目标路径。

倒数第八行中间的两个0，是图片插入的坐标轴，width 同 height 等于图片的尺寸，可以自由调整。

如果你的图片是其他的格式，还需要把 jpg 改成所对应的图片格式。

实现自动判断图片格式并写入也是可以的。我有点懒……

不过需要大量导入的应该都会统一格式吧……
https://zhuanlan.zhihu.com/p/20709824
"""

from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas


f_pdf = 'xx.pdf'
(w, h) = landscape(A4)
c = canvas.Canvas(f_pdf, pagesize = landscape(A4))
for i in range(3):
    f=str(i+1)+'.BMP'
    c.drawImage(f, 0, 0, w, h)
    c.showPage()
c.save()
print "okkkkkkkk."
 

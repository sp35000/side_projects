#!/usr/bin/python
import qrcode
text = 'http://work4love.net/'
img = qrcode.make(text)
img.show()

#!/usr/bin/env python3
"""Regenerate Desk PNG icons. Requires Pillow."""
from PIL import Image, ImageDraw
from pathlib import Path
root = Path(__file__).resolve().parents[1] / 'desktop' / 'assets'
root.mkdir(parents=True, exist_ok=True)
BLUE=(61,139,253,255); BG=(21,32,54,255)
def icon(name, fn, size=64):
    im=Image.new('RGBA',(size,size),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((2,2,size-3,size-3), radius=14, fill=BG); fn(d,size); im.save(root/name)
def start(d,s):
    d.ellipse((12,12,s-13,s-13), outline=BLUE, width=3)
    d.line((s//2,18,s//2,s//2), fill=BLUE, width=3)
icon('start-icon.png', start)
print('wrote', root)

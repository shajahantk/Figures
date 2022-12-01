#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
from matplotlib.patches import FancyArrow
import matplotlib.patches as patches
import os
from pathlib import Path
import config



fig=plt.figure(figsize=(12,6))
"""
ax1=fig.add_subplot(131)
arrowPatch = FancyArrow(0.3, 0.8, 0.3, 0.0, width=0.01,
               length_includes_head=False,
               head_width=0.02, head_length=0.02,
               shape='full', overhang=0,
               head_starts_at_zero=False,
               transform=ax1.figure.transFigure,
               clip_on=False, color="black", linewidth=0.1)

ax1.add_patch(arrowPatch)
#ax1.text(0, -5, "(a)", fontsize=10, color="k",weight='bold')
ax1.text(0.7, 0.9, "$\overrightarrow{E}$", fontsize=10, color="black",weight='bold')
ax1.set_axis_off()
"""
#Give figure numbers below

#ACW
img_list=[]
for img in os.listdir():
    if img.endswith('.png'):
        img_list.append(img)
try:
   os.makedirs("ArrowImages")
except FileExistsError:
   # directory already exists
   pass
x=config.x
y=config.y
omega=config.omega
for t,img in enumerate(img_list):
    im=mpimg.imread(img)
    angle=omega*t
    dx = 25*np.cos(angle)
    dy = 25*np.sin(angle)
    plt.imshow(im)
    plt.arrow(x, y, dx,dy,head_width = 2, width = 0.05)
    fname=Path(img).stem
    fname2='ArrowImages/'+fname+'arrow.png'
    plt.savefig(fname2)
    plt.clf()



# In[ ]:





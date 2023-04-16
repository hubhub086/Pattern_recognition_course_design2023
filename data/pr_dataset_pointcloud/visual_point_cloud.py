# -*- coding: utf-8 -*-
import os 
import imageio
import numpy as np
import mayavi.mlab


point_cloud_path = "E:\\模式识别课设\\MDepth-00000001.npy"
cloud_im = np.load(point_cloud_path).transpose(1,0)

xx= cloud_im[0,:]
yy= cloud_im[1,:]
zz= cloud_im[2,:]


mayavi.mlab.figure(fgcolor=(0.5, 0.5, 0.5), bgcolor=(1, 1, 1))
nodes = mayavi.mlab.points3d(-xx, -yy, zz ,mode="cube", scale_factor="10")
nodes.glyph.scale_mode = 'scale_by_vector'

mayavi.mlab.view(azimuth= 00, elevation=185,distance=9800,roll = None)
mayavi.mlab.show()
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 11:01:03 2016

@author: Ka Wai Tsoi
"""

import vtk

# Write mesh data into a PLY file
# Input: desired path and name of the PLY file 
#        input mesh data, should be a vtkPolyData object
class vtkPLYWriter:
    def __init__(self, filename, inputData):
        self.writer = vtk.vtkPLYWriter()
        self.writer.SetFileTypeToASCII()
        self.writer.SetFileName(filename)
        self.writer.SetInputConnection(inputData)
        self.writer.Write()        
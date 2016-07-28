# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 15:38:24 2016

@author: Ka Wai Tsoi
"""

import vtk

# Smooth the mesh
class vtkSmoothPolyDataFilter:
    
    # Input: path and name of the ply file of the mesh to be smoothed
    #        the number of iterations to smooth the mesh. higher number results in more smooth result but  will the mesh will shink
    #        relaxation factor, recommended to be 0.1
    def __init__(self, fileName, iteration, relaxation):
        self.reader = vtk.vtkPLYReader()
        self.reader.SetFileName(fileName)
        self.reader.Update()
        self.inputPolyData = self.reader.GetOutput()
        self.iter = iteration
        self.rela = relaxation

    def SetInputData(self, data):
        self.inputPolyData = data    
    
    # Begin to smooth the mesh
    def Smooth(self):
        self.smooth = vtk.vtkSmoothPolyDataFilter()
        self.smooth.SetInputData(self.inputPolyData)
        self.smooth.SetNumberOfIterations(self.iter)
        self.smooth.SetRelaxationFactor(self.rela)
        self.smooth.SetConvergence(0.0)
        #self.smooth.FeatureEdgeSmoothingOff()
        #self.smooth.BoundarySmoothingOff()
        self.smooth.Update()
        #########################
        self.normalGenerator = vtk.vtkPolyDataNormals()
        self.normalGenerator.SetInputConnection(self.smooth.GetOutputPort())
        self.normalGenerator.ComputePointNormalsOff()
        self.normalGenerator.ComputeCellNormalsOff()
        self.normalGenerator.Update()
        self.outputPolyData = self.normalGenerator.GetOutput()
        
      




# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 15:14:47 2016

@author: Ka Wai Tsoi
"""
import vtk

class visualCompare:

    def __init__(self, inputData, outputData):
        self.inputPolyData = inputData
        self.outputPolyData = outputData
    
    def SetInputMapper(self):
            self.inputMapper = vtk.vtkPolyDataMapper()
            self.inputMapper.SetInputData(self.inputPolyData)
          
    def SetInputActor(self):
        self.inputActor = vtk.vtkActor()
        self.inputActor.SetMapper(self.inputMapper)
        self.inputActor.GetProperty().SetInterpolationToFlat()

    def SetDecimatedMapper(self):
        self.decimatedMapper = vtk.vtkPolyDataMapper()
        self.decimatedMapper.SetInputData(self.outputPolyData)

    def SetDecimatedActor(self):
        self.decimatedActor = vtk.vtkActor()
        self.decimatedActor.SetMapper(self.decimatedMapper)
       
    def SetRenderWindow(self):
        self.renderWindow = vtk.vtkRenderWindow()
        self.renderWindow.SetSize(600, 300)

    def SetInteractor(self):
        self.interactor = vtk.vtkRenderWindowInteractor()
        self.interactor.SetRenderWindow(self.renderWindow)

    def Render(self):
        self.leftViewport = [0.0, 0.0, 0.5, 1.0]
        self.rightViewport = [0.5, 0.0, 1.0, 1.0]
        self.leftRenderer = vtk.vtkRenderer()
        self.rightRenderer = vtk.vtkRenderer()
        self.renderWindow.AddRenderer(self.leftRenderer)
        self.leftRenderer.SetViewport(self.leftViewport)
        self.leftRenderer.SetBackground(0.6, 0.5, 0.4)
        self.renderWindow.AddRenderer(self.rightRenderer)
        self.rightRenderer.SetViewport(self.rightViewport)
        self.rightRenderer.SetBackground(0.4, 0.5, 0.6);
        self.leftRenderer.AddActor(self.inputActor)
        self.rightRenderer.AddActor(self.decimatedActor)
        self.camera = vtk.vtkCamera()
        self.leftRenderer.SetActiveCamera(self.camera)
        self.rightRenderer.SetActiveCamera(self.camera)
        self.leftRenderer.ResetCamera()
        self.renderWindow.Render()
        self.interactor.Start()
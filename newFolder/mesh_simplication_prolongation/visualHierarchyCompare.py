# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 14:07:59 2016

@author: Ka Wai Tsoi
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 15:14:47 2016

@author: Ka Wai Tsoi
"""
import vtk

# To visulize and compare the mesh hierarchy
class visualHierarchyCompare:

    # Input: 4 input mesh data, all should be vtkPolyData objects
    def __init__(self, inputData1, inputData2, inputData3, inputData4):
        self.inputPolyData1 = inputData1
        self.inputPolyData2 = inputData2
        self.inputPolyData3 = inputData3
        self.inputPolyData4 = inputData4
    
    def SetInputMapper(self):
        self.inputMapper1 = vtk.vtkPolyDataMapper()
        self.inputMapper1.SetInputData(self.inputPolyData1)
        self.inputMapper2 = vtk.vtkPolyDataMapper()
        self.inputMapper2.SetInputData(self.inputPolyData2)
        self.inputMapper3 = vtk.vtkPolyDataMapper()
        self.inputMapper3.SetInputData(self.inputPolyData3)
        self.inputMapper4 = vtk.vtkPolyDataMapper()
        self.inputMapper4.SetInputData(self.inputPolyData4)
          
    def SetInputActor(self):
        self.inputActor1 = vtk.vtkActor()
        self.inputActor1.SetMapper(self.inputMapper1)
        self.inputActor1.GetProperty().SetInterpolationToFlat()
        self.inputActor2 = vtk.vtkActor()
        self.inputActor2.SetMapper(self.inputMapper2)
        self.inputActor3 = vtk.vtkActor()
        self.inputActor3.SetMapper(self.inputMapper3)
        self.inputActor4 = vtk.vtkActor()
        self.inputActor4.SetMapper(self.inputMapper4)

       
    def SetRenderWindow(self):
        self.renderWindow = vtk.vtkRenderWindow()
        self.renderWindow.SetSize(1200, 1200)

    def SetInteractor(self):
        self.interactor = vtk.vtkRenderWindowInteractor()
        self.interactor.SetRenderWindow(self.renderWindow)

    def Render(self):
        self.Viewport1 = [0.0, 0.0, 0.5, 0.5]
        self.Viewport2 = [0.5, 0.0, 1.0, 0.5]
        self.Viewport3 = [0.0, 0.5, 0.5, 1.0]
        self.Viewport4 = [0.5, 0.5, 1.0, 1.0]
        self.Renderer1 = vtk.vtkRenderer()
        self.Renderer2 = vtk.vtkRenderer()
        self.Renderer3 = vtk.vtkRenderer()
        self.Renderer4 = vtk.vtkRenderer()
        self.renderWindow.AddRenderer(self.Renderer1)
        self.Renderer1.SetViewport(self.Viewport1)
        self.Renderer1.SetBackground(0.6, 0.5, 0.3)
        self.renderWindow.AddRenderer(self.Renderer2)
        self.Renderer2.SetViewport(self.Viewport2)
        self.Renderer2.SetBackground(0.5, 0.5, 0.4)
        self.renderWindow.AddRenderer(self.Renderer3)
        self.Renderer3.SetViewport(self.Viewport3)
        self.Renderer3.SetBackground(0.4, 0.5, 0.5)
        self.renderWindow.AddRenderer(self.Renderer4)
        self.Renderer4.SetViewport(self.Viewport4)
        self.Renderer4.SetBackground(0.0, 0.5, 0.6)
        self.Renderer1.AddActor(self.inputActor1)
        self.Renderer2.AddActor(self.inputActor2)
        self.Renderer3.AddActor(self.inputActor3)
        self.Renderer4.AddActor(self.inputActor4)
        self.camera = vtk.vtkCamera()
        self.Renderer1.SetActiveCamera(self.camera)
        self.Renderer2.SetActiveCamera(self.camera)
        self.Renderer3.SetActiveCamera(self.camera)
        self.Renderer4.SetActiveCamera(self.camera)
        self.Renderer1.ResetCamera()
        self.renderWindow.Render()
        self.interactor.Start()
"""
Created on Mon Jul 18 11:01:03 2016

@author: Ka Wai Tsoi
"""
import vtk

# Mesh simplification using decimate clustering algorithm and 
# match vertices of different mesh levels 
class vtkQuadricClustering:
    def __init__(self):
        pass
    

    # Read PLY mesh file
    # Input: path to the mesh PLY file    
    def readFile(self, fileName):
        self.reader = vtk.vtkPLYReader()
        self.reader.SetFileName(fileName)
        self.reader.Update()
        self.bounds = range(6)
        self.inputPolyData = self.reader.GetOutput()

    # Simplify the mesh using decimate clustering
    # Input: desired number of levels of mesh simplify hierarchy  
    def Cluster(self, i):
        self.inputPolyData.GetBounds(self.bounds)
        self.xRange = (self.bounds[1]-self.bounds[0])
        self.yRange = (self.bounds[3]-self.bounds[2])
        self.zRange = (self.bounds[5]-self.bounds[4])
        #Decimation Starts Here
        self.decimate = vtk.vtkQuadricClustering()
        self.decimate.AutoAdjustNumberOfDivisionsOff()
        self.decimate.UseInputPointsOn()
        self.decimate.SetNumberOfDivisions(int(self.xRange/(0.001*i)), int(self.yRange/(0.001*i)), int(self.zRange/(0.001*i)))
        self.decimate.SetInputData(self.inputPolyData)        
        self.decimate.Update()
        self.NumberOfDivisions = range(3)
        self.decimate.GetNumberOfDivisions(self.NumberOfDivisions)
        self.XBinSize = self.xRange/self.NumberOfDivisions[0]
        self.YBinSize = self.yRange/self.NumberOfDivisions[1]
        self.ZBinSize = self.zRange/self.NumberOfDivisions[2]
        self.outputPolyData = self.decimate.GetOutput()
        
        
    # Print number of input mesh vertices    
    def numInputPoints(self):
        print "Number of input points = %d" % (self.inputPolyData.GetNumberOfPoints())
        print "x bounds = %.3f, %.3f" % (self.bounds[0], self.bounds[1])
        print "y bounds = %.3f, %.3f" % (self.bounds[2], self.bounds[3])
        print "z bounds = %.3f, %.3f" % (self.bounds[4], self.bounds[5])
        
    # Print number of output mesh vertices 
    def numOutputPoints(self):
        print "Number of output points = %d" % (self.decimate.GetOutput().GetNumberOfPoints())


    # Given a vertex, clasify which bin it should belong to
    # Input: the 3D coordinates of the vertex as an array
    # Output: the bin ID of the bin this vertex belongs to
    def HashPoint(self, point):
        self.XBinStep = 1/self.XBinSize if self.XBinSize>0.0 else 0.0
        self.YBinStep = 1/self.YBinSize if self.YBinSize>0.0 else 0.0
        self.ZBinStep = 1/self.ZBinSize if self.ZBinSize>0.0 else 0.0
        
        xBinCoord = int( (point[0]-self.bounds[0]) * self.XBinStep )
        if xBinCoord < 0:
            xBinCoord = 0
        elif xBinCoord >= self.NumberOfDivisions[0]:
            xBinCoord = self.NumberOfDivisions[0]-1
        
        yBinCoord = int( (point[1]-self.bounds[2]) * self.YBinStep )
        if yBinCoord < 0:
            yBinCoord = 0
        elif yBinCoord >= self.NumberOfDivisions[1]:
            yBinCoord = self.NumberOfDivisions[1]-1
            
        zBinCoord = int( (point[2]-self.bounds[4]) * self.ZBinStep )
        if zBinCoord < 0:
            zBinCoord = 0
        elif zBinCoord >= self.NumberOfDivisions[2]:
            zBinCoord = self.NumberOfDivisions[2]-1
            
        binId = xBinCoord + yBinCoord*self.NumberOfDivisions[0] + zBinCoord*self.NumberOfDivisions[0]*self.NumberOfDivisions[1]
        return binId


    # Put every input/output vertex into its bin
    def HashVertices(self):
        self.numberOfBins = self.NumberOfDivisions[0]*self.NumberOfDivisions[1]*self.NumberOfDivisions[2]        
        self.inputVerticesBin = [[] for i in range(self.numberOfBins)]
        self.outputVerticesBin = [[] for i in range(self.numberOfBins)]
        
        for i in range (self.inputPolyData.GetNumberOfPoints()):
            binId = self.HashPoint(self.inputPolyData.GetPoint(i) ) 
            self.inputVerticesBin[binId].append(i)
            
        for i in range (self.outputPolyData.GetNumberOfPoints()):
            binId = self.HashPoint(self.outputPolyData.GetPoint(i) ) 
            self.outputVerticesBin[binId].append(i)
        
    # for every vertex in the finner level mesh, map it to its corresponding vertex in its next level corser mesh
    def VertexToVertex(self):
        self.VToVMap = [[-1] for j in range(self.inputPolyData.GetNumberOfPoints())]
        for i in range(self.numberOfBins):
            if len(self.outputVerticesBin[i])>0:
                for j in self.inputVerticesBin[i]:
                    self.VToVMap[j] = self.outputVerticesBin[i]
        














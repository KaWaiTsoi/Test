# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:36:16 2016

@author: Ka Wai Tsoi
"""
from collections import deque

# To compute the geodesic distance of vertices in a mesh
class GeodesicDistance:
    
    # Input: the mesh data, should be in a vtkPolyData object
    def __init__(self, input):
        self.input = input
        self.numPolys = input.GetPolys().GetNumberOfCells()
        self.numPoints = input.GetNumberOfPoints()
        
    # for every vertex, find faces that include that vertex
    # also, for every face, find its 3 vertices 
    def vertexFaceMap(self):
        p = self.input.GetPolys().GetData()
        self.MyMap = [[] for j in range(self.numPoints)]
        self.FaceToPoint = [[] for j in range(self.numPolys)]
        for i in range (self.numPolys):
            self.MyMap[p.GetValue(4*i+1)].append(i)
            self.MyMap[p.GetValue(4*i+2)].append(i)
            self.MyMap[p.GetValue(4*i+3)].append(i)
            self.FaceToPoint[i] = [p.GetValue(4*i+1), p.GetValue(4*i+2), p.GetValue(4*i+3)]
        
    # Compute the geodesic distance needed in our application, 
    # Input: maximum distance we would like to compute (e.g. 3), distances over this is not computed
    # Output: List of list of dimension [numberOfVertices x maxDistance]. Each row is for 1 vertex
    #         The first list contains vertices that are 1 edge away, the second list contains vertices 
    #         that are 2 edges away and so on.
    def computeDistance(self, maxDistance):
        self.distanceMap = [[set() for j in range(maxDistance)] for i in range(self.numPoints)]
        for i in range(self.numPoints):
            queueList = [deque() for j in range(maxDistance)]
            queueList[0].append(i)
            computed = set([i])
            for currentDis in range(maxDistance):
                while len(queueList[currentDis])>0:
                    ver = queueList[currentDis].popleft()
                    Faces = self.MyMap[ver]
                    for face in Faces:
                        vertices = self.FaceToPoint[face]
                        for v in vertices:
                            if v not in computed:
                                computed.add(v)
                                self.distanceMap[i][currentDis].add(v)
                                if currentDis < maxDistance-1 :
                                    queueList[currentDis+1].append(v)
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                
        
        
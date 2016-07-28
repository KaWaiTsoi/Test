from vtkQuadricClustering import vtkQuadricClustering
from visualHierarchyCompare import visualHierarchyCompare
from vtkSmoothPolyDataFilter import vtkSmoothPolyDataFilter
from vtkPLYWriter import vtkPLYWriter
from GeodesicDistance import GeodesicDistance


smooth = False
visual = False
meshes = []
x = vtkQuadricClustering()
x.readFile("C:\meshes\simon_face.ply")
s = vtkSmoothPolyDataFilter("c:/meshes/simon_face.ply", 5, 0.1)
meshes.append(x.inputPolyData)
# Perform the first decimation
x.Cluster(1)
print "x division = %f" % (x.xRange/(0.001))
x.numInputPoints()
x.numOutputPoints()
if smooth:
    s.SetInputData(x.outputPolyData)
    s.Smooth()        
    x.outputPolyData = s.outputPolyData
    vtkPLYWriter("C:\meshes\Smoothed_simon_face1", s.normalGenerator.GetOutputPort())
vtkPLYWriter("C:\meshes\Clustered_simon_face%s"%(1), x.decimate.GetOutputPort())
        
for i in range(2,4):
    x.inputPolyData = x.outputPolyData
    meshes.append(x.inputPolyData)
    x.Cluster(i)
    print "x division = %f" % (x.xRange/(0.001*i))
    x.numInputPoints()
    x.numOutputPoints()
    if smooth:
        s.SetInputData(x.outputPolyData)
        s.Smooth()        
        x.outputPolyData = s.outputPolyData
    vtkPLYWriter("C:\meshes\Clustered_simon_face%s"%(i), x.decimate.GetOutputPort())

meshes.append(x.outputPolyData)

if visual:
    y = visualHierarchyCompare(meshes[0],meshes[1],meshes[2],meshes[3])
    y.SetInputMapper()
    y.SetInputActor()
    y.SetRenderWindow()
    y.SetInteractor()
    y.Render()
    
x.VertexToVertex()
x.HashVertices()
a = []
for i in range(x.numberOfBins):
    if len(x.inputVerticesBin[i])>0:
        a.append(i)
        
b = []
for i in range(x.numberOfBins):
    if len(x.outputVerticesBin[i])>0:
        b.append(i)

print "len(a) = %d , len(b)=%d  " %(len(a), len(b))

f = GeodesicDistance(x.outputPolyData)
f.vertexFaceMap()
f.computeDistance(3)
v = x.VToVMap
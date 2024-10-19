import pyslm
import pyslm.visualise
from pyslm import hatching as hatching

# Imports the part and sets the geometry to an STL file (frameGuide.stl)
solidPart = pyslm.Part('myFrameGuide')
solidPart.setGeometry('../models/frameGuide.stl')

# Set te slice layer position
z = 23.

# Create a StripeHatcher object for performing any hatching operations
myHatcher = hatching.StripeHatcher()
myHatcher.stripeWidth = 5.0 # [mm]

# Set the base hatching parameters which are generated within Hatcher
myHatcher.hatchAngle = 10 # [°]
myHatcher.volumeOffsetHatch = 0.08 # [mm]
myHatcher.spotCompensation = 0.06 # [mm]
myHatcher.numInnerContours = 2
myHatcher.numOuterContours = 1

# Slice the object at Z and get the boundaries
geomSlice = solidPart.getVectorSlice(z)

# Perform the hatching operations
layer = myHatcher.hatch(geomSlice)

# Plot the layer geometries generated
pyslm.visualise.plot(layer, plot3D=False, plotOrderLine=True) # plotArrows=True)

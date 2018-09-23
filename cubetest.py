import cubeanim
import cubeenums

#cub = cube.Cube()
#print(cub.positions)

ca = cubeanim.CubeAnim()

ca.rotateFace('F1', 0, 60)

# F neg is cw, pos is ccw
# L neg is ccw, pos is cw

#exec(compile(open("C:\workspaces\BlenderCube\cubeanim.py").read(), "C:\workspaces\BlenderCube\cubetest.py", 'exec'))

import sys
import importlib
sys.path.append('C:\workspaces\BlenderCube')
import cube
import cubeenums
importlib.reload(cube)
importlib.reload(cubeenums)
c = cube.Cube()
c.rotateFace('F1', cubeenums.Direction.CW, 1, 60)
c.rotateFace('L1', cubeenums.Direction.CCW, 60, 120)
c.rotateFace('F1', cubeenums.Direction.CW, 120, 180)
c.rotateAllZ(cubeenums.Direction.CCW, 180, 240)



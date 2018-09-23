import bpy
import math
import cube

class CubeAnim:
    def __init__(self):
        self.thecube = cube.Cube()

        #give all cubies a keyframe at 1
        for cubie in self.thecube.positions:
            #print(self.thecube.positions[cubie])
            #bpy.context.scene.frame_current = 1
            cubiename = self.thecube.positions[cubie]
            print(cubiename)
            obj = bpy.data.objects.get(cubiename)
            obj.keyframe_insert('rotation_euler')

    def rotateFace(self, face, axis, tokeyfrm):

        selections = {}

        if face == "F1":
            selections = {
                bpy.data.objects.get(self.thecube.positions[1]),
                bpy.data.objects.get(self.thecube.positions[2]),
                bpy.data.objects.get(self.thecube.positions[3]),
                bpy.data.objects.get(self.thecube.positions[4]),
                bpy.data.objects.get(self.thecube.positions[5]),
                bpy.data.objects.get(self.thecube.positions[6]),
                bpy.data.objects.get(self.thecube.positions[7]),
                bpy.data.objects.get(self.thecube.positions[8]),
                bpy.data.objects.get(self.thecube.positions[9])
            }

        for cubie in selections:
            print(cubie)
            #bpy.context.scene.frame_current = tokeyfrm
            #cubie.rotation_euler[axis] += (2 * math.pi)
            #cubie.keyframe_insert('rotation_euler')
'''
    def TestKeyframe(self):
        
        bpy.context.scene.frame_set(x)
        bpy.ops.object.select_pattern(pattern="Cube1") #select something so we can toggle everything unselected next
        bpy.ops.object.select_all(action='TOGGLE') #unselects all
        bpy.ops.object.select_pattern(pattern="Cube4")
        
        ob = bpy.data.objects.get("Cube4")

        bpy.context.scene.frame_current = 1
        ob.keyframe_insert('rotation_euler')
        
        #bpy.ops.anim.keyframe_insert()
        
        bpy.context.scene.frame_current = 60

        ob.rotation_euler[0] += (2 * math.pi)
        ob.keyframe_insert('rotation_euler')

        #bpy.context.object.rotation_euler[0] +=  (2 * math.pi)
        #bpy.ops.anim.keyframe_insert()
        return
'''

#exec(compile(open("C:\workspaces\BlenderCube\cubeanim.py").read(), "C:\workspaces\BlenderCube\cubeanim.py", 'exec'))


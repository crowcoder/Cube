import bpy
import math

def TestKeyframe():
    '''
    bpy.context.scene.frame_set(x)
    bpy.ops.object.select_pattern(pattern="Cube1") #select something so we can toggle everything unselected next
    bpy.ops.object.select_all(action='TOGGLE') #unselects all
    bpy.ops.object.select_pattern(pattern="Cube4")
    '''

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

TestKeyframe()

#exec(compile(open("C:\workspaces\BlenderCube\cubeanim.py").read(), "C:\workspaces\BlenderCube\cubeanim.py", 'exec'))


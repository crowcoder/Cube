import bpy
import math
import copy
import cubeenums

class Cube:
    
    def __init__(self):
        self.positions = {
            1 : 'WhtGrRed',
            2 : 'WhtRed',
            3 : 'WhtBlRed',
            4 : 'GrRed',
            5 : 'Red',
            6 : 'BlRed',
            7 : 'GrRedYlw',
            8 : 'RedYlw',
            9 : 'BlRedYlw',
            10 : 'GrWht',
            11 : 'Wht',
            12 : 'WhtBl',
            13 : 'Gr',
            15 : 'Bl',
            16 : 'GrYlw',
            17 : 'Ylw',
            18 : 'BlYlw',
            19 : 'WhtGrOr',
            20 : 'WhtOr',
            21 : 'WhtBlOr',
            22 : 'GrOr',
            23 : 'Or',
            24 : 'OrBl',
            25 : 'OrGrYlw',
            26 : 'OrYlw',
            27 : 'OrBlYlw'
        }

        self.cubieParent = bpy.data.objects.get("Empty") 

    def rotateAllZ(self, direction, fromkeyfrm, tokeyfrm):
        
        for pos in range(1, 28):
            if pos != 14:
                cubie = bpy.data.objects.get(self.positions[pos])                

                bpy.context.scene.frame_current = fromkeyfrm
                cubie.keyframe_insert('rotation_euler')
                
                bpy.context.scene.frame_current = tokeyfrm
                cubie.rotation_euler[2] += 1.5708 * direction.value # (math.pi * 90 / 180) * direction.value
                cubie.keyframe_insert('rotation_euler')

        if direction == cubeenums.Direction.CW:
            self.RotateZPrime()
        else:
            self.RotateZ()

    def rotateFace(self, face, direction, fromkeyfrm, tokeyfrm): 
        axis = 0
        angle = 1
        
        self.UnparentAll()

        if face == "F1":
            selections = {
                bpy.data.objects.get(self.positions[1]),
                bpy.data.objects.get(self.positions[2]),
                bpy.data.objects.get(self.positions[3]),
                bpy.data.objects.get(self.positions[4]),
                bpy.data.objects.get(self.positions[5]),
                bpy.data.objects.get(self.positions[6]),
                bpy.data.objects.get(self.positions[7]),
                bpy.data.objects.get(self.positions[8]),
                bpy.data.objects.get(self.positions[9])
            }
            axis = cubeenums.Axis.X
            if direction == cubeenums.Direction.CW:                
                self.Front1()
                angle = -1
            else:
                self.Front1Prime()
                                
        if face == "L1":
            selections = {
                bpy.data.objects.get(self.positions[1]),
                bpy.data.objects.get(self.positions[4]),
                bpy.data.objects.get(self.positions[7]),
                bpy.data.objects.get(self.positions[10]),
                bpy.data.objects.get(self.positions[13]),
                bpy.data.objects.get(self.positions[16]),
                bpy.data.objects.get(self.positions[19]),
                bpy.data.objects.get(self.positions[22]),
                bpy.data.objects.get(self.positions[25])
            }
            axis = cubeenums.Axis.Y
            if direction == cubeenums.Direction.CW:
                self.Left1()                
            else:                
                self.Left1Prime()
                angle = -1
                                
        for cubie in selections:
            #print(cubie)
            bpy.context.scene.frame_current = fromkeyfrm
            cubie.keyframe_insert('rotation_euler')
            bpy.context.scene.frame_current = tokeyfrm
            cubie.parent = self.cubieParent

        for x in range(3):
            self.cubieParent.rotation_euler[axis.value] = 0

        self.cubieParent.rotation_euler[axis.value] += (1.5708 * angle)
        # math.pi / 2 * angle
        # ((90 * direction.value) * (math.pi / 180))            

        for cubie in selections:
            print(cubie)            
            self.select_cubie(cubie.name)
            bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
            cubie.keyframe_insert('rotation_euler')
        
        #reset the Empty's rotation so next spin resets from zero
        self.select_cubie("Empty")
        bpy.ops.object.rotation_clear(clear_delta=True)
        bpy.ops.object.select_all(action='TOGGLE') #unselects all

    def select_cubie(self, cubieName):
        bpy.ops.object.select_pattern(pattern="Empty") #select something so we can toggle everything unselected next
        bpy.ops.object.select_all(action='TOGGLE') #unselects all
        bpy.ops.object.select_pattern(pattern=cubieName)

    def UnparentAll(self):
        for pos in range(1, 28):
            if pos != 14:
                cubie = bpy.data.objects.get(self.positions[pos])
                cubie.parent = None

    def Front1(self):
        print("Before cloning F1")
        self.print_positions()
        orig = copy.deepcopy(self.positions)
        self.positions[3] = orig[1]
        self.positions[6] = orig[2]
        self.positions[9] = orig[3]
        self.positions[2] = orig[4]        
        self.positions[8] = orig[6]
        self.positions[1] = orig[7]
        self.positions[4] = orig[8]
        self.positions[7] = orig[9]
        print("After cloning F1")
        self.print_positions()

    def Front1Prime(self):
        #self.print_positions()
        orig = copy.deepcopy(self.positions)
        self.positions[7] = orig[1]
        self.positions[4] = orig[2]
        self.positions[1] = orig[3]
        self.positions[8] = orig[4]        
        self.positions[2] = orig[6]
        self.positions[9] = orig[7]
        self.positions[6] = orig[8]
        self.positions[3] = orig[9]

    def Front2(self):
        #self.print_positions()
        orig = copy.deepcopy(self.positions)
        self.positions[12] = orig[10]
        self.positions[15] = orig[11]
        self.positions[18] = orig[12]
        self.positions[11] = orig[13]        
        self.positions[17] = orig[15]
        self.positions[10] = orig[16]
        self.positions[13] = orig[17]
        self.positions[16] = orig[18]

    def Front2Prime(self):
        #self.print_positions()
        orig = copy.deepcopy(self.positions)
        self.positions[16] = orig[10]
        self.positions[13] = orig[11]
        self.positions[10] = orig[12]
        self.positions[17] = orig[13]        
        self.positions[11] = orig[15]
        self.positions[18] = orig[16]
        self.positions[15] = orig[17]
        self.positions[12] = orig[18]

    def Front3(self):
        #self.print_positions()
        orig = copy.deepcopy(self.positions)
        self.positions[21] = orig[19]
        self.positions[24] = orig[20]
        self.positions[27] = orig[21]
        self.positions[20] = orig[22]        
        self.positions[26] = orig[24]
        self.positions[19] = orig[25]
        self.positions[22] = orig[26]
        self.positions[25] = orig[27]

    def Front3Prime(self):
        #self.print_positions()
        orig = copy.deepcopy(self.positions)
        self.positions[25] = orig[19]
        self.positions[22] = orig[20]
        self.positions[19] = orig[21]
        self.positions[26] = orig[22]        
        self.positions[20] = orig[24]
        self.positions[27] = orig[25]
        self.positions[24] = orig[26]
        self.positions[21] = orig[27]

    def Left1(self):
        #self.print_positions()
        orig = copy.deepcopy(self.positions)
        self.positions[7] = orig[1]
        self.positions[16] = orig[4]
        self.positions[25] = orig[7]
        self.positions[4] = orig[10]  
        self.positions[22] = orig[16]
        self.positions[1] = orig[19]
        self.positions[10] = orig[22]
        self.positions[19] = orig[25]
        #self.print_positions()

    def Left1Prime(self):
        print("In Left2Prime")
        self.print_positions()
        orig = copy.deepcopy(self.positions)
        self.positions[19] = orig[1]
        self.positions[10] = orig[4]
        self.positions[1] = orig[7]
        self.positions[22] = orig[10]        
        self.positions[4] = orig[16]
        self.positions[25] = orig[19]
        self.positions[16] = orig[22]
        self.positions[7] = orig[25]
        self.print_positions()

    def Left2(self):
        #self.print_positions()
        orig = copy.deepcopy(self.positions)
        self.positions[8] = orig[2]
        self.positions[17] = orig[5]
        self.positions[26] = orig[8]
        self.positions[5] = orig[11]        
        self.positions[23] = orig[17]
        self.positions[2] = orig[20]
        self.positions[11] = orig[23]
        self.positions[20] = orig[26]

    def Left2Prime(self):
        #self.print_positions()
        orig = copy.deepcopy(self.positions)
        self.positions[20] = orig[2]
        self.positions[11] = orig[5]
        self.positions[2] = orig[8]
        self.positions[23] = orig[11]        
        self.positions[5] = orig[17]
        self.positions[26] = orig[20]
        self.positions[17] = orig[23]
        self.positions[8] = orig[26]

    def Left3(self):
        #self.print_positions()
        orig = copy.deepcopy(self.positions)
        self.positions[9] = orig[3]
        self.positions[18] = orig[6]
        self.positions[27] = orig[9]
        self.positions[6] = orig[12]        
        self.positions[24] = orig[18]
        self.positions[3] = orig[21]
        self.positions[12] = orig[24]
        self.positions[21] = orig[27]

    def Left3Prime(self):
        #self.print_positions()
        orig = copy.deepcopy(self.positions)
        self.positions[21] = orig[3]
        self.positions[12] = orig[6]
        self.positions[3] = orig[9]
        self.positions[24] = orig[12]        
        self.positions[6] = orig[18]
        self.positions[27] = orig[21]
        self.positions[18] = orig[24]
        self.positions[9] = orig[27]

    def Top1(self):
        #self.print_positions()
        orig = copy.deepcopy(self.positions)
        self.positions[19] = orig[1]
        self.positions[10] = orig[2]
        self.positions[1] = orig[3]
        self.positions[20] = orig[10]        
        self.positions[2] = orig[12]
        self.positions[21] = orig[19]
        self.positions[12] = orig[20]
        self.positions[3] = orig[21]
        
    def Top1Prime(self):
        #self.print_positions()
        orig = copy.deepcopy(self.positions)
        self.positions[3] = orig[1]
        self.positions[12] = orig[2]
        self.positions[21] = orig[3]
        self.positions[2] = orig[10]        
        self.positions[20] = orig[12]
        self.positions[1] = orig[19]
        self.positions[10] = orig[20]
        self.positions[19] = orig[21]

    def Top2(self):
        #self.print_positions()
        orig = copy.deepcopy(self.positions)
        self.positions[22] = orig[4]
        self.positions[13] = orig[5]
        self.positions[4] = orig[6]
        self.positions[23] = orig[13]        
        self.positions[5] = orig[15]
        self.positions[24] = orig[22]
        self.positions[15] = orig[23]
        self.positions[6] = orig[24]

    def Top2Prime(self):
        #self.print_positions()
        orig = copy.deepcopy(self.positions)
        self.positions[6] = orig[4]
        self.positions[15] = orig[5]
        self.positions[24] = orig[6]
        self.positions[5] = orig[13]        
        self.positions[23] = orig[15]
        self.positions[4] = orig[22]
        self.positions[13] = orig[23]
        self.positions[22] = orig[24]

    def Top3(self):
        #self.print_positions()
        orig = copy.deepcopy(self.positions)
        self.positions[25] = orig[7]
        self.positions[16] = orig[8]
        self.positions[7] = orig[9]
        self.positions[26] = orig[16]        
        self.positions[8] = orig[18]
        self.positions[27] = orig[25]
        self.positions[18] = orig[26]
        self.positions[9] = orig[27]

    def Top3Prime(self):
        #self.print_positions()
        orig = copy.deepcopy(self.positions)
        self.positions[9] = orig[7]
        self.positions[18] = orig[8]
        self.positions[27] = orig[9]
        self.positions[8] = orig[16]  
        self.positions[26] = orig[18]
        self.positions[7] = orig[25]
        self.positions[16] = orig[26]
        self.positions[25] = orig[27]

    def RotateY(self):
        #self.print_positions()
        self.Left1()
        self.Left2()
        self.Left3()
        
    def RotateYPrime(self):
        #self.print_positions()
        self.Left1Prime()
        self.Left2Prime()
        self.Left3Prime()
    
    def RotateX(self):
        #self.print_positions()
        self.Front1()
        self.Front2()
        self.Front3()
        
    def RotateXPrime(self):
        #self.print_positions()
        self.Front1Prime()
        self.Front2Prime()
        self.Front3Prime()
        
    def RotateZ(self):
        #self.print_positions()
        self.Top1()
        self.Top2()
        self.Top3()

    def RotateZPrime(self):
        #self.print_positions()
        self.Top1Prime()
        self.Top2Prime()
        self.Top3Prime()

    def print_positions(self):
        print(self.positions)

# cub = Cube()
# print(cub.positions)
# print('-------------------')
# cub.Front1()
# print(cub.positions)
# print('-------------------')
# cub.Front1Prime()
# print(cub.positions)

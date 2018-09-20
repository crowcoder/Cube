import copy

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
            14 : 'pivot',
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

    def Front1(self):
        orig = copy.deepcopy(self.positions)
        self.positions[3] = orig[1]
        self.positions[6] = orig[2]
        self.positions[9] = orig[3]
        self.positions[2] = orig[4]        
        self.positions[8] = orig[6]
        self.positions[1] = orig[7]
        self.positions[4] = orig[8]
        self.positions[7] = orig[9]

    def Front1Prime(self):
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
        orig = copy.deepcopy(self.positions)
        self.positions[] = orig[19]
        self.positions[] = orig[20]
        self.positions[] = orig[21]
        self.positions[] = orig[22]        
        self.positions[] = orig[24]
        self.positions[] = orig[25]
        self.positions[] = orig[26]
        self.positions[] = orig[27]

    def Left1(self):
        orig = copy.deepcopy(self.positions)
        self.positions[] = orig[1]
        self.positions[] = orig[4]
        self.positions[] = orig[7]
        self.positions[] = orig[10]        
        self.positions[] = orig[16]
        self.positions[] = orig[19]
        self.positions[] = orig[22]
        self.positions[] = orig[25]

    def Left1Prime(self):
        orig = copy.deepcopy(self.positions)
        self.positions[] = orig[1]
        self.positions[] = orig[4]
        self.positions[] = orig[7]
        self.positions[] = orig[10]        
        self.positions[] = orig[16]
        self.positions[] = orig[19]
        self.positions[] = orig[22]
        self.positions[] = orig[25]

    def Left2(self):
        orig = copy.deepcopy(self.positions)
        self.positions[] = orig[2]
        self.positions[] = orig[5]
        self.positions[] = orig[8]
        self.positions[] = orig[11]        
        self.positions[] = orig[17]
        self.positions[] = orig[20]
        self.positions[] = orig[23]
        self.positions[] = orig[26]

    def Left2Prime(self):
        orig = copy.deepcopy(self.positions)
        self.positions[] = orig[2]
        self.positions[] = orig[5]
        self.positions[] = orig[8]
        self.positions[] = orig[11]        
        self.positions[] = orig[17]
        self.positions[] = orig[20]
        self.positions[] = orig[23]
        self.positions[] = orig[26]

    def Left3(self):
        orig = copy.deepcopy(self.positions)
        self.positions[] = orig[3]
        self.positions[] = orig[6]
        self.positions[] = orig[9]
        self.positions[] = orig[12]        
        self.positions[] = orig[19]
        self.positions[] = orig[21]
        self.positions[] = orig[24]
        self.positions[] = orig[27]

    def Left3Prime(self):
        orig = copy.deepcopy(self.positions)
        self.positions[] = orig[3]
        self.positions[] = orig[6]
        self.positions[] = orig[9]
        self.positions[] = orig[12]        
        self.positions[] = orig[19]
        self.positions[] = orig[21]
        self.positions[] = orig[24]
        self.positions[] = orig[27]

    def Top1(self):
        orig = copy.deepcopy(self.positions)
        self.positions[] = orig[1]
        self.positions[] = orig[2]
        self.positions[] = orig[3]
        self.positions[] = orig[10]        
        self.positions[] = orig[12]
        self.positions[] = orig[19]
        self.positions[] = orig[20]
        self.positions[] = orig[21]

    def Top1Prime(self):
        orig = copy.deepcopy(self.positions)
        self.positions[] = orig[1]
        self.positions[] = orig[2]
        self.positions[] = orig[3]
        self.positions[] = orig[10]        
        self.positions[] = orig[12]
        self.positions[] = orig[19]
        self.positions[] = orig[20]
        self.positions[] = orig[21]

    def Top2(self):
        orig = copy.deepcopy(self.positions)
        self.positions[] = orig[4]
        self.positions[] = orig[5]
        self.positions[] = orig[6]
        self.positions[] = orig[13]        
        self.positions[] = orig[15]
        self.positions[] = orig[22]
        self.positions[] = orig[23]
        self.positions[] = orig[24]

    def Top2Prime(self):
        orig = copy.deepcopy(self.positions)
        self.positions[] = orig[4]
        self.positions[] = orig[5]
        self.positions[] = orig[6]
        self.positions[] = orig[13]        
        self.positions[] = orig[15]
        self.positions[] = orig[22]
        self.positions[] = orig[23]
        self.positions[] = orig[24]

    def Top3(self):
        orig = copy.deepcopy(self.positions)
        self.positions[] = orig[7]
        self.positions[] = orig[8]
        self.positions[] = orig[9]
        self.positions[] = orig[16]        
        self.positions[] = orig[18]
        self.positions[] = orig[25]
        self.positions[] = orig[26]
        self.positions[] = orig[27]

    def Top3Prime(self):
        orig = copy.deepcopy(self.positions)
        self.positions[] = orig[7]
        self.positions[] = orig[8]
        self.positions[] = orig[9]
        self.positions[] = orig[16]  
        self.positions[] = orig[18]
        self.positions[] = orig[25]
        self.positions[] = orig[26]
        self.positions[] = orig[27]

    def RotateY(self):
        orig = copy.deepcopy(self.positions)
        self.positions[] = orig[1]
        self.positions[] = orig[2]
        self.positions[] = orig[3]
        self.positions[] = orig[4]
        self.positions[] = orig[5]
        self.positions[] = orig[6]
        self.positions[] = orig[7]
        self.positions[] = orig[8]
        self.positions[] = orig[9]
        self.positions[] = orig[10]
        self.positions[] = orig[11]
        self.positions[] = orig[12]
        self.positions[] = orig[14]
        self.positions[] = orig[16]
        self.positions[] = orig[17]
        self.positions[] = orig[18]
        self.positions[] = orig[19]
        self.positions[] = orig[20]
        self.positions[] = orig[21]
        self.positions[] = orig[22]
        self.positions[] = orig[23]
        self.positions[] = orig[24]
        self.positions[] = orig[25]
        self.positions[] = orig[26]
        self.positions[] = orig[27]
        
    def RotateYPrime(self):
        orig = copy.deepcopy(self.positions)
        self.positions[] = orig[1]
        self.positions[] = orig[2]
        self.positions[] = orig[3]
        self.positions[] = orig[4]
        self.positions[] = orig[5]
        self.positions[] = orig[6]
        self.positions[] = orig[7]
        self.positions[] = orig[8]
        self.positions[] = orig[9]
        self.positions[] = orig[10]
        self.positions[] = orig[11]
        self.positions[] = orig[12]
        self.positions[] = orig[14]
        self.positions[] = orig[16]
        self.positions[] = orig[17]
        self.positions[] = orig[18]
        self.positions[] = orig[19]
        self.positions[] = orig[20]
        self.positions[] = orig[21]
        self.positions[] = orig[22]
        self.positions[] = orig[23]
        self.positions[] = orig[24]
        self.positions[] = orig[25]
        self.positions[] = orig[26]
        self.positions[] = orig[27]        

    def RotateZ(self):
        orig = copy.deepcopy(self.positions)
        self.positions[] = orig[1]
        self.positions[] = orig[2]
        self.positions[] = orig[3]
        self.positions[] = orig[4]
        self.positions[] = orig[5]
        self.positions[] = orig[6]
        self.positions[] = orig[7]
        self.positions[] = orig[8]
        self.positions[] = orig[9]
        self.positions[] = orig[10]
        self.positions[] = orig[12]
        self.positions[] = orig[13]
        self.positions[] = orig[14]
        self.positions[] = orig[15]
        self.positions[] = orig[16]
        self.positions[] = orig[18]
        self.positions[] = orig[19]
        self.positions[] = orig[20]
        self.positions[] = orig[21]
        self.positions[] = orig[22]
        self.positions[] = orig[23]
        self.positions[] = orig[24]
        self.positions[] = orig[25]
        self.positions[] = orig[26]
        self.positions[] = orig[27]

    def RotateZPrime(self):
        orig = copy.deepcopy(self.positions)
        self.positions[] = orig[1]
        self.positions[] = orig[2]
        self.positions[] = orig[3]
        self.positions[] = orig[4]
        self.positions[] = orig[5]
        self.positions[] = orig[6]
        self.positions[] = orig[7]
        self.positions[] = orig[8]
        self.positions[] = orig[9]
        self.positions[] = orig[10]
        self.positions[] = orig[12]
        self.positions[] = orig[13]
        self.positions[] = orig[14]
        self.positions[] = orig[15]
        self.positions[] = orig[16]
        self.positions[] = orig[18]
        self.positions[] = orig[19]
        self.positions[] = orig[20]
        self.positions[] = orig[21]
        self.positions[] = orig[22]
        self.positions[] = orig[23]
        self.positions[] = orig[24]
        self.positions[] = orig[25]
        self.positions[] = orig[26]
        self.positions[] = orig[27]

cub = Cube()
print(cub.positions)
print('-------------------')
cub.Front1()
print(cub.positions)
print('-------------------')
cub.Front1Prime()
print(cub.positions)

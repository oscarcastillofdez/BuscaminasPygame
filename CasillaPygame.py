class Casilla():
    def __init__(self):
        self.marcado = False
        self.estado = False
        self.mina = False
        self.val = 0

    def convertirMina(self):
        self.mina = True

    def aumentarVal(self):
        self.val = self.val + 1

    def getVal(self) -> int:
        if (self.mina == True):
            return 0
        else:
            return self.val
        
    def mostrar(self):
        if (self.estado == True):
            return -2
        self.estado = True
        if (self.mina == True):
            return -1
        else:
            return self.val
        
    #Funcion antigua cuando se hacia por terminal
    def print(self):
        if (self.estado == False):
            print("[X]",end= " ")
        else: 
            if (self.mina == True):
                print("[O]",end= " ")
            else: 
                if (self.val == 0):
                    print("[ ]",end= " ")
                else:
                    print("["+ str(self.val) +"]",end= " ")
                    
    # Devuelve 0 si la casilla se puede seleccionar
    def seleccion(self):
        if (self.marcado == False) & (self.estado == False):
            return 1
        else:
            return 0

    def marcar(self):
        #Si ya se mostro no se hace nada si no se toggle la marca
        if self.estado == False:
            if self.marcado == False:
                self.marcado = True
                return 0
            else:
                self.marcado = False
                return 1
        else:
            return -1

    def mostrar(self) -> int:
        if (self.marcado == False) & (self.estado == False):
            self.estado = True
            if self.mina == True:
                return 9
            return self.val
        else:
            return -1





    

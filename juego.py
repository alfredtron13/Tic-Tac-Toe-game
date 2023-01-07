class TicTacToe:

    matriz = [" "] * 9 
    jugador = None 
    computadora = None
    
    def tablero(self):

        print("TRES EN RAYA / TIC TAC TOE")
        print("")
        print("1       |2       |3       ")
        print("    {}   |    {}   |     {}  ".format(self.matriz[0],self.matriz[1],self.matriz[2]))
        print("        |        |        ")
        print("--------------------------")
        print("4       |5       |6       ")
        print("    {}   |    {}   |     {}  ".format(self.matriz[3],self.matriz[4],self.matriz[5]))
        print("        |        |        ")
        print("--------------------------")
        print("7       |8       |9       ")
        print("    {}   |    {}   |     {}  ".format(self.matriz[6],self.matriz[7],self.matriz[8]))
        print("        |        |        ")


    def iniciar_juego(self):

        self.simbolo = input("Elija una ficha: X/O:\n")
        self.simbolo = self.simbolo.upper()

        while True:

            if self.simbolo == "X":

                self.jugador = "X"
                self.computadora = "O"
                break

            elif self.simbolo == "O":

                self.jugador = "O"
                self.computadora = "X"
                break

            else:

                self.simbolo = input("Porfavor ingrese una ficha valida:\n")
                self.simbolo = self.simbolo.upper()

    def empate(self):

        self.empatE = True
        self.i = 0 
        while (self.empatE == True) and (self.i < 9):
            if self.matriz[self.i] == " ":
                self.empatE = False 
            self.i += 1

        return self.empatE
   
    def victoria(self,matriz,ficha):

        if (matriz[0] == ficha and matriz[1] == ficha and matriz[2] == ficha) or (matriz[3] == ficha and matriz[4] == ficha and matriz[5] == ficha) or (matriz[6] == ficha and matriz[7] == ficha and matriz[8] == ficha) or (matriz[0] == ficha and matriz[3] == ficha and matriz[6] == ficha) or (matriz[1] == ficha and matriz[4] == ficha and matriz[7] == ficha) or (matriz[2] == ficha and matriz[5] == ficha and matriz[8] == ficha) or (matriz[0] == ficha and matriz[4] == ficha and matriz[8] == ficha) or (matriz[2] == ficha and matriz[4] == ficha and matriz[6] == ficha):

            return True 

        else:

            return False

    def movimiento_jugador(self):

        self.posiciones = [1,2,3,4,5,6,7,8,9]

        self.mov = int(input("¿Cual es tu proxima jugada?\n"))

        while True:

            if (not self.mov in self.posiciones):

                self.mov = int(input("Porfavor ingrese una posicion correcta:\n"))

            else:

                if self.matriz[self.mov - 1] == " ":

                    self.matriz[self.mov - 1] = self.jugador
                    break

                else:

                    self.mov = int(input("Posicion ocupada, ingrese una valida:\n"))

    def movimiento_computadora(self):

        import random

        self.posiciones = [0,1,2,3,4,5,6,7,8]
        self.casilla = None
    
        for i in self.posiciones:
            self.copia = list(self.matriz)
            if self.copia[i] == " ":
                self.copia[i] = self.computadora
                if self.victoria(self.copia,self.computadora) == True:
                    self.casilla = i 
        
        if self.casilla == None:

            for i in self.posiciones:
                self.copia = list(self.matriz)
                if self.copia[i] == " ":
                    self.copia[i] = self.jugador
                    if self.victoria(self.copia,self.jugador) == True:
                        self.casilla = i

        if self.casilla == None:
            
            self.casilla = random.randint(0,8)
            while not self.matriz[self.casilla] == " ":
                self.casilla = random.randint(0,8)

        self.matriz[self.casilla] = self.computadora

    def jugar(self):

        import os 
        import random 
        import time 

        self.turno = random.randint(0,1)
        self.iniciar_juego()

        if self.turno == 0:
            print("La computadora ira primero")
            self.tablero()
            print("La computadora esta pensando.....")
            self.movimiento_computadora()
            time.sleep(2)
            os.system("clear")
            self.tablero()
            self.turno = 1
        else:
            print("Empiezas tú")
            self.tablero()
            self.movimiento_jugador()
            os.system("clear")
            self.tablero()
            self.turno = 0 

        while True:

            if self.victoria(self.matriz,self.jugador):
                print("¡Ganaste!")
                break 
            elif self.victoria(self.matriz,self.computadora):
                print("¡Perdiste!")
                break
            elif self.empate() == True:
                print("Empate")
                break


            if self.turno == 0:
                print("La computadora esta pensando....")
                time.sleep(2)
                self.movimiento_computadora()
                os.system("clear")
                self.tablero()
                self.turno = 1
            else:
                self.movimiento_jugador()
                os.system("clear")
                self.tablero()
                self.turno = 0 
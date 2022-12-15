#INTEGRANTE:
#CRISTIAN JAVIER TARAPUEZ JARAMILLO
#SOLUCION TALLER

import sys
class Usuario():
    def __init__(self, nombre,apellido, cedula, edad ):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._edad = edad

    def  get_nombre(self):
           
        return  f"{self._nombre} {self._apellido} \ncedula: {self._cedula} \nedad: {self._edad}"

class Cuenta(Usuario):
    def  __init__(self, nombre, apellido, cedula, edad, saldo=0):
        super().__init__(nombre, apellido, cedula, edad)
        self._saldo = saldo

    def set_balance(self, saldo):
        self._saldo = saldo

    def get_balance(self):
        return self._saldo

    def estado_cuenta(self):
        print("Informacion De la Cuenta\nNombre:  ", self.get_nombre())
        print("Balance de cuenta:  $", self._saldo)

    def depositar (self, monto):
        if monto < 0:
            print ("------¡ALERTA!------\n Es imposible depositar un valor negativo en la cuenta")
            return
        
        self._saldo += monto
        print ("--------¡ALERTA!------\n Deposito exitoso , Su nuevo saldo es: $", self._saldo)

    def retirar (self, monto):
        if monto < 0:
            
            print ("-----¡ALERTA!-------\n Es imposible retirar un valor negativo en la cuenta")
            return
          
        elif self._saldo - monto < 0:
            print("-----¡ALERTA!------\n Fondos Insucficentes en la cuenta")

        else:
            self._saldo -= monto
            print ("------¡ALERTA!------\nRetiro Exitoso, Su nuevo saldo es: $", self._saldo)

class Beneficio(Cuenta):
    def __init__(self, nombre, apellido, cedula, edad, saldo):
   
        super().__init__(nombre, apellido, cedula, edad, saldo)
        
    def  es_beneficiario(self):
        if self._edad  > 18 and self._edad < 28:
           
            beneficio = self._saldo*0.05
            nuevosaldo=self._saldo+beneficio
            print("Su saldo es de : $",self._saldo,"\nSu Beneficio es de : $",beneficio,"\nSu Saldo total  es de: $",nuevosaldo)
        else:
            
            print("¡Alerta! \nUsted supera la edad para ser beneficiario\n su edad es de: ", self._edad)
    
usuario1 =Beneficio("Cristian", "Tarapuez", "1085938744", 27,1000000)


resp=1

while resp<= 1:
    try:
        opc=int(input("******************************************\nBienvenido a Nuestro Banco \n------------------------------------------\nSeleccione la opcion que desea realizar:\n------------------------------------------\n1.) Informacion de cuenta\n2.) Depositar dinero\n 3.) Retirar Dinero \n 4.) Mirar Beneficio\n 5.) Salir\n"))
    except:
        print("Opcion Icorrecta", file=sys.stderr)
        sys.exit()
    if opc == 1 :
        usuario1.estado_cuenta()
        resp=int(input("Desea realizar otra operacion?\n1=> Para SI\n2=> Para NO\n"))
        

    elif opc==2:
        usuario1.depositar(int(input("Ingrese el valor a Depositar\n")))
        resp=int(input("Desea realizar otra operacion?\n1=> Para SI\n2=> Para NO\n"))
        
        
    elif opc==3:
        usuario1.retirar(int(input("Monto a Retirar\n")))
        resp=int(input("Desea realizar otra operacion?\n1=> Para SI\n2=> Para NO\n"))
        
        
    elif opc==4:
        
        usuario1.es_beneficiario()
        resp=int(input("Desea realizar otra operacion?\n1=> Para SI\n2=> Para NO\n"))
        
    else:
        resp=resp+1
        
print("Gracias por utilizar nuestros servicio\nAdios")
        



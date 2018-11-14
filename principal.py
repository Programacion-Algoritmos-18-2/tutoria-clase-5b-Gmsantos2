from paquete_académico.Persona import *

est1 = EstDistancia()
est1.agregar_nombres("José")
est1.agregar_apellido("Diaz")
est1.agregar_codigo("11012")
est1.agregar_nmaterias(5)
est1.agregar_modulo("Noveno")
p = Pais("Ecuador","Quito")
est1.agregar_pais(p)
print(est1.presentarD())
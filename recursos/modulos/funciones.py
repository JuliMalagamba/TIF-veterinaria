def decorar():
    print(" ")
    print("#"*60)
    print("-"*60)
    print("#"*60)
    print(" ")

def decorar2():
    print(" ")
    print("-"*60)
    print(" ")

def registrarPaciente(identificador,datosPaciente,registrosVeterinarios):
    nuevoRegistro={identificador:datosPaciente}
    registrosVeterinarios.update(nuevoRegistro)
    return f"""
REGISTRO INGRESADO CON ÉXITO.
Nº DE IDENTIFICADOR (ID): {identificador}"""

def mostrarRegistros(identificador,paciente):
    
    return(f"""
ID DEL REGISTRO: {identificador}
Nombre: {paciente["nombre"]},
Edad: {paciente["edad"]}, 
Sexo: {paciente["sexo"]}, 
Especie: {paciente["especie"]},
Rasgos: {paciente["rasgos"]}, 
Enfermedad: {paciente["enfermedad"]},
Dueño: {paciente["dueño"]}, 
Telefono: {paciente["telefono"]}
""")

def eliminarRegistro(registrosVeterinarios, idIngresado):
    registrosVeterinarios.pop(idIngresado)
    return """
REGISTRO ELIMINADO CON ÉXITO. """
    
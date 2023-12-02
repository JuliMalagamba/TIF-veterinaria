from recursos.modulos.funciones import decorar, decorar2, registrarPaciente, mostrarRegistros, eliminarRegistro
def main():
    registrosVeterinarios={}
    identificador=0
    registrosEliminados=0

    print("BIENVENIDO AL SISTEMA DE PACIENTES DE LA CLÍNICA VETERINARIA")

    while True:
        opcionIngresada= int(input("""
OPCIONES:
                          
1) REGISTRAR UN NUEVO PACIENTE
2) CONSULTAR EL REGISTRO DE PACIENTE/S
3) MODIFICAR UN REGISTRO
4) ELIMINAR UN REGISTRO
5) SALIR Y MOSTRAR EL REPORTE FINAL DE PACIENTES

¿ QUÉ DESEA HACER ? :  """))
        
        match opcionIngresada:
            case 1:
                print("""
REGISTRAR NUEVO PACIENTE
                      """)
                datosPaciente={}
                datosPaciente["nombre"]= input("Nombre del paciente: ")
                datosPaciente["edad"]=input("Edad: ")
                datosPaciente["sexo"]=input("Sexo: ")
                datosPaciente["especie"]=input("Especie: ")
                datosPaciente["rasgos"]=input("Rasgos: ")
                datosPaciente["enfermedad"]=input("Enfermedad o motivo de consulta: ")
                datosPaciente["dueño"]=input("Nombre del dueño: ")
                datosPaciente["telefono"]=input("Teléfono de contacto: ")
                identificador=identificador+1
                print(registrarPaciente(identificador, datosPaciente, registrosVeterinarios))

            case 2:
                opcionConsultar=input("""
CONSULTAR REGISTRO DE PACIENTE/S
                                  
Ingrese (1) si quiere consultar por un registro en especial, 
Ingrese (2) si quiere consultar el registro general de pacientes.

¿ QUÉ DESEA HACER ? :  """)
                if opcionConsultar=="1":
                    idConsultar=int(input("""
Ingrese el ID del registro que quiere consultar: """))
                    if idConsultar in registrosVeterinarios:
                        paciente=registrosVeterinarios[idConsultar]
                        print(mostrarRegistros(idConsultar, paciente))
                    else: print("""
ID NO ENCONTRADO.""")
                elif opcionConsultar=="2":
                    for identificador in registrosVeterinarios:
                        paciente=registrosVeterinarios[identificador]
                        print(mostrarRegistros(identificador,paciente))
                    if len(registrosVeterinarios)==0:
                        print("""
REGISTRO DE PACIENTES VACIO.""")
                else: print("""
OPCIÓN INGRESADA INVÁLIDA. """)
            case 3:
                opcionModificar=int(input("""
MODIFICAR REGISTRO DE PACIENTE

Ingrese el ID del registro que desea modificar: """))
                if opcionModificar in registrosVeterinarios:
                    paciente=registrosVeterinarios[opcionModificar]
                    print("""
Ingrese las modificaciones 
                  """)
                    paciente["nombre"]= input("Nombre del paciente: ")
                    paciente["edad"]= input("Edad: ")
                    paciente["sexo"]= input("Sexo: ")
                    paciente["especie"]=input("Especie: ")
                    paciente["rasgos"]=input("Rasgos: ")
                    paciente["enfermedad"]= input("Enfermedad o motivo de consulta: ")
                    paciente["dueño"]=input("Nombre del dueño: ")
                    paciente["telefono"]=input("Teléfono de contacto: ")
                    print("""
REGISTRO MODIFICADO CON ÉXITO. """)
                     
                else: print("""
ID NO ENCONTRADO.""")
            case 4:
                idIngresado= int(input("""
ELIMINAR REGISTRO DE PACIENTE
                               
Ingrese el ID del registro que desea eliminar: """))
                if idIngresado in registrosVeterinarios:
                    registrosEliminados= registrosEliminados+1
                    print(eliminarRegistro(registrosVeterinarios, idIngresado))
                else: print("""
ID NO ENCONTRADO""")
            case 5:
                print(f"""
REPORTE FINAL

CANTIDAD DE REGISTROS VIGENTES: {len(registrosVeterinarios)}
CANTIDAD DE REGISTROS ELIMINADOS: {registrosEliminados} 
                  """)
                break
            case _: print("""
OPCIÓN INGRESADA INVÁLIDA, INTENTE NUEVAMENTE""")
        
    print("GRACIAS POR UTILIZAR EL REGISTRO VIRTUAL DE PACIENTES VETERINARIOS")


if __name__=="__main__":
    main()
#pruebagithub
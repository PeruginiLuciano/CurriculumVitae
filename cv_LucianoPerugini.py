
from colorama import Fore, init
import os
import time
import keyboard
import pygame
import threading
pygame.init()
pygame.mixer.init()
sonido= pygame.mixer.Sound("sonido.mp3")
def suenaMusica():
    pygame.mixer.Sound.play(sonido)

hilo = threading.Thread(target=suenaMusica)


init()
os.system("cls")
contInvalid=0
itemsVistos=[False,False,False,False,False,False,False,False,False]
def PrintStart():
    os.system("cls")
    print("\n*************************************")
    print("*                                   *")
    print("*  Bienvenido a mí Curriculum vitae *")
    print("*                                   *")
    print("*************************************")

def PrintCorrect():
    print(Fore.GREEN+"\nRespuesta CORRECTA!!\n\n")
    print(Fore.WHITE+"Espere mientras inicia el sistema",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    os.system("cls")
    print(Fore.RED+"\n\n\n\n\t\t***************************")
    print("\t\t*                         *")
    print("\t\t*        "+Fore.WHITE+"IMPORTANTE       "+Fore.RED+"*")
    print("\t\t*                         *")
    print("\t\t***************************\n\n")
    print(Fore.WHITE+"Para la correcta visualización de la interfaz asegúrese que esté en pantalla completa\n")
    input("Si ya está en pantalla completa presione ENTER para continuar...")

def PrintIncorerct():
    print(Fore.RED+"\nRespuesta INCORRECTA!\n")
    print(Fore.WHITE+"Fue una pregunta sencilla me gustaría que este curriculum sea visto por alguien que tenga conocimientos mínimo de Python\n\n")
    time.sleep(5)
    print(Fore.WHITE+"Igualmente podés darle un vistazo",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    os.system("cls")
    print(Fore.RED+"\n\n\n\n***************************")
    print("*                         *")
    print("*        "+Fore.WHITE+"IMPORTANTE       "+Fore.RED+"*")
    print("*                         *")
    print("***************************\n\n")
    print(Fore.WHITE+"Para la correcta visualización de la interfaz asegúrese que esté en pantalla completa\n")
    input("Si ya está en pantalla completa presione ENTER para continuar...")
    


def PrintDatosPersonales():
    print("\n---------------------------------------------------\n")
    print(Fore.YELLOW+"Nombre y apellido:"+Fore.WHITE+" LUCIANO NAHUEL PERUGINI ROLDAN")
    print(Fore.YELLOW+"D.N.I:"+Fore.WHITE+" 38375743")
    print(Fore.YELLOW+"Fecha de nacimiento:"+Fore.WHITE+" 01/03/1994")
    print(Fore.YELLOW+"Dirección:"+Fore.WHITE+" ESPAÑA 362 (2000) ROSARIO, SANTA FE, ARGENTINA")
    print(Fore.YELLOW+"Nacionalidad:"+Fore.WHITE+" ARGENTINO")
    print(Fore.YELLOW+"Estado civil:"+Fore.WHITE+" SOLTERO")
    print(Fore.YELLOW+"Teléfono:"+Fore.WHITE+" +543413070122")
    print(Fore.YELLOW+"E-mail:"+Fore.WHITE+" PERUGINILUCIANO@YAHOO.COM.AR")
    print(Fore.YELLOW+"Licencia:"+Fore.WHITE+" A2,B1")
    print("\n---------------------------------------------------\n")

def FormacionAcademica():
    print("\n---------------------------------------------------\n")
    print(Fore.YELLOW+"* "+Fore.WHITE+"Cursando 1 año de la tecnicatura universitaria en inteligencia artificial\n en U.N.R. Facultad de Ciencias Exactas Ingeniería y Agrimensura\n")
    print(Fore.YELLOW+"* "+Fore.WHITE+"Ingeniero Electrónico (orientación sistemas digitales) en U.N.R. Facultad\n de Ciencias Exactas Ingeniería y Agrimensura\n")
    print("\n---------------------------------------------------\n")

def FormacionProfesional():
    print("\n---------------------------------------------------\n")
    print(Fore.YELLOW+"* "+Fore.WHITE+"CCNA 1 (Cisco Certifield Network Associate) de Cisco (12 meses)\n")
    print(Fore.YELLOW+"* "+Fore.WHITE+"Curso desarrollo de aplicaciones Android en Universidad Tecnológica de Rosario (3 meses)\n" )
    print(Fore.YELLOW+"* "+Fore.WHITE+"Curso de diseño de piezas mecánicas en Solidworks 'Colegio San Jose de Rosario' (4 meses)\n")
    print("\n---------------------------------------------------\n")

def Aptitudes():
    print("\n---------------------------------------------------\n")
    print(Fore.YELLOW+"* "+Fore.WHITE+"Programación avanzada en lenguaje Python, tkinter, openCV, django, numpy.\n")
    print(Fore.YELLOW+"* "+Fore.WHITE+"Programación avanzada en Flutter, desarrollo de aplicaciones móviles.\n")
    print(Fore.YELLOW+"* "+Fore.WHITE+"Programación en lenguaje C , C++ orientado a objetos, microcontroladores, y PLC.\n")
    print(Fore.YELLOW+"* "+Fore.WHITE+"Manejo básico de protocolos de redes TCP/IP, Ethernet y redes inalámbricas.\n")
    print(Fore.YELLOW+"* "+Fore.WHITE+"Diseño de circuitos y plaquetas electrónicas en altium.\n")
    print(Fore.YELLOW+"* "+Fore.WHITE+"Diseño de piezas en Solidworks.\n")
    print(Fore.YELLOW+"* "+Fore.WHITE+"Manejo de planillas de textos, planilla de cálculos, Word, presentaciones, Mat-Lab, redes sociales.\n")
    print(Fore.YELLOW+"* "+Fore.WHITE+"Actitud positiva con gran predisposición para trabajar en equipo.\n  ")
    print("\n---------------------------------------------------\n")

def Lenguajes():
    print("\n---------------------------------------------------\n")
    print(Fore.YELLOW+"Español: "+Fore.WHITE+"Nativo\n")
    print(Fore.YELLOW+"Ingles: "+Fore.WHITE+"Nivel pre-intermedio, con capacidad de interpretar textos, manuales y datasheet\n")
    print(Fore.YELLOW+"Italiano: "+Fore.WHITE+"Nivel básico\n")
    print("\n---------------------------------------------------\n")

def Antecedentes():
    print("\n---------------------------------------------------\n")
    print(Fore.YELLOW+"* "+Fore.WHITE+"Actualmente me encuentro trabajando como ingeniero electrónico encargado del área de desarrollo de hardware y \nsoftware en Enertik, importante empresa nacional de energías renovables. (2021 a 2023)\n")
    print(Fore.YELLOW+"* "+Fore.WHITE+"Realice actividades como ingeniero y técnico en área de electromedicina del “Hospital Provincial del Centenario”,\n realizando tareas de mantenimiento, reparación y capacitación de uso de equipos médicos electrónicos. \n  Además de realizar los estudios correspondientes para la compra y baja de estos equipos.(2019 a 2021)\n")
    print(Fore.YELLOW+"* "+Fore.WHITE+"Realice actividades como encargado de personal en restaurante “Bound”. Salta 198 (2012 a 2019).")
    
    print("\n---------------------------------------------------\n")
def Referencias():
    print("\n---------------------------------------------------\n")
    print(Fore.YELLOW+"ING. Mariano Garcias: "+Fore.WHITE+"Encargado de logística de Enertik importante empresa de energías renovables\n                      Teléfono: +543415052531\n")
    print(Fore.YELLOW+"ING. Claudio Aguirre: "+Fore.WHITE+"Jefe de departamento de Electromedicina de la provincia de Santa Fe\n                      Teléfono: +543416971029")
    print("\n---------------------------------------------------\n")

def AcercaDeMi():
    print("\n---------------------------------------------------\n")
    print(Fore.YELLOW+"****************************************************************************************************************************************************************************")
    print("*                                                                                                                                                                          *")
    print("*"+Fore.WHITE+"  Soy ingeniero electrónico orientado en sistemas digitales, me encuentro trabajando como encargado del desarrollo de hardware y software de la empresa Enertik. Empresa  "+Fore.YELLOW+"*")
    print("*"+Fore.WHITE+" dedicada a las energías renovables.                                                                                                                                      "+Fore.YELLOW+"*")
    print("*                                                                                                                                                                          *") 
    print("*"+Fore.WHITE+"  En la misma, mi tarea es desarrollar código en C para microcontroladores, y código en Python, ya sea para la solución de problemas presentes, o el desarrollo de nuevas "+Fore.YELLOW+"*")
    print("*"+Fore.WHITE+" tecnologías, también hago trabajos de corrección de códigos para actualizaciones de software ya existentes que se acoplen a las nuevas necesidades y demandas.           "+Fore.YELLOW+"*")
    print("*                                                                                                                                                                          *")
    print("*"+Fore.WHITE+"  Cuento con más de 5 años de experiencia trabajando con Python                                                                                                           "+Fore.YELLOW+"*")
    
    print("*                                                                                                                                                                          *")
    print("*"+Fore.WHITE+"  También trabajo desarrollando hardware en Altium, ya sea diseño,  elaboración, o ambas, de  placas PCB, como también la  actualización  de las mismas.                  "+Fore.YELLOW+"*")
    print("*                                                                                                                                                                          *")
    print("*"+Fore.WHITE+"  Soy desarrollador de aplicaciones móviles en Flutter.                                                                                                                   "+Fore.YELLOW+"*")
    print("*                                                                                                                                                                          *")
    print("*"+Fore.WHITE+"  Mi labor como ingeniero electrónico y desarrollador de hardware y software me mantiene en constante capacitación y aprendizaje de nuevas tecnologías.                   "+Fore.YELLOW+"*")
    print("*                                                                                                                                                                          *")
    print("*"+Fore.WHITE+"  Participación en proyecto de programación en reconocimiento de imagines en lenguaje Python con librería openCV.                                                         "+Fore.YELLOW+"*")
    print("*                                                                                                                                                                          *")
    print("*"+Fore.WHITE+"  En lo personal soy muy autodidacta estoy constantemente realizando proyectos personales, y soy un apasionado de la tecnología, es por eso mismo que decidí iniciar la   "+Fore.YELLOW+"*")
    print("*"+Fore.WHITE+" Tecnicatura Universitaria en Inteligencia Artificial en la U.N.R.                                                                                                        "+Fore.YELLOW+"*")
    print("*                                                                                                                                                                          *")
    print("*"+Fore.WHITE+"  Me encuentro en búsqueda de un trabajo donde pueda estar en constante crecimiento tanto personal, como profesional.                                                     "+Fore.YELLOW+"*")
    print("*                                                                                                                                                                          *")
    print("****************************************************************************************************************************************************************************"+Fore.WHITE)
    print("\n---------------------------------------------------\n")
def Salir():
    os.system("cls")
    print(Fore.YELLOW+"\n\n\n                   !              !                \n")
    print(Fore.YELLOW+"                             _)\n")
    print(Fore.YELLOW+"             *   *  *  *  *  *  *  *   *")
    print(Fore.YELLOW+"               *                      * ")
    print(Fore.YELLOW+"                  *                 *  ")
    print(Fore.YELLOW+"                     *  *  *  *  *      ")
    print("")
    print("")
    

    print(Fore.YELLOW+"        *********************************")
    print(Fore.YELLOW+"        *                               *")
    print(Fore.YELLOW+"        *           "+Fore.WHITE+"GRACIAS"+Fore.YELLOW+"             *")
    print(Fore.YELLOW+"        *                               *")
    print(Fore.YELLOW+"        *********************************\n")
    print(Fore.WHITE+"Espero tu contacto tengo muchas mas cosas para mostrarte")

def Bonus():
    os.system("cls")
    print(Fore.YELLOW+"        *********************************")
    print(Fore.YELLOW+"        *                               *")
    print(Fore.YELLOW+"        *           "+Fore.WHITE+"Bonus"+Fore.YELLOW+"               *")
    print(Fore.YELLOW+"        *                               *")
    print(Fore.YELLOW+"        *********************************\n"+Fore.WHITE)
    print("\n---------------------------------------------------\n")
    print("\n¿POR QUÉ APRETAS EL 9? SI NO HAY 9")
    print("\n---------------------------------------------------\n")
    print("\nDisfruta de Konki bailando\n\n")
    time.sleep(5)
    
    hilo.start()
    while True:
        
        if keyboard.is_pressed ('enter'):
            break
        time.sleep(0.35)
        os.system("cls")
        print(Fore.WHITE+"\nDisfruta de Konki bailando\n\n")
        print("                    "+Fore.YELLOW+"*  *  *             ")
        print("             *      "+Fore.YELLOW+"*  *  *      *  ")
        print("               *    "+Fore.YELLOW+"*  *  *    *   ")
        print("                  "+Fore.RED+"*    "+Fore.YELLOW+"*    "+Fore.RED+"*")
        print("                     "+Fore.RED+"* * *")
        print("                       "+Fore.RED+"*  ")
        print("                       "+Fore.RED+"*  ")
        print("                     "+Fore.BLUE+"*   * ")
        print("                   "+Fore.BLUE+"*       *")
        print("                  "+Fore.YELLOW+"*         *")
        print("               "+Fore.YELLOW+"***           ***")
        print(Fore.WHITE+"\n\nPresiona ENTER para salir...\n\n")
        time.sleep(0.35)
        os.system("cls")
        
        print(Fore.WHITE+"\nDisfruta de Konki bailando\n\n")
        print("                    "+Fore.YELLOW+"*  *  *             ")
        print("                    "+Fore.YELLOW+"*  *  *        ")
        print("                    "+Fore.YELLOW+"*  *  *       ")
        print("                       "+Fore.YELLOW+"*    ")
        print("                     "+Fore.RED+"* * *")
        print("                   "+Fore.RED+"*   *   *")
        print("                   "+Fore.YELLOW+"*   "+Fore.RED+"*   "+Fore.YELLOW+"*")
        print("                      "+Fore.BLUE+"* * ")
        print("                     "+Fore.BLUE+"*   *")
        print("                     "+Fore.YELLOW+"*   *")
        print("                   "+Fore.YELLOW+"***   ***")
        print(Fore.WHITE+"\n\nPresiona ENTER para salir...\n\n")
        time.sleep(0.35)
        os.system("cls")
        
        print(Fore.WHITE+"\nDisfruta de Konki bailando\n\n")
        print("                                        "+Fore.YELLOW+"*  *  *             ")
        print("                                 "+Fore.YELLOW+"*      *  *  *      *  ")
        print("                                   "+Fore.YELLOW+"*    *  *  *    *   ")
        print("                                      "+Fore.RED+"*    "+Fore.YELLOW+"*    "+Fore.RED+"*")
        print("                                         "+Fore.RED+"* * *")
        print("                                           "+Fore.RED+"*  ")
        print("                                           "+Fore.RED+"*  ")
        print("                                         "+Fore.BLUE+"*   * ")
        print("                                       "+Fore.BLUE+"*       *")
        print("                                      "+Fore.YELLOW+"*         *")
        print("                                   "+Fore.YELLOW+"***           ***")
        print(Fore.WHITE+"\n\nPresiona ENTER para salir...\n\n")
        time.sleep(0.35)
        os.system("cls")
        
        print(Fore.WHITE+"\nDisfruta de Konki bailando\n\n")
        print("                                        "+Fore.YELLOW+"*  *  *             ")
        print("                                        "+Fore.YELLOW+"*  *  *        ")
        print("                                        "+Fore.YELLOW+"*  *  *       ")
        print("                                           "+Fore.YELLOW+"*    ")
        print("                                         "+Fore.RED+"* * *")
        print("                                       "+Fore.RED+"*   *   *")
        print("                                       "+Fore.YELLOW+"*   "+Fore.RED+"*   "+Fore.YELLOW+"*")
        print("                                          "+Fore.BLUE+"* * ")
        print("                                         "+Fore.BLUE+"*   *")
        print("                                         "+Fore.YELLOW+"*   *")
        print("                                      "+Fore.YELLOW+"***   ***")
        print(Fore.WHITE+"\n\nPresiona ENTER para salir...\n\n")
    
def Menu(cont,list):

    Uno=Fore.RED
    Dos=Fore.RED
    Tres=Fore.RED
    Cuatro=Fore.RED
    Cinco=Fore.RED
    Seis=Fore.RED
    Siete=Fore.RED
    Ocho=Fore.RED

    if(list[1]):
        Uno=Fore.GREEN
    if(list[2]):
        Dos=Fore.GREEN
    if(list[3]):
        Tres=Fore.GREEN
    if(list[4]):
        Cuatro=Fore.GREEN
    if(list[5]):
        Cinco=Fore.GREEN
    if(list[6]):
        Seis=Fore.GREEN
    if(list[7]):
        Siete=Fore.GREEN
    if(list[8]):
        Ocho=Fore.GREEN

    print("------------------------")
    print("\n*--------MENU---------*")
    print(Fore.YELLOW+"1"+Uno+"->"+Fore.WHITE+" Datos personales")
    print(Fore.YELLOW+"2"+Dos+"->"+Fore.WHITE+" Formación academica")
    print(Fore.YELLOW+"3"+Tres+"->"+Fore.WHITE+" Formación profesional")
    print(Fore.YELLOW+"4"+Cuatro+"->"+Fore.WHITE+" Aptitudes")
    print(Fore.YELLOW+"5"+Cinco+"->"+Fore.WHITE+" Lenguajes")
    print(Fore.YELLOW+"6"+Seis+"->"+Fore.WHITE+" Antecedentes laborales")
    print(Fore.YELLOW+"7"+Siete+"->"+Fore.WHITE+" Referencias")
    print(Fore.YELLOW+"8"+Ocho+"->"+Fore.WHITE+" Acerca de mi")
    print(Fore.YELLOW+"0"+Fore.WHITE+"->"+Fore.WHITE+" Salir")
    print("------------------------")
    try:
        rta2=int(input("Teclear la opcion deseada: "))
    except:
        os.system("cls")
        print("\n*--------------------------------------------------------------------------------------------*")
        print(Fore.RED+"ERROR "+Fore.WHITE+" en el tipo de entrada debe ser un numero entero como muestra el menú, no puede ser una letra o carácter")
        print("*--------------------------------------------------------------------------------------------\n*")
        print("------------------------")
        print("\n*--------MENU---------*")
        print(Fore.YELLOW+"1"+Uno+"->"+Fore.WHITE+" Datos personales")
        print(Fore.YELLOW+"2"+Dos+"->"+Fore.WHITE+" Formacion academica")
        print(Fore.YELLOW+"3"+Tres+"->"+Fore.WHITE+" Formacion profesional")
        print(Fore.YELLOW+"4"+Cuatro+"->"+Fore.WHITE+" Aptitudes")
        print(Fore.YELLOW+"5"+Cinco+"->"+Fore.WHITE+" Lenguajes")
        print(Fore.YELLOW+"6"+Seis+"->"+Fore.WHITE+" Antecedentes laborales")
        print(Fore.YELLOW+"7"+Siete+"->"+Fore.WHITE+" Referencias")
        print(Fore.YELLOW+"8"+Ocho+"->"+Fore.WHITE+" Acerca de mi")
        print(Fore.YELLOW+"0"+Fore.WHITE+ "->"+Fore.WHITE+" Salir")
        print("------------------------\n")
        try:
            rta2=int(input("Teclear la opción deseada: "))
        except:
            print(Fore.RED+"\nERROR "+Fore.WHITE+" El error persiste, vuelva a intentarlo mas tarde\n")
            time.sleep(3)
            rta2=0
    if(rta2==1):
        list[1]=True
        PrintStart()
        print("Seleccionaste la opción DATOS PERSONALES.\n")
        
        PrintDatosPersonales()
        a=input("Precione ENTER para continuar...")
        os.system("cls")
        PrintStart()
        Menu(0,list)
    elif(rta2==2):
        list[2]=True
        PrintStart()
        print("Seleccionaste la opción FORMACIÓN ACADEMICA.\n")
        
        FormacionAcademica()
        a=input("Precione ENTER para continuar...")
        os.system("cls")
        PrintStart()
        Menu(0,list)
    elif(rta2==3):
        list[3]=True
        PrintStart()
        print("Seleccionaste la opción FORMACIÓN PROFESIONAL.\n")
        
        FormacionProfesional()
        a=input("Precione ENTER para continuar...")
        os.system("cls")
        PrintStart()
        Menu(0,list)
    elif(rta2==4):
        list[4]=True
        PrintStart()
        print("Seleccionaste la opción APTITUDES.\n")
        
        Aptitudes()
        a=input("Precione ENTER para continuar...")
        os.system("cls")
        PrintStart()
        Menu(0,list)
    elif(rta2==5):
        list[5]=True
        PrintStart()
        print("Seleccionaste la opción LENGUAJES.\n")
        
        Lenguajes()
        a=input("Precione ENTER para continuar...")
        os.system("cls")
        PrintStart()
        Menu(0,list)
    elif(rta2==6):
        list[6]=True
        PrintStart()
        print("Seleccionaste la opción ANTECEDENTES LABORALES.\n")
        
        Antecedentes()
        a=input("Precione ENTER para continuar...")
        os.system("cls")
        PrintStart()
        Menu(0,list)
    elif(rta2==7):
        list[7]=True
        PrintStart()
        print("Seleccionaste la opción REFERENCIAS.\n")
        
        Referencias()
        a=input("Precione ENTER para continuar...")
        os.system("cls")
        PrintStart()
        Menu(0,list)
    elif(rta2==8):
        list[8]=True
        PrintStart()
        print("Seleccionaste la opción ACERCA DE MI.\n")
        
        AcercaDeMi()
        a=input("Precione ENTER para continuar...")
        os.system("cls")
        PrintStart()
        Menu(0,list)
    elif(rta2==9):
        Bonus()  
    elif(rta2==0):
        Salir()
    elif(rta2==10):
        os.system("cls")
        print("\n\n\n Creado por Luciano Perugini R. en codigo Python 3\n\n")
        a=input("Precione ENTER para continuar...")
        os.system("cls")
        PrintStart()
        Menu(0,list)         
    else:
        cont=cont+1
        if(cont<3):
            os.system("cls")
            print(Fore.RED+"OPCIÓN INVALIDA!\n\n"+Fore.WHITE+"Quedan ",3-cont," intentos")
            Menu(cont,list)
        else:
           print("\n\n\nNo hay mas intentos, proba nuevamente mas tarde.")
           time.sleep(5)
PrintStart()
print(Fore.GREEN+"Antes de continuar necesito que responda la siguiente pregunta\n")
print("Cual es la salida del siguiente código Python?")
print(Fore.CYAN+"-----------------------------------------------")
print("A=5\nB=10\nC=20\nprint('Salida= ',A*B)")
print("-----------------------------------------------")
print(Fore.GREEN+"Opcion A:"+Fore.WHITE+ " 50" +Fore.GREEN+"              Opcion B:"+Fore.WHITE+ " TypeError")
print(Fore.GREEN+"Opcion C:"+Fore.WHITE+ " A*B"+Fore.GREEN+"             Opcion D:"+Fore.WHITE+ " Salida= 50")
rta=input(Fore.WHITE+"Ingrese la respuesta correcta A,B,C o D --> ")
print("-----------------------------------------------\n\n")
if(rta=='D' or rta=='d'):
    os.system("cls")
    PrintCorrect()
    PrintStart()
    Menu(contInvalid,itemsVistos)
else:
    os.system("cls")
    PrintIncorerct()
    PrintStart()
    Menu(contInvalid,itemsVistos)

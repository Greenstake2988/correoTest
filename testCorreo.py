import smtplib

de = 'bitso4bot@gmail.com'
lui = ''
osk = '0skr.vazquez@gmail.com'
oskh = 'pure_energy_akira@hotmail.com'
artu = 'parawat_06@hotmail.com'
userE = 'bitso4bot@gmail.com'
passE = 'bitso118'

body = "Probando 1 2 3..."

	

msg = "From: {}\r\nTo: {},\r\n\r\n{}\r\n".format(de, osk, body)


server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(userE,passE)
server.sendmail(de, osk, msg)
server.quit()

	

import os
import sys
import commands

import psycopg2 # instalar biblioteca de acordo com readme


# Tenta conectar

try:
    con=psycopg2.connect("host='IP_D0_Banco' dbname='NomeDoBanco' user='UsuarioBanco' password='SenhaBanco'")
    cur = con.cursor()    
    cur.execute("SELECT framedipaddress, senha_equipamento from mk_conexoes")
	result = cur.fetchall()
	count = result.__len__()
	for i in result:
		print " TENTANDO CONECTAR NO IP: "  +  str(i[0]) + " Senha: "  + str(i[1])
		os.system("sshpass -p " + str(i[1]) + " ssh -o StrictHostKeyChecking=no admin@" + str(i[0]) + " 'rm -f atualiza.sh'")
		os.system("sshpass -p " + str(i[1]) + " ssh -o StrictHostKeyChecking=no admin@" + str(i[0])+ " 'wget -qO- https://wwww.SEUDOMINIO.COM/atualiza_on_ubnt.sh | sh'&")	
except:
    print "Nao foi possivel Executar Operacoes:("

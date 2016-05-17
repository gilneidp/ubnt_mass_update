import os
import sys
import commands

import psycopg2

# Tenta conectar

try:
    conn=psycopg2.connect("host='IP_D0_Banco' dbname='NomeDoBanco' user='UsuarioBanco' password='SenhaBanco'")
except:
    print "Nao foi possivel conectar a base :("
    
cur = conn.cursor()
try:
    cur.execute("""SELECT framedipaddress, senha_equipamento from mk_conexoes""")
except:
    print "Nao foi possivel buscar informacoes!"
	
result = cur.fetchall()
count = result.__len__()
for i in result:
     print " TENTANDO CONECTAR NO IP: "  +  i[0] + " Senha: "  + i[1]
     os.system("sshpass -p " + i[1] + " ssh -o StrictHostKeyChecking=no admin@" + i[0] + " 'rm -f atualiza.sh'")
     os.system("sshpass -p " + i[1] + " ssh -o StrictHostKeyChecking=no admin@" + i[0] + " 'wget -qO- https://wwww.SEUDOMINIO.COM/atualiza_on_ubnt.sh | sh'&")

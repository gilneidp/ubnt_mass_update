import os
import sys
import commands

import MySQLdb

DB_HOST = 'IP_DO_SEU_RADIUS'
DB_USER = 'USUARIO_RADIUS'
DB_PASS = 'SENHA_RADIUS'
DB_NAME = 'nome_DB'

def run_query(query=''):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    conn = MySQLdb.connect(*datos)
    cursor = conn.cursor()
    cursor.execute(query)

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()
    else:
        conn.commit()
        data = None

    cursor.close()
    conn.close()

    return data
query = "SELECT DISTINCT (radacct.framedipaddress), radcheck.id, radacct.username, radcheck.value FROM radacct, radcheck WHERE radacct.username = radcheck.username AND radcheck.attribute =  'User-Password' ORDER BY radcheck.id"
result = run_query(query)
count = result.__len__()
for i in result:
     print " TENTANDO CONECTAR NO IP: "  +  i[0] + " Senha: "  + i[3]
     os.system("sshpass -p " + i[3] + " ssh -o StrictHostKeyChecking=no admin@" + i[0] + " 'rm -f atualiza.sh'")
     os.system("sshpass -p " + i[3] + " ssh -o StrictHostKeyChecking=no admin@" + i[0] + " 'wget -qO- https://github.com/gilneidp/ubnt_mass_update/atualiza_on_ubnt.sh | sh '")

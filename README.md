# ubnt_mass_update
Conecta em cada dispositivo UBNT com as respectivas senhas a partir das tabelas do banco de dados Radius... Envia o script para atualizar os equipamentos via ssh.

1 - Em uma maquina Linux (Com IP confiavel da sua rede):

$ apt-get install python-dev libmysqlclient-dev
$ pip install MySQL-python
$ git init
$ git pull https://github.com/gilneidp/ubnt_mass_update.git

3 - adicionar o firmware que voce deseja utilizar para atualizacao em uma public html ex: www.seuprovedor.com.br/xm/fwupdate.bin (opcional)

4 - adicionar o arquivo atualiza_on_ubnt.sh em uma public html conforme exemplo a cima

5 - modifique atualiza.py de acordo com sua necessidade

6- python atualiza.py

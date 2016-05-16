# ubnt_mass_update
Conecta em cada dispositivo UBNT a partir da tabela radius e evia script para atualizar os equipamentos via ssh.

1 - Em uma maquina Linux (Com IP confiavel da sua rede):
apt-get install python-dev libmysqlclient-dev
 pip install MySQL-python
 
2 - wget https://github.com/gilneidp/ubnt_mass_update/atualiza.py

3 - adicionar o firmware que voce deseja utilizar para atualizacao em uma public html ex: www.seuprovedor.com.br/xm/fwupdate.bin

4 - adicionar o arquivo atualiza_on_ubnt.sh em uma public html conforme exemplo a cima
     - > wget https://github.com/gilneidp/ubnt_mass_update/atualiza_on_ubnt.py

5 - modifique atualiza.py de acordo com sua necessidade

6- python atualiza.py

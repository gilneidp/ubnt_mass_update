#!/bin/bash
VAR=`cat /etc/version`
cd /tmp/
rm -f fwupdate.bin
if echo "$VAR" | egrep "5.6.5" >/dev/null;then
  echo "Ja na versao" $VAR
  exit
fi
if echo "$VAR" | egrep 'XM' >/dev/null;then
  wget http://www.seudominio.com.br/xm/fwupdate.bin
  ubntbox fwupdate.real -m /tmp/fwupdate.bin
else
  wget http://www.seudominio.com.br/xw/fwupdate.bin
  ubntbox fwupdate.real -m /tmp/fwupdate.bin
fi
exit 1

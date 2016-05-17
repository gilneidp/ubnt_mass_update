#!/bin/bash
cd /etc/persistent/
rm -f mf.tar
rm -f rc.poststart
rm -R .mf
cfgmtd -p /etc/persistent/ -w
VAR=`cat /etc/version`
cd /tmp/
rm -f fwupdate.bin
if echo "$VAR" | egrep "5.6.5" >/dev/null;then
  echo "Ja na versao" $VAR
  exit
fi
if echo "$VAR" | egrep 'XM' >/dev/null;then
  wget https://github.com/gilneidp/ubnt_mass_update/xm/fwupdate.bin
  ubntbox fwupdate.real -m /tmp/fwupdate.bin
else
  wget https://github.com/gilneidp/ubnt_mass_update/xw/fwupdate.bin
  ubntbox fwupdate.real -m /tmp/fwupdate.bin
fi
exit 1

echo running temperature software

set pass ["raspberry"]
set host [172.20.10.3]
ssh -t pi@172.20.10.3

send "$pass\n";
interact
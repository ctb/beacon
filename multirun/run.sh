#! /bin/bash
for i in {1..20}
do
	cp -r /root/run.template run.$i
	cd run.$i
	avida
	cd ../
done


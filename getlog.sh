#!/bin/bash
PATTERN_LIST="[0-9a-z]+/ .*compile/ [0-9]+/ console.html"


getlog()
{
 url=$1
 pattern=$(echo ${PATTERN_LIST}|cut -d " " -f$2)

 for i in $(s3cmd ls $url|grep -Eo $url$pattern);do
    count=$(($2+1))
    if test $count -lt 5 ;then
        getlog $i $count
    else
        name=`echo $i|cut -d "/" -f4- |sed "s#/#_#g"`
        s3cmd get $i $name
    fi
 done
}

#s3cmd ls s3://logs > /home/sxh/list
for i in $(cat /home/sxh/list);do
        getlog $i 1
done;



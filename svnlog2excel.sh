#!/bin/bash
if [ ! $# = 4 ]  
then
	echo "usage: $0 svn_url start_version stop_version user_name";
	exit 0
fi
svnpath=${1};
start_ver=${2};
stop_ver=${3};
user_name=${4};
filename=$(echo ${svnpath} | awk -F'/' '{print $5 $7}');
REV=$(svn info --username=${user_name} ${svnpath} | grep 'Last Changed Rev:'  | awk  -F: '{ print $2 }') ;
svn log --username=${user_name} -r${start_ver}:${stop_ver} ${svnpath} -v --xml > ${filename//\//_}.xml  ;
./svnlog2excel.py ${filename//\//_}
rm -rf ${filename//\//_}.xml 
#encoding=utf-8
#Name: wang qing 
#Date: 2015-4-13 Monday
#Program: final deal data
import os
from parser import *
from getIpv6Fib import *
from commandSh import *

def reduceFIBs(sourcePath, destPath, destDir):
	filelist = os.listdir(sourcePath)
	if os.path.exists(destPath+destDir+'/'):
        		pass
    	else:
       		os.mkdir(destPath+destDir+'/')
	filelist = os.listdir(sourcePath)
	for i in filelist:
		reduceFIB(sourcePath+i, destPath+destDir+'/'+i+'.fib')

def reduceIpv6FIBs(sourcePath, destPath, destDir, asns):
	filelist = os.listdir(sourcePath)
	if os.path.exists(destPath+destDir+'/'):
		os.popen('rm -rf  ' + destPath+destDir+'/')
		os.mkdir(destPath+destDir+'/')
    	else:
       		os.mkdir(destPath+destDir+'/')
	filelist = os.listdir(sourcePath)
	fw = open(destPath+destDir+'/res.txt', 'w')
	for i in filelist:
		res = reduceIpv6Fib(sourcePath+i, destPath+destDir+'/'+i+'.ipv6fib', asns)
		fw.write(sourcePath+i +"   " + str(res[0]) + "    " + str(res[1]) + "   percentage: " + str(1.0-res[1]*1.0/res[0]) + "\n")
	fw.close()


def randomAsn(filename, percentage):
	f = open(filename, 'r');
	lines = f.readlines();
	asNums = [];
	for line in lines:
		params = line.split("|");
		asNums.append(params[0]);
	return random.sample(asNums, int(len(asNums)*percentage))

def getOrderedAsn(filename, percentage):
	f = open(filename, 'r');
	lines = f.readlines();
	dicAsn = {};
	finalres =[];
	asnnum = 0;
	for line in lines:
		asnnum += 1;
		params = line.split("|");
		params[1] = int(params[1])
		if params[1] not in dicAsn.keys():
			dicAsn[params[1]]=[];
		dicAsn[params[1]].append(params[0]);
	res = sorted(dicAsn.iteritems(), key=lambda d:d[0], reverse=True);
	num = int(asnnum*percentage);
	for i  in res:
		for j in i[1]:
			finalres.append(j);	
			if len(finalres) >= num:
				return finalres;

	


#nowsdays  choose arranged ASN
asns = getOrderedAsn("/home/cnpt/wqfile/simbgp/data/asrel/as2addrsNew.txt", 0.2);
print asns;
#choose tier1 ASN
asns = ['174','209','286','701','1239','1299','2828','2914','3257','4436','3320','3356','4436','5511','6453','6461','6762','7018','12956'];
print asns;
reduceIpv6FIBs( "/home/cnpt/wqfile/simbgp/data/FIBData/20150502.0000/", "/home/cnpt/wqfile/simbgp/data/Ipv6FIBData/20150502/","tier1", asns)
#old days before 2015.6.10
'''
asns = getOrderedAsn("/home/cnpt/wqfile/simbgp/data/asrel/as2addrsNew.txt", 0.2);
print asns;
print "*******************************************************************************";
reduceIpv6FIBs( "/home/cnpt/wqfile/simbgp/data/FIBData/20150502.0000/", "/home/cnpt/wqfile/simbgp/data/Ipv6FIBData/20150502/","20150502.0000.0.2", asns)
asns = getOrderedAsn("/home/cnpt/wqfile/simbgp/data/asrel/as2addrsNew.txt", 0.4);
print asns;
print "*******************************************************************************";
reduceIpv6FIBs( "/home/cnpt/wqfile/simbgp/data/FIBData/20150502.0000/", "/home/cnpt/wqfile/simbgp/data/Ipv6FIBData/20150502/","20150502.0000.0.4", asns)
asns = getOrderedAsn("/home/cnpt/wqfile/simbgp/data/asrel/as2addrsNew.txt", 0.6);
print asns;
print "*******************************************************************************";
reduceIpv6FIBs( "/home/cnpt/wqfile/simbgp/data/FIBData/20150502.0000/", "/home/cnpt/wqfile/simbgp/data/Ipv6FIBData/20150502/","20150502.0000.0.6", asns)
asns = getOrderedAsn("/home/cnpt/wqfile/simbgp/data/asrel/as2addrsNew.txt", 0.8);
print asns;
print "*******************************************************************************";
reduceIpv6FIBs( "/home/cnpt/wqfile/simbgp/data/FIBData/20150502.0000/", "/home/cnpt/wqfile/simbgp/data/Ipv6FIBData/20150502/","20150502.0000.0.8", asns)
'''


#old old days before 2015.5.1
'''getAsToAddrs("/home/cnpt/wqfile/simbgp/data/FIBData/20150403.0000/route-views.saopaulo-rib.20150403.0000.out.fib",
 "/home/cnpt/wqfile/CABAsimBgp/tempdata/as2addrs.txt")

asns = randomAsn("/home/cnpt/wqfile/CABAsimBgp/tempdata/as2addrs.txt", 0.2)
reduceIpv6FIBs( "/home/cnpt/wqfile/simbgp/data/FIBData/20150403.0000/", "/home/cnpt/wqfile/simbgp/data/Ipv6FIBData/20150422/","20150403.0000.0.2", asns)
asns = randomAsn("/home/cnpt/wqfile/CABAsimBgp/tempdata/as2addrs.txt", 0.4)
reduceIpv6FIBs( "/home/cnpt/wqfile/simbgp/data/FIBData/20150403.0000/", "/home/cnpt/wqfile/simbgp/data/Ipv6FIBData/20150422/","20150403.0000.0.4", asns)
asns = randomAsn("/home/cnpt/wqfile/CABAsimBgp/tempdata/as2addrs.txt", 0.6)
reduceIpv6FIBs( "/home/cnpt/wqfile/simbgp/data/FIBData/20150403.0000/", "/home/cnpt/wqfile/simbgp/data/Ipv6FIBData/20150422/","20150403.0000.0.6", asns)
asns = randomAsn("/home/cnpt/wqfile/CABAsimBgp/tempdata/as2addrs.txt", 0.8)
reduceIpv6FIBs( "/home/cnpt/wqfile/simbgp/data/FIBData/20150403.0000/", "/home/cnpt/wqfile/simbgp/data/Ipv6FIBData/20150422/","20150403.0000.0.8", asns)
asns = randomAsn("/home/cnpt/wqfile/CABAsimBgp/tempdata/as2addrs.txt", 1.0)
reduceIpv6FIBs( "/home/cnpt/wqfile/simbgp/data/FIBData/20150403.0000/", "/home/cnpt/wqfile/simbgp/data/Ipv6FIBData/20150422/","20150403.0000.1.0", asns)


getAsToAddrs("/home/cnpt/wqfile/simbgp/data/FIBData/20150403.0000/route-views.saopaulo-rib.20150403.0000.out.fib",
 "/home/cnpt/wqfile/CABAsimBgp/tempdata/as2addrs.txt")

produceAsn("/home/cnpt/wqfile/CABAsimBgp/tempdata/as2addrs.txt", 10, "/home/cnpt/wqfile/CABAsimBgp/tempdata/as2addrs.out");

produceConfig("/home/cnpt/wqfile/CABAsimBgp/tempdata/config.txt", "28624|38|187.110.64.0/19|187.110.64.0/20|187.110.64.0/21|187.110.72.0/21|187.110.80.0/20|187.110.80.0/21|187.110.88.0/21|187.110.96.0/19|187.110.96.0/20|187.110.96.0/21|187.110.104.0/21|187.110.112.0/20|200.237.128.0/19|200.237.128.0/20|200.237.128.0/21|200.237.128.0/24|200.237.129.0/24|200.237.136.0/21|200.237.144.0/20|200.237.144.0/21|200.237.145.0/24|200.237.152.0/21|201.33.32.0/19|201.33.32.0/20|201.33.32.0/21|201.33.40.0/21|201.33.48.0/20|201.33.48.0/21|201.33.56.0/21|201.33.56.0/23|201.54.160.0/20|201.54.160.0/21|201.54.160.0/22|201.54.164.0/22|201.54.168.0/21|201.54.168.0/22|201.54.172.0/22|2804:3bc::/32|");


simBgpCommand("/home/cnpt/wqfile/CABAsimBgp/dealCode/simBGP_run.py","/home/cnpt/wqfile/CABAsimBgp/tempdata/config.txt",
 "/home/cnpt/wqfile/CABAsimBgp/tempdata/simBgpCommand.sh", 39);

produceAsn("/home/cnpt/wqfile/CABAsimBgp/tempdata/as2addrs.txt", 20, "/home/cnpt/wqfile/CABAsimBgp/tempdata/as2addrs.out");

produceConfig("/home/cnpt/wqfile/CABAsimBgp/tempdata/temp2/config.txt","/home/cnpt/wqfile/CABAsimBgp/tempdata/as2addrs.out");
simBgpCommand("/home/cnpt/wqfile/CABAsimBgp/dealCode/simBGP_run.py","/home/cnpt/wqfile/CABAsimBgp/tempdata/temp2/config.txt",
 "/home/cnpt/wqfile/CABAsimBgp/tempdata/simBgpCommand.sh", 20);'''

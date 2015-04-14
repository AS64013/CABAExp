#Name: wang qing 
#Date: 2015-4-3 Friday
#Program: change ipv4 fib  to ipv6 fib for CABA   

#TABLE_DUMP_V2|03/31/15 02:00:00|A|206.126.236.37|6939|1.0.224.0/19|6939 38040 9737|IGP
class RouteInfo:
	def __init__(self, routeName, time, type, addr, asn, prefix, asPath, protocol):
		self.routeName = routeName;
		self.time = time;
		self.type = type;
		self.addr = addr;
		self.asn = asn;
		self.prefix = prefix;
		self.asPath = asPath;
		self.protocol = protocol;
	def printRouteInfo(self):
		print self.asn;
		print self.asPath;
	def modifyRouteInfo(self, routeInfo):
		paramsRecord = self.asPath.split(' ');
		params = routeInfo.asPath.split(' ');
		numRecord = len(paramsRecord);
		num = len(params);
		if num > numRecord:
			return;
		elif num  < numRecord:
			self = routeInfo;
		elif num == numRecord and int(params[0])< int(paramsRecord[0]):
			self = routeInfo;
		else:
			return;
	def aS2Ipv6Addr(self):
		ipv6Str = str(hex(int(self.asn)))
		res = ''
		for i in range(10-len(ipv6Str)):
			res+='0'
		res+=ipv6Str;
		res+="00"
		self.prefix = res[0:4] + ':' + res[4:8]+':'+res[8:12]+"::"
	def  RouteInfoToStr(self):
		return self.routeName + '|' + self.time+'|' + self.type + '|' + self.addr + '|' + self.asn + '|' + self.prefix + '|' + self.asPath + '|' + self.protocol;



f  = open('fib', 'r');
fw = open('ipv6Fib','w');
line = f.readline();
results= {};
while line:
	params = line.split('|');
	line = f.readline();
	route = RouteInfo(params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7]);
	if route.asn in results:
		routeRecord = results[route.asn];
		routeRecord.modifyRouteInfo(route);
	else:
		results[route.asn] = route;
	#route.printRouteInfo();
for value in results.values():
	value.aS2Ipv6Addr();
	fw.write(value.RouteInfoToStr());
fw.close();
f.close();
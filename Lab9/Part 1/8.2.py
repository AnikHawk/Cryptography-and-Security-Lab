import dpkt
import sys
import socket

f = open(sys.argv[1], 'rb')
pcap = dpkt.pcap.Reader(f)

syn_count = {}
synack_count = {}

for ts, buf in pcap:
    try:
        eth = dpkt.ethernet.Ethernet(buf)
    except:
        continue

    if eth.type == dpkt.ethernet.ETH_TYPE_IP:
        ip = eth.data
        protocol = ip.p

        if protocol == dpkt.ip.IP_PROTO_TCP:
            tcp = ip.data
            ip_src = socket.inet_ntoa(ip.src)
            ip_dst = socket.inet_ntoa(ip.dst)

            if ((tcp.flags & dpkt.tcp.TH_SYN != 0) and (tcp.flags & dpkt.tcp.TH_ACK == 0)):
                syn_count[ip_src] = 1 if syn_count.get(ip_src) is None else syn_count[ip_src] + 1


            if ((tcp.flags & dpkt.tcp.TH_SYN != 0) and (tcp.flags & dpkt.tcp.TH_ACK != 0)):
                synack_count[ip_dst] = 1 if synack_count.get(ip_dst) is None else synack_count[ip_dst] + 1


result = []
for ip_addr in syn_count:
    if ip_addr not in synack_count:
        synack_count[ip_addr] = 0
    if syn_count[ip_addr] > synack_count[ip_addr] * 3:
        result.append(ip_addr)

for ip_addrs in result:
    print(ip_addrs)


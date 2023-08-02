import netfilterqueue

def process_packet(packet):
    print(packet)
    packet.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(1,process_packet)
queue.run()
import matplotlib.pyplot as plt

x1 = [80, 160, 240, 320, 400, 480]
UniCast_SAFW1 = [498, 848, 1198, 1359, 1359, 1359]
UniCast_CCKP1 = [500, 849, 1199, 1363, 1363, 1363]
UniCast_FCPS1 = [272, 339, 394, 437, 473, 502]
l1 = plt.plot(x1, UniCast_SAFW1, 'r--', label='UniCast-SAFW')
l2 = plt.plot(x1, UniCast_CCKP1, 'g--', label='UniCast-CCKP')
l3 = plt.plot(x1, UniCast_FCPS1, 'b--', label='UniCast-FCPS')
plt.plot(x1, UniCast_SAFW1, 'ro-', x1, UniCast_CCKP1, 'g+-', x1, UniCast_FCPS1, 'b^-')
plt.title('UniCast Time Delay')
plt.xlabel('Packet_Sum 1000Byte/stream')
plt.ylabel('Time Delay/ms')
plt.legend()
plt.show()

UniCast_SAFW1 = [80, 160, 240, 277, 277, 277]
UniCast_CCKP1 = [80, 160, 240, 278, 278, 278]
UniCast_FCPS1 = [80, 160, 240, 320, 400, 471]
l1 = plt.plot(x1, UniCast_SAFW1, 'r--', label='UniCast-SAFW')
l2 = plt.plot(x1, UniCast_CCKP1, 'g--', label='UniCast-CCKP')
l3 = plt.plot(x1, UniCast_FCPS1, 'b--', label='UniCast-FCPS')
plt.plot(x1, UniCast_SAFW1, 'ro-', x1, UniCast_CCKP1, 'g+-', x1, UniCast_FCPS1, 'b^-')
plt.title('UniCast Arrive Packet')
plt.xlabel('Packet_Sum 1000Byte/stream')
plt.ylabel('Arrive Packet')
plt.legend()
plt.show()

x2 = [16, 32, 48, 64, 80, 96, 112, 128, 144, 160]
BroadCast_SAFW1 = [302, 498, 705, 913, 1123, 1332, 1542, 1751, 1908, 1908]
BroadCast_CCKP1 = [299, 494, 703, 912, 1121, 1331, 1541, 1751, 1907, 1907]
BroadCast_FCPS1 = [280, 490, 700, 910, 1120, 1330, 1540, 1750, 1920, 1920]
l1 = plt.plot(x2, BroadCast_SAFW1, 'r--', label='BroadCast-SAFW')
l2 = plt.plot(x2, BroadCast_CCKP1, 'g--', label='BroadCast-CCKP')
l3 = plt.plot(x2, BroadCast_FCPS1, 'b--', label='BroadCast-FCPS')
plt.plot(x2, BroadCast_SAFW1, 'ro-', x2, BroadCast_CCKP1, 'g+-', x2, BroadCast_FCPS1, 'b^-')
plt.title('BroadCast Time Delay')
plt.xlabel('Packet_Sum 1000Byte/stream')
plt.ylabel('Time Delay/ms')
plt.legend()
plt.show()

BroadCast_SAFW1 = [16, 32, 48, 64, 80, 96, 112, 128, 140, 140]
BroadCast_CCKP1 = [16, 32, 48, 64, 80, 96, 112, 128, 140, 140]
BroadCast_FCPS1 = [16, 32, 48, 64, 80, 96, 112, 128, 141, 141]
l1 = plt.plot(x2, BroadCast_SAFW1, 'r--', label='BroadCast-SAFW')
l2 = plt.plot(x2, BroadCast_CCKP1, 'g--', label='BroadCast-CCKP')
l3 = plt.plot(x2, BroadCast_FCPS1, 'b--', label='BroadCast-FCPS')
plt.plot(x2, BroadCast_SAFW1, 'ro-', x2, BroadCast_CCKP1, 'g+-', x2, BroadCast_FCPS1, 'b^-')
plt.title('BroadCast Arrive Packet')
plt.xlabel('Packet_Sum 1000Byte/stream')
plt.ylabel('Arrive Packet')
plt.legend()
plt.show()

x3 = [32, 64, 96, 128, 160, 192, 224, 256]
UniBroadCast_SAFW1 = [369, 606, 843, 1081, 1319, 1502, 1502, 1502]
UniBroadCast_CCKP1 = [368, 604, 841, 1079, 1317, 1488, 1496, 1496]
UniBroadCast_FCPS1 = [337, 548, 758, 968, 1179, 1389, 1577, 1588]
l1 = plt.plot(x3, UniBroadCast_SAFW1, 'r--', label='UniBroadCast-SAFW')
l2 = plt.plot(x3, UniBroadCast_CCKP1, 'g--', label='UniBroadCast-CCKP')
l3 = plt.plot(x3, UniBroadCast_FCPS1, 'b--', label='UniBroadCast-FCPS')
plt.plot(x3, UniBroadCast_SAFW1, 'ro-', x3, UniBroadCast_CCKP1, 'g+-', x3, UniBroadCast_FCPS1, 'b^-')
plt.title('UniBroadCast Time Delay')
plt.xlabel('Packet_Sum 1000Byte/stream')
plt.ylabel('Time Delay/ms')
plt.legend()
plt.show()

UniBroadCast_SAFW1 = [32, 64, 96, 128, 160, 187, 187, 187]
UniBroadCast_CCKP1 = [32, 64, 96, 128, 160, 186, 188, 188]
UniBroadCast_FCPS1 = [32, 64, 96, 128, 160, 192, 228, 226]
l1 = plt.plot(x3, UniBroadCast_SAFW1, 'r--', label='UniBroadCast-SAFW')
l2 = plt.plot(x3, UniBroadCast_CCKP1, 'g--', label='UniBroadCast-CCKP')
l3 = plt.plot(x3, UniBroadCast_FCPS1, 'b--', label='UniBroadCast-FCPS')
plt.plot(x3, UniBroadCast_SAFW1, 'ro-', x3, UniBroadCast_CCKP1, 'g+-', x3, UniBroadCast_FCPS1, 'b^-')
plt.title('UniBroadCast Arrive Packet')
plt.xlabel('Packet_Sum 1000Byte/stream')
plt.ylabel('Arrive Packet')
plt.legend()
plt.show()
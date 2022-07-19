import matplotlib.pyplot as plt

x1 = [40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560]
UniCast_SAFW1 = [323, 498, 673, 848, 1023, 1198, 1355, 1359, 1359, 1359, 1359, 1359, 1359, 1359]
UniCast_CCKP1 = [327, 500, 674, 849, 1024, 1199, 1355, 1363, 1363, 1363, 1363, 1363, 1363, 1363]
UniCast_FCPS1 = [236, 272, 307, 339,  367,  394,  415,  437,  455,  473,  492,  502,  502,  502]
l1 = plt.plot(x1, UniCast_SAFW1, 'r--', label='UniCast-SAFW')
l2 = plt.plot(x1, UniCast_CCKP1, 'g--', label='UniCast-CCKP')
l3 = plt.plot(x1, UniCast_FCPS1, 'b--', label='UniCast-FCPS')
plt.plot(x1, UniCast_SAFW1, 'ro-', x1, UniCast_CCKP1, 'g+-', x1, UniCast_FCPS1, 'b^-')
plt.title('UniCast Time Delay')
plt.xlabel('Packet_Sum 1000Byte/stream')
plt.ylabel('Time Delay/ms')
plt.legend()
plt.show()

UniCast_SAFW1 = [40, 80, 120, 160, 200, 240, 276, 277, 277, 277, 277, 277, 277, 277]
UniCast_CCKP1 = [40, 80, 120, 160, 200, 240, 276, 278, 278, 278, 278, 278, 278, 278]
UniCast_FCPS1 = [40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 471, 485, 485]
l1 = plt.plot(x1, UniCast_SAFW1, 'r--', label='UniCast-SAFW')
l2 = plt.plot(x1, UniCast_CCKP1, 'g--', label='UniCast-CCKP')
l3 = plt.plot(x1, UniCast_FCPS1, 'b--', label='UniCast-FCPS')
plt.plot(x1, UniCast_SAFW1, 'ro-', x1, UniCast_CCKP1, 'g+-', x1, UniCast_FCPS1, 'b^-')
plt.title('UniCast Arrive Packet')
plt.xlabel('Packet_Sum 1000Byte/stream')
plt.ylabel('Arrive Packet')
plt.legend()
plt.show()

x2 = [16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192]
BroadCast_SAFW1 = [360, 563, 772, 981, 1191, 1401, 1611, 1820, 1977, 1977, 1977, 1977]
BroadCast_CCKP1 = [350, 539, 743, 950, 1158, 1367, 1576, 1786, 1942, 1942, 1942, 1942]
BroadCast_FCPS1 = [313, 454, 594, 734,  874, 1014, 1154, 1294, 1434, 1574, 1714, 1776]
l1 = plt.plot(x2, BroadCast_SAFW1, 'r--', label='BroadCast-SAFW')
l2 = plt.plot(x2, BroadCast_CCKP1, 'g--', label='BroadCast-CCKP')
l3 = plt.plot(x2, BroadCast_FCPS1, 'b--', label='BroadCast-FCPS')
plt.plot(x2, BroadCast_SAFW1, 'ro-', x2, BroadCast_CCKP1, 'g+-', x2, BroadCast_FCPS1, 'b^-')
plt.title('BroadCast Time Delay')
plt.xlabel('Packet_Sum 1000Byte/stream')
plt.ylabel('Time Delay/ms')
plt.legend()
plt.show()

BroadCast_SAFW1 = [16, 32, 48, 64, 80, 96, 112, 128, 140, 140, 140, 140]
BroadCast_CCKP1 = [16, 32, 48, 64, 80, 96, 112, 128, 140, 140, 140, 140]
BroadCast_FCPS1 = [16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 183]
l1 = plt.plot(x2, BroadCast_SAFW1, 'r--', label='BroadCast-SAFW')
l2 = plt.plot(x2, BroadCast_CCKP1, 'g--', label='BroadCast-CCKP')
l3 = plt.plot(x2, BroadCast_FCPS1, 'b--', label='BroadCast-FCPS')
plt.plot(x2, BroadCast_SAFW1, 'ro-', x2, BroadCast_CCKP1, 'g+-', x2, BroadCast_FCPS1, 'b^-')
plt.title('BroadCast Arrive Packet')
plt.xlabel('Packet_Sum 1000Byte/stream')
plt.ylabel('Arrive Packet')
plt.legend()
plt.show()

x3 = [32, 64, 96, 128, 160, 192, 224, 256, 288, 320]
UniBroadCast_SAFW1 = [420, 698, 977, 1256, 1536, 1749, 1749, 1749, 1749, 1749]
UniBroadCast_CCKP1 = [419, 693, 971, 1250, 1530, 1729, 1737, 1737, 1737, 1737]
UniBroadCast_FCPS1 = [339, 480, 620,  760,  900, 1040, 1180, 1320, 1399, 1399]
l1 = plt.plot(x3, UniBroadCast_SAFW1, 'r--', label='UniBroadCast-SAFW')
l2 = plt.plot(x3, UniBroadCast_CCKP1, 'g--', label='UniBroadCast-CCKP')
l3 = plt.plot(x3, UniBroadCast_FCPS1, 'b--', label='UniBroadCast-FCPS')
plt.plot(x3, UniBroadCast_SAFW1, 'ro-', x3, UniBroadCast_CCKP1, 'g+-', x3, UniBroadCast_FCPS1, 'b^-')
plt.title('UniBroadCast Time Delay')
plt.xlabel('Packet_Sum 1000Byte/stream')
plt.ylabel('Time Delay/ms')
plt.legend()
plt.show()

UniBroadCast_SAFW1 = [32, 64, 96, 128, 160, 187, 187, 187, 187, 187]
UniBroadCast_CCKP1 = [32, 64, 96, 128, 160, 186, 188, 188, 188, 188]
UniBroadCast_FCPS1 = [32, 64, 96, 128, 160, 192, 224, 256, 276, 276]
l1 = plt.plot(x3, UniBroadCast_SAFW1, 'r--', label='UniBroadCast-SAFW')
l2 = plt.plot(x3, UniBroadCast_CCKP1, 'g--', label='UniBroadCast-CCKP')
l3 = plt.plot(x3, UniBroadCast_FCPS1, 'b--', label='UniBroadCast-FCPS')
plt.plot(x3, UniBroadCast_SAFW1, 'ro-', x3, UniBroadCast_CCKP1, 'g+-', x3, UniBroadCast_FCPS1, 'b^-')
plt.title('UniBroadCast Arrive Packet')
plt.xlabel('Packet_Sum 1000Byte/stream')
plt.ylabel('Arrive Packet')
plt.legend()
plt.show()
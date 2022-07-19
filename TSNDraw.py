import matplotlib.pyplot as plt
x1 = [80, 160, 240, 320, 400, 480]
UniCast_SAFW = [498, 848, 1198, 1359, 1359, 1359]
UniCast_CCKP = [500, 849, 1199, 1363, 1363, 1363]
UniCast_FCPS = [272, 339, 394, 437, 473, 502]
l1 = plt.plot(x1, UniCast_SAFW, 'r--', label='UniCast-SAFW')
l2 = plt.plot(x1, UniCast_CCKP, 'g--', label='UniCast-CCKP')
l3 = plt.plot(x1, UniCast_FCPS, 'b--', label='UniCast-FCPS')
plt.plot(x1, UniCast_SAFW, 'ro-', x1, UniCast_CCKP, 'g+-', x1, UniCast_FCPS, 'b^-')
plt.title('UniCast Time Delay')
plt.xlabel('Packet_Sum 1000Byte/stream')
plt.ylabel('Time Delay/ms')
plt.legend()
plt.show()

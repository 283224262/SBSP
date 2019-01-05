import random
output_dir = 'C:\\Users\\Administrator\\Desktop\\Instances for paper3\\'

visiable_ratio = 3 
g_sate = 10
g_ter = 8
g_times = 20
for n in range(7,13):
    sate = g_sate * n
    ter = g_ter * n
    times = g_times * n
    b0 = times 
    a0 = times - 20 
    for m in range(0,5):
        b = b0 - m
        a = a0 - m
        output_file = output_dir + 'PB_'+ str(sate)+'_'+str(ter)+'_'+ str(times)+'_'+str(a)+'_'+str(b)+'.txt'
        with open(output_file, 'w') as fo:
            fo.writelines(str(sate)+'\n')
            fo.writelines(str(ter)+'\n')
            fo.writelines(str(times)+'\n')
            for i in range(sate):
                for j in range(ter):
                    for k in range(times):
                        if random.randint(1,4) <= visiable_ratio:
                            fo.writelines(str(1)+' ')
                        else:
                            fo.writelines(str(0)+' ')
                    fo.writelines('\n')
            for i in range(sate):
                fo.writelines(str(random.randint(int(a),int(b)))+' ')


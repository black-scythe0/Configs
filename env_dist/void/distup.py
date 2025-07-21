#!/bin/python3

from multiprocessing import Process
import sys
def CommandArgs():
    if sys.argv.__len__() >= 3:
        if (arg:=sys.argv[1]) in ['--dissect','-d', '--join','j'] :
            return arg
            

def dissector(file_name: str):
    div_data1 = ''

    with open(file_name , 'rb') as file:
        
        data = file.readlines()
        data_len: int = data.__len__()
        return data

# i know it's horrible 
# i know it's horrible 
# i know it's horrible 
# i know it's horrible 
# i know it's horrible 

def joiner(file_name, data):
    o = 0
    import pickle
    with open(file_name + '.data','wb') as file:
        with open(file_name + '.data1', 'wb') as file1:
            with open(file_name + '.data2', 'wb') as file2:
                with open(file_name + '.data3', 'wb') as file3:
                    with open(file_name + '.data4', 'wb') as file4:
                    
                        for i in data:
                            if o < 83210: 
                                pickle.dump(i, file)
                            elif o < 83210*2:
                                pickle.dump(i,file1)
                            elif o < 83210*3:
                                pickle.dump(i,file2)                            
                        
                            elif o < 83210*4:
                                pickle.dump(i,file3)                            
                            else:
                                pickle.dump(i,file4)                            
                            o += 1
                        print(o/5)
        

CommandArgs()
if __name__ == '__main__':

    #a = Process(target=dissector, args=('void.tar.xz',))
    a = dissector('void.tar.xz')
    #print(type(a))
    joiner('void.tar.xz', a)

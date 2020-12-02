import pandas as pd
import numpy as np
import pyvisa
import time

def get_instrument_id(instrument):
    instrument.write('*IDN?')
    id_string = instrument.read()
    #id_string = 'Chroma ATE,61500,123456,01.00'
    parse_id_string = id_string.split(',')
    _company_ = parse_id_string[0]
    _model_ = parse_id_string[1]
    _serial_ = parse_id_string[2]
    _firmware_ = parse_id_string[3]
    return _company_, _model_, _serial_, _firmware_

def reset_setting_to_default(instrument):
    instrument.write('*RST')
    time.sleep(5)
    return 0

sel_instrument = []

rm = pyvisa.ResourceManager()
my_instruments = rm.list_resources()
print(my_instruments)

for index, my_instrument in enumerate(my_instruments):
    sel_instrument[index] = rm.open_resource(my_instrument)
    company, model, serial, firmware = get_instrument_id(sel_instrument[index])
    print(company, '|', model, '|', serial, '|', firmware)

    #if model == '61512' or model == '61702' or model == '61507' or model == '61508' or model == '61509':
    #    sel_instrument = rm.open_resource(my_instrument)

rm.close()

#loads = np.arange(0, 20+2, 2)
#for load in loads:
#    print('%.0f %.2f %.2fV %.3fmA %.4fohm' %(load, load, load, load, load))
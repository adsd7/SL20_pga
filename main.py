# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import datetime
import numpy as np
import matplotlib.pyplot as plt


def make_list(line: str) -> list:
    return [int(line[i:i + 2], 16) for i in range(0, len(line), 2)]


def main():
    pg_keys = ['TVGAIN0', 'TVGAIN1', 'TVGAIN2', 'TVGAIN3', 'TVGAIN4', 'TVGAIN5', 'TVGAIN6', 'INIT_GAIN', 'FREQUENCY',
               'DEADTIME', 'PULSE_P1', 'PULSE_P2', 'CURR_LIM_P1', 'CURR_LIM_P2', 'REC_LENGTH', 'FREQ_DIAG',
               'SAT_FDIAG_TH', 'FVOLT_DEC', 'DECPL_TEMP', 'DSP_SCALE', 'TEMP_TRIM', 'P1_GAIN_CTRL', 'P2_GAIN_CTRL']
    gain_time = [100, 200, 300, 400, 600, 800, 1000, 1200, 1400, 2000, 2400, 3200, 4000, 5200, 6400, 8000]
    a = json.loads('''{"date":"1651346402",
                       "PG":["ffffff10a520a00032824810c088ff00ee7c4f0000224c"],
                       "TH":["c558cffffffffe69084210808080800788888888888884210842108080808000"],
                       "RW":["fffffff132170f100e1314100d0909082a2b3838201a171406070704050504050504030405060604040404040\
404050504050605070606070707060606070708080a090a2a2c2a303036ffff9238404c464a4c52444a52545e604e4e56685e5\
8745a5c5c625e56646a685c625c6460725e745e56605c586a5c54686462606466"]}''')
    print(a)
    print(datetime.datetime.fromtimestamp(int(a["date"])))
    pg = make_list(a["PG"][0])
    th = make_list(a["TH"][0])
    rw = make_list(a["RW"][0])
    pg_dict = {key: pg[index] for index, key in enumerate(pg_keys)}
    print(f"Record time for preset 1= {4.096 * ((pg_dict['REC_LENGTH'] >> 4) + 1)} [ms]")
    print(f"Record time for preset 1= {4.096 * ((pg_dict['REC_LENGTH'] & 0b1111) + 1)} [ms]")
    x_th = []
    for x in th[:6]:
        for y in [gain_time[x >> 4], gain_time[x & 0b1111]]:
            x_th.append(y if not x_th else y+x_th[-1])
    print(x_th)
    print(len(pg))
    print(len(th))
    print(len(rw))
    plt.plot(range(0, len(rw)), rw)
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

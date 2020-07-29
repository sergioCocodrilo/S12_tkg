'''
Reads the result from the S12 instruction: DISPLAY-TRUNK-STATUS:ALL
and produces a report of the state of every tkg.

tkg: trunk group
DISPLAY-TRUNK-STATUS is the instruction 4018
'''
import re
import pandas as pd

def analyse_4018(in_file):
    '''reads the result of instruction 4018'''
    # date regex
    daterx = re.compile(r'(\d{4}-\d{2}-\d{2})  \d{2}:\d{2}:\d{2}')
    date = None

    # counters
    en_count = 0

    # data frame output
    df = pd.DataFrame(columns=['en', 'tn', 'tkgid', 'tkseq', 'type', 'state'])
    df_i = 0 # data frame index

    with open(in_file, 'r') as f:
        for l in f:
            # search for the date of the file
            daterx_ = daterx.search(l)
            if daterx_:
                date = daterx_.group(1)
            if l[9:11] == "H'":
                en = l[9:16].strip()
                tn = l[27:33].strip()
                tkgid = l[34:51].strip()
                tkseq = l[52:58].strip()
                type_ = l[59:68].strip()
                state = l[68:77].strip()
                #print(en, tn, tkgid, tkseq, type_, state)
                if tkgid != '':
                    df.loc[df_i] = [en, tn, tkgid, tkseq, type_, state]
                    df_i += 1
    df.to_csv('data/output/s12_4018_result_' + date + '.csv', index=False)

    # Processing the results
    tkgs = df.tkgid.unique()
    # get all possible states of trunks
    all_trunk_states = df.state.unique()

    with open('data/output/trunk_groups_status.txt', 'w') as f:
        for tkg in tkgs:
            f.write('-' * 50 + '\n' + tkg + '\n')
            for state in all_trunk_states:
                f.write("\t{:8}:{}\n".format(state, len(df[(df.tkgid == tkg) & (df.state == state)].index)))



if __name__ == '__main__':
    analyse_4018('data/input/result_of_4018.txt')

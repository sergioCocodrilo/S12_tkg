
class TKG:
    def __init__(self, tkgid):
        self.tkgid   = tkgid
        self.extblk  = 0
        self.avfree  = 0
        self.avbusy  = 0
        self.ready   = 0
        self.blocked = 0
        self.unavail = 0
    def __repr__(self):
        repstr = []
        spacer = ''
        if self.extblk > 0 or self.ready > 0 or self.unavail > 0:
            spacer = '\t\t\t'
        else:
            return ''
        repstr.append(spacer + self.tkgid)
        repstr.append(spacer + '   ‣ EXTBLK :{:4}'.format(self.extblk))
        repstr.append(spacer + '   ‣ AVFREE :{:4}'.format(self.avfree))
        repstr.append(spacer + '   ‣ AVBUSY :{:4}'.format(self.avbusy))
        repstr.append(spacer + '   ‣ READY  :{:4}'.format(self.ready))
        repstr.append(spacer + '   ‣ BLOCKED:{:4}'.format(self.blocked))
        repstr.append(spacer + '   ‣ UNAVAIL:{:4}'.format(self.unavail))
        return ('\n'.join(repstr) + '\n')


def display_results(in_file):
    all_tkg = []
    tkg = None
    with open(in_file, 'r') as f:
        for l in f:
            l = l.strip()
            if l.startswith('-----'):
                if tkg:
                    all_tkg.append(tkg)
                tkg = None
            elif not tkg:
                tkg = TKG(l.strip())
            elif l.startswith('EXT'):
                tkg.extblk = int(l.split(':')[1])
            elif l.startswith('AVF'):
                tkg.avfree = int(l.split(':')[1])
            elif l.startswith('AVB'):
                tkg.avbusy = int(l.split(':')[1])
            elif l.startswith('REA'):
                tkg.ready = int(l.split(':')[1])
            elif l.startswith('BLO'):
                tkg.blocked = int(l.split(':')[1])
            elif l.startswith('UNA'):
                tkg.unavail = int(l.split(':')[1])
    [print(tkg,end='') for tkg in all_tkg]

if __name__ == '__main__':
    display_results('data/output/trunk_groups_status.txt')

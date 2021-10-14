

class Statistics:
    def __init__(self):
        self.stat={
            'python':0,
            'нейронные сети': 0,
            'big data': 0,
            'sql': 0,
            'django': 0,
            'resr': 0,
            'c++': 0,
            'linux': 0,
            'api': 0,
            'http': 0,
            'flask': 0,
            'java': 0,
            'git': 0,
            'javascript': 0,
            'pytest': 0,
            'postgresql': 0,
            'oracle': 0,
            'mysql': 0,
            'mssql': 0
        }

    def go_seek( self, s ):
        n = 0
        try:
            s = s.lower()
            k = self.stat.keys()
            for ki in k:
                i = s.find(ki)
                if i > 0:
                    self.stat[ki] += 1
                    n += 1
        except AttributeError:
            pass
        return n

    def get_stat( self ):
        sorted_tuple = sorted( self.stat.items(), key=lambda x: x[1], reverse=True )
        return sorted_tuple

class Corona:
    
    import pandas as pd

    def makeDates(self, s, e, p, freq = 'D'):
        import pandas as pd
        self.s = s
        self.e = e
        self.freq = freq
        self.p = p
        if not p:
            out = pd.date_range(start=self.s, end=self.e, periods = None, freq = self.freq)
        elif p:
            out = pd.date_range(start=self.s, end=self.e, periods = self.p, freq = self.freq)
        return(out) 

    def getData(self, url):
        ''' retrieves data from given url '''
        import requests
        import pandas as pd

        self.url = url
        html = requests.get(url).content
        df_list = pd.read_html(html)
        return(df_list)

    def getIndianDataFromWiki(self, url):
        ''' retrieves Indian coronavirus status '''
        
        import requests
        import pandas as pd

        self.url = url
        html = requests.get(url).content
        df_list = pd.read_html(html)
        out = pd.DataFrame(df_list[6])
        out = out.drop([0, 1, 2, 39, 40])
        out.rename(columns={0: "States", 1: "Cases", 2: "Deaths", 3:"Recoveries", 4:"Active"}, inplace = True)
        return(out)

    def cleanValues(self, var, pat):
        ''' clearn and convert string values into float values '''
        self.var = var
        self.pat = pat
        
        var = var.str.replace(self.pat, '')
        return(var)
        

        
        

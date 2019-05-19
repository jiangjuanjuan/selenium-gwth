import xlrd
class ReadE():
    def Read_excel(self,path,sheetname="Sheet1"):
        data=xlrd.open_workbook(path)
        table=data.sheet_by_name(sheetname)
        nrows=table.nrows
        ncols=table.ncols
        keys=table.row_values(0)
        if nrows <=1:
            print("行数小于1")
        else:
            r = []
            j = 1
            for x in range(1,nrows):
                s = {}
                values = table.row_values(x)
                for x in range(ncols):
                    s[keys[x]] = values[x]
                r.append(s)
                j+=1
            return r
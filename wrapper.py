import sys
import pandas as pd
import xlrd as xlrd
import os


class Wrapper:

    def __init__(self, route_files):
        self.route_files = route_files

    def iterate_folder(self):
        for itm in os.listdir(self.route_files):
            if '.xls' in itm:
                self.new_file(self.route_files + '\\' + itm)

    def new_file(self, file_name):
        #file_name = sys.argv[1]
        header = True
        try:
            sheet = xlrd.open_workbook(file_name).sheet_by_index(0)
        except Exception as err:
            print(err)
        take = False
        list_tramos = []
        for row in range(sheet.nrows):
            row_to_add = []
            for col in range(sheet.ncols):
                if 'Cámaras' in str(sheet.cell(row, 0)):
                    take = True
                    break
                if take and sheet.cell(row, col).ctype != 0:
                    row_to_add.append(str(sheet.cell(row, col)).replace('text:', ''))

                if ':' in str(sheet.cell(row, 0)).replace('text:', '') and take is True:
                    take = False
            if row_to_add.__len__() > 1:
                print(';'.join(row_to_add))
                #if 'Código actividad' in ';'.join(row_to_add) and header:
                #    list_tramos.append(';'.join(row_to_add).replace("'", ""))
                #    header = False
                if 'Código actividad' not in ';'.join(row_to_add):
                    list_tramos.append(';'.join(row_to_add).replace("'", ""))
            file_name = 'D:\Proyecto_de_levantamiento_de_recibo_de_obra\\total_camaras.csv'
            if os.path.exists(file_name):
                append_write = 'a'  # append if already exists
            else:
                append_write = 'w'  # make a new file if not
            with open(file_name, append_write) as f:
                for item in list_tramos:
                    f.write("%s\n" % item)

# https://www.uktradeinfo.com/media/413de34u/bds_export_import_technical_specification.xlsx

class ImportExport:
    def __init__(self, line):
        self.period_reference = line[0:6]
        self.type = line[6:7]
        self.month_of_account = line[7:13]
        self.comcode = line[13:21]
        self.sitc = line[21:26]
        self.country_of_destination_dispatch_consignment_1 = line[26:29]
        self.country_of_destination_dispatch_consignment_2 = line[29:31]
        self.port_code_1 = line[31:34]
        self.port_code_2 = line[34:37]
        self.country_of_origin_1 = line[37:40]
        self.country_of_origin_2 = line[40:42]
        self.mode_of_transport = line[42:44]
        self.statistical_value = line[44:56]
        self.netmass = line[56:68]
        self.supplementary_unit = line[68:80]
        self.suppression_indicator = line[80:81]
        self.flow = line[81:84]
        self.record_type = line[84:85]

file = open("BDSimp2201.txt", "r")
lines = file.readlines()

line = lines[270793]
import_export = ImportExport(line)

print(import_export.__dict__)
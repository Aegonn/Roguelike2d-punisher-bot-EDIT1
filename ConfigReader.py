"""
Reads in simple config files
"""

import configparser

class ConfigReader:
    DATA_FOLDUER = "TekkenData/"

    values = {}

    def __init__(self, filename):
        self.path = ConfigReader.DATA_FOLDUER + filename + ".ini"
        self.parser = configparser.ConfigParser()
        try:
            self.parser.read(self.path)
        except:
            print("Error reading config data from " + self.path + ". Using default values.")


    def get_property(self, section, property_string, default_value):

        try:
            if type(default_value) is bool:
                value = self.parser.getboolean(section, property_string)
            else:
                value = self.parser.get(section, property_string)
        except:
            value = default_value

        if section not in self.parser.sections():
            self.parser.add_section(section)
        self.parser.set(section, property_string, str(value))
        return value

    def set_property(self, section, property_string, value):
        self.parser.set(section, property_string, str(value))


    def add_comment(self, comment):
        if 'Comments' not in self.parser.sections():
            self.parser.add_section('Comments')
        self.parser.set('Comments', '; ' + comment, "")


    def write(self):
        with open(self.path, 'w') as fw:
            self.parser.write(fw)



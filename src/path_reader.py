import ConfigParser

#parsing the property file
def configParser(section):

    Config = ConfigParser.ConfigParser()
    Config.read('prop.ini')
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

#list name of subjects path
def source_name():
    name_path = configParser("SectionOne")['source_list_name']
    return name_path

#scaled data (in g units)
def source_scaled(name):
    path = configParser("SectionOne")['source_path_scaled']
    scaled_path = path + name + '.csv'
    return scaled_path

#data that have been micro-annotated
def source_micro(name):
    path = ConfigParser("SectionOne")['source_path_micro']
    micro_path = path + name + '.csv'

from lxml import etree

class corpcode:
    comps = []
    def __init__(self):
        comp_dict = {}
        f = open("corpcode/CORPCODE.xml", "r")
        xml = f.read().encode()
        tree = etree.fromstring(xml)
        for comp in tree.getchildren():
            for elem in comp.getchildren():
                if elem.text:
                    text = elem.text
                comp_dict[elem.tag] = text
            if comp.tag == "list":
                self.comps.append(comp_dict)
                comp_dict = {}
        
    def findWithCode(self, code):
        for dict_ in self.comps:
            if dict_["corp_code"] == code:
                return dict_
        return {}
    
    def findWithName(self, name):
        for dict_ in self.comps:
            if dict_["corp_name"] == name:
                return dict_
        return {}
import os
import xml.etree.cElementTree as ET
import pandas as pd 
    
    
    
class xml_Parser:
    
    def __init__(self):
        
        self.xml_file = r'C:\Users\XS00053\Desktop\參數調整python\python_workspace\For_XML\for_xml\text.xml'
        self.tree = ET.parse(self.xml_file)
        self.root = self.tree.getroot()
        self.APTCharV3_attrib = []
        self.APTChanFreq_attrib = []
        self.APTBandwidthPA_attrib = []
        self.APTRec_attrib = []
        self.APT = []
        self.df1 = pd.DataFrame()
        self.df2 = pd.DataFrame()
        self.df3 = pd.DataFrame()
        self.df4 = pd.DataFrame()
        self.df5 = pd.DataFrame()
        
    def find_APTCharV3_attrib(self):
        root = self.tree.getroot() 
        APTCharV3 ='./APTCharV3'
        APTCharV3_list = root.findall(APTCharV3)

        for APTCharV3 in APTCharV3_list :
            self.APTCharV3_attrib.append(APTCharV3.attrib)
            for APTChanFreq in APTCharV3:
                self.APTChanFreq_attrib.append(APTChanFreq.attrib)
                for APTBandwidthPA in APTChanFreq :
                    self.APTBandwidthPA_attrib.append(APTBandwidthPA.attrib)
                    for APTRec in APTBandwidthPA:
                        self.APTRec_attrib.append(APTRec.attrib)
                        combined_dict = {**APTCharV3.attrib, **APTChanFreq.attrib, **APTBandwidthPA.attrib, **APTRec.attrib}  
                        self.APT.append(combined_dict)

                
        self.df1 = pd.DataFrame(self.APTCharV3_attrib)
        self.df2 = pd.DataFrame(self.APTChanFreq_attrib)
        self.df3 = pd.DataFrame(self.APTBandwidthPA_attrib)
        self.df4 = pd.DataFrame(self.APTRec_attrib)
        self.df5 = pd.DataFrame(self.APT)
        
        
        unique_list = []
        df =pd.DataFrame()
        for col in self.df5.columns:
            unique_values = self.df5[col].unique()
            unique_list.append(unique_values)
            # print(f"Column {col} has unique values: {unique_values}")
        print(unique_list)
        # df.to_csv('unique_df.csv')

    def find_APTCharV3_value(self,manuf_id, product_id, tech, band, subband, sig_path, value):
        root = self.tree.getroot()
        APTCharV3 ='./APTCharV3[@manuf_id="{0}"][@product_id="{1}"][@product_rev="{2}"][@tech="{3}"][@band="{4}"][@subband="{5}"][@sig_path="{6}"]'.format(manuf_id, product_id, product_rev, tech ,band ,subband ,sig_path)
        print("Xpath = " + APTCharV3)
        elements = root.find(APTCharV3)
        
        if len(elements)==0:
            print("Can't find the node")
        # else:
        #     print("Find APTCharV3 elements")
        #     return
        
        for element in elements:
            
            if value is not None and unit is not None and pa_state is not None and bw is not None:
                xpath_str = './APTChanFreq[@value="{0}"][@unit="{1}"]'.format(value, unit)
                print(xpath_str)
            else:
                print(" xpath_str : Error ")
                
            for sub_element in elements.find(xpath_str):
                print("APTBandwidthPA = " + str(sub_element.attrib))
            
                if sub_element is None:
                    print("Can't find the attribute")
                    return
                else:
                    pass

    def APTCharV3 (self):
        for APTCharV3 in self.root.iter('APTCharV3'):
            print(APTCharV3.attrib)

    def APTChanFreq (self):
        for APTChanFreq in self.root.iter('APTChanFreq'):
            print(APTChanFreq.attrib)

    def APTBandwidthPA (self):
        for APTBandwidthPA in self.root.iter('APTBandwidthPA'):
            print(APTBandwidthPA.attrib)

    def APTRec (self):
        for APTRec in self.root.iter('APTRec'):
            print(APTRec.attrib)
    
    def Mod(self):
        for year in self.root.iter('year'):
            new_year = int(year.text) +1
            year.text = str(new_year)
            year.set('update', 'yes')
        self.tree.write('papa1.xml')

xml_Parser().Mod()
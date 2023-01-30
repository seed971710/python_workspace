import configparser

# 讀取 CFG 檔案
config = configparser.RawConfigParser()
config.optionxform = lambda option: option

path=r'C:\Users\XS00053\Desktop\參數調整python\python_workspace\XS_TTT.CFG'
config.read(path,encoding="utf-8-sig")
Sections_get = config.sections()

sections = [Sections_get[5], Sections_get[6], Sections_get[7], Sections_get[8]]
#['DUT1 Cable Loss Mapping', 'DUT1 RFIO2 Table', 'DUT1 RFIO3 Table', 'DUT1 RFIO4 Table']

RFs = ['RF1', 'RF3', 'RF5', 'RF7']


def adjusted_LTE(Band_num, new_setting):
        Band_num=input("輸入要修改的LTE Band_Number: ")
        print(config.get(Sections_get[5],f"LTE_Band{Band_num}_TX"))
        new_setting=input("Band %s 要更新的數值: "%Band_num)
        LTE_adjusted_lists = []
        lte_options = [f"LTE_Band{Band_num}_TX", f"LTE_Band{Band_num}_RX", f"LTE_Band{Band_num}_RXd"]
        section_rf_map = dict(zip(sections, RFs))
        for section in sections:
            for option in lte_options:
                new_value = f"{section_rf_map[section]}, {new_setting}"
                ad = section, option, new_value
                LTE_adjusted_lists.append(ad)
    
        return LTE_adjusted_lists

def adjusted_NR(Band_num, new_setting):
        Band_num=input("輸入要修改的NR Band_Number: ")
        print(config.get(Sections_get[5],f"NR_n{Band_num}_TX"))
        new_setting=input("Band %s 要更新的數值: "%Band_num)
        NR_adjusted_lists = []
        lte_options = [f"NR_n{Band_num}_TX", f"NR_n{Band_num}_RX", f"NR_n{Band_num}_RXd"]
        section_rf_map = dict(zip(sections, RFs))
        for section in sections:
            for option in lte_options:
                new_value = f"{section_rf_map[section]}, {new_setting}"
                ad = section, option, new_value
                NR_adjusted_lists.append(ad)
    
        return NR_adjusted_lists

def LTE_new_setting():
    x=adjusted_LTE('Band_num', 'new_setting')
    for i in range(len(x)):
        config.set(x[i][0],x[i][1],x[i][2])
        
def NR_new_setting():
    x=adjusted_NR('Band_num', 'new_setting')
    for i in range(len(x)):
        config.set(x[i][0],x[i][1],x[i][2])


keyword='no'

while True:
    user_input = input( "要修改 LTE/NR Band 參數嗎 ?" )
    if keyword in user_input :
        break
    elif 'lte' in user_input :
        LTE_new_setting()
    elif 'nr' in user_input :
        NR_new_setting()
        


with open(path,'w') as fp:
    config.write(fp)


import configparser

# 讀取 CFG 檔案
config = configparser.RawConfigParser()
config.optionxform = lambda option: option

path=r'C:\Users\jgy21\OneDrive\桌面\python_workspace\XS_TEST01.CFG'
config.read(path,encoding="utf-8-sig")

global sections ,RFs

sections = ['DUT1 Cable Loss Mapping', 'DUT1 RFIO2 Table', 'DUT1 RFIO3 Table', 'DUT1 RFIO4 Table']
RFs = ['RF1', 'RF3', 'RF5', 'RF7']


def adjusted_LTE(Band_num, new_setting):
        Band_num=input("輸入要修改的 Band_Number: ")
        print(config.get('DUT1 Cable Loss Mapping',f"LTE_Band{Band_num}_TX"))
        new_setting=input("Band %s 要更新的數值: "%Band_num)
        ad_lists = []
        lte_options = [f"LTE_Band{Band_num}_TX", f"LTE_Band{Band_num}_RX", f"LTE_Band{Band_num}_RXd"]
        section_rf_map = dict(zip(sections, RFs))
        for section in sections:
            for option in lte_options:
                new_value = f"{section_rf_map[section]}, {new_setting}"
                ad = section, option, new_value
                ad_lists.append(ad)
    
        return ad_lists 


def new_setting():
    x=adjusted_LTE('Band_num', 'new_setting')
    for i in range(len(x)):
        config.set(x[i][0],x[i][1],x[i][2])

keyword='no'
while True:
    user_input = input( "要修改 Band 參數嗎 ?" )
    if keyword in user_input :
        break
    new_setting()


with open(path,'w') as fp:
    config.write(fp)


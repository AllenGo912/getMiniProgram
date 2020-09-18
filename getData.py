import requests
import json
import xlwt

# 获取某一页数据
def getOne(index,cityId):
    url = "http://api.tc688.net/api/services/app/merchant/LoadCategoryMerchants"
    header = {
        'Accept':'application/json',
        'Origin':'http://zazhi.tc688.net',
        'Host':'api.tc688.net',
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.14(0x17000e2e) NetType/WIFI Language/zh_CN',
        'Authorization':'Bearer G2sOmL0stfJ5vuN0dO3Ilesw2yF_KhbIX_4grGnXFKac1qXhj2qUa53SDhX5xkH49dsQk013-RwPCIPutdNFe2nhf8dqFkuLxDEFLjTmX03SLFIBle1b6q7YhUlOpQdtFNcHHdasAapPdolHdQw4k6-uVnyZrqa0nXNCbA6V1fT2ehEsqZ54eO3fepXA_gg-hS7gvih6yQ7lSwkmehvQxg0gyV1x1eiPjxqBIx1KIwjNdCuCCJCmgWfPTemo2Xuqfl5KN4miNyeopDDQGArwpn3NfnLRiIy7gaTlsiZajSqX0Gzzw64xLoN_C0p17Pspo3WvCqmj6njZJkHaJVmmWJtzb8nAXHkBcSiFmup97NaasnAfM53bxy12gm7TgJglo6rTvMTtCgH6HyexnuBqMJxjv3Zsv3TIH7_JHZjHNgWA89OCQ9oKv3nHU4Tipo6PqbbWksrFVYcYjcaJqKqVN92EfwqtuFAiTD7iPmWamlrDYZ_fWyymQF0Qd9WaoqcD',
        'Accept-Encoding':'gzip, deflate',
        'Referer':'http://zazhi.tc688.net/companylist?id=148',
        'Accept-Language':'zh-cn',
        'Cookie':"ASP.NET_SessionId=hjievwpnjs25nkrmr3crlgql; UM_distinctid=1748d78aa953cf-0f85e5e5e1461d8-26182142-3d10d-1748d78aa96a96; Abp.Localization.CultureName=zh-cn",
    }
    data = {"pageIndex":index,"pageSize":50,"regionId":cityId,"categoryId":"148","orderRule":0}
    r = requests.post(url=url,data=data,headers=header)
    data_lst = json.loads(r.text)['result']
    return data_lst

def dealData():
    # 创建xls对象
    file = xlwt.Workbook()
    chongqing = file.add_sheet('重庆')
    guizhou = file.add_sheet('贵州')
    # 添加表头
    titles = ['名称','电话','地区']
    for i in range(0,3):
        chongqing.write(0,i,titles[i])
        guizhou.write(0,i,titles[i])
    # 配置变量
    flag1 = True
    flag2 = True
    index = 1
    c1_col = 1
    c2_col = 1
    sum = 1
    # 爬取数据
    while True:
        data_lst1 = getOne(index,'32')# 获取信息1
        data_lst2 = getOne(index,'8')# 获取信息2
        # 写入信息
        if data_lst1:
            for d in data_lst1:
                print(f"正在爬取到第{sum}条数据：名称：{d['name']} 电话：{d['contactPhone']} 城市名字：{d['cityName']}")
                chongqing.write(c1_col,0,d['name'])
                chongqing.write(c1_col,1,d['contactPhone'])
                chongqing.write(c1_col,2,d['cityName'])
                c1_col = c1_col + 1
                sum = sum + 1
                
        else :
            flag1 = False
        if data_lst2:
            for d in data_lst2:
                print(f"正在爬取到第{sum}条数据：名称：{d['name']} 电话：{d['contactPhone']} 城市名字：{d['cityName']}")
                guizhou.write(c2_col,0,d['name'])
                guizhou.write(c2_col,1,d['contactPhone'])
                guizhou.write(c2_col,2,d['cityName'])
                c2_col = c2_col + 1
                sum = sum + 1
        else :
            flag2 = False
        if flag1 == False and flag2 == False:
            break        
        index = index + 1
    file.save("维修部信息.xls") 
    print(f"保存成功！共计{sum-1}条数据")

if __name__ == "__main__":
    dealData()
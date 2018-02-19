import itchat
import re
#import matplotlib.pyplot as plt

def display(dic_list):
	for info_dic in dic_list:
		print('NickName:'+info_dic['NickName'])
		print('RemarkName:'+info_dic['RemarkName'])
		print('RemarkPYInitial:'+info_dic['RemarkPYInitial'])
		print('Signature:'+info_dic['Signature'])
		print('Sex:'+info_dic['Sex'])
		print('Loacl:'+info_dic['Province']+'  '+info_dic['City'])
		print('---------------------')


itchat.login()
friends = itchat.get_friends(update=True)[0:]

info_list = []
name_list = []

MaleNum = 0
FemaleNum = 0
OtherNum = 0
#-------------
print('<<<<<<<<<<<<<<<朋友信息>>>>>>>>>>>>>>>>')
for i in friends:
	info_dic = {}
	name_list_temp = []
	Signature = re.sub('<.*>','',i["Signature"],re.S)
	NickName = re.sub('<.*>','',i["NickName"],re.S)
	if i['Sex'] == 1:
		Sex = '男'
		MaleNum += 1
	elif i['Sex'] == 2:
		Sex = '女'
		FemaleNum +=1
	else: 
		Sex = '未知'
		OtherNum +=1

	info_dic['NickName'] = NickName
	info_dic['RemarkName'] = i['RemarkName']
	info_dic['RemarkPYInitial']=i['RemarkPYInitial']
	info_dic['Signature'] = Signature
	info_dic['Sex'] = Sex
	info_dic['Province'] = i['Province']
	info_dic['City'] = i['City']
	info_list.append(info_dic)

	name_list_temp.append(i['RemarkName'])
	name_list_temp.append(i['RemarkPYInitial'])
	name_list.append(name_list_temp)

display(info_list)
#-------------
print('<<<<<<<<<<<<<<<性别比例>>>>>>>>>>>>>>>>')
TotalNum = FemaleNum+MaleNum+OtherNum
print("男:"+str(MaleNum)+'  '+str(MaleNum/TotalNum))
print("女:"+str(FemaleNum)+'  '+str(FemaleNum/TotalNum))
print("未知:"+str(OtherNum)+'  '+str(OtherNum/TotalNum))
print("总人数:"+str(TotalNum))

#-------------
print('<<<<<<<<<<<<<<<相同备注名缩写>>>>>>>>>>>>>>>>')
RemarkPYInitial_sorted = sorted(name_list,key=lambda item:item[1])
for index,value in enumerate(RemarkPYInitial_sorted):
	repeated = False
	if index<len(RemarkPYInitial_sorted)-1:
		if value[1]!='' and value[1] == RemarkPYInitial_sorted[index+1][1]:
			if repeated == False:
				print(value)
				print(RemarkPYInitial_sorted[index+1])
				repeated = True
			else:
				print(RemarkPYInitial_sorted[index+1])
		else:
			repeated = False;
	else: print("Finish")

#-------------城市图表
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


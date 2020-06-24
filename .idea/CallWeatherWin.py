'''
天气信息查询

'''

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow
from WeatherWin import Ui_Form
import requests

class MainWindow(QMainWindow ):
	def __init__(self, parent=None):    
		super(MainWindow, self).__init__(parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
 		
	def queryWeather(self):
		cityName = self.ui.weatherComboBox.currentText()
		cityCode = self.transCityName(cityName)

		rep = requests.get('http://www.weather.com.cn/data/sk/' + cityCode + '.html')
		rep.encoding = 'utf-8'
		print( rep.json() ) 
		
		msg1 = '城市: %s' % rep.json()['weatherinfo']['city'] + '\n'
		msg2 = '风向: %s' % rep.json()['weatherinfo']['WD'] + '\n'
		msg3 = '温度: %s' % rep.json()['weatherinfo']['temp'] + ' 度' + '\n'
		msg4 = '风力: %s' % rep.json()['weatherinfo']['WS'] + '\n'
		msg5 = '湿度: %s' % rep.json()['weatherinfo']['SD'] + '\n'
		result = msg1 + msg2 + msg3 + msg4 + msg5
		self.ui.resultText.setText(result)
		
	def transCityName(self ,cityName):
		cityCode = ''
		if cityName == '北京' :
			cityCode = '101010100'
		elif cityName == '天津' :
			cityCode = '101030100'
		elif cityName == '上海' :
			cityCode = '101020100'
		elif cityName == '重庆' :
			cityCode = '101040100'
		elif cityName == '哈尔滨' :
			cityCode = '101050101'
		elif cityName == '齐齐哈尔' :
			cityCode = '101050201'
		elif cityName == '大兴安岭' :
			cityCode = '101050701'
		elif cityName == '长春' :
			cityCode = '101060101'
		elif cityName == '吉林' :
			cityCode = '101060201'
		elif cityName == '通化' :
			cityCode = '101060501'
		elif cityName == '沈阳' :
			cityCode = '101070101'
		elif cityName == '大连' :
			cityCode = '101070201'
		elif cityName == '抚顺' :
			cityCode = '101070401'
		elif cityName == '锦州' :
			cityCode = '101070701'
		elif cityName == '辽阳' :
			cityCode = '101071001'
		elif cityName == '铁岭' :
			cityCode = '101071101'
		elif cityName == '呼和浩特' :
			cityCode = '101080101'
		elif cityName == '石家庄' :
			cityCode = '101090101'
		elif cityName == '唐山' :
			cityCode = '101090501'
		elif cityName == '廊坊' :
			cityCode = '101090601'
		elif cityName == '衡水' :
			cityCode = '101090801'
		elif cityName == '邯郸' :
			cityCode = '101091001'
		elif cityName == '秦皇岛' :
			cityCode = '101091101'
		elif cityName == '雄安新区' :
			cityCode = '101091201'
		elif cityName == '太原' :
			cityCode = '101100101'
		elif cityName == '西安' :
			cityCode = '101110101'
		elif cityName == '济南' :
			cityCode = '101120101'
		elif cityName == '青岛' :
			cityCode = '101120201'
		elif cityName == '烟台' :
			cityCode = '101120501'
		elif cityName == '潍坊' :
			cityCode = '101120601'
		elif cityName == '临沂' :
			cityCode = '101120901'
		elif cityName == '乌鲁木齐' :
			cityCode = '101130101'
		elif cityName == '拉萨' :
			cityCode = '101140101'
		elif cityName == '西宁' :
			cityCode = '101150101'
		elif cityName == '兰州' :
			cityCode = '101160101'
		elif cityName == '酒泉' :
			cityCode = '101160801'
		elif cityName == '天水' :
			cityCode = '101160901'
		elif cityName == '银川' :
			cityCode = '101170101'
		elif cityName == '郑州' :
			cityCode = '101180101'
		elif cityName == '许昌' :
			cityCode = '101180401'
		elif cityName == '洛阳' :
			cityCode = '101180901'
		elif cityName == '南京' :
			cityCode = '101190101'
		elif cityName == '无锡' :
			cityCode = '101190201'
		elif cityName == '镇江' :
			cityCode = '101190301'
		elif cityName == '苏州' :
			cityCode = '101190401'
		elif cityName == '南通' :
			cityCode = '101190501'
		elif cityName == '盐城' :
			cityCode = '101190701'
		elif cityName == '徐州' :
			cityCode = '101190801'
		elif cityName == '淮安' :
			cityCode = '101190901'
		elif cityName == '常州' :
			cityCode = '101191101'
		elif cityName == '泰州' :
			cityCode = '101191201'
		elif cityName == '武汉' :
			cityCode = '101200101'
		elif cityName == '杭州' :
			cityCode = '101210101'
		elif cityName == '合肥' :
			cityCode = '101220101'
		elif cityName == '福州' :
			cityCode = '101230101'
		elif cityName == '南昌' :
			cityCode = '101240101'
		elif cityName == '长沙' :
			cityCode = '101250101'
		elif cityName == '贵阳' :
			cityCode = '101260101'
		elif cityName == '成都' :
			cityCode = '101270101'
		elif cityName == '广州' :
			cityCode = '101280101'
		elif cityName == '昆明' :
			cityCode = '101290101'
		elif cityName == '南宁' :
			cityCode = '101300101'
		elif cityName == '海口' :
			cityCode = '101310101'
		elif cityName == '香港' :
			cityCode = '101320101'
		elif cityName == '澳门' :
			cityCode = '101330101'
		elif cityName == '台北' :
			cityCode = '101340101'

		return cityCode
				
	def clearResult(self):
		print('* clearResult  ')
		self.ui.resultText.clear()	
		
if __name__=="__main__":  
	app = QApplication(sys.argv)  
	win = MainWindow()  
	win.show()  
	sys.exit(app.exec_())  

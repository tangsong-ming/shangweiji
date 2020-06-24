import sys
from PyQt5.QtWidgets import QApplication , QMainWindow
from film_recommend import Ui_Form
import requests
import bs4
import re
import pandas as pd
import random
def open_url(url):
    # 使用代理
    # proxies = {"http": "127.0.0.1:1080", "https": "127.0.0.1:1080"}
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}

    # res = requests.get(url, headers=headers, proxies=proxies)
    res = requests.get(url, headers=headers)

    return res


def find_movies(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # 电影名
    movies = []
    targets = soup.find_all("div", class_="hd")
    for each in targets:
        movies.append(each.a.span.text)

    # 评分
    ranks = []
    targets = soup.find_all("span", class_="rating_num")
    for each in targets:
        ranks.append(',评分：%s,' %each.text)

    # 资料
    messages = []
    targets = soup.find_all("div", class_="bd")
    for each in targets:
        try:
            messages.append(each.p.text.split('\n')[1].strip()+','+each.p.text.split('\n')[2].strip())
        except:
            continue

    result = []
    length = len(movies)
    for i in range(length):
        result.append(movies[i] + ranks[i] + messages[i] + '\n')

    return result


# 找出一共有多少个页面
def find_depth(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    depth = soup.find('span', class_='next').previous_sibling.previous_sibling.text

    print(depth)
    return int(depth)


def main():
    host = "https://movie.douban.com/top250"
    res = open_url(host)
    depth = find_depth(res)

    result = []
    for i in range(depth):
        url = host + '/?start=' + str(25 * i)
        res = open_url(url)
        result.extend(find_movies(res))

    with open("./src/豆瓣TOP250电影.txt", "w", encoding="utf-8") as f:
        for each in result:
            f.write(each)


class MainWindow(QMainWindow ):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    def acheieveData(self):
        main()
    def searchData(self):
        data=pd.read_csv(r'.\src\豆瓣TOP250电影.txt',names=['电影名称','评分','导演及主演','影片类型'],sep=',')
        data1 = data['电影名称']
        data2 = data['评分']
        data3 = data['影片类型']
        american = []
        china = []
        france = []
        italy = []
        japan = []
        uk = []
        india = []
        korean = []
        swit = []
        germany = []
        spanish = []
        crime = []
        plot = []
        love = []
        action = []
        war = []
        disaster = []
        cartoon = []
        fantasy = []
        history = []
        suspense = []
        adventure = []
        fiction = []
        music = []
        comedy = []
        panic = []
        biography = []
        for i in range(len(data)):
            if '美国' in data3[i]:
                american.append(data1[i])
            if '中国' in data3[i]:
                china.append(data1[i])
            if '法国' in data3[i]:
                france.append(data1[i])
            if '意大利' in data3[i]:
                italy.append(data1[i])
            if '日本' in data3[i]:
                japan.append(data1[i])
            if '英国' in data3[i]:
                uk.append(data1[i])
            if '印度' in data3[i]:
                india.append(data1[i])
            if '韩国' in data3[i]:
                korean.append(data1[i])
            if '瑞士' in data3[i]:
                swit.append(data1[i])
            if '德国' in data3[i]:
                germany.append(data1[i])
            if '西班牙' in data3[i]:
                spanish.append(data1[i])
            if '犯罪' in data3[i]:
                crime.append(data1[i])
            if '剧情' in data3[i]:
                plot.append(data1[i])
            if '爱情' in data3[i]:
                love.append(data1[i])
            if '动作' in data3[i]:
                action.append(data1[i])
            if '战争' in data3[i]:
                war.append(data1[i])
            if '灾难' in data3[i]:
                disaster.append(data1[i])
            if '动画' in data3[i]:
                cartoon.append(data1[i])
            if '奇幻' in data3[i]:
                fantasy.append(data1[i])
            if '历史' in data3[i]:
                history.append(data1[i])
            if '悬疑' in data3[i]:
                suspense.append(data1[i])
            if '冒险' in data3[i]:
                adventure.append(data1[i])
            if '科幻' in data3[i]:
                fiction.append(data1[i])
            if '音乐' in data3[i]:
                music.append(data1[i])
            if '喜剧' in data3[i]:
                comedy.append(data1[i])
            if '惊悚' in data3[i]:
                panic.append(data1[i])
            if '传记' in data3[i]:
                biography.append(data1[i])
        if self.ui.comboBox.currentText()=='犯罪':
            self.ui.textEdit.setPlainText(random.choice(crime))
        if self.ui.comboBox.currentText()=='剧情':
            self.ui.textEdit.setPlainText(random.choice(plot))
        if self.ui.comboBox.currentText()=='爱情':
            self.ui.textEdit.setPlainText(random.choice(love))
        if self.ui.comboBox.currentText()=='动作':
            self.ui.textEdit.setPlainText(random.choice(action))
        if self.ui.comboBox.currentText()=='战争':
            self.ui.textEdit.setPlainText(random.choice(war))
        if self.ui.comboBox.currentText()=='灾难':
            self.ui.textEdit.setPlainText(random.choice(disaster))
        if self.ui.comboBox.currentText()=='动画':
            self.ui.textEdit.setPlainText(random.choice(cartoon))
        if self.ui.comboBox.currentText()=='奇幻':
            self.ui.textEdit.setPlainText(random.choice(fantasy))
        if self.ui.comboBox.currentText()=='历史':
            self.ui.textEdit.setPlainText(random.choice(history))
        if self.ui.comboBox.currentText()=='悬疑':
            self.ui.textEdit.setPlainText(random.choice(suspense))
        if self.ui.comboBox.currentText()=='冒险':
            self.ui.textEdit.setPlainText(random.choice(adventure))
        if self.ui.comboBox.currentText()=='科幻':
            self.ui.textEdit.setPlainText(random.choice(fiction))
        if self.ui.comboBox.currentText()=='音乐':
            self.ui.textEdit.setPlainText(random.choice(music))
        if self.ui.comboBox.currentText()=='喜剧':
            self.ui.textEdit.setPlainText(random.choice(comedy))
        if self.ui.comboBox.currentText()=='惊悚':
            self.ui.textEdit.setPlainText(random.choice(panic))
        if self.ui.comboBox.currentText()=='传记':
            self.ui.textEdit.setPlainText(random.choice(biography))
        if self.ui.comboBox_2.currentText()=='美国':
            self.ui.textEdit.append(random.choice(american))
        if self.ui.comboBox_2.currentText()=='中国':
            self.ui.textEdit.append(random.choice(china))
        if self.ui.comboBox_2.currentText()=='法国':
            self.ui.textEdit.append(random.choice(france))
        if self.ui.comboBox_2.currentText()=='意大利':
            self.ui.textEdit.append(random.choice(italy))
        if self.ui.comboBox_2.currentText()=='日本':
            self.ui.textEdit.append(random.choice(japan))
        if self.ui.comboBox_2.currentText()=='英国':
            self.ui.textEdit.append(random.choice(uk))
        if self.ui.comboBox_2.currentText()=='印度':
            self.ui.textEdit.append(random.choice(india))
        if self.ui.comboBox_2.currentText()=='韩国':
            self.ui.textEdit.append(random.choice(korean))
        if self.ui.comboBox_2.currentText()=='瑞士':
            self.ui.textEdit.append(random.choice(swit))
        if self.ui.comboBox_2.currentText()=='德国':
            self.ui.textEdit.append(random.choice(germany))
        if self.ui.comboBox_2.currentText()=='西班牙':
            self.ui.textEdit.append(random.choice(spanish))
if __name__=="__main__":
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())




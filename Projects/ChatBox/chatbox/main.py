"""
Project Name: Flask 框架下的多语种自动语音翻译（问答）系统后台
Author: 杨若瑶、许逸文
Structure:
1. 第一步 进入用户界面 （index()函数实现）
2. 第二步 接收前端wav语音、语言对、二进制音频/字符串、session_id存到本机，将二进制音频/字符串写入文件，并以session_id命名（recerive()函数实现）
3. 第三步 把路径传给“黑盒子系统”的语音识别模块（二进制音频情况下）/机器翻译（字符串情况下）的接口（recerive()函数实现）
4. 第四步 接收“黑盒子系统”语音合成模块生成的wav，存到本地（recerive()函数实现）
5. 第五步 对前端的定期监听做反馈，返回音频存储路径（listen()函数实现）（如果文件已经生成，则返回path=文件路径；如果文件还没生成，则返回path=''（空））

"""
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

from flask_restful import request

app = Flask(__name__)

'''
@app.route("/hello")
def hello():
    #return "Hello World!"
	return render_template('index.html',pp="world")
'''


#后台首页地址	
@app.route("/")
def index():
	return render_template('index.html',name="index")



@app.route("/receive_files", methods=['GET','POST'])
def receive():
##接收前端传来的session_id、语言对和二进制音频/字符串##
	#if request.method == 'POST':
	#	f = request.files['fileUpload']
	#	f.save('' + secure_filename(f.filename))
	# 前端url传过来session_id
	session_id = request.args.get("session_id")
	# 前端POST方法传过来session_id，二选一
	session_id = request.form['session_id']
	# 强制类型转换将int转换为str
	session_id = str(session_id)
	# 前端POST方法传过来用户角色
	role = request.form['role']
	# 接收前端返回的语言对
	in_lang = request.form['in_lang']
	out_lang = request.form['out_lang']
	# 前端返回的是音频还是字符串
	audio_or_str = request.form['audio_or_str']



##判断接收到的是二进制音频还是字符串：是audio返回True,是str返回False##
	if (audio_or_str == 'audio'):
		# 前端传来的是二进制音频，把它写入本地'./input/audio/'地址下，以session_id命名的wav文件，以区分不同回合的语音
		audio_file = request.form['data']
		path='static/input/audio/'+session_id+'.wav'
		f = open(path,'wb')
		f.write(audio_file)
		f.close()
		# 将本地音频路径、语言对传给“黑盒子系统”的语音识别模块的接口
		# 接收“黑盒子系统”语音合成模块生成的wav，存到本地'./output/audio/'地址下，以session_id命名
		return_path = start_from_speech_recognition(path,role,in_lang,out_lang)
		k = open(return_path,'rb')
		addr='static/output/audio/'+session_id+'.wav'
		g = open(addr,'wb')
		for line in k:
			g.write(line)
		k.close()
		g.close()


	else:
		#前端传来的是字符串
		text = request.form['data']
		#判断字符串是否为空，不为空才执行下方操作
		if text != "":
			# 把字符串写入本地'./input/text/'地址下，以session_id命名的txt文件，以区分不同回合的字符串
			path='static/input/text/'+session_id+'.txt'
			f = open(path,'w')
			f.write(text)
			f.close()
			# 将本地文本路径、语言对传给“黑盒子系统”的机器翻译模块的接口
			# 接收“黑盒子系统”语音合成模块生成的wav path，存到本地固定路径'./output/audio/'下，以session_id命名
			return_path = start_from_machine_translation(path,role,in_lang,out_lang)
			k = open(return_path,'rb')
			addr='static/output/audio/'+session_id+'.wav'
			g = open(addr,'wb')
			status = '2333'
			try:
				for line in k:
					g.write(line)
				status = '6666'
			except Exception as e:
				status = '2333'
			finally:
				k.close()
				g.close()
	addr='/static/output/audio/'+session_id+'.wav'
	return addr


# 假的语音识别->机器翻译->语音合成模块
def start_from_speech_recognition(path,role,in_lang,out_lang):
    return_path = "ch-short.wav"
    return return_path

# 假的机器翻译->语音合成模块
def start_from_machine_translation(path,role,in_lang,out_lang):
    return_path = "ch-short.wav"
    return return_path



'''
@app.route("/listen", methods=['GET'])
def listen():
##接收前端监听传来的session_id，根据session_id生成“待查找文件的路径”##
	session_id = request.args.get("session_id")
	# 强制类型转换将int转换为str
	session_id = str(session_id)
	path='static/output/audio/'+session_id+'.wav'
	# 通过查找本地是否存在该“待查找文件的路径”，判断“黑盒子系统”语音合成模块是否已生成目标文件，向前端返回状态码。
	# 已存在：返回path=文件路径，不存在（即还未生成）：返回path=''（空）
	if os.path.exists(path):
		path='/static/output/audio/'+session_id+'.wav'
	else:
		path = ''
	return path
'''



if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
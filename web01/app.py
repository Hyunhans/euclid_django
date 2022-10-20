from flask import Flask, render_template, request, redirect
import os


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/test/<username>')
def test(username):  #함수의 파라미터 값으로 route와 동일하게 적어주어야해
    print(username)
    return render_template('test_result.html', name=username)

@app.route('/methodin')
def methodin():
    return render_template('inputform.html')

@app.route('/methodout', methods=['GET', 'POST'])
def methodout():
    if request.method =='post':
        print('Post')
        data = request.form
    else:
        print('GET')
        data = request.args

    return render_template('method.html', data1=data, data2=request.method)

@app.route('/fileupload', methods=['GET', 'POST'])
def fileupload():
    if request.method == 'GET':
        return render_template('fileinput.html')
    else:
        f = request.files['formFile']
        path = os.path.dirname(__file__)+'\\upload\\'+f.filename  # __file__ : 실행하는 파일의 정보가 들어감(app.py의 dir 이름을 뽑아간다. )
        print(path)
        f.save(path)
        print('저장성공')
        return redirect('/')   # clients 쪽에서 아무런 request가 없이 다른 페이지로 보내주기 위해서는 redirect 를 사용해야한다. 

if __name__ == '__main__' :
    app.run(debug = True, port = 80)



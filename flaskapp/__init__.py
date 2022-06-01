from flask import Flask, Response, g, make_response, redirect, render_template, request

app = Flask(__name__)
#  debug 모드
app.debug=True



# route 요청을 응답하기전 처리 전역변수를 사용하는데 쓰인다.
@app.before_request
def before_request():
  print('--- 응답 전 처리 ---')
  g.siteName = 'lililli.kr'

@app.route('/')
def index():
  list = [('박민규', '주술사'), ('에크모', '도적')]
  return render_template('index.html', list=list)

# 동적 라우팅
@app.route('/read/<id>')
def read(id):
  print(id)
  return 'Read' + id

# get, post 처리
@app.route('/create', methods=['GET', 'POST'])
def create():
  if request.method == 'POST':
    title = request.form['title']
    body = request.form['body']
    # db 처리
    return redirect('/')


# api 라우팅
@app.route('/video')
def video():
  custom_res = Response("Custom Response", 201, {'title': 'avengers'})
  return make_response(custom_res) # 스트림으로 파일을 내려줌

# 리퀘스트 쿼리(url 파라미터) 얻기
@app.route('/rq')
def rq():
  q = request.args.get('keyword')
  return 'keyword: ' + q

# debug: 서버에 수정사항이 생길시 자동으로 재시작
app.run(port=5001)
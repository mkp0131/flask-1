# Flask 플라스크

## `__name__` 변수

- 해당파일(원본파일) 에서 함수를 실행시키면 '**main**' 이라는 값이 들어간다.
- 다른 파일에서 모듈로 import 해서 사용하면 해당파일의 이름이 들어간다. 'server'

## python import 비밀

- import 를 하게 되면 해당패키지의 `__init__.py` 를 실행한다.
- `from game.__init__ import *` 이런 구조인 것이다!

## url 에 포트 없애는 법

- `80` 포트는 기본포트로 `:80` 이라고 붙이지 않아도 된다.

## 파일구조

```
webapp/
  flaskapp/
    static/
      css/
      images/
      js/
    templates/
      about/
      index.html
    __init__.py
  start_flask.py
```

## 전역변수 사용법

```py
# route 요청을 응답하기전 처리 전역변수를 사용하는데 쓰인다.
@app.before_request
def before_request():
  print('--- 응답 전 처리 ---')
  g.siteName = 'lililli.kr'
```

- @app.before_first_request: 첫요청을 부를때 서버에 처음들어왔을때
- @app.before_request: 라우터가 실행하기 전에!
- @app.after_request: 응답이 나가기 직전에! 예) db.close
- @app.teardown_request: 응답이 나간후!
- @app.teardown_appcontext: 전역변수가 끝났을때, application context 가 끝났을때!

## 동적라이팅 리다이렉션 처리

- if. 동적라이팅에 값이 안들어왔을때 리다이렉션 처리

```py
@app.route('/test', default={'page': 'index'}) # <page> 값이 없을경우 index로 리다이렉션
@app.route('/test/<page>')
def test():
```

## 라이팅 리다이렉션 처리

```py
@app.route('/test', redirect_to='/new_test')
```

## 리퀘스트 쿼리(url 파라미터) 얻기

```py
@app.route('/rq')
def rq():
  q = request.args.get('keyword')
  return 'keyword: ' + q
```

- POST

```py
request.form.get('p', 123) # post 값에서 p 인값을 찾고 없으면 123
request.values.get('p') # post, get 모두 (php request 와 같음)
request.args.getlist('keyword') # keyword를 여러개 받을때, array 형태로 받아온다.
```

## 템플릿 엔진

- render_template('index.html', title='타이틀') 으로 템플릿 엔진 실행

### jinja 개행 없애기

- pythone 코드에 `-`(하이픈)을 붙여준다.

```html
<pre>
    ddd
    {%- if True -%}
    트루다
    {%- endif -%}qq
  </pre
>
```

### jinja 이스케이프

- 문자열처럼 `'` OR `"` 로 감싸준다.

```html
{{"안녕 {민규} 님"}}
```

- 개발 코드 등을 표현할때 {% raw %} 를 활용한다.

- 변수로 html 코드가 온 경우 {{title | safe}} 를 사용

- 혹은 변수를 전달할때 markup(변수)로 감싸준다.

### jinja for문 사용

```html
<ul>
  {% for name, job in list %}
  <li>{{loop.index}}. {{name}} - {{job}}</li>
  {% else %}
  <li>자료가 없습니다.</li>
  {% endfor %}
</ul>
```

- loop.index: 1부터 시작
- loop.index0: 0부터 시작
- loop.revindex: 뒤부터 시작
- loop.first: 첫번째 아이템일 경우 True
- loop.last: 마지막 아이템일 경우 True
- loop.length
- loop.depth
- loop.cicle('aaa', 'bbb'): 첫번째 'aaa', 두번째 'bbb' 순서대로 순회함

### jinja 파일 path / css, js 링크

- url_for() 를 사용

```html
<link rel="stylesheet" href="{{url_for('static', filename='css/style.css')}}" />
```

### jinja block 에서 layout에 입력되어 있는 텍스트를 출력할때

- super() 를 사용한다.

```
{% block section %}
{{super()}}
안녕하세요. 인덱스 입니다.
{% endblock %}
```

### jinja scoped / block 을 반복시키기

- block 을 반복해서 선언하는 것은 불가능!
- 디버그 용도로만 사용

```html
{% for item in [1,2,3] %} {% block list scoped %}
<div>ddd: {{item}}</div>
{% endblock list %} {% endfor %}
```

### jinja 매크로 사용법 / macro

- laout.html 에 macro 를 선언하여 자주 사용하는 html 을 동적으로 생성 할 수 있다.

```html
{% macro test_macro(title) -%}
<h2>{{title}}</h2>
{%- endmacro %}
```

- index.html 에서는 block 안에 macro 를 실행한다.

```html
{% block section %} {{ test_macro('민규') }} {% endblock %}
```

- callable macro: 변수뿐만 아니라 child 에 html 을 받을수도있다(block 처럼 사용하는 법)

```html
<!-- layout.html -->
{% macro test_macro(title) -%}
<h2>{{title}}</h2>
<div>{{caller()}}</div>
{%- endmacro %}

<!-- index.html -->
{% call test_macro('민규') %}
<p>Hello!</p>
{% endcall %}
```

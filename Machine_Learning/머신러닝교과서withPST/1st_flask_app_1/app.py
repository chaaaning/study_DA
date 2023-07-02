from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('first_app.html')

if __name__=='__main__':
    app.run()
    
"""

1. 애플리케이션은 하나의 모듈로 실행됨
    - 매개변수 __name__으로 새로운 플라스크 인스턴스를 초기화
    - 이렇게 하면 플라스크는 현재 디렉터리와 같은 위치에서 HTML 템플릿 폴더 templates를 찾음
    - __name__은 파이썬의 특수한 변수로 모듈 이름이 담김
    - 파이썬 모듈을 스크립트로 실행하면 __name__의 값은 '__main__'이 됨
    - 플라스크는 모듈 이름이 '__main__'일 경우 현재 위치에서 템플릿 폴더를 찾음
    
2. 그 다음 라우트 데코레이터(@app.route('/'))를 사용하여 특정 URL이 index 함수를 실행하도록 지정

3. 여기서 index 함수는 단순히 templates 폴더 아래에 있는 first_app.html HTML 파일을 화면에 출력

4. 마지막으로 이 스크립트가 파이썬 인터프리터에 의해 직접 실행될 때만 run 메서드를 사용하여 어플리케이션을 시작
    - 이를 위해 if __name__='__main__' 구문을 사용
    
"""
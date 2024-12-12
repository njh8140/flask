from flask import Flask
# app 객체를 전체 전역으로 사용
# 프로젝트 규모가 커질 수록 문제가 발생
# 문제 : 순환 참조 오류

# 방지하기 위한 방법 : 애플리케이션 팩토리
# app = Flask(__name__)


# 애플리케이션 팩토리 완성
# create_app() 함수 안에
# app이라는 Flask 인스턴스를 생성해서 작동
def create_app():
    app = Flask(__name__)

    # '/' 주소가 호출이 되면
    # 밑에 있는 hello_pybo가 실행
    # @app.route와 같은 애너테이션으로 url을 매핑하는 함수를 라우팅 함수
    @app.route('/')
    # hello_pybo()는 라우팅 함수
    def hello_pybo():
        return 'Hello, Pybo!'
    
    # 만약 새로운 url 매핑이 필요하면 라우팅 함수를
    # create_app 함수 안에 계속 추가해야 함.
    # 그럴 경우 create_app 함수는 크고 복잡한 함수가 됨
    # 이를 위해 블루프린트를 사용해서 관리
    
    return app
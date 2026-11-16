from flask import Flask, request


def create_app():
    app = Flask(__name__)
    
    @app.get("/api/basics")
    def get_basics():
        return ({"message": "MeowMeow"},201)
    
    @app.get("/api/params1/<int:fruit_id>")
    def test_id(fruit_id):
        return ({"message": "TESTING!!!!", "restricted_mode": fruit_id}, 201)    

    @app.get("/api/params2/<str_id>")
    def test2_id(str_id):
        return ({"message": "TESTING!!!!", "unrestricted_mode": str_id}, 201)
    
    @app.get("/")
    def get_root():
        return ({"message": "Hello from my-ajax-api!"}, 201)

    #查詢字串參數
    @app.get("/api/q1")
    def my_q1():
        id = request.args.get("id", 1, type=int)
        return {"id": id}
    return app

def main() -> None:
    print("Hello from my-ajax-api!")

from flask import Flask

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
    
    return app

def main() -> None:
    print("Hello from my-ajax-api!")

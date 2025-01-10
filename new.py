from flask import Flask, redirect, render_template, url_for, request




# import yfinance as yf
import requests
myToken1 = 'xoxb-8253119763543-8261667911078-yraxeRyPyAGWTVzlJuNVr8ho'
iss=0
def post_message(token, channel, text):
        response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    # print(response)
    
    
myToken = "xoxp-8253119763543-8267564139155-8270790338500-1b68812eb024bccde71be48561404053"
messages = "서버가 초기화 되었습니다"
post_message(myToken,"#chiho",messages)


app = Flask(__name__)



# 루트로 가면 저home()함수를 실행한다. 
# 항상 서버를 시작하고 서버가 동작하면 사용가능하다
# 127.0.0.1:5000 포트
@app.route('/')
def home():
    
    global iss 
    iss+=1
    
    messages = "서버작동동 후 " + str(iss) + " 명이 Home Page 방문왔습니다."
    post_message(myToken,"#chiho",messages)
    
    return render_template("index.html")


@app.route("/index", methods=["POST","GET"])
def login():
     if request.method == "POST":
            user=request.form['name']
            post_message(myToken,"#chiho",user)
            phone=request.form['phone']
            post_message(myToken1,"#chiho",phone)
            email=request.form['email']
            post_message(myToken1,"#chiho",email)
            contend=request.form['contend']
            post_message(myToken1,"#chiho",contend)
            return render_template("goodbye.html", content=[user,phone,email,contend])
     
     else:
        return render_template("index.html")


@app.route("/<usr>")
def user(usr):
     messages=usr
     post_message(myToken1,"#chiho",messages)
     return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0',debug=True, port='5000')





    
   
    


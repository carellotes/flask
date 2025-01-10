from flask import Flask, redirect, render_template, url_for, request


iss=0
import requests
url2="T087F3HNFFZ/B0885J6C2QJ/4IRFBtdvqmCpDoAoCktc6qI1"
url = "https://hooks.slack.com/services/"
web_hook_url = url+url2

text = "안녕하세요! 오늘의 날씨는 '맑음'입니다."

payload = {"text" : text}

requests.post(web_hook_url, json=payload)

# def sendMessage(data):
#     try:
        
#         header = {'Content-type': 'application/json'}
#         data=data
#         return requests.post(url, headers=header, json=data)
        
#     except Exception as e:
#         exit(0)
#     # print(response)
    
    

# messages = "서버가 초기화 되었습니다"
# sendMessage(messages)


app = Flask(__name__)



# 루트로 가면 저home()함수를 실행한다. 
# 항상 서버를 시작하고 서버가 동작하면 사용가능하다
# 127.0.0.1:5000 포트


@app.route('/')
def home():
    global iss 
    iss+=1
    messages = "서버작동동 후 " + str(iss) + " 명이 Home Page 방문왔습니다."
    payload = {"text" : messages}
    requests.post(web_hook_url, json=payload)
    return render_template("/index.html")

# @app.route('/templates')
# def hsome():
#     global iss 
#     iss+=1
#     messages = "서버작동동 후 " + str(iss) + " 명이 Home Page 방문왔습니다."
#     # post_message(myToken1,"#chiho",messages)
#     return render_template("/index.html")


@app.route("/templates", methods=["POST","GET"])
def login():
     if request.method == "POST":
            
            user=request.form['name']
            
            phone=request.form['phone']
            
            email=request.form['email']
            
            contend=request.form['contend']
            
            data=[user,phone,email,contend]
            payload ={"text" : data}
            requests.post(web_hook_url, json=payload)
            return render_template("./goodbye.html", content=[user,phone,email,contend])
     
     else:
        return render_template("/templates/index.html")


@app.route("/<usr>")
def user(usr):
    messages=usr
    payload = {"text" : messages}
    requests.post(web_hook_url, json=payload)
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0',debug=True, port='5000')





    
   
    


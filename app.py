from flask import Flask, redirect, render_template, url_for, request


iss=0
# import requests
url2='B0885J6C2QJ/4IRFBtdvqmCpDoAoCktc6qI1'
url1 = "https://hooks.slack.com/services/T087F3HNFFZ/"
url=url1+url2
web_hook_url = url

text = "안녕하세요! 아직쫒겨나진 않음'입니다.ㄴㄴㅇㅇㅇㅇㄴㄴ"

payload = {"text" : text}

# requests.post(web_hook_url, json=payload)



app = Flask(__name__)




@app.route('/')
def home():
    global iss 
    iss+=1
    messages = "서버작동동 후 " + str(iss) + " 명이 Home Page 방문왔습니다."
    payload = {"text" : messages}
    # requests.post(web_hook_url, json=payload)
    return render_template("/index.html")



@app.route("/templates", methods=["POST","GET"])
def login():
     if request.method == "POST":
            user=request.form['name']
            phone=request.form['phone']
            email=request.form['email']
            contend=request.form['contend']
            
            data={'text':user}
            payload = data 
            # requests.post(web_hook_url, json=payload)
            data={'text':phone}
            payload = data 
            # requests.post(web_hook_url, json=payload)
            data={'text':email}
            payload = data 
            # requests.post(web_hook_url, json=payload)
            data={'text':contend}
            payload = data 
            # requests.post(web_hook_url, json=payload)




            return render_template("./goodbye.html", content=[user,phone,email,contend])
     else:
        return render_template("/templates/index.html")


@app.route("/<usr>")
def user(usr):
    messages=usr
    payload = {"text" : messages}
    # requests.post(web_hook_url, json=payload)
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0',debug=True, port='5000')





    
   
    


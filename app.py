from flask import Flask, render_template, make_response, request
import chatbot
import config

CHAT_HISTROY=[]
app = Flask(__name__)
@app.route('/', methods = ['POST', 'GET'])

def data():
    if request.method == 'GET':
        headers = {"Content-Type": "text/html"}
        result = make_response(render_template(config.website_template), 200, headers)
        return result
    if request.method == 'POST':
        headers = {"Content-Type": "text/html"}
        if len(request.form["user_input"])>0:
            user_input = str(request.form["user_input"])
            CHAT_HISTROY.append("User: "+ user_input+"\n")
            CHAT_HISTROY.append("AI: "+ chatbot.response(user_input)+"\n")
        else: 
            CHAT_HISTROY.append(chatbot.translate(config.empty_input_prompt, config.target_language))
        result = make_response(render_template(config.website_template, chat=CHAT_HISTROY), 200, headers)
        return result
        
if __name__=="__main__":
    app.run(debug=True)
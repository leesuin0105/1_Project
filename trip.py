from flask import Flask, request, render_template, send_file
import openai
import os
import pandas as pd
import html


openai.api_key = ''  # ' 'api_key 입력

app = Flask(__name__) # Flask 애플리케이션 객체 생성

dialogs = ""
messages = [] 

# 1. 홈 페이지 (index.html) 렌더링
@app.route('/')
def index():
    return render_template('index.html')

# 2. 여행 계획 생성 요청 처리
@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    num_days = int(request.form['num_days'])
    place = request.form['place']

    plan = []

    messages = []
    messages.append({"role": "system", "content": "사용자에게 여행 일 수와 여행 장소를 입력받아 위도와 경도를 포함한 여행 계획을 html로 생성해줘"})
    messages.append({"role": "user", "content": f"여행 일 수: {num_days}"})
    messages.append({"role": "user", "content": f"여행 장소: {place}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    response = completion.choices[0].message['content']
    plan.append([f"Day {num_days}", response])
    messages.append({"role": "assistant", "content": response})

    return render_template('result.html', plan=plan)

# 3. Flask 서버 실행 (디버그 모드 활성화)
if __name__ == '__main__':
    app.run(debug=True)

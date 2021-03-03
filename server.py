#flask_api.py
from transformers import pipeline
from flask import Flask, request, render_template,jsonify
import os

qa_pipeline = pipeline(
    "question-answering",
    model="mrm8488/bert-tiny-5-finetuned-squadv2",
    tokenizer="mrm8488/bert-tiny-5-finetuned-squadv2"
)

app = Flask(__name__,static_folder="templates")
def get_answer(content,question):
   answer=[]
   for i in content:
        result=qa_pipeline({'context': i,'question': question })
        answer.append(result["answer"])
        answer.append("\n")
   return answer

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text = request.form['text1']
    word = request.args.get('text1')
    content=["சென்னை எக்ஸ்பிரஸ் மாலை 5 மணிக்கு சென்னையிலிருந்து கோயம்புத்தூர் சென்றடையும்","ஏபிசி எக்ஸ்பிரஸ் ஹைதராபாத்தில் இருந்து அதிகாலை 5 மணிக்கு தொடங்கி மாலை 5 மணிக்கு சென்னை அடையும்"]
    answer = get_answer(content,text)
    print(answer)
    result = {"output": answer}         
    #result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':  
    app.run(debug=True)
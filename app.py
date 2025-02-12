from flask import Flask, request,session, jsonify, render_template
import requests 
import os      
import google.generativeai as genai
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/category')
def category():
    return render_template('category.html')
@app.route('/search')
def search():
    return render_template('search.html')
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')
@app.route('/fill form')
def fill():
    return render_template('fill form.html')
@app.route('/forms')
def form():
    return render_template('forms.html')
@app.route('/loho')
def loho():
    return render_template('loho.html')
@app.route('/DEVICE')
def DEVICE():
    return render_template('DEVICE.html')
@app.route('/feature')
def feature():
    return render_template('feature.html')
@app.route('/over')
def over():
    return render_template('over.html')
@app.route('/family')
def family():
    return render_template('family.html')
@app.route('/HERBAL')
def HERBAL():
    return render_template('HERBAL.html')
@app.route('/house')
def house():
    return render_template('house.html')
@app.route('/BEAUTY')
def BEAUTY():
    return render_template('BEAUTY.html')
@app.route('/e')
def e():
    return render_template('e.html')
@app.route('/s')
def s():
    return render_template('s.html')
@app.route('/p')
def p():
    return render_template('p.html')
@app.route('/profile')
def profile():
    return render_template('profile.html')
@app.route('/medicine3')
def madicine3():
    return render_template('medicine3.html')
@app.route('/medicine4')
def madicine4():
    return render_template('medicine4.html')
@app.route('/medicine5')
def madicine5():
    return render_template('medicine5.html')
@app.route('/medicine6')
def madicine6():
    return render_template('medicine6.html')
@app.route('/realfeature')
def realfeature():
    return render_template('realfeature.html')
@app.route('/realcounter')
def realcounter():
    return render_template('realcounter.html')
@app.route('/realfamily')
def realfamily():
    return render_template('realfamily.html')
@app.route('/realherbal')
def realherbal():
    return render_template('realherbal.html')
@app.route('/realhouse')
def realhouse():
    return render_template('realhouse.html')
@app.route('/realbeauty')
def realbeauty():
    return render_template('realbeauty.html')
@app.route('/realdevice')
def realdevice():
    return render_template('realdevice.html')
@app.route('/realcategory')
def realcategory():
    return render_template('realcategory.html')
@app.route('/inde')
def inde():
    return render_template('inde.html')
GEMINI_API_URL = ""
API_KEY = "AIzaSyCZsPpcwGXJohwFG70QlmPXALnqSgcoeJQ"
@app.route('/', methods=['GET'])
def home():
    return render_template('search.html')
@app.route('/ask', methods=['POST'])
def ask_gemini():
    prompt = request.form['query']
    genai.configure(api_key="AIzaSyCZsPpcwGXJohwFG70QlmPXALnqSgcoeJQ")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    aiResponse = response.text
    return jsonify({'response': aiResponse})
if __name__ == '__main__':
    app.run(debug=True)

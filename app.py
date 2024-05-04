from flask import Flask, render_template, request
from flask import jsonify

app = Flask(__name__)

# Global list to store scores
scores = []

@app.route('/')
def home():
    return render_template('index9.html') 

@app.route('/irs', methods=['GET', 'POST'])
def index():

    return render_template('irs.html')

@app.route('/m2', methods=['GET', 'POST'])
def index2():
    score = request.form.get('verificationScore', type=int)
    scores.clear()
    scores.append(score)
    print("Updated scores list:", scores)
    # Optionally handle something with scores here
    return render_template('m2.html')

@app.route('/m3', methods=['GET', 'POST'])
def index3():
    score = request.form.get('verificationScore', type=int)
    
    scores.append(score)
    print("Updated scores list:", scores)
    # Optionally handle something with scores here
    return render_template('m3.html')

@app.route('/m4', methods=['GET', 'POST'])
def index4():
    score = request.form.get('verificationScore', type=int)
    
    scores.append(score)
    print("Updated scores list:", scores)
    # Optionally handle something with scores here
    return render_template('m4.html')

scores2 = [1,1,1,1,1]
@app.route('/m5', methods=['GET', 'POST'])
def index5():
    if request.method == 'POST':
        score = request.form.get('verificationScore', type=int)
        if score is not None:  # Check if score is not None before appending
            scores.append(score)
            print("Updated scores list:", scores2)
        else:
            print("No score provided in POST request.")
    else:
        print("GET request received, displaying page without updating scores.")
    # Pass the updated or existing scores list to the template
    return render_template('m5.html', score3=scores)


if __name__ == '__main__':
    app.run()
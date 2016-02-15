from flask import Flask,render_template
import os
app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

@app.route('/',methods=['GET','POST'])
def hello_stock():
	# return "ok"
	return render_template('Main.html')
@app.route('/Stock_Open_Price',methods=['POST'])
def Stock_Open_Price():
	return render_template('Stock_Open_Price.html')

@app.route('/ROI',methods=['POST'])	
def ROI():
	return render_template('ROI.html')

@app.route('/More_Analysis_1',methods=['POST'])	
def More_Analysis_1():
	return render_template('More_Analysis_1.html')

@app.route('/More_Analysis_2',methods=['POST'])	
def More_Analysis_2():
	return render_template('More_Analysis_2.html')

@app.route('/More_Analysis_3',methods=['POST'])	
def More_Analysis_3():
	return render_template('More_Analysis_3.html')

@app.route('/More_Analysis_4',methods=['POST'])	
def More_Analysis_4():
	return render_template('More_Analysis_4.html')




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

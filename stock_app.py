from flask import Flask,render_template
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

@app.route('/')
def hello_stock():
	return "ok"
# 	return render_template('Main.html')
# @app_stock.route('/Stock_Open_Price',methods=['POST'])
# def Stock_Open_Price():
# 	return render_template('Stock_Open_Price.html')

# @app_stock.route('/ROI',methods=['POST'])	
# def ROI():
# 	return render_template('ROI.html')	

if __name__ == "__main__":
    app.run()

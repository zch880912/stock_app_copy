from flask import Flask,render_template
app_stock = Flask(__name__)

@app_stock.route('/')
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
    app_stock.run()

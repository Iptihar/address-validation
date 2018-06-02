from flask import Flask, flash
from flask import request
from flask import render_template
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

def runTest():
	testURL = 'http://trial.serviceobjects.com/AV3/api.svc/GetBestMatchesJson?'
	#first test case with wrong streen address number, should return Error
	test1 = {'BusinessName': 'mBusinessName', 'Address': '44.05 McKinley St.', 'Address2': ' ', 'City': 'houston', 'State': 'Texas', 'PostalCode': '77023', 'LicenseKey': 'WS72-GRC5-OJT1'}
	test1result = requests.get(testURL, params=test1)
	test1outputs = test1result.json()
	if 'Error' in test1outputs.keys():
		return True
	#second test case with non existing address, should return Error too
	test2 = {'BusinessName': 'mBusinessName', 'Address': '4405 McKinney St.', 'Address2': ' ', 'City': 'Austin', 'State': 'Montana', 'PostalCode': '59102', 'LicenseKey': 'WS72-GRC5-OJT1'}
	test2result = requests.get(testURL, params=test2)
	test2outputs = test2result.json()
	if 'Error' in test2outputs.keys():
		return True
	#third test case with wrong Zip code, should auto correct it and find match
	test3 = {'BusinessName': 'mBusinessName', 'Address': '4405 McKinney St.', 'Address2': ' ', 'City': 'houston', 'State': 'Texas', 'PostalCode': '770.23', 'LicenseKey': 'WS72-GRC5-OJT1'}
	test3result = requests.get(testURL, params=test3)
	test3outputs = test3result.json()
	if 'Error' not in test3outputs.keys():
		return True
	#fourth test case with wrong city name, should auto correct it and find match
	test4 = {'BusinessName': 'mBusinessName', 'Address': '4405 McKinney St.', 'Address2': ' ', 'City': 'HTX', 'State': 'Texas', 'PostalCode': '77023', 'LicenseKey': 'WS72-GRC5-OJT1'}
	test4result = requests.get(testURL, params=test4)
	test4outputs = test4result.json()
	if 'Error' not in test4outputs.keys():
		return True

	return False


@app.route("/", methods=['GET', 'POST'])
def my_form_post():
	if request.method == 'POST':
	    mAddress = request.form['lu_address1']
	    if mAddress is None or mAddress == "":
	        mAddress = " "
	    mAddress2 = request.form['lu_address2']
	    if mAddress2 is None or mAddress2 == "":
	        mAddress2 = " "
	    mCity = request.form['lu_city']
	    if mCity is None or mCity == "":
	        mCity = " "
	    mState = request.form['lu_state']
	    if mState is None or mState == "":
	        mState = " "
	    mPostalCode = request.form['lu_postal_code']
	    if mPostalCode is None or mPostalCode == "":
	        mPostalCode = " "
	    mLicenseKey = "WS72-GRC5-OJT1"

	    primaryURL = 'http://trial.serviceobjects.com/AV3/api.svc/GetBestMatchesJson?'

	    inputs = {'BusinessName': 'mBusinessName', 'Address': mAddress, 'Address2': mAddress2, 'City':mCity, 'State':mState, 'PostalCode': mPostalCode, 'LicenseKey': mLicenseKey}

	    try:
	        result = requests.get(primaryURL, params=inputs)
	        outputs = result.json()

	        if 'Error' in outputs.keys():
	        	flash('Error: ' + str(outputs['Error']['Desc']))

	        else:
	                for i in range(0, len(outputs['Addresses'])):
	                    flash("Address Match #"+str(i+1))
	                    flash('Address1: ' + str(outputs['Addresses'][i]['Address1']))
	                    flash('Address2: ' + str(outputs['Addresses'][i]['Address2']))
	                    flash('City: ' + str(outputs['Addresses'][i]['City']))
	                    flash('State: ' + str(outputs['Addresses'][i]['State']))
	                    flash('ZipCode: ' + str(outputs['Addresses'][i]['Zip']))
	    except:
	        flash("Connection Error. Please check your network.")
	
	return render_template("project.html")

if __name__ == '__main__':
	if(runTest()):
		print ("All tests successful.")
		app.run()
	else:
		print ("Some tests failed.")

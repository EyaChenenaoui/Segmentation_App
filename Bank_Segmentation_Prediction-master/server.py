import model # Import the python file containing the ML model
from flask import Flask, request, render_template,jsonify # Import flask libraries
import sklearn
# Initialize the flask class and specify the templates directory
app = Flask(__name__,template_folder="templates")

# Default route set as 'home'
@app.route('/home')
def home():
    return render_template('home.html') # Render home.html

# Route 'classify' accepts GET request
@app.route('/classify',methods=['POST','GET'])
def classify_type():
    try:
        CATEG_INTERNE = request.args.get('CLT_CATEG_INTERNE') # Get parameters for sepal length
        INTITULE = request.args.get('CLT_INTITULE') # Get parameters for sepal width
        GESTIONNAIRE = request.args.get('CLT_GESTIONNAIRE') # Get parameters for petal length
        VILLE_NAISSANCE = request.args.get('CLT_VILLE_NAISSANCE') # Get parameters for petal width
        CLT_CODE = request.args.get('CLT_CODE') # Get parameters for petal width
        CHAMP_LIBRE_1 = request.args.get('CLT_CHAMP_LIBRE_1') # Get parameters for petal width
        AGE = request.args.get('AGE') # Get parameters for petal width
        SECTEUR_ACTIVITE = request.args.get('CLT_SECTEUR_ACTIVITE') # Get parameters for petal width
        TYPE_P_IDENT = request.args.get('CLT_TYPE_P_IDENT') # Get parameters for petal width


        # Get the output from the classification model
        variety = model.classify(CATEG_INTERNE,INTITULE,GESTIONNAIRE,CLT_CODE,AGE,CHAMP_LIBRE_1,
        SECTEUR_ACTIVITE,VILLE_NAISSANCE,TYPE_P_IDENT)
        variety_Num = model.classifyNum(CATEG_INTERNE,INTITULE,GESTIONNAIRE,CLT_CODE,AGE,CHAMP_LIBRE_1,
        SECTEUR_ACTIVITE,VILLE_NAISSANCE,TYPE_P_IDENT)
            
        # Render the output in new HTML page
        return render_template('output.html', variety=variety,variety_Num = variety_Num)
    except:
        return 'Error'

# Run the Flask server
if(__name__=='__main__'):
    app.run(debug=True)        
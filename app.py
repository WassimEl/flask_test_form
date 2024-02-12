import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nom = request.form['nom']
    data_nom = {'nom': nom}

    prenom = request.form['prenom']
    data_prenom = {'prenom': prenom}

    naissance = request.form['naissance']
    data_naissance = {'naissance': naissance}

    ecole = request.form['ecole']
    data_ecole = {'ecole': ecole}

    ville = request.form['ville']
    data_ville = {'ville': ville}

    annee = request.form['annee']
    data_annee = {'annee': annee}

    classe = request.form['classe']
    data_classe = {'classe': classe}

    option = request.form['option']
    data_option = {'option': option}


    with open('data.json', 'w') as outfile:
        json.dump(data_nom, outfile)
        outfile.write('\n')
        json.dump(data_prenom, outfile)
        outfile.write('\n')
        json.dump(data_naissance, outfile)
        outfile.write('\n')
        json.dump(data_ecole, outfile)
        outfile.write('\n')
        json.dump(data_ville, outfile)
        outfile.write('\n')
        json.dump(data_annee, outfile)
        outfile.write('\n')
        json.dump(data_classe, outfile)
        outfile.write('\n')
        json.dump(data_option, outfile)
        outfile.write('\n')
        
    return render_template('result.html', nom=nom, prenom=prenom, naissance=naissance, ecole=ecole, ville=ville, annee=annee, classe=classe, option=option)

if __name__ == '__main__':
    app.run(debug=True)
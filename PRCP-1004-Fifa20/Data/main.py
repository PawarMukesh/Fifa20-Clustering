from flask import Flask,render_template,request
import jsonify
import pickle # help to load the data
import numpy as np
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)  # Creating app

model = pickle.load(open("kmeans_clustering_model.pkl" , "rb"))


@app.route('/',methods=['GET']) #if someone hitting the webside that time method will be get
def home():
    return render_template('index.html') #Pushing the ui and html code


# Start preprocessing

min_max = MinMaxScaler()
@app.route('/predict',methods=['POST']) #Collect the inputs
def predict():
    if request.method == 'POST':
        age = float(request.form['age'])
        height_cm = float(request.form['height_cm'])
        weight_kg = float(request.form['weight_kg'])
        overall = float(request.form['overall'])
        potential = float(request.form['potential'])
        value_eur = float(request.form['value_eur'])
        wage_eur = float(request.form['wage_eur'])
        preferred_foot =request.form['preferred_foot_Right']
        if (preferred_foot == 'Right'):
            preferred_foot_Right = 1
            preferred_foot_Left = 0
        else:
            preferred_foot_Right = 0
            preferred_foot_Left = 1

        international_reputation = int(request.form['international_reputation'])
        weak_foot = int(request.form['weak_foot'])
        skill_moves = int(request.form['skill_moves'])
        team_position =request.form['team_position_SUB']
        if (team_position == 28 ):
            SUB = 28
            RES = 27
            GK = 26
            RCB = 25
            LCB = 24
            RB = 23
            LB = 22
            ST = 21
            RCM = 20
            LCM = 19
            RM = 18
            LM = 17
            CAM = 16
            RDM = 15
            LDM = 14
            RS = 13
            LS= 12
            CDM = 11
            LW = 10
            RW = 9
            CB = 8
            CM = 7
            RWB = 6
            LWB = 5
            RAM = 4
            LAM = 3
            RF = 2
            LF = 1
            CF = 0
        else:
            SUB = 0
            RES = 1
            GK = 2
            RCB = 3
            LCB = 4
            RB = 5
            LB = 6
            ST = 7
            RCM = 8
            LCM = 9
            RM = 10
            LM = 11
            CAM = 12
            RDM = 13
            LDM = 15
            RS = 14
            LS = 16
            CDM = 17
            LW = 18
            RW = 19
            CB = 20
            CM = 21
            RWB = 22
            LWB = 23
            RAM = 24
            LAM = 25
            RF = 26
            LF = 27
            CF = 28

        pace = float(request.form['pace'])
        shooting = float(request.form['shooting'])
        passing = float(request.form['passing'])
        dribbling = float(request.form['dribbling'])
        defending = float(request.form['defending'])
        physic = float(request.form['physic'])
        attacking_crossing = float(request.form['attacking_crossing'])
        attacking_finishing = float(request.form['attacking_finishing'])
        attacking_heading_accuracy = float(request.form['attacking_heading_accuracy'])
        attacking_volleys = float(request.form['attacking_volleys'])
        skill_dribbling = float(request.form['skill_dribbling'])
        skill_curve= float(request.form['skill_curve'])
        skill_fk_accuracy = float(request.form['skill_fk_accuracy'])
        skill_long_passing = float(request.form['skill_long_passing'])
        movement_acceleration = float(request.form['movement_acceleration'])
        movement_agility = float(request.form['movement_agility'])
        movement_reactions = float(request.form['movement_reactions'])
        movement_balance = float(request.form['movement_balance'])
        power_shot_power = float(request.form['power_shot_power'])
        power_jumping = float(request.form['power_jumping'])
        power_stamina = float(request.form['power_stamina'])
        power_strength = float(request.form['power_strength'])
        power_long_shots = float(request.form['power_long_shots'])
        mentality_aggression = float(request.form['mentality_aggression'])
        mentality_vision = float(request.form['mentality_vision'])
        mentality_penalties = float(request.form['mentality_penalties'])
        mentality_composure = float(request.form['mentality_composure'])
        defending_sliding_tackle = float(request.form['defending_sliding_tackle'])
        goalkeeping_kicking = float(request.form['goalkeeping_kicking'])

        prediction = model.predict(np.array([age,height_cm,weight_kg,overall,potential,value_eur,
                                             wage_eur,preferred_foot,international_reputation,weak_foot,
                                             skill_moves,team_position,pace,shooting,passing,dribbling,
                                             defending,physic,attacking_crossing,attacking_finishing,
                                             attacking_heading_accuracy,attacking_volleys,skill_dribbling,
                                             skill_curve,skill_fk_accuracy,skill_long_passing,movement_acceleration,
                                             movement_agility,movement_reactions,movement_balance,power_shot_power,
                                             power_jumping,power_stamina,power_strength,
                                             power_long_shots,mentality_aggression,mentality_vision,
                                             mentality_penalties,mentality_composure,defending_sliding_tackle,goalkeeping_kicking]))
        output = round(prediction[0], 2)
        if output == 3:  # Condition for output
            return render_template('index.html',pred="The Player Has been 3RD Group ")  # Connect ot html page and app
        elif output == 2:
            return render_template('index.html',pred="The Player Has been 2RD Group ")
        else:
            pred = "The Player Has Been 1ST Group  ".format(output)
            return render_template('index.html', pred=pred)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)



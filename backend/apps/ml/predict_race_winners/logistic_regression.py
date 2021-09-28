import joblib
import numpy as np
import pandas as pd


class LinearRegression:
    pass


class LogisticRegression:
    def __init__(self):
        path_to_artifacts = '..\\..\\predict_race_winners\\'
        self.values_fill_missing = joblib.load(path_to_artifacts + 'train_mean.joblib')
        self.scaler = joblib.load(path_to_artifacts + 'min_max_scaler.joblib')
        self.model = joblib.load(path_to_artifacts + 'log_reg.joblib')


    def preprocessing(self, input_data):
        # JSON to pandas DataFrame
        input_data = pd.DataFrame(input_data)
        # Fill missing values
        input_data.fillna(self.values_fill_missing)
        # Update daysSinceLasyRace ## 
        input_data['daysSinceLastRace'] = np.where((input_data['daysSinceLastRace'] == 0) & (input_data['nPastRaces'] == 0), input_data['ageInDays'], input_data['daysSinceLastRace'])
        # Normalize variables ##
        columns_normalize = ['weight', 'ageInDays', 'daysSinceLastRace', 'nPastRaces']
        input_data[columns_normalize] = self.scaler.transform(input_data[columns_normalize])
        return input_data


    def predict(self, input_data):
        return self.model.predict_proba(input_data)


    def postprocessing(self, input_data, prediction):
        # Join data with raceID ##
        join_data = pd.DataFrame({'raceID': input_data['raceID'],
                                  'horseID': input_data['horseID'],
                                  'win_loss': prediction
                                })
        # For each raceID, set the maximum probability to 1 and the remaining values to 0 ##
        join_data['win_loss'] = (join_data['win_loss'] == join_data['win_loss'].groupby(join_data['raceID']).transform('max')).astype(int)
        # Winners data frame ##
        winners = join_data.iloc[np.where(join_data['win_loss'] == 1)[0]][['raceID', 'horseID']]
        # Winners dictionary
        winners = winners.to_dict('records')[0]
        winners['status'] = 'OK'
        return winners


    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            columns_predict = ['weight', 'ageInDays', 'daysSinceLastRace', 'nPastRaces'] ##
            prediction = self.predict(input_data[columns_predict])[:,-1:].reshape(1, -1)[0] ##
            prediction = self.postprocessing(input_data, prediction)
        except Exception as e:
            return {'status': 'Error', 'message':str(e)}
        return prediction


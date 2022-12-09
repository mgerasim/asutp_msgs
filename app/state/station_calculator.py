from app.models.data import Data
import pandas as pd
from numpy import sqrt


def ratio_count(data, severity_name):
    data[f'ratio_count_{severity_name}'] = data[f'count_{severity_name}'] / data['count_total']


# Функция расчёта модели показателя нештатной работоспособности станции
def state(data):
    # Коэффициент выравнивающий масштаб аварийных и предупредительных сообщений
    A = 4
    data['state'] = sqrt((A*data['ratio_count_severity_critical'])**2 + (A*A*data['ratio_count_severity_warning'])**2)


class StationCalculator:
    @staticmethod
    def calculate(station_title):
#        print(f'station calculate: {station_title}')
        data = Data.select().where(Data.nps == station_title)
        if len(data) == 0:
            return -1
        df = pd.DataFrame(data.dicts())
        df.index = df['id']
        df.pop('id')

        ratio_count(df, 'severity_info')
        ratio_count(df, 'severity_warning')
        ratio_count(df, 'severity_critical')

        state(df)

        df['state_normalized'] = (df['state'] - df['state'].min()) / (df['state'].max() - df['state'].min())

        state_value = df.iloc[-1:]['state_normalized']
        return state_value

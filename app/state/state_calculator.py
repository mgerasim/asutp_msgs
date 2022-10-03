from app.models.station import Station
from app.state.station_calculator import StationCalculator


class StateCalculator:
    @staticmethod
    def calculate():
        stations = Station.select()
        for row in stations:
            state = StationCalculator.calculate(row.title)
            print(state)
            row.state = state
            row.save()

from app.models.station import Station


class SaveNpsHelper:
    @staticmethod
    def save(title):
        station = Station.get_or_create(title=title)

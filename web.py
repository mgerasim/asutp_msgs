

from flask import Flask

from app.models.station import Station
from app.core.models.base_model import conn

app = Flask(__name__)


@app.route('/metrics')
def metrics():
    conn.connect()
    metrics = ''
    query = Station.select().where(Station.state > 0)
    for row in query:

       metrics += 'state{metric="%s",} %f\n' \
                   % (row.title, row.state)
    conn.close()
    return metrics


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0')

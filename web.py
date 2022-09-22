

from flask import Flask

from app.models.station import Station

app = Flask(__name__)


@app.route('/metrics')
def metrics():
    metrics = ''
    query = Station.select()
    for row in query:
        metrics += 'state{metric="%s"} %f\n' \
                   % (row.title, row.state)
    return metrics


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0')

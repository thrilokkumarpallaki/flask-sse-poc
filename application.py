from flask import Flask, render_template, jsonify
from flask_sse import sse


# flask app object creation
app = Flask(__name__)

app.register_blueprint(sse, url_prefix='/stream')
app.config['REDIS_URL'] = 'redis://localhost:6379'


# simulate persistant Data store
user_channel_map = {
    'bob': 'bob_channel',
    'kane': 'kane_channel'
}


@app.route('/load-ui')
def load_ui():
    return render_template('index.html')


@app.route('/event-trigger/<user>/<msg>')
def trigger_event(user, msg):
    channel = user_channel_map[user]
    sse.publish({'message': f'{user}_channel - {msg}'}, type='publish', channel=channel)
    return jsonify('success')


@app.route('/simulate-login/<username>')
def user_login(username):
    channel = user_channel_map[username]
    res_dict = {'sse_url': f'http://localhost:5000/stream?channel={channel}'}
    return jsonify(res_dict)


if __name__ == '__main__':
    app.run(host='localhost', debug=True)

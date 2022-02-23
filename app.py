import json

from flask import Flask,jsonify
from datetime import datetime
from datetime import timedelta
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.config["DEBUG"] = True

event = [
    {'Event_id':0,'Event_Name': 'Spiderman Dance', 'Start_time':'02/24/22 08:30:00' ,'Duration':'60min' },
    {'Event_id':1,'Event_Name': 'Superman Weight Lifting', 'Start_time': '02/24/22 09:30:00', 'Duration': '50min'},
    {'Event_id':2,'Event_Name': 'Batman Magic', 'Start_time': '02/24/22 10:20:00', 'Duration': '120min'},
    {'Event_id':3,'Event_Name': 'Avengers vs Justice League', 'Start_time': '02/24/22 12:20:00', 'Duration': '190min'},
    {'Event_id':4,'Event_Name': 'Ironman Techno Show', 'Start_time': '02/24/22 15:30:00', 'Duration': '60min'},
	{'Event_id':5,'Event_Name': 'Hulk Power House Show', 'Start_time': '02/24/22 16:30:00', 'Duration': '90min'},
    {'Event_id':6,'Event_Name': 'Wonder Woman Stunts', 'Start_time': '02/24/22 18:00:00', 'Duration': '60min'},
    {'Event_id':7,'Event_Name': 'Mortal Kombat Fight Show', 'Start_time': '02/24/22 19:00:00', 'Duration': '150min'},
	{'Event_id':8,'Event_Name': 'The Final Showdown', 'Start_time': '02/24/22 21:30:00', 'Duration': '120min'}
]


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello User!<h1>'

@app.route('/events',methods=['GET'])
def get_events():
    return jsonify({'Events List':event})

@app.route('/events/<int:event_id>',methods=['GET'])
def get_event(event_id):
    return jsonify({'Events List':event[event_id]})

@app.route('/events/upcoming',methods=['GET'])
def get_upcoming_event():
    today = datetime.now()
    date2 = today.strftime('%m/%d/%y %H:%M:%S')
    a_key = "Start_time"
    values_of_key = [a_dict[a_key] for a_dict in event]
    print(values_of_key)

    datetime2 = datetime.strptime('08/11/2019 05:45PM', '%m/%d/%Y %I:%M%p')

    upcoming_show_list_time = []

    for timevalues in values_of_key:
        datetime1 = datetime.strptime(timevalues, '%m/%d/%y %H:%M:%S')
        datetime2 = datetime.strptime(date2, '%m/%d/%y %H:%M:%S')
        if datetime1 > datetime2:
            upcoming_show_list_time.append(timevalues)
            print("datetime2 is Greater")
            print(upcoming_show_list_time)

    temp_event = event.copy();

    upcoming_events_list = []
    for list_item in upcoming_show_list_time:
        for i in range(len(temp_event)):
            if temp_event[i]['Start_time'] == list_item:
                upcoming_events_list.append(temp_event[i])
                print(temp_event[i])

    print(upcoming_events_list)

    return jsonify({'Upcoming Events':upcoming_events_list})

@app.route('/events/live',methods=['GET'])
def get_live_event():
    a_key = "Start_time"
    values_of_key = [a_dict[a_key] for a_dict in event]
    print(values_of_key)

    now = datetime.now()
    now_plus_10 = now + timedelta(minutes=10)

    live_events = []
    for timevalues in values_of_key:
        datetime1 = datetime.strptime(timevalues, '%m/%d/%y %H:%M:%S')
        if now <= datetime1 <= now_plus_10:
            live_events.append(timevalues)

    print(live_events)

    temp_event = event.copy();
    live_events_list = []
    for list_item in live_events:
        for i in range(len(temp_event)):
            if temp_event[i]['Start_time'] == list_item:
                live_events_list.append(temp_event[i])
                print(temp_event[i])

    return jsonify({'Upcoming Events':live_events_list})


if __name__ == '__main__':
    app.run()

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response
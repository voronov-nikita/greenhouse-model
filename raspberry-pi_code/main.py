from flask import Flask, jsonify
import serial

app = Flask(__name__)


@app.route('/')
def index():
    return {"Hello": "world"}


# <---------------- Температуры и влажности воздуха --------------->
@app.route('/ppo_it/api/temp_hum/1')
def index1():
    ser = serial.Serial("COM5", 9600)
    ser.write(b"1")
    data_value = ser.readline().decode('utf-8').split()
    data = {
        'id': 1,
        'temperature': float(data_value[0]),
        'humidity': float(data_value[1])
    }
    return jsonify(data)


@app.route('/ppo_it/api/temp_hum/2')
def index2():
    ser = serial.Serial("COM5", 9600)
    ser.write(b"1")
    data_value = ser.readline().decode('utf-8').split()
    data = {
        'id': 2,
        'temperature': float(data_value[0]),
        'humidity': float(data_value[1])
    }
    return jsonify(data)


@app.route('/ppo_it/api/temp_hum/3')
def index3():
    ser = serial.Serial("COM5", 9600)
    ser.write(b"1")
    data_value = ser.readline().decode('utf-8').split()
    data = {
        'id': 3,
        'temperature': float(data_value[0]),
        'humidity': float(data_value[1])
    }
    return jsonify(data)


@app.route('/ppo_it/api/temp_hum/4')
def index4():
    ser = serial.Serial("COM5", 9600)
    ser.write(b"1")
    data_value = ser.readline().decode('utf-8').split()
    data = {
        'id': 4,
        'temperature': float(data_value[0]),
        'humidity': float(data_value[1])
    }
    return jsonify(data)


# <---------------- Почва --------------->

@app.route('/ppo_it/api/hum/1')
def index5():
    ser = serial.Serial("COM5", 9600)
    ser.write(b"2")
    data_value = ser.readline().decode('utf-8')
    data = {
        'id': 1,
        'humidity': float(data_value[1])
    }
    return jsonify(data)


@app.route('/ppo_it/api/hum/2')
def index6():
    ser = serial.Serial("COM5", 9600)
    ser.write(b"2")
    data_value = ser.readline().decode('utf-8')
    data = {
        'id': 2,
        'humidity': float(data_value[1])
    }
    return jsonify(data)


@app.route('/ppo_it/api/hum/3')
def index7():
    ser = serial.Serial("COM5", 9600)
    ser.write(b"2")
    data_value = ser.readline().decode('utf-8')
    data = {
        'id': 3,
        'humidity': float(data_value[1])
    }
    return jsonify(data)


@app.route('/ppo_it/api/hum/4')
def index8():
    ser = serial.Serial("COM5", 9600)
    ser.write(b"2")
    data_value = ser.readline().decode('utf-8')
    data = {
        'id': 4,
        'humidity': float(data_value[1])
    }
    return jsonify(data)


@app.route('/ppo_it/api/hum/5')
def index9():
    ser = serial.Serial("COM5", 9600)
    ser.write(b"2")
    data_value = ser.readline().decode('utf-8')
    data = {
        'id': 5,
        'humidity': float(data_value[1])
    }
    return jsonify(data)


@app.route('/ppo_it/api/hum/6')
def index10():
    ser = serial.Serial("COM5", 9600)
    ser.write(b"2")
    data_value = ser.readline().decode('utf-8')
    data = {
        'id': 6,
        'humidity': float(data_value[1])
    }
    return jsonify(data)


# <---------------- Сервопривод --------------->
@app.route('/ppo_it/api/fork_drive/')
def index11():
    ser = serial.Serial("COM5", 9600)
    ser.write(b"3")
    return "Hello"


# старт сервера
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

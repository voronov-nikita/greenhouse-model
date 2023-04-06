from flask import Flask, jsonify
import serial

PORT = "COM5"

app = Flask(__name__)


@app.route('/')
def index():
    return {"Hello": "world"}


# <---------------- Температуры и влажности воздуха --------------->
@app.route('/ppo_it/api/temp_hum/1')
def index1():
    pin = 2
    ser = serial.Serial(PORT, 9600)
    ser.write(f"b'2{pin}'")
    data_value = ser.readline().decode('utf-8').split()
    data = {
        'pin': pin,
        'temperature': float(data_value[0]),
        'humidity': float(data_value[1])
    }
    return jsonify(data)


@app.route('/ppo_it/api/temp_hum/2')
def index2():
    pin = 3
    ser = serial.Serial(PORT, 9600)
    ser.write(f"b'2{pin}'")
    data_value = ser.readline().decode('utf-8').split()
    data = {
        'pin': pin,
        'temperature': float(data_value[0]),
        'humidity': float(data_value[1])
    }
    return jsonify(data)


@app.route('/ppo_it/api/temp_hum/3')
def index3():
    pin = 4
    ser = serial.Serial(PORT, 9600)
    ser.write(f"b'2{pin}'")
    data_value = ser.readline().decode('utf-8').split()
    data = {
        'pin': pin,
        'temperature': float(data_value[0]),
        'humidity': float(data_value[1])
    }
    return jsonify(data)


@app.route('/ppo_it/api/temp_hum/4')
def index4():
    pin = 5
    ser = serial.Serial(PORT, 9600)
    ser.write(f"b'2{pin}'")
    data_value = ser.readline().decode('utf-8').split()
    data = {
        'pin': pin,
        'temperature': float(data_value[0]),
        'humidity': float(data_value[1])
    }
    return jsonify(data)


# <---------------- Почва --------------->

@app.route('/ppo_it/api/hum/1')
def index5():
    pin = 7
    ser = serial.Serial(PORT, 9600)
    ser.write(f"b'1{pin}'")
    data_value = ser.readline().decode('utf-8')
    data = {
        'pin': pin,
        'humidity': float(data_value[1])
    }
    return jsonify(data)


@app.route('/ppo_it/api/hum/2')
def index6():
    pin = 8
    ser = serial.Serial(PORT, 9600)
    ser.write(f"b'1{pin}'")
    data_value = ser.readline().decode('utf-8')
    data = {
        'pin': pin,
        'humidity': float(data_value[1])
    }
    return jsonify(data)


@app.route('/ppo_it/api/hum/3')
def index7():
    pin = 9
    ser = serial.Serial(PORT, 9600)
    ser.write(f"b'1{pin}'")
    data_value = ser.readline().decode('utf-8')
    data = {
        'pin': pin,
        'humidity': float(data_value[1])
    }
    return jsonify(data)


@app.route('/ppo_it/api/hum/4')
def index8():
    pin = 10
    ser = serial.Serial(PORT, 9600)
    ser.write(f"b'1{pin}'")
    data_value = ser.readline().decode('utf-8')
    data = {
        'pin': pin,
        'humidity': float(data_value[1])
    }
    return jsonify(data)


@app.route('/ppo_it/api/hum/5')
def index9():
    pin = 11
    ser = serial.Serial(PORT, 9600)
    ser.write(f"b'1{pin}'")
    data_value = ser.readline().decode('utf-8')
    data = {
        'pin': pin,
        'humidity': float(data_value[1])
    }
    return jsonify(data)


@app.route('/ppo_it/api/hum/6')
def index10():
    pin = 12
    ser = serial.Serial(PORT, 9600)
    ser.write(f"b'1{pin}'")
    data_value = ser.readline().decode('utf-8')
    data = {
        'pin': pin,
        'humidity': float(data_value[1])
    }
    return jsonify(data)


# <---------------- Сервопривод --------------->
@app.route('/ppo_it/api/fork_drive/')
def index11():
    ser = serial.Serial(PORT, 9600)
    ser.write(b"3")
    return "Hello"


# старт сервера
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

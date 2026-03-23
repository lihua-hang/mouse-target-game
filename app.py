from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

# 获取所有程序
def get_programs():
    programs = []
    base_dir = "D:\各种各样的小程序"
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py"):
                program_path = os.path.join(root, file)
                relative_path = os.path.relpath(program_path, base_dir)
                programs.append({
                    "name": file,
                    "path": relative_path,
                    "description": "Python程序"
                })
    return programs

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/program/<path:program_path>')
def program(program_path):
    return send_file(os.path.join("D:\各种各样的小程序", program_path))

@app.route('/play/mouse_target')
def play_mouse_target():
    return render_template('mouse_target.html')

@app.route('/play/piano')
def play_piano():
    return render_template('piano.html')

@app.route('/play/fps_game')
def play_fps_game():
    return render_template('fps_game.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
from flask import Flask, render_template, request
import docker

app = Flask(__name__)
client = docker.from_env()

@app.route('/')
def index():
    containers = client.containers.list(all=True)
    container_info = []

    for container in containers:
        status = container.status
        if status == 'running':
            color = "#50FA7B"  # Green for running
        elif status == 'created':
            color = "#6272A4"  # Blueish for created
        elif status == 'exited':
            color = "#FF5555"  # Red for stopped
        elif status == 'unhealthy':
            color = "#F1FA8C"  # Yellow for unhealthy
        else:
            color = "#F1FA8C"  # Yellow for anything else
        
        container_info.append({
            'name': container.name,
            'id': container.short_id,
            'status': status,
            'color': color
        })

    return render_template('index.html', containers=container_info)

@app.route('/start/<container_id>')
def start_container(container_id):
    container = client.containers.get(container_id)
    container.start()
    return "Container started", 200

@app.route('/stop/<container_id>')
def stop_container(container_id):
    container = client.containers.get(container_id)
    container.stop()
    return "Container stopped", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8765)
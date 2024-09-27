<div align="center">
  <img src="https://github.com/MattDGTL/shipyard/blob/main/images/shipyard.png">
</div>

# Shipyard

Shipyard is a sleek, responsive iFrame widget designed for [Homarr](https://github.com/ajnart/homarr "Homarr"), your customizable dashboard for homelab management. With Shipyard, you can effortlessly control your Docker containers from Homarr, giving you a smooth and user-friendly way to manage your infrastructure.

<div align="center">
  <img src="https://github.com/MattDGTL/shipyard/blob/main/images/ss-shipyard-light.png"> <img src="https://github.com/MattDGTL/shipyard/blob/main/images/ss-shipyard-dark.png">
</div>

# Features
- Container Management: Start, stop, and monitor your Docker containers directly from the Homarr dashboard.

- Responsive Design: Adapts to any screen size, ensuring a seamless experience.

- Real-time Status Indicators: Easily distinguish container states:Running: Green check mark (✅)

- Stopped: Red cross (❌)

- Other statuses: Purple dot (🟣)

- Dark & Light Theme Support: Automatically adapts to your system theme.

- Sorting: Quickly sort containers by name or status for efficient management.

# Installation

Pull

`git clone https://github.com/MattDGTL/shipyard.git`

CD into the main directory

`CD shipyard/`

In the directory where your Dockerfile, app.py, and templates folder are located, run the following commands:

`docker build -t shipyard .`

Run the Docker container:

`docker run -d -p 8765:8765 -v /var/run/docker.sock:/var/run/docker.sock --name shipyard shipyard`

 Add a Homarr iFrame, insert URL (http://$DOCKERIP:8765)



# Usage

Once installed and running, Shipyard will appear on your Homarr dashboard. You can:

- View all Docker containers and their statuses.

- Start or stop containers with a single click.

- Sort containers for quick management.

# Customization

For further customization, modify the index.html file in the repository.

# Contributing

We welcome contributions! If you find any issues or have ideas for improvement, feel free to open a pull request or issue.


![](https://github.com/MattDGTL/shipyard/blob/main/images/ss-dark.png)

![](https://github.com/MattDGTL/shipyard/blob/main/images/ss-light.png)

# License

Licensed under the MIT License. See the LICENSE file for more details.


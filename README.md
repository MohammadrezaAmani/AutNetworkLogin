# Auto-Login for Amirkabir University of Technology (AUT) Internet

This script allows students and staff at Amirkabir University of Technology (AUT) to log in to the university's internet network automatically, without needing to open a browser. It can be configured to run as a service, ensuring seamless internet access every time the system starts.

## Features

- **Automatic Login**: Logs in to the AUT network without manual input.
- **Flexible Credentials Handling**: Accepts username and password via:
  - Command-line arguments
  - Environment variables
- **System Service Compatibility**: Can be set up as a background service to run on startup.

## Installation

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/MohammadrezaAmani/AutNetworkLogin aut-login
   cd aut-login
   ```

2. **Install Dependencies** (if required by `main.py`):

   ```sh
   pip install -r requirements.txt
   ```

3. **Set Your Credentials**:

   - Option 1: Using command-line arguments:

     ```sh
     python main.py -u your_username -p your_password
     ```

   - Option 2: Using environment variables:

     ```sh
     export USERNAME=your_username
     export PASSWORD=your_password
     python main.py
     ```

## Running as a Service (Linux)

To ensure the script runs on startup, you can set it up as a systemd service.

1. **Create a systemd service file**:

   ```sh
   sudo nano /etc/systemd/system/aut-login.service
   ```

2. **Add the following content**:

   ```ini
   [Unit]
   Description=Auto-Login to AUT Internet
   After=network.target

   [Service]
   ExecStart=/usr/bin/python3 /path/to/main.py
   Restart=always
   User=your_user
   Environment="USERNAME=your_username" "PASSWORD=your_password"

   [Install]
   WantedBy=multi-user.target
   ```

3. **Enable and Start the Service**:

   ```sh
   sudo systemctl daemon-reload
   sudo systemctl enable aut-login
   sudo systemctl start aut-login
   ```

Now, every time your system boots up, it will automatically log in to the AUT internet network.

## License

This project is open-source and available under the MIT License.

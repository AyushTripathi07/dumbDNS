# dumbDNS

**dumbDNS** is a lightweight and specialized DNS resolver written in Python. This resolver supports two primary functionalities:

1. **Unit Conversion**: Converts between different units (e.g., `42km-mi.unit` returns `"42.00 Kilometer (km) = 26.10 Mile (mi)"`).
2. **UUID Generation**: Generates a random UUID (e.g., `uuid.generate` returns `"550e8400-e29b-41d4-a716-446655440000"`).

This project leverages the `dnslib` library to handle DNS queries and responses and includes extensible features for adding more use cases in the future.

## Features

- **Unit Conversion**: Supports conversion of various units like length, weight, and more using the [Pint](https://pint.readthedocs.io/) library.
- **UUID Generation**: Generates and returns a unique UUID for each query.
- Handles TXT record responses for specific DNS query formats.
- Lightweight and easy to deploy using Docker or directly on platforms like Railway.

## Query Examples

### 1. Unit Conversion

```bash
dig @<server_address> -p 5353 42km-mi.unit TXT
```

**Response**
```
42km-mi.unit.   0   IN   TXT   "42.00 Kilometer (km) = 26.10 Mile (mi)"
```

### 2. UUID Generation

```bash
dig @<server_address> -p 5353 uuid.generate TXT
```

**Response**
```
uuid.generate.   0   IN   TXT   "550e8400-e29b-41d4-a716-446655440000"
```

## Requirements
- Python 3.12+
- dnslib for DNS query handling
- pint for unit conversions

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Server
1. Clone the repository:
```bash
git clone https://github.com/yourusername/dumbDNS.git
cd dumbDNS
```

2. Create and activate a virtual environment:
```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Start the DNS resolver:
```bash
python resolver.py
```

The server will start on 127.0.0.1 and listen on UDP port 5353 by default.

### Deploying with Docker
1. Build the Docker image:
```bash
docker build -t dumbdns .
```

2. Run the Docker container:
```bash
docker run -d -p 5353:5353/udp dumbdns
```

3. Test the resolver:
```bash
dig @<container_ip> -p 5353 uuid.generate TXT
```

### Deployment on Railway

This project can be deployed on Railway.app for global access. Follow these steps:
1. Push the repository to GitHub.
2. Connect your repository to Railway.
3. Configure the project to expose UDP port 5353.
4. Deploy and use the public hostname/IP for queries.

## Project Structure
```
/dumbDNS
├── resolver.py           # Main DNS resolver logic
├── requirements.txt      # Dependencies
├── Dockerfile           # Docker configuration for containerizing the app
└── README.md            # Documentation (this file)
```

## Extending the Project

**dumbDNS** is designed to be extensible. You can add more functionalities by modifying the resolve method in resolver.py to handle new query patterns.

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.

## Author

[Ayush Tripathi](https://github.com/AyushTripathi07)
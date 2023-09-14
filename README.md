# SaaS Business Management Platform

This is a modular SaaS business management platform built with a microservices architecture and an API-first design. It uses React JS for the front-end, Lucee for server-side operations, and MSSQL for database management.

## Installation

1. Clone the repository:
```
git clone https://github.com/your-repo/saas-business-management.git
```

2. Install Python dependencies:
```
pip install -r requirements.txt
```

3. Install JavaScript dependencies:
```
npm install
```

4. Set up your MSSQL database and update the `DATABASE_URI` in `src/config.py`.

5. Set your secret key for authentication in `src/config.py`.

## Running the Application

1. Start the server:
```
python src/main.py
```

2. In a new terminal window, start the front-end:
```
npm start
```

The application will be running at `http://localhost:3000`.

## Testing

Run the test suite with:
```
python -m unittest discover -s src/tests
```

## Docker

You can also run the application with Docker. Build and run the Docker image with:
```
docker-compose up --build
```

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.
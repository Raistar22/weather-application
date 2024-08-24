# Weather Application

## Overview

The Weather Application is a Django-based project that provides weather information through a REST API. It allows users to query current weather conditions for a specific location. This project demonstrates how to integrate Django with Django REST Framework to build a simple API.

## Features

- Current Weather Information: Provides current weather data including temperature, humidity, and description.
- REST API: Built using Django REST Framework to handle requests and responses.
- Template Integration: Basic front-end for testing purposes (if applicable).

## Prerequisites

- Python 3.x
- Django 4.x
- Django REST Framework
- An API key for a weather service (e.g., OpenWeatherMap)

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

### Set Up Virtual Environment

1. Create and Activate Virtual Environment:

   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # On Windows
   source myenv/bin/activate  # On macOS/Linux
   ```

2. Install Dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. Create a `.env` File:

   In the root directory of your project, create a `.env` file and add your API key and other environment variables:

   ```env
   WEATHER_API_KEY=your_api_key_here
   ```

2. Update `settings.py`:

   Ensure that your `settings.py` is configured to load environment variables and configure the weather API key.

### Run the Application

1. Apply Migrations:

   ```bash
   python manage.py migrate
   ```

2. Run the Development Server:

   ```bash
   python manage.py runserver
   ```

3. Access the Application:

   Open your web browser and go to `http://127.0.0.1:8000/api/weather/` to access the weather API endpoint.

## Usage

### API Endpoints

- GET /api/weather/?location={city_name}

  Retrieves the current weather information for the specified city.

  Query Parameters:

  - `location`: City name (e.g., `London`, `New York`).

  Response:

  ```json
  {
    "temperature": "15°C",
    "humidity": "72%",
    "description": "Clear sky"
  }
  ```

## Example

To get the weather information for London, use the following cURL command:

```bash
curl "http://127.0.0.1:8000/api/weather/?location=India"
```

## Development

- Add New Features: Modify the API views and serializers to include additional weather data.
- Testing: Write tests for the API endpoints to ensure reliability.

## Contributing

1. Fork the Repository:

   Click the "Fork" button on GitHub to create your copy of the repository.

2. Create a Branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make Changes and Commit:

   ```bash
   git add .
   git commit -m "Add feature"
   ```

4. Push Changes:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Create a Pull Request: 

   Go to the original repository on GitHub and open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django REST Framework: For providing an easy way to build APIs.
- Weather API Service: For providing weather data.


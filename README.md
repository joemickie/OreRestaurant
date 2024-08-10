# OreRestaurant

## Overview

OreRestaurant is a Django-based web application designed to manage a restaurant's menu, orders, and staff members. The application allows for seamless interaction between the frontend and backend, handling various operations such as user authentication, menu management, and order processing.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
  - [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **User Authentication:** Secure login, registration, and role-based access control for staff members.
- **Menu Management:** Create, update, and delete menu items with pricing and discount options.
- **Order Processing:** Manage customer orders, including order creation, updates, and tracking.
- **Responsive Design:** Optimized for various screen sizes and devices.

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Environment Management:** Python Dotenv
- **Version Control:** Git
- **Deployment:** Vercel/AWS EC2 (if applicable)

## Getting Started

### Prerequisites

- **Python 3.12** or later
- **PostgreSQL 14** or later
- **pip** (Python package installer)
- **Git** (for version control)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/OreRestaurant.git
   cd OreRestaurant
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Environment Variables

Create a `.env` file in the root directory of your project and configure the following variables:

```bash
SECRET_KEY="h0h-8yzw)1u+h3ezxvx*!6xhqlh!wya1u6h_14fb&#7-*zuum&"
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL="postgres://postgres:Mickiejoe#@localhost:5432/orerestaurant"
```

### Database Setup

1. **Make and apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Create a superuser (admin):**
   ```bash
   python manage.py createsuperuser
   ```

## Running the Application

1. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

2. **Access the application in your browser:**
   ```
   http://localhost:8000/
   ```

## Testing

Run the test suite to ensure that everything is working correctly:

```bash
python manage.py test
```

## Deployment

For production, ensure that the `DEBUG` setting is set to `False`, and configure your database and static files settings accordingly.

### Deploy to AWS EC2

1. **Setup EC2 instance and configure your environment.**
2. **Install PostgreSQL and other dependencies.**
3. **Clone the repository and follow the [Installation](#installation) steps on the server.**
4. **Configure Gunicorn and Nginx for production.**

### Deploy to Vercel (Optional)

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```
2. **Deploy:**
   ```bash
   vercel --prod
   ```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed explanation of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For any inquiries or issues, please contact:

- **Chukwuemeka Chinemelu**
- **Email:** chukwuemekachinemeluj@gmail.com
- **GitHub:** [joemickie](https://github.com/joemickie)
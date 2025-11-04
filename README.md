AIN-3005: Car Rental & Fleet Maintenance System

This project is a solution for the 1st Homework Assignment for the "Advanced Python Programming" (AIN-3005) course at Bahçeşehir University.

It is a complete, object-oriented system for managing car rentals, fleet maintenance, and billing, built using clean architecture principles.

Project Description

The system (CRFMS) is designed to support:

Customers: Creating and managing reservations.

Branch Agents: Handling vehicle pickups and returns, recording odometer/fuel, and assessing charges.

Fleet Managers: Enforcing maintenance holds based on vehicle odometer or time.

It correctly calculates rental charges, late fees, mileage overage, and fuel refill penalties, all while being fully testable thanks to an injectable Clock.

Core Design & Architecture

This project was built with a focus on SOLID principles and a Clean Architecture (Ports and Adapters) approach.

Domain (crfms/domain): Contains all core business logic, entities (like Vehicle, Reservation), and Value Objects (like Money, Kilometers). It has no dependencies on other layers.

Services (crfms/services): The orchestration layer that coordinates domain entities to perform use cases (e.g., RentalService, AccountingService).

Adapters (crfms/adapters): Concrete implementations of the interfaces defined in the domain.

FakePaymentAdapter simulates payment success/failure.

InMemoryNotificationAdapter records sent notifications for testing.

Strategy Pattern: The PricingPolicy uses the Strategy Pattern to allow new pricing rules (like BaseDailyRateRule) to be "plugged in" without changing core code.

UML: A complete UML class diagram is available in design.puml.

Project Structure

car_rental_system/
├── crfms/              # The main Python package
│   ├── __init__.py
│   ├── adapters/         # Implementations of ports
│   │   ├── __init__.py
│   │   ├── notifications.py
│   │   └── payments.py
│   ├── domain/           # Core entities, value objects, ports
│   │   ├── __init__.py
│   │   ├── fleet.py
│   │   ├── pricing.py
│   │   ├── rental.py
│   │   ├── users.py
│   │   └── values.py
│   └── services/         # Use-case orchestration
│       ├── __init__.py
│       ├── accounting.py
│       ├── database.py
│       ├── inventory.py
│       ├── maintenance.py
│       ├── rental.py
│       └── reservation.py
├── tests/              # All pytest tests
│   ├── __init__.py
│   └── test_rental_workflow.py
├── .gitignore          # Files for Git to ignore
├── design.puml         # The UML class diagram
└── README.md           # This file
└── requirements.txt    # Python dependencies



How to Run This Project

Prerequisites:

Python 3.10+

git

Clone & Install:

# Clone the repository (or just use your local folder)
# git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
# cd car_rental_system

# Create a virtual environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate
# (macOS/Linux)
# source venv/bin/activate

# Install the required packages
pip install -r requirements.txt



Run the Tests:
To verify all business logic is working correctly, run pytest from the main (car_rental_system) directory:

pytest



You should see an output showing 2 passed.
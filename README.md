# Python Financial Manager Application

A financial management application designed to help users track and analyze their financial data with real-time stock monitoring and trend analysis using the Alpha Vantage API. It features an intuitive PySimpleGUI interface, secure PostgreSQL database for personalized data storage, and tools like an income statement generator and bill management system for comprehensive financial planning. 

## Installation
  1. Clone the repository in IDE of choice using: https://github.com/cshevick/Finance_Manager_App.git
  2. Install the required dependencies: pip install pandas alpha_vantage PySimpleGUI psycopg2-binary

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Setup and Installation](#setup-and-installation)

## Overview

The financial manager application is designed to provide users with tools for financial tracking, analysis, and management. It includes real-time stock monitoring, trend analysis, financial statement management, an income statement generator, a bill management system, and a learning feature for financial guidance.

- **Real-time Stock Data:**
  - Fetch and display real-time stock data using the Alpha Vantage API.
  - Monitor stock prices and analyze trends.
- **Intuitive User Interface:**
  - Built with PySimpleGUI for easy navigation and a user-friendly experience.
- **Secure Database Management:**
  - PostgreSQL database managed through PG Admin 4 for secure user authentication.
  - Stores essential data such as usernames, passwords, and personalized stock lists.
- **SQL Queries:**
  - Retrieve and display user-specific data using SQL queries.
  - Interact with stored stock information directly within the app.
- **Financial Tools:**
  - Income statement generator.
  - Bill management system.
  - Learning feature for financial guidance and tips.

## Architecture

The application consists of the following components:
- **Frontend:** PySimpleGUI for building the user interface.
- **Backend:** Python scripts for handling business logic, API requests, and database interactions.
- **Database:** PostgreSQL database for storing user data securely.
- **API:** Alpha Vantage API for fetching real-time stock data.



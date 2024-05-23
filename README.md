# Galapago Telegram Bot

![Logo](https://example.com/path/to/your/logo.jpg)

Welcome to the Galapago Telegram Bot project. This bot allows users to access the [Galapago Web App](https://testnet.galapago.app) directly from Telegram, providing real-time updates and seamless integration.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## About

Project Galapago is designed to offer a comprehensive digital asset liquidity solution for seamless web app integration within Telegram. For more details about Project Galapago, please refer to the [official documentation](https://docs.galapago.app).

## Features

- **Easy Access**: Users can access the Galapago web app directly from Telegram.
- **Real-time Updates**: Stay updated with the latest information from the Galapago web app.
- **Seamless Integration**: The bot provides a seamless user experience by integrating the web app within Telegram.

## Installation

### Prerequisites

- Python 3.10+
- [Telegram Bot Token](https://core.telegram.org/bots#botfather)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/jack-jackhui/galapago-telegram-bot.git
    cd galapago-telegram-bot
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your Telegram bot token:

    ```env
    TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
    ```

## Usage

Run the bot with the following command:

```bash
python galapago-telegram-bot.py
```

### Commands

- `/start`: Initiates the bot and provides the user with a welcome message, a description, and a link to open the Galapago web app.

### Configuration

Ensure that the `.env` file contains your Telegram bot token:

```env
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

### Contributing

We welcome contributions to improve the Galapago Telegram Bot. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

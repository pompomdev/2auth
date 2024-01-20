# 2auth

[![Apache-2.0 License](https://img.shields.io/github/license/pompomdev/2auth)](https://opensource.org/licenses/Apache-2.0)
[![GitHub Repo](https://img.shields.io/badge/Github-2auth-blue)](https://github.com/pompomdev/2auth)

2auth is a software that provides two-factor authentication using One-Time Passwords (OTP). It allows users to save their authentication entries and generate OTP codes.

## Installation

To use 2auth, you need to have Python installed on your machine. You can install Python by visiting the [Python website](https://www.python.org) and following the instructions for your operating system.

After installing Python, you can clone the `2auth` repository to your local machine using the following command:

```shell
$ git clone https://github.com/pompomdev/2auth.git
```

## Usage

To start using 2auth, navigate to the cloned repository directory in your terminal:

```shell
$ cd 2auth
```

Run the following command to execute the software:

```shell
$ python main.py
```

Once the software is running, you will see a menu with the following options:

1. Save Entries: Allows you to save authentication entries by providing a name and secret.
2. Generate OTP Codes: Generates OTP codes for the saved authentication entries.
3. Exit: Exits the software.

Choose an option by entering the corresponding number and following the prompts. Refer to the on-screen instructions for more details on each option.

## Data Storage

2auth stores the saved entries in a file named `entries.2auth` in the `data` directory. The entries are serialized using the pickle module. Make sure to back up this file if you intend to switch devices or reinstall the software.

## Contributing

Contributions to 2auth are welcome! If you find any issues or have suggestions for improvements, please open a new issue or submit a pull request on the [2auth repository](https://github.com/pompomdev/2auth).

## License

This project is licensed under the [Apache 2.0 License](https://opensource.org/licenses/Apache-2.0). Feel free to use, modify, and distribute this software. See the `LICENSE` file for more information.

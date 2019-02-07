
# [POLITICO](https://lawrencemuema.github.io/politico_p/UI)

an immersive online voting platform
andela pre bootcamp challenge


## Code Status
[![Build Status](https://travis-ci.org/lawrencemuema/politico_p.svg?branch=develop)](https://travis-ci.org/lawrencemuema/politico_p)

[![Coverage Status](https://coveralls.io/repos/github/lawrencemuema/politico_p/badge.svg?branch=develop)](https://coveralls.io/github/lawrencemuema/politico_p?branch=develop)

[![Maintainability](https://api.codeclimate.com/v1/badges/0e533517d5d3fe5dfa6f/maintainability)](https://codeclimate.com/github/lawrencemuema/politico_p/maintainability)




### End points
Method | Endpoint | Usage |
| ---- | ---- | --------------- |
|POST| `/api/v1/party` |  Create a party. |
|POST| `/api/v1/office` |  Create a office. |
|GET| `/api/v1/party` | Get all parties.|
|GET| `/api/v1/office` | Get all offices.|
|GET| `/api/v1/party/<p_id>` | Get specific party. |
|GET| `/api/v1/office/<o_id>` | Get specific office. |
|PUT| `/api/v1/party/<p_id>` | edit a party. |
|DELETE| `/api/v1/party/<p_id>` | Delete a specific party. |



## Installation

Clone the Github repository and use pip to install the dependencies
1. `$ git clone https://github.com/lawrencemuema/politico_p.git`
2. `$ cd/politico_p`
3. `$ venv\scripts\activate`
4. `$ pip install -r requirements.txt`


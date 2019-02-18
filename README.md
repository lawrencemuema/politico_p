
# [POLITICO](https://lawrencemuema.github.io/politico_p/ui)
https://lawrencemuema.github.io/politico_p/ui

an immersive online voting platform
andela pre bootcamp challenge


## Code Status
[![Build Status](https://travis-ci.org/lawrencemuema/politico_p.svg?branch=develop)](https://travis-ci.org/lawrencemuema/politico_p)
[![Coverage Status](https://coveralls.io/repos/github/lawrencemuema/politico_p/badge.svg)](https://coveralls.io/github/lawrencemuema/politico_p?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/f859e7a849e3207e4eba/maintainability)](https://codeclimate.com/github/lawrencemuema/politico_p/maintainability)



### api End points
Method | Endpoint | Usage |
| ---- | ---- | --------------- |

|PARTY| | |
|POST| `/api/v1/party` |  Create a party. |
|GET| `/api/v1/party` | Get all parties.|
|GET| `/api/v1/party/<p_id>` | Get specific party. |
|PUT| `/api/v1/party/<p_id>` | edit a party. |
|DELETE| `/api/v1/party/<p_id>` | Delete a specific party. |

|OFFICE| | |
|POST| `/api/v1/office` |  Create a office. |
|GET| `/api/v1/office` | Get all offices.|
|GET| `/api/v1/office/<o_id>` | Get specific office.|

|USERS| | |
|POST| `/api/v1/signup` | register user. |
|GET| `/api/v1/signin` | user login. |

|VOTES| | |
|POST| `/api/v1/vote` | proces voting. |
|GET| `/api/v1/vote` | get all votes cast. |
|GET| `/api/v1/vote/<v_id`> | get all votes cast by specific voter. |
|GET| `/api/v1/vote/<candidate_name`> | get all votes cast to a specific candidate. |




## Installation

Clone the Github repository and use pip to install the dependencies
1. ` git clone https://github.com/lawrencemuema/politico_p.git`
2. ` cd/politico_p`
3. ` venv\scripts\activate`
4. ` pip install -r requirements.txt`


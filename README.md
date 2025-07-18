### Hexlet tests and linter status:
[![Actions Status](https://github.com/MuhutDil/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/MuhutDil/python-project-83/actions)
[![PyCI](https://github.com/MuhutDil/python-project-83/actions/workflows/pyci.yml/badge.svg)](https://github.com/MuhutDil/python-project-83/actions/workflows/pyci.yml)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=MuhutDil_python-project-83&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=MuhutDil_python-project-83)

# Page analyzer
The "Page_analyzer" is website for analyze web pages for their SEO suitability similar to [PageSpeed ​​Insights](https://pagespeed.web.dev/). The project provides users with the ability to check the availability of websites and analyze these elements(main heading tag, headers and site descriptions).

## Demo version of the site
[Page_analyzer](https://python-project-83-gn03.onrender.com)
 
## Installation
### Prerequisites
- Python version 3.10 or higher
- Flask version 3.1.1 or higher
- PostgreSQL version 16.6 or higher
- Uv version 0.5 or higher (optional)
 
### Download
    git clone https://github.com/MuhutDil/python-project-83.git

### Configuration
Rename the `.env_example` file to `.env` and following the example in this file, enter your data.

`Makefile` simplifies the installation and startup process.
#### Build the application and create database tables
    make build
#### Starting a local development server
    make dev
#### Starting a production (working) server
    make start

# Proyecto Final - Automation Testing

## Descripción del Proyecto

### Este proyecto es un framework de automatización de pruebas UI y API usando Python. El framework combina pruebas UI con Selenium WebDriver, pruebas de API utilizando la biblioteca Requests, y estructura el código de manera eficiente usando el patrón Page Object Model (POM).

### El framework permite ejecutar pruebas automatizadas de UI y API, incluyendo reportes visuales HTML y screenshots de fallos.

## Tecnologías utilizadas
#### - Python
#### - Pytest
#### - Selenium WebDriver
#### - Requests
#### - pytest_html
#### - Git + GitHub
#### - GitHub Actions

## Estructura del Proyecto

#### main
#### │
#### ├── conftest.py 
#### │
#### ├── pytest.ini 
#### │
#### ├── requirements.txt 
#### │
#### ├── README.md
#### │
#### ├── pages
#### │ ├── base_page.py
#### │ ├── cart_page.py
#### │ ├── checkout_page.py
#### │ ├── inventory_page.py
#### │ └── login_page.py
#### │
#### ├── tests
#### │ ├── ui
#### │    ├── test_add_cart.py
#### │    ├── test_checkout.py
#### │    ├── test_login_negative.py
#### │    ├── test_login_ui.py
#### │    └── test_navigation.py
#### │
#### │ └── api
#### │    ├── test_create_user_api.py
#### │    ├── test_delete_user_api.py
#### │    └── test_users_api.py
#### │
#### ├── utils
#### │ ├── api_client.py
#### │ ├── data_reader.py
#### │ ├── driver_factory.py
#### │ └── logger.py
#### │
#### ├── .github
#### │ └── workflows
#### │    └── test.yml
#### │
#### ├── config
#### │ └── config.yaml
#### │
#### ├── data
#### │ └── checkout_data.json
#### │ └── invalid_users.json
#### │ └── users.csv
#### │
#### ├── screenshots
#### │
#### ├── reports
#### │ └── report.html
#### │
#### └── logs


## Instalación de dependencias desde pip (línea de comandos):

### Ejecutar: _pip install selenium pytest pytest-html pyyaml requests_

#### Si solicita actualización, se debe ejecutar:
##### _pip install --upgrade pip_ 
###### o intentar con:
##### _python.exe -m pip install --upgrade pip_

### Se creó un archivo _requeriments.txt_ como otra forma de instalación de las dependencias:

#### _pip install -r requirements.txt_



## Ejecución de las pruebas

### Usando Pytest: 

#### Ejecutar: _pytest tests/ --html=reports/report.html --self-contained-html_

#### Si se desea ejecutar solo las pruebas UI:

##### _pytest tests/ui/ --html=reports/report.html --self-contained-html_

#### Si se desea ejecutar solo las pruebas API:

##### _pytest tests/api/ --html=reports/report.html --self-contained-html_


### Se creó un archivo pytest.ini para otra forma de ejecutar las pruebas:

#### Ejecutar: _pytest_


## Interpretación de los Reportes

### Los reportes HTML se generan en la carpeta reports/

### Cada test incluye:
#### - Estado: Pasado o Fallado
#### - Duración de ejecución
#### - Logs detallados de cada paso (pasos clave de UI o API)
#### - Capturas de pantalla adjuntas automáticamente en tests fallidos
#### - Los logs completos se encuentran en logs/, con fecha y hora de ejecución

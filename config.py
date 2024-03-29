import os
basedir = os.path.abspath(os.path.dirname(__file__))

class DefaultConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAPI_VERSION = '3.0.2'
    OPENAPI_URL_PREFIX = '/docs'
    OPENAPI_SWAGGER_UI_PATH = '/swagger'
    OPENAPI_SWAGGER_UI_URL = 'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.19.5/'
    API_TITLE = 'stacks'
    API_VERSION = 'v0.1'
    JSON_AS_ASCII = False
    API_SPEC_OPTIONS = {
        'security':[{"bearerAuth": []}],
        'components':{
            "securitySchemes":
                {
                    "bearerAuth": {
                        "type":"http",
                        "scheme": "bearer",
                    }
                }
        }
    }

class Config(DefaultConfig):
    MYSQL_DATABASE_HOST = os.environ.get('STACKS_MYSQL_HOST')
    MYSQL_USER = os.environ.get('STACKS_MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('STACKS_MYSQL_ROOT_PASSWORD')
    MYSQL_DB = 'stacks'
    MYSQL_PORT = os.environ.get('STACKS_MYSQL_PORT')
    SQLALCHEMY_DATABASE_URI = \
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_DATABASE_HOST}:{MYSQL_PORT}/{MYSQL_DB}"


class ProductionConfig(DefaultConfig):
    MYSQL_DATABASE_HOST = os.environ.get('STACKS_MYSQL_DO_HOST')
    MYSQL_USER = os.environ.get('STACKS_MYSQL_DO_USER')
    MYSQL_PASSWORD = os.environ.get('STACKS_MYSQL_DO_PASSWORD')
    MYSQL_DB = 'stacks'
    MYSQL_PORT = os.environ.get('STACKS_MYSQL_DO_PORT')
    SQLALCHEMY_DATABASE_URI = \
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_DATABASE_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

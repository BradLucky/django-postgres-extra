import dj_database_url

DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = 'this is my secret key'  # NOQA

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

DATABASES = {
        'default': dj_database_url.config(default='postgres:///psqlextra')
}

DATABASES['default']['ENGINE'] = 'psqlextra.backend'

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
    ('ro', 'Romanian'),
    ('nl', 'Dutch')
)

INSTALLED_APPS = (
    'psqlextra',
    'tests',
)

MIGRATION_DEFAULT_TIMEOUT = None

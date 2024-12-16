from setuptools import setup, find_packages

setup(
    name='weather_app',
    version='0.1',
    packages=find_packages(),
    install_requires=['requests', 'json'],
    entry_points={'console_scripts': [
        'weather_app = weather_app.main:main'
    ]},
    author='ZakNastia',
    author_email='zaknastia2004@gmail.com',
    description='Приложение для получения данных о погоде с Openweather API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    pyton_requires='>=3.6'
)
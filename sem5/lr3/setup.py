import setuptools

setuptools.setup(
    name='AppOpenWeather',
    version='0.1',
    packages=setuptools.find_packages(),
    install_requires=['requests', 'json'],
    entry_points={'console_scripts': [
        'weather_app = weather_app.main:main'
    ]},
    author='ZakNastia',
    author_email='zaknastia2004@gmail.com',
    description='Приложение для получения данных о погоде с Openweather API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nasirdn/prog/tree/main/sem5/lr3',
    pyton_requires='>=3.6'
)
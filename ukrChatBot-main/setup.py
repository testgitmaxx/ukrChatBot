from setuptools import setup, find_packages

setup(
    name='ukrChatBot',
    version='1.0',
    packages=find_packages(),
    install_requires=open('requirements.txt').read(),
    author='Олег Філіпенков',
    author_email='o.filipenkov@gmail.com',
    description="""
    Цей телеграм бот надає можливість 
    вивчити лексику української мови через
    сайт "https://ukr-mova.in.ua/""",
    long_description=open('README.md').read(),
    url='https://github.com/testgitmaxx/ukrChatBot',
    entry_points={
        'console_scripts': [
            'your_script_name = your_package_name.module_name:main_function',
        ],
    },
)

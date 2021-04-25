from setuptools import setup, find_packages

setup(
    name='SAF',
    version='1.0.0',
    description='Selenium test automation framework',
    url='https://github.com/IncluIT17/selenium-automation-framework',
    author='Adrian Esteban Gonzalez',
    author_email='adrianesteban274@gmail.com',
    classifiers=[
        'DEVELOPMENT STATUS :: BETA',
        'Topic :: Test Automation :: Selenium, Appium',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='automation appium selenium framework page_object webdriver',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    install_requires=[
        'atomicwrites==1.3.0',
        'attrs==19.1.0',
        'certifi==2019.3.9',
        'chardet==3.0.4',
        'colorama==0.4.1',
        'idna==2.8',
        'more-itertools==7.0.0',
        'pluggy==0.9.0',
        'py==1.8.0',
        'pytest==4.4.1',
        'python-dotenv==0.10.1',
        'requests==2.21.0',
        'selenium==3.141.0',
        'six==1.12.0',
        'urllib3==1.24.1'
    ],
    project_urls={
        'Source': 'https://github.com/IncluIT17/selenium-automation-framework'
    }
)

# README #

### What is this repository for? ###

Test automation framework based on Python. Developed for web applications in different browsers/platforms and rest api allowing integration
with several testing framework platforms. 

### Main Features:
*  Python 3.7.0
*  Selenium 3.141.0
*  Custom API request
*  Page Object Model
*  dot.env configurations

### Dynamic framework based on environment variables

#### Here is a dot.env file example:

*  DRIVER: selenium or appium drive to execute test against(chrome, firefox, ie, edge, safari, android or ios). In case of mobile it will depend on your configuration file capabalities.
*  APPIUM_HUB: appium url to host appium instance(http://127.0.0.1:4723/wd/hub)
*  SELENIUM_GRID: selenium grid url to host local grid(http://127.0.0.1:4723/wd/hub)
*  CLOUD_SERVER: cloud farm provider url in order to execute tests against cloud platform
*  CLOUD_USER: user to authenticate against cloud server
*  CLOUD_KEY: password to authenticate against cloud server
*  BUILD_VERSION: optional dot.env variable to track the build version of branch in continuous integration
*  PLATFORM: platform to execute tests: local, to execute tests in your local machine. Cloud, to execute tests against cloud server

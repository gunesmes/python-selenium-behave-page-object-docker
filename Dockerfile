FROM python:3.6

MAINTAINER Mesut Güneş <gunesmes@gmail.com>

# Set timezone
RUN echo "US/Eastern" > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get update -y && \
  apt-get install -y unzip xvfb \
  qt5-default libqt5webkit5-dev \
  gstreamer1.0-plugins-base \
  gstreamer1.0-tools gstreamer1.0-x \
  freetds-dev \
  libnss3 libxi6 libgconf-2-4 \
  xvfb

# install chrome
RUN apt-get update -y && \
  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
  dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# install chromedriver and place it ib path
RUN wget https://chromedriver.storage.googleapis.com/2.42/chromedriver_linux64.zip && \
  unzip chromedriver_linux64.zip && \
  mv chromedriver /usr/local/bin/

# install Python packages
RUN pip3 install selenium
RUN pip3 install behave
RUN pip3 install allure-behave


# create seperate folder for project
RUN mkdir /project
WORKDIR /project
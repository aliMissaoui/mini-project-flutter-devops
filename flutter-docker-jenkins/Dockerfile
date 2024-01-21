FROM ubuntu:18.04

# Prerequisites
RUN apt update && apt install -y curl git unzip xz-utils zip libglu1-mesa openjdk-8-jdk wget
RUN apt update
RUN apt install -y libgtk-3-dev
RUN apt install -y clang
RUN apt install -y  cmake ninja-build pkg-config


# Set up new user
RUN useradd -ms /bin/bash developer
USER developer
WORKDIR /home/developer



# Prepare Android directories and system variables
RUN mkdir -p Android/sdk
ENV ANDROID_SDK_ROOT /home/developer/Android/sdk
RUN mkdir -p .android && touch .android/repositories.cfg

# Set up Android SDK
RUN wget -O sdk-tools.zip https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip
RUN unzip sdk-tools.zip && rm sdk-tools.zip
RUN mv tools Android/sdk/tools
RUN cd Android/sdk/tools/bin && yes | ./sdkmanager --licenses
RUN cd Android/sdk/tools/bin && ./sdkmanager "build-tools;29.0.2" "platform-tools" "platforms;android-29" "sources;android-29"
ENV PATH "$PATH:/home/developer/Android/sdk/platform-tools"

# Download Flutter SDK
RUN git clone https://github.com/flutter/flutter.git --branch=stable
ENV PATH "$PATH:/home/developer/flutter/bin"
RUN cd Android/sdk/tools/ && bin/sdkmanager --install "cmdline-tools;latest"
USER root
RUN apt install -y default-jdk
RUN git config --global --add safe.directory /home/developer/flutter
# RUN flutter doctor --android-licenses
RUN flutter doctor
RUN flutter upgrade 
WORKDIR /home/developer/workspace
USER root


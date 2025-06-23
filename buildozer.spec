name: Build APK

on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 60

    steps:
    - uses: actions/checkout@v3

    - name: Setup Python 3.8
      uses: actions/setup-python@v4
      with:
        python-version: '3.8'

    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y build-essential git python3-pip openjdk-11-jdk unzip zip wget ant
        pip3 install --upgrade pip
        pip3 install cython==0.29.36
        pip3 install --no-cache-dir buildozer

    - name: Setup Android SDK
      run: |
        mkdir -p $HOME/android-sdk/cmdline-tools/latest
        cd $HOME/android-sdk/cmdline-tools/latest
        
        wget https://dl.google.com/android/repository/commandlinetools-linux-8512546_latest.zip -O cmdline-tools.zip
        unzip cmdline-tools.zip
        rm cmdline-tools.zip
        
        mv cmdline-tools/* .
        rm -rf cmdline-tools
        
        echo "ANDROID_HOME=$HOME/android-sdk" >> $GITHUB_ENV
        echo "ANDROID_SDK_ROOT=$HOME/android-sdk" >> $GITHUB_ENV
        echo "PATH=$HOME/android-sdk/cmdline-tools/latest/bin:$HOME/android-sdk/platform-tools:$HOME/android-sdk/build-tools/34.0.0:$PATH" >> $GITHUB_ENV

    - name: Accept licenses and install components
      run: |
        yes | sdkmanager --sdk_root=$ANDROID_HOME --licenses
        sdkmanager --sdk_root=$ANDROID_HOME "platform-tools" "build-tools;34.0.0" "platforms;android-34" "ndk;23.1.7779620"

    - name: Update buildozer.spec
      run: |
        # Обновляем устаревшие параметры в spec файле
        sed -i 's/android.arch = /android.archs = /' buildozer.spec
        sed -i '/android.sdk = /d' buildozer.spec
        sed -i '/android.sdk_path = /d' buildozer.spec
        echo "android.ndk_path = $ANDROID_HOME/ndk/23.1.7779620" >> buildozer.spec

    - name: Build APK
      run: |
        # Проверяем конфигурацию
        buildozer -v android update
        
        # Собираем APK (3 попытки)
        for i in {1..3}; do
          buildozer -v android clean && \
          buildozer -v android debug && break || sleep 30
        done

    - name: Upload APK artifact
      if: success()
      uses: actions/upload-artifact@v4
      with:
        name: MyAssistant-apk
        path: bin/*.apk

    - name: Show build logs if failed
      if: failure()
      run: |
        cat .buildozer/android/platform/build-*/build.out
        cat .buildozer/android/platform/build-*/build.err

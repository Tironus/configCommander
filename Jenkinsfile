pipeline {
	agent any
	environment {
		CONFIG_COMMANDER='1.0'
		APP_PATH="$HOME/configCommander"
	}
	stages {
		stage('build') {
			steps {
				echo "configCommander version $CONFIG_COMMANDER"
				sh '''
					pwd
					ls
					python3 --version
					python3 -m venv ./venv
					source ./venv/bin/activate
					export PKG_CONFIG_PATH=libffi.pc
					pip --version
					/var/jenkins_home/workspace/configCommander_main/venv/bin/python3 -m pip install --upgrade pip
					pip --version
					pip install -r requirements.txt
				'''
			}
		}
	}
}
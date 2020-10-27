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
					pip --version
					pip install -r requirements.txt
				'''
			}
		}
	}
}
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
					python3 --version
					pip --version
					python3 -m venv ./venv
					source ./venv/bin/activate
					make install
				'''
			}
		}
		stage('lint') {
			steps {
				echo "configCommander version $CONFIG_COMMANDER"
				sh '''
					pwd
					python3 --version
					source ./venv/bin/activate
					make lint
				'''
			}
		}
		stage('test') {
			steps {
				echo "configCommander version $CONFIG_COMMANDER"
				sh '''
					pwd
					python3 --version
					source ./venv/bin/activate
					make test
				'''
			}
		}
	}
}
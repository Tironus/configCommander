pipeline {
	agent any
	environment {
		CONFIG_COMMANDER='1.0'
		APP_PATH="$HOME/configCommander"
	}
	stages {
		stage('stage-1') {
			steps {
				echo "configCommander version $CONFIG_COMMANDER"
				sh '''
					ls
					pwd
					python --version
				'''
			}
		}
	}
}
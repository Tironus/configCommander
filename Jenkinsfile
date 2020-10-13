pipeline {
	agent any
	environment {
		CONFIG_COMMANDER='1.0'
		APP_PATH="$HOME/configCommander"
	}
	stages {
		stage('stage-1') {
			echo "configCommander version $CONFIG_COMMANDER"
			sh '''
				source $HOME/cc_venv/bin/activate
				cd APP_PATH
				make test
			'''
		}
	}
}
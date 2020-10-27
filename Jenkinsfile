pipeline {
    agent { docker { image 'python:3.5.1' } }
    environment {
		CONFIG_COMMANDER='1.0'
		APP_PATH="$HOME/configCommander"
	}
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}
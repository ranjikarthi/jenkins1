pipeline {
    agent any

    stages {

     

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t python-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run --rm python-app'
            }
        }
    }
}

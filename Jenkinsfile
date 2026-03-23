pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
    steps {
        sh '''
        rm -rf venv
        python3 -m venv venv
        venv/bin/python -m ensurepip --upgrade
        venv/bin/python -m pip install -r requirements.txt
        '''
    }
}

stage('Run Tests') {
    steps {
        sh '''
        venv/bin/python -m pytest
        '''
    }
}

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t flask-benchmark .
                '''
            }
        }

    }
}

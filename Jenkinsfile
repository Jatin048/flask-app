pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
    steps {
        sh '''
        python3 -m venv venv
        venv/bin/python -m pip install --upgrade pip setuptools wheel
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

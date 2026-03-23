pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
    steps {
        sh '''
        python3 -m venv venv
        python3 -m venv --upgrade-deps venv
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

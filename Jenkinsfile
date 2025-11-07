pipeline {
    agent any
    environment {
        IMAGE_NAME = "snakegame"
        CONTAINER_NAME = "snakegame"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/<your-username>/snake-game.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🧱 Building Docker image...'
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo '🧪 Running tests...'
                sh 'docker run --rm $IMAGE_NAME pytest -q || true'
            }
        }

        stage('Deploy Application') {
            steps {
                echo '🚀 Deploying container...'
                sh '''
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                    docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME
                '''
            }
        }
    }

    post {
        always {
            echo '✅ Pipeline completed (success or fail).'
        }
    }
}

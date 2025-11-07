pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo '📦 Checking out repository...'
                git branch: 'main', url: 'https://github.com/danushrajaram/snake-game.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🧱 Building Docker image...'
                bat 'docker build -t snakegame .'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo '🧪 Running tests...'
                // ✅ set working directory to /app to fix "No module named app"
                bat 'docker run --rm -w /app snakegame pytest tests/'
            }
        }

        stage('Deploy Application') {
            steps {
                echo '🚀 Deploying container...'
                // Stop old container if running
                bat '''
                docker ps -q --filter "name=snakegame" | findstr . && docker stop snakegame && docker rm snakegame
                docker run -d -p 5000:5000 --name snakegame snakegame
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

pipeline {
    agent any

    environment {
        DOCKER_USERNAME = "cossiala7" // username docker
        IMAGE_VERSION = "1.${BUILD_NUMBER}"  // version dynamique de l’image
        DOCKER_IMAGE = "${DOCKER_USERNAME}/django_app:${IMAGE_VERSION}" // nom de l’image docker
        DOCKER_CONTAINER = "django_app"  // nom du conteneur
        COMPOSE_PROJECT_NAME = "gestion_notes_ci"
    }

    stages {
        stage('Cloner le projet') {
            steps {
                git 'https://github.com/cossiala7/Application_gestion_notes.git'
            }
        }

        stage('Build de l’image Docker') {
            steps {
                script{
                sh 'docker build -t $DOCKER_IMAGE .'
                }    
            }
        }

        stage('Push vers Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'delatchaille',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }

        stage('Démarrage avec docker-compose') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh '''
                        docker container stop django_app || true
                        docker container rm django_app || true
                        docker container run -d \
                            --name django_app \
                            -e DB_NAME=gestion_notes \
                            -e DB_USER=django_user \
                            -e DB_PASSWORD=django_pass \
                            -e DB_HOST=mysql_django \
                            -p 8000:8000 \
                            $IMAGE_NAME
                    '''
                }
            }
        }
    }

    
}

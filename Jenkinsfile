pipeline {
    agent {
        docker {
            image 'docker:20.10.24-dind'
            args '--privileged -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        DOCKER_USERNAME = "cossiala7"                         // Ton identifiant Docker Hub
        IMAGE_VERSION   = "1.${BUILD_NUMBER}"                // Version auto-incrémentée
        DOCKER_IMAGE    = "${DOCKER_USERNAME}/django_app:${IMAGE_VERSION}"
        DOCKER_CONTAINER = "django_app"
        COMPOSE_PROJECT_NAME = "gestion_notes_ci"
    }

    stages {
        stage('Vérification Docker') {
            steps {
                sh 'docker version'
            }
        }

        stage('Build de l’image Docker') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push vers Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'delatchaille',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $DOCKER_IMAGE
                    '''
                }
            }
        }

        stage('Démarrage avec docker-compose') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Déploiement') {
            steps {
                sh '''
                    docker container stop $DOCKER_CONTAINER || true
                    docker container rm $DOCKER_CONTAINER || true
                    docker run -d \
                        --name $DOCKER_CONTAINER \
                        -e DB_NAME=gestion_notes \
                        -e DB_USER=django_user \
                        -e DB_PASSWORD=django_pass \
                        -e DB_HOST=mysql_django \
                        -p 8000:8000 \
                        $DOCKER_IMAGE
                '''
            }
        }
    }
}

pipeline {
    agent any

    environment {
        DOCKER_USERNAME     = "cossiala7"
        IMAGE_VERSION       = "1.${BUILD_NUMBER}"
        DOCKER_IMAGE        = "${DOCKER_USERNAME}/django_app:${IMAGE_VERSION}"
        DOCKER_CONTAINER    = "django_app"
        COMPOSE_PROJECT_NAME = "gestion_notes_ci"
    }

    stages {
        stage('Pipeline Dockerisé') {
            steps {
                script {
                    docker.image('docker:20.10.24-dind').inside('--privileged -v /var/run/docker.sock:/var/run/docker.sock') {

                        sh 'docker version'

                        sh 'docker build -t $DOCKER_IMAGE .'

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

                        sh 'docker-compose up -d'

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
    }
}

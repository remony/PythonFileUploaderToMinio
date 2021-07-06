pipeline {
    environment {
    registry = "registry.home.local/file_uploader/"
	dockerImage = ''
                }
    agent any
    stages {
		stage('Create & Push Image'){
              agent {
	                  label 'docker-agent'
		            }
                    stages {					
		                    stage('Create Image') {
                                                  steps {
                                                         script {
														         unstash 'build'
                                                                 dockerImage = docker.build registry + "audit-ui:$BUILD_NUMBER"
                                                                 }
                                                        }
                                                   }
                            stage('Push Image') {
                                                 steps {
                                                        script {
                                                                docker.withRegistry( '' ) {
                                                                                           dockerImage.push()
						                                                                   }
                                                                }
                                                        }
                                                }
							}
							         }
		
            }
    }

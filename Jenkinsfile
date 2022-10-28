pipeline {
  agent {
    kubernetes {
      cloud "kubernetes-scrapper-system"
      label "jenkins-agent"
      yamlFile "jenkins-build-pod.yaml"
    }
  }

  stages {
    stage("Build") {
      steps {
        container("gcloud") {
          sh """
          pwd
          ls
          """
        }
      }
    }
    stage("Deploy") {
      steps {
        container("helm") {
          sh """
          pwd
          ls
          """
        }
      }
    }
  }
}
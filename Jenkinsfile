pipeline {
  agent {
    kubernetes {
      // Without cloud, Jenkins will pick the first cloud in the list
      cloud "test-cluster"
      label "jenkins-agent"
      yamlFile "jenkins-build-pod.yaml"
    }
  }

  stages {
    stage("Deploy") {
      steps {
        container("helm") {
          sh "
          helm version
          kubectl version
          "
        }
      }
    }
  }
}
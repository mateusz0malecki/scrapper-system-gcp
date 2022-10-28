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
          sh '''
          cd microservices/job_offers_scrapper/praca
          git config --global --add safe.directory /home/jenkins/agent/workspace/test-job
          git rev-parse --short HEAD
          export BUILD_VERSION=$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/praca-offers-scrapper:$BUILD_VERSION"
          cd ..
          cd praca_subscriber
          gcloud builds submit --tag "gcr.io/scrapper-system/praca-offers-db-handler:$BUILD_VERSION"
          cd ..
          cd pracuj
          gcloud builds submit --tag "gcr.io/scrapper-system/pracuj-offers-scrapper:$BUILD_VERSION"
          cd ..
          cd pracuj_subscriber
          gcloud builds submit --tag "gcr.io/scrapper-system/pracuj-offers-db-handler:$BUILD_VERSION"
          '''
        }
      }
    }
    stage("Deploy") {
      steps {
        container("helm") {
          sh deploy.sh
        }
      }
    }
  }
}
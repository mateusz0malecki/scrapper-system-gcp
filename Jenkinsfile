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
          gcloud builds submit --tag "gcr.io/scrapper-system/praca-offers-scrapper:$(sudo git rev-parse --short HEAD)"
          cd ..
          cd praca_subscriber
          gcloud builds submit --tag "gcr.io/scrapper-system/praca-offers-db-handler:$(sudo git rev-parse --short HEAD)"
          cd ..
          cd pracuj
          gcloud builds submit --tag "gcr.io/scrapper-system/pracuj-offers-scrapper:$(sudo git rev-parse --short HEAD)"
          cd ..
          cd pracuj_subscriber
          gcloud builds submit --tag "gcr.io/scrapper-system/pracuj-offers-db-handler:$(sudo git rev-parse --short HEAD)"
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
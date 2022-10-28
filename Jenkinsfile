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
          gcloud builds submit --tag 'gcr.io/scrapper-system/praca-offers-scrapper:"$(git rev-parse --short HEAD)"'
          cd ..
          cd praca_subscriber
          gcloud builds submit --tag 'gcr.io/scrapper-system/praca-offers-db-handler:"$(git rev-parse --short HEAD)"'
          cd ..
          cd pracuj
          gcloud builds submit --tag 'gcr.io/scrapper-system/pracuj-offers-scrapper:"$(git rev-parse --short HEAD)"'
          cd ..
          cd pracuj_subscriber
          gcloud builds submit --tag 'gcr.io/scrapper-system/pracuj-offers-db-handler:"$(git rev-parse --short HEAD)"'
          '''
        }
      }
    }
    stage("Deploy") {
      steps {
        container("helm") {
          sh '''
          sed -i "/^\([[:space:]]*tag: \).*/s//\1$(git rev-parse --short HEAD)/" scrapper-system-chart/values.yaml
          '''
        }
      }
    }
  }
}
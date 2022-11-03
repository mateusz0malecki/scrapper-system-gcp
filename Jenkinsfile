pipeline {
  agent {
    kubernetes {
      cloud "kubernetes-scrapper-system"
      label "jenkins-agent"
      yamlFile "jenkins-build-pod.yaml"
    }
  }
  stages {
    stage("Build container scrapper praca") {
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/praca
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system
          git rev-parse --short HEAD
          export BUILD_VERSION=$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/praca-offers-scrapper:$BUILD_VERSION"
          '''
        }
      }
    }
    stage("Build container subscriber praca") {
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/praca_subscriber
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system
          git rev-parse --short HEAD
          export BUILD_VERSION=$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/praca-offers-db-handler:$BUILD_VERSION"
          '''
        }
      }
    }
    stage("Build container scrapper pracuj") {
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/pracuj
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system
          git rev-parse --short HEAD
          export BUILD_VERSION=$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/pracuj-offers-scrapper:$BUILD_VERSION"
          '''
        }
      }
    }
    stage("Build container subscriber pracuj") {
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/pracuj_subscriber
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system
          git rev-parse --short HEAD
          export BUILD_VERSION=$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/pracuj-offers-db-handler:$BUILD_VERSION"
          '''
        }
      }
    }
    stage("Deploy helm chart") {
      steps {
        container("helm") {
          sh '''
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system
          sed -i "/^\\([[:space:]]*tag: \\).*/s//\\1$(git rev-parse --short HEAD)/" scrapper-system-chart/values.yaml
          helm upgrade scrapper-system scrapper-system-chart/ --atomic --install
          '''
        }
      }
    }
    stage("Test helm") {
      steps {
        container("helm") {
          sh '''
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system
          helm test scrapper-system
          '''
        }
      }
    }
  }
}

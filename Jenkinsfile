pipeline {
  agent none
  stages {

    stage("Build container scrapper praca dev") {
      when { branch 'dev' }
      agent {
        kubernetes {
          cloud "kubernetes-scrapper-system"
          label "jenkins-agent-normal-${env.BUILD_NUMBER}"
          yamlFile "jenkins-build-pod.yaml"
          slaveConnectTimeout 300
          idleMinutes 5
        }
      }
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/praca
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_dev
          git rev-parse --short HEAD
          export BUILD_VERSION=$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/praca-offers-scrapper-dev:$BUILD_VERSION"
          '''
        }
      }
    }

    stage("Build container subscriber praca dev") {
      when { branch 'dev' }
      agent {
        kubernetes {
          label "jenkins-agent-normal-${env.BUILD_NUMBER}"
        }
      }
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/praca_subscriber
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_dev
          git rev-parse --short HEAD
          export BUILD_VERSION=$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/praca-offers-db-handler-dev:$BUILD_VERSION"
          '''
        }
      }
    }

    stage("Build container scrapper pracuj dev") {
      when { branch 'dev' }
      agent {
        kubernetes {
          label "jenkins-agent-normal-${env.BUILD_NUMBER}"
        }
      }
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/pracuj
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_dev
          git rev-parse --short HEAD
          export BUILD_VERSION=$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/pracuj-offers-scrapper-dev:$BUILD_VERSION"
          '''
        }
      }
    }

    stage("Build container subscriber pracuj dev") {
      when { branch 'dev' }
      agent {
        kubernetes {
          label "jenkins-agent-normal-${env.BUILD_NUMBER}"
        }
      }
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/pracuj_subscriber
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_dev
          git rev-parse --short HEAD
          export BUILD_VERSION=$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/pracuj-offers-db-handler-dev:$BUILD_VERSION"
          '''
        }
      }
    }

    stage("Build container scrapper praca prod") {
      when { branch 'prod' }
      agent {
        kubernetes {
          cloud "kubernetes-scrapper-system"
          label "jenkins-agent-normal-${env.BUILD_NUMBER}"
          yamlFile "jenkins-build-pod.yaml"
          slaveConnectTimeout 300
          idleMinutes 5
        }
      }
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/praca
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_prod
          git rev-parse --short HEAD
          export BUILD_VERSION=$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/praca-offers-scrapper-prod:$BUILD_VERSION"
          '''
        }
      }
    }

    stage("Build container subscriber praca prod") {
      when { branch 'prod' }
      agent {
        kubernetes {
          label "jenkins-agent-normal-${env.BUILD_NUMBER}"
        }
      }
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/praca_subscriber
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_prod
          git rev-parse --short HEAD
          export BUILD_VERSION=$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/praca-offers-db-handler-prod:$BUILD_VERSION"
          '''
        }
      }
    }

    stage("Build container scrapper pracuj prod") {
      when { branch 'prod' }
      agent {
        kubernetes {
          label "jenkins-agent-normal-${env.BUILD_NUMBER}"
        }
      }
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/pracuj
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_prod
          git rev-parse --short HEAD
          export BUILD_VERSION=$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/pracuj-offers-scrapper-prod:$BUILD_VERSION"
          '''
        }
      }
    }

    stage("Build container subscriber pracuj prod") {
      when { branch 'prod' }
      agent {
        kubernetes {
          label "jenkins-agent-normal-${env.BUILD_NUMBER}"
        }
      }
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/pracuj_subscriber
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_prod
          git rev-parse --short HEAD
          export BUILD_VERSION=$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/pracuj-offers-db-handler-prod:$BUILD_VERSION"
          '''
        }
      }
    }

    stage("Deploy helm chart pracuj dev") {
      when { branch 'dev' }
      agent {
        kubernetes {
          cloud "kubernetes-scrapper-system-dev"
          label "jenkins-agent-dev-${env.BUILD_NUMBER}"
          yamlFile "jenkins-build-pod-dev.yaml"
          slaveConnectTimeout 300
          idleMinutes 5
        }
      }
      steps {
        container("helm") {
          sh '''
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_dev
          sed -i "/^\\([[:space:]]*tag: \\).*/s//\\1$(git rev-parse --short HEAD)/" scrapper-system-chart-pracuj/values-dev.yaml
          helm upgrade scrapper-system-pracuj-dev scrapper-system-chart-pracuj/ --create-namespace -n dev -f scrapper-system-chart-pracuj/values.dev.yaml --atomic --install
          '''
        }
      }
    }

    stage("Deploy helm chart praca dev") {
      when { branch 'dev' }
      agent {
        kubernetes {
          label "jenkins-agent-dev-${env.BUILD_NUMBER}"
        }
      }
      steps {
        container("helm") {
          sh '''
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_dev
          sed -i "/^\\([[:space:]]*tag: \\).*/s//\\1$(git rev-parse --short HEAD)/" scrapper-system-chart-praca/values-dev.yaml
          helm upgrade scrapper-system-praca-dev scrapper-system-chart-praca/ --create-namespace -n dev -f scrapper-system-chart-praca/values.dev.yaml --atomic --install
          '''
        }
      }
    }

    stage("Deploy helm chart pracuj prod") {
      when { branch 'prod' }
      agent {
        kubernetes {
          cloud "kubernetes-scrapper-system-prod"
          label "jenkins-agent-prod-${env.BUILD_NUMBER}"
          yamlFile "jenkins-build-pod-prod.yaml"
          slaveConnectTimeout 300
          idleMinutes 5
        }
      }
      steps {
        container("helm") {
          sh '''
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_prod
          sed -i "/^\\([[:space:]]*tag: \\).*/s//\\1$(git rev-parse --short HEAD)/" scrapper-system-chart-pracuj/values-prod.yaml
          helm upgrade scrapper-system-pracuj-prod scrapper-system-chart-pracuj/ --create-namespace -n prod -f scrapper-system-chart-pracuj/values.dev.yaml --atomic --install
          '''
        }
      }
    }

    stage("Deploy helm chart praca prod") {
      when { branch 'prod' }
      agent {
        kubernetes {
          label "jenkins-agent-prod-${env.BUILD_NUMBER}"
        }
      }
      steps {
        container("helm") {
          sh '''
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_prod
          sed -i "/^\\([[:space:]]*tag: \\).*/s//\\1$(git rev-parse --short HEAD)/" scrapper-system-chart-praca/values-prod.yaml
          helm upgrade scrapper-system-praca-prod scrapper-system-chart-praca/ --create-namespace -n prod -f scrapper-system-chart-praca/values.dev.yaml --atomic --install
          '''
        }
      }
    }
  }
}

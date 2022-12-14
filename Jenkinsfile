pipeline {
  agent {
    kubernetes {
      cloud "kubernetes-scrapper-system"
      label "jenkins-agent-normal-${env.BUILD_NUMBER}"
      yamlFile "jenkins-build-pod.yaml"
      slaveConnectTimeout 300
      idleMinutes 5
    }
  }
  stages {

    stage("Build container scrapper praca dev") {
      when {
       allOf {
         branch 'dev'
         changeset "microservices/job_offers_scrapper/praca/*"
       }
      }
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/praca
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_dev
          git rev-parse --short HEAD
          export BUILD_VERSION=M$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/praca-offers-scrapper-dev:$BUILD_VERSION"
          '''
        }
      }
    }

    stage("Build container subscriber praca dev") {
      when {
       allOf {
         branch 'dev'
         changeset "microservices/job_offers_scrapper/praca_subscriber/*"
       }
      }
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/praca_subscriber
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_dev
          git rev-parse --short HEAD
          export BUILD_VERSION=M$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/praca-offers-db-handler-dev:$BUILD_VERSION"
          '''
        }
      }
    }

    stage("Build container scrapper pracuj dev") {
      when {
       allOf {
         branch 'dev'
         changeset "microservices/job_offers_scrapper/pracuj/*"
       }
      }
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/pracuj
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_dev
          git rev-parse --short HEAD
          export BUILD_VERSION=M$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/pracuj-offers-scrapper-dev:$BUILD_VERSION"
          '''
        }
      }
    }

    stage("Build container subscriber pracuj dev") {
      when {
       allOf {
         branch 'dev'
         changeset "microservices/job_offers_scrapper/pracuj_subscriber/*"
       }
      }
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/pracuj_subscriber
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_dev
          git rev-parse --short HEAD
          export BUILD_VERSION=M$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/pracuj-offers-db-handler-dev:$BUILD_VERSION"
          '''
        }
      }
    }

    stage("Build container scrapper praca prod") {
      when {
       allOf {
         branch 'prod'
         changeset "microservices/job_offers_scrapper/praca/*"
       }
      }
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/praca
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_prod
          git rev-parse --short HEAD
          export BUILD_VERSION=M$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/praca-offers-scrapper-prod:$BUILD_VERSION"
          '''
        }
      }
    }

    stage("Build container subscriber praca prod") {
      when {
       allOf {
         branch 'prod'
         changeset "microservices/job_offers_scrapper/praca_subscriber/*"
       }
      }
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/praca_subscriber
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_prod
          git rev-parse --short HEAD
          export BUILD_VERSION=M$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/praca-offers-db-handler-prod:$BUILD_VERSION"
          '''
        }
      }
    }

    stage("Build container scrapper pracuj prod") {
      when {
       allOf {
         branch 'prod'
         changeset "microservices/job_offers_scrapper/pracuj/*"
       }
      }
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/pracuj
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_prod
          git rev-parse --short HEAD
          export BUILD_VERSION=M$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/pracuj-offers-scrapper-prod:$BUILD_VERSION"
          '''
        }
      }
    }

    stage("Build container subscriber pracuj prod") {
      when {
       allOf {
         branch 'prod'
         changeset "microservices/job_offers_scrapper/pracuj_subscriber/*"
       }
      }
      steps {
        container("gcloud") {
          sh '''
          cd microservices/job_offers_scrapper/pracuj_subscriber
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_prod
          git rev-parse --short HEAD
          export BUILD_VERSION=M$(git rev-parse --short HEAD)
          gcloud builds submit --tag "gcr.io/scrapper-system/pracuj-offers-db-handler-prod:$BUILD_VERSION"
          '''
        }
      }
    }

    stage("Add tags to container images dev") {
      when {
        branch 'dev'
        anyOf {
          changeset "microservices/job_offers_scrapper/pracuj/*"
          changeset "microservices/job_offers_scrapper/pracuj_subscriber/*"
          changeset "microservices/job_offers_scrapper/praca/*"
          changeset "microservices/job_offers_scrapper/praca_subscriber/*"
        }
      }
      steps {
        container("gcloud") {
          sh '''
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_dev
          export BUILD_VERSION=M$(git rev-parse --short HEAD)
          export NEW_TAG_PRACA_SCR=$(gcloud container images list-tags gcr.io/scrapper-system/praca-offers-scrapper-dev --limit 1 --format="value(format('{0}',digest))")
          yes | gcloud container images add-tag gcr.io/scrapper-system/praca-offers-scrapper-dev@sha256:$NEW_TAG_PRACA_SCR gcr.io/scrapper-system/praca-offers-scrapper-dev:$BUILD_VERSION
          export NEW_TAG_PRACA_DB=$(gcloud container images list-tags gcr.io/scrapper-system/praca-offers-db-handler-dev --limit 1 --format="value(format('{0}',digest))")
          yes | gcloud container images add-tag gcr.io/scrapper-system/praca-offers-db-handler-dev@sha256:$NEW_TAG_PRACA_DB gcr.io/scrapper-system/praca-offers-db-handler-dev:$BUILD_VERSION
          export NEW_TAG_PRACUJ_SCR=$(gcloud container images list-tags gcr.io/scrapper-system/pracuj-offers-scrapper-dev --limit 1 --format="value(format('{0}',digest))")
          yes | gcloud container images add-tag gcr.io/scrapper-system/pracuj-offers-scrapper-dev@sha256:$NEW_TAG_PRACUJ_SCR gcr.io/scrapper-system/pracuj-offers-scrapper-dev:$BUILD_VERSION
          export NEW_TAG_PRACUJ_DB=$(gcloud container images list-tags gcr.io/scrapper-system/pracuj-offers-db-handler-dev --limit 1 --format="value(format('{0}',digest))")
          yes | gcloud container images add-tag gcr.io/scrapper-system/pracuj-offers-db-handler-dev@sha256:$NEW_TAG_PRACUJ_DB gcr.io/scrapper-system/pracuj-offers-db-handler-dev:$BUILD_VERSION
          '''
        }
      }
    }

    stage("Add tags to container images prod") {
      when {
        branch 'prod'
        anyOf {
          changeset "microservices/job_offers_scrapper/pracuj/*"
          changeset "microservices/job_offers_scrapper/pracuj_subscriber/*"
          changeset "microservices/job_offers_scrapper/praca/*"
          changeset "microservices/job_offers_scrapper/praca_subscriber/*"
        }
      }
      steps {
        container("gcloud") {
          sh '''
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_prod
          export BUILD_VERSION=M$(git rev-parse --short HEAD)
          export NEW_TAG_PRACA_SCR=$(gcloud container images list-tags gcr.io/scrapper-system/praca-offers-scrapper-prod --limit 1 --format="value(format('{0}',digest))")
          yes | gcloud container images add-tag gcr.io/scrapper-system/praca-offers-scrapper-prod@sha256:$NEW_TAG_PRACA_SCR gcr.io/scrapper-system/praca-offers-scrapper-prod:$BUILD_VERSION
          export NEW_TAG_PRACA_DB=$(gcloud container images list-tags gcr.io/scrapper-system/praca-offers-db-handler-prod --limit 1 --format="value(format('{0}',digest))")
          yes | gcloud container images add-tag gcr.io/scrapper-system/praca-offers-db-handler-prod@sha256:$NEW_TAG_PRACA_DB gcr.io/scrapper-system/praca-offers-db-handler-prod:$BUILD_VERSION
          export NEW_TAG_PRACUJ_SCR=$(gcloud container images list-tags gcr.io/scrapper-system/pracuj-offers-scrapper-prod --limit 1 --format="value(format('{0}',digest))")
          yes | gcloud container images add-tag gcr.io/scrapper-system/pracuj-offers-scrapper-prod@sha256:$NEW_TAG_PRACUJ_SCR gcr.io/scrapper-system/pracuj-offers-scrapper-prod:$BUILD_VERSION
          export NEW_TAG_PRACUJ_DB=$(gcloud container images list-tags gcr.io/scrapper-system/pracuj-offers-db-handler-prod --limit 1 --format="value(format('{0}',digest))")
          yes | gcloud container images add-tag gcr.io/scrapper-system/pracuj-offers-db-handler-prod@sha256:$NEW_TAG_PRACUJ_DB gcr.io/scrapper-system/pracuj-offers-db-handler-prod:$BUILD_VERSION
          '''
        }
      }
    }

    stage("Deploy helm chart pracuj dev") {
      when {
        beforeAgent true
        branch 'dev'
        anyOf {
          changeset "microservices/job_offers_scrapper/pracuj/*"
          changeset "microservices/job_offers_scrapper/pracuj_subscriber/*"
          changeset "scrapper-system-chart-pracuj/*"
        }
      }
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
          git rev-parse --short HEAD
          export BUILD_VERSION=M$(git rev-parse --short HEAD)
          sed -i "/^\\([[:space:]]*tag: \\).*/s//\\1$BUILD_VERSION/" scrapper-system-chart-pracuj/values.dev.yaml
          helm upgrade scrapper-system-pracuj-dev scrapper-system-chart-pracuj/ --create-namespace -n dev -f scrapper-system-chart-pracuj/values.dev.yaml --atomic --install
          '''
        }
      }
    }

    stage("Deploy helm chart praca dev") {
      when {
        beforeAgent true
        branch 'dev'
        anyOf {
          changeset "microservices/job_offers_scrapper/praca/*"
          changeset "microservices/job_offers_scrapper/praca_subscriber/*"
          changeset "scrapper-system-chart-praca/*"
        }
      }
      agent {
        kubernetes {
          label "jenkins-agent-dev-${env.BUILD_NUMBER}"
        }
      }
      steps {
        container("helm") {
          sh '''
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_dev
          git rev-parse --short HEAD
          export BUILD_VERSION=M$(git rev-parse --short HEAD)
          sed -i "/^\\([[:space:]]*tag: \\).*/s//\\1$BUILD_VERSION/" scrapper-system-chart-praca/values.dev.yaml
          helm upgrade scrapper-system-praca-dev scrapper-system-chart-praca/ --create-namespace -n dev -f scrapper-system-chart-praca/values.dev.yaml --atomic --install
          '''
        }
      }
    }

    stage("Deploy helm chart pracuj prod") {
      when {
        beforeAgent true
        branch 'prod'
        anyOf {
          changeset "microservices/job_offers_scrapper/pracuj/*"
          changeset "microservices/job_offers_scrapper/pracuj_subscriber/*"
          changeset "scrapper-system-chart-pracuj/*"
        }
      }
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
          git rev-parse --short HEAD
          export BUILD_VERSION=M$(git rev-parse --short HEAD)
          sed -i "/^\\([[:space:]]*tag: \\).*/s//\\1$BUILD_VERSION/" scrapper-system-chart-pracuj/values.prod.yaml
          helm upgrade scrapper-system-pracuj-prod scrapper-system-chart-pracuj/ --create-namespace -n prod -f scrapper-system-chart-pracuj/values.prod.yaml --atomic --install
          '''
        }
      }
    }

    stage("Deploy helm chart praca prod") {
      when {
        beforeAgent true
        branch 'prod'
        anyOf {
          changeset "microservices/job_offers_scrapper/praca/*"
          changeset "microservices/job_offers_scrapper/praca_subscriber/*"
          changeset "scrapper-system-chart-praca/*"
        }
      }
      agent {
        kubernetes {
          label "jenkins-agent-prod-${env.BUILD_NUMBER}"
        }
      }
      steps {
        container("helm") {
          sh '''
          git config --global --add safe.directory /home/jenkins/agent/workspace/scrapper-system-dev-prod_prod
          git rev-parse --short HEAD
          export BUILD_VERSION=M$(git rev-parse --short HEAD)
          sed -i "/^\\([[:space:]]*tag: \\).*/s//\\1$BUILD_VERSION/" scrapper-system-chart-praca/values.prod.yaml
          helm upgrade scrapper-system-praca-prod scrapper-system-chart-praca/ --create-namespace -n prod -f scrapper-system-chart-praca/values.prod.yaml --atomic --install
          '''
        }
      }
    }
  }
}

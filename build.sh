cd microservices/job_offers_scrapper/praca || return
gcloud builds submit --tag gcr.io/scrapper-system/praca-offers-scrapper:"$(git rev-parse --short HEAD)""
cd ..
cd praca_subscriber
gcloud builds submit --tag gcr.io/scrapper-system/praca-offers-db-handler:$(git rev-parse --short HEAD)"
cd ..
cd pracuj ||return
gcloud builds submit --tag gcr.io/scrapper-system/pracuj-offers-scrapper:"$(git rev-parse --short HEAD)""
cd ..
cd pracuj_subscriber
gcloud builds submit --tag gcr.io/scrapper-system/pracuj-offers-db-handler:$(git rev-parse --short HEAD)"
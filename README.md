py -3 -m venv .venv
.venv\scripts\activate

C:\Users\Admin\PycharmProjects\asutp_msgs\venv\Scripts\activate.ps1

pip install -r requirements.txt

docker compose -f docker-compose.yaml build

45 docker compose -f .\docker-compose.yaml build
  46 docker tag asutp_msgs_app_main mgerasimdev/asutp_msgs_app_main:latest
  47 docker push mgerasimdev/asutp_msgs_app_main:latest
  48 docker compose -f .\docker-compose.prod.yaml build

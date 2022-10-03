py -3 -m venv .venv
.venv\scripts\activate

C:\Users\Admin\PycharmProjects\asutp_msgs\venv\Scripts\activate.ps1

pip install -r requirements.txt

docker compose -f docker-compose.yaml build

45 docker compose -f .\docker-compose.yaml build
  46 docker tag asutp_msgs_app_main mgerasimdev/asutp_msgs_app_main:latest
  47 docker push mgerasimdev/asutp_msgs_app_main:latest
  48 docker compose -f .\docker-compose.prod.yaml build


sudo docker tag asutp_msgs_app_main mgerasimdev/asutp_msgs_app_main
sudo docker tag 66a976b71b54 mgerasimdev/datascience-notebook

sudo docker push mgerasimdev/asutp_msgs_app_main

sudo docker save -o ~/asutp_msgs_app_main.tar mgerasimdev/asutp_msgs_app_main:latest
sudo chown redos:redos ~/asutp_msgs_app_main.tar 


sudo docker tag asutp_msgs_app_web mgerasimdev/asutp_msgs_app_web
sudo docker push mgerasimdev/asutp_msgs_app_web
sudo docker save -o ~/asutp_msgs_app_web.tar mgerasimdev/asutp_msgs_app_web:latest
sudo chown redos:redos ~/asutp_msgs_app_web.tar 

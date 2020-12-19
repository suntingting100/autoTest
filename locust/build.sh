PREFIX=registry.cn-beijing.aliyuncs.com/duodian_game/game_locust
read -p "输入tag：" tag

docker build -t ${PREFIX}:${tag} .

docker login --username=boyu.sun@1375493082618412 --password=sun0011991 registry.cn-beijing.aliyuncs.com

docker push ${PREFIX}:${tag}

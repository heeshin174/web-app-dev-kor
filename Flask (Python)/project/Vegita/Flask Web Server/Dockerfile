FROM python:3.6

# set a directory for the app
WORKDIR /app

# copy all the files to the container
COPY . .

# install dependencies 라이브러리 설치 용 목록
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./server.py"]

# 현재 경로의 도커설정 파일을 사용하여 도커 이미지 생성
# > $ docker build -t {image_name} .

# 도커 컨테이너 실행 docker run (<옵션>) <이미지 식별자> (<명령어>) (<인자>)
# > $ docker run --name={컨테이너명} -p {외부포트}:{내부포트} {이미지명}

# 도커 컨테이너 중지
# > $ docker stop {컨테이너명}

# 도커 컨테이너 재실행
# > $ docker restart {컨테이너명}

# 도커 컨테이너 지우기
# > $ docker rm {컨테이너명}
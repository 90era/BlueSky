FROM registry.saintic.com/python
MAINTAINER Mr.tao <staugur@saintic.com>
ADD ./src /BlueSky
ADD requirements.txt /tmp
ADD supervisord.conf /etc
WORKDIR /BlueSky
RUN pip install --index https://pypi.douban.com/simple/ -r /tmp/requirements.txt
ENTRYPOINT ["supervisord"]
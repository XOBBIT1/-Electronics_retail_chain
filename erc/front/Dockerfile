FROM node:14.17.3 as base

WORKDIR /erc/front

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN npm install

EXPOSE 3000

COPY ./front/my-app ./

CMD ["npm", "start"]
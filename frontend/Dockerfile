FROM node:latest

RUN mkdir -p /app/frontend
WORKDIR /app/frontend

COPY ./package*.json /app/frontend/
RUN npm ci

COPY . /app/frontend/

EXPOSE 3000

CMD ["npm", "start"]
FROM node:latest

RUN mkdir -p /app/backend
WORKDIR /app/backend

COPY ./package*.json /app/backend/
RUN npm ci

COPY . /app/backend/

EXPOSE 5000

CMD ["npm", "start"]
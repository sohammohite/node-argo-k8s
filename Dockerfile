FROM node:22 AS install

WORKDIR /app

COPY . .

RUN npm install

#------

FROM node:22-alpine

WORKDIR /app

COPY --from=install /app .

EXPOSE 3000

ENTRYPOINT ["npm"]

CMD ["start"]

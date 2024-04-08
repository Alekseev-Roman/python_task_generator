FROM node:20

ARG PYGENERATOR_DIR

WORKDIR "${PYGENERATOR_DIR}/frontend"
COPY . .

RUN npm config set update-notifier false
RUN npm install --loglevel=error --no-fund --no-audit

CMD [ "npm", "run", "serve" ]

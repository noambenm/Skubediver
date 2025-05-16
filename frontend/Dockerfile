# -------- Build phase --------
FROM node:20-alpine AS build
WORKDIR /app

# Install dependencies first for layer caching
COPY package.json package-lock.json* pnpm-lock.yaml* yarn.lock* ./
RUN npm ci           # or pnpm i / yarn install if you prefer

# Copy source and build
COPY . .
RUN npm run build

# -------- Runtime phase --------
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

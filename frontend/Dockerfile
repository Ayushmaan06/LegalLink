FROM node:18-alpine

WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy project files
COPY . .

# Build the app
RUN npm run build

# Install serve to serve the built app
RUN npm install -g serve

# Serve the app
CMD ["serve", "-s", "dist", "-l", "8080"]
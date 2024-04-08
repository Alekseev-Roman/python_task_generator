const { defineConfig } = require("@vue/cli-service");
// module.exports = defineConfig({
//   transpileDependencies: true
// });

module.exports = {
  devServer: {
    proxy: {
      "^/backend": {
        target: `http://192.168.0.6:8088/`, //${process.env.PYGENERATOR_BACKEND_HOST}`,
        pathRewrite: {'^/backend': ''},
        ws: true,
        changeOrigin: true
      }
    },
    port: 8080 //process.env.PYGENERATOR_FRONTEND_PORT
  }
}
const { defineConfig } = require("@vue/cli-service");
// module.exports = defineConfig({
//   transpileDependencies: true
// });

module.exports = {
  devServer: {
    proxy: {
      "^/backend": {
        target: `http://localhost:8088/`,
        pathRewrite: {'^/backend': ''},
        ws: true,
        changeOrigin: true
      }
    },
    port: 8080 //process.env.PYGENERATOR_FRONTEND_PORT
  }
}

const path = require("path");
const BundleTracker = require("webpack-bundle-tracker");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const webpack = require("webpack");

module.exports = {
  target: "web",
  context: path.join(__dirname, "../"),
  entry: {
    project: path.resolve(__dirname, "../wonderland/static/js/project"),
    vendors: path.resolve(__dirname, "../wonderland/static/js/vendors"),
    project_bootstrap: path.resolve(
      __dirname,
      "../wonderland/static/js/project_bootstrap",
    ),
    vendors_bootstrap: path.resolve(
      __dirname,
      "../wonderland/static/js/vendors_bootstrap",
    ),
  },
  output: {
    path: path.resolve(__dirname, "../wonderland/static/webpack_bundles/"),
    publicPath: "/static/webpack_bundles/",
    filename: "js/[name]-[fullhash].js",
    chunkFilename: "js/[name]-[hash].js",
  },
  plugins: [
    new BundleTracker({
      path: path.resolve(path.join(__dirname, "../")),
      filename: "webpack-stats.json",
    }),
    new MiniCssExtractPlugin({ filename: "css/[name].[contenthash].css" }),
    new webpack.ProvidePlugin({ htmx: "htmx.org" }),
  ],
  module: {
    rules: [
      // we pass the output from babel loader to react-hot loader
      {
        test: /\.js$/,
        loader: "babel-loader",
      },
      {
        test: /\.s?css$/i,
        use: [
          MiniCssExtractPlugin.loader,
          "css-loader",
          {
            loader: "postcss-loader",
            options: {
              postcssOptions: {
                plugins: ["postcss-preset-env", "autoprefixer", "pixrem"],
              },
            },
          },
          "sass-loader",
        ],
      },
    ],
  },
  resolve: {
    modules: ["node_modules"],
    extensions: [".js", ".jsx"],
  },
};

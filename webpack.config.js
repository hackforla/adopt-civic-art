const ExtractTextPlugin = require('extract-text-webpack-plugin');
const UglifyJSPlugin = require('uglifyjs-webpack-plugin');

module.exports = {
  // devtool: 'inline-source-map',
  entry: ['./static/js/app.js', './static/scss/main.scss'],
  output: {
    filename: 'dist/js/app.js',
  },
  module: {
    loaders: [
      {
        test: /\.scss$/,
        use: ExtractTextPlugin.extract({
          use: [
            {
              loader: 'css-loader?sourceMap', options: {
                // sourceMap: true,
                minimize: true
              }
            },
            {
              loader: 'sass-loader?sourceMap', options: {
              }
            }
          ]
        })
      }
    ]
  },
  plugins: [
    new ExtractTextPlugin({
      filename: 'dist/css/styles.css'
    }),
    new UglifyJSPlugin({
      // sourceMap: true
    })
  ]
};

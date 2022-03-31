var str_url = 'https://api.upbit.com/v1/candles/days?market=KRW-BTC&count=1';
const request = require('request')

const options = {
    method: 'GET',
    url: str_url,
    headers: {Accept: 'application/json'}
};

var object;
function getData() {
  return new Promise(function(resolve, reject) {
    request(options, function(error, response, body) {
      if (error) throw new Error(error);
      object = JSON.parse(body);
      console.log("a" + object[0].trade_price);
      resolve(object[0].trade_price);
    });
  });
}

getData().then(function(resolvedData) {
  var price;
  console.log("b" + resolvedData);
  price = Number(resolvedData);
  console.log("c" + price);
});

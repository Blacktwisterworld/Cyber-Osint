const https = require('https');

const token = "8274980094:AAFOCAHI_9c1JykEFqkh2ftDoDPNKYaOU4A";
const url = `https://api.telegram.org/bot${token}/getWebhookInfo`;

https.get(url, (res) => {
  let data = '';
  res.on('data', (chunk) => {
    data += chunk;
  });
  res.on('end', () => {
    console.log("Telegram Webhook Info:");
    console.log(JSON.stringify(JSON.parse(data), null, 2));
  });
}).on("error", (err) => {
  console.log("Error: " + err.message);
});
